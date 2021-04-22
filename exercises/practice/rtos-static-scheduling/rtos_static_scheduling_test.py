import unittest
from z3 import *
import matplotlib.pyplot as plt
import random
from rtos_static_scheduling_classes import *
from rtos_static_scheduling import get_rtos_static_schedule

def plot_graphical_representation(task_dict):
    """
    Plots sequence of tasks
    """
    Y_MAX = 10
    Y_MIN = 0
    Y_MID = (Y_MAX - Y_MIN) / 2

    fig = plt.figure()
    for taskId, execution_time_list in task_dict.items():
        for start_time, end_time in execution_time_list:
            duration = end_time - start_time
            plt.broken_barh([(start_time, duration)], (Y_MIN, Y_MAX), figure=fig, label=taskId)
            midpoint = start_time + (duration / 2)
            plt.text(midpoint, Y_MID, taskId, figure=fig, color="black", fontsize="x-large", ha="center")
    plt.show()

def get_num_periodic_task_repetitions(task):
    num_repetitions = int((task.end_time - task.start_time) / task.period)
    if (task.start_time + (num_repetitions * task.period) + task.execution_time) <= task.end_time:
        num_repetitions += 1
    return num_repetitions

def get_total_execution_time(output_dict):
    max_end_time = 0
    for _, executions_times in output_dict.items():
        for _, end_time in executions_times:
            if (end_time > max_end_time):
                max_end_time = end_time
    return max_end_time

def check_periodic_task_constraints(ut, task, actual_task_output):
    """
    Verify Periodic Task is executed expected number of times
    and start and end time for each repetition are as expected
    """
    num_repetitions = get_num_periodic_task_repetitions(task)
    ut.assertEqual(num_repetitions, len(actual_task_output))
    for i in range(num_repetitions):
        start_time = task.start_time + (i * task.period)
        end_time = start_time + task.execution_time
        ut.assertIn((start_time, end_time), actual_task_output)

def check_dynamic_task_constraints(ut, task, actual_task_output):
    """
    Verify Dynamic Task is only executed once
    and start and end times satisfy specified task constraints
    """
    ut.assertEqual(1, len(actual_task_output))
    start_time, end_time = actual_task_output[0]
    ut.assertGreaterEqual(start_time, task.release_time)
    ut.assertLessEqual(end_time, task.deadline)
    ut.assertEqual(task.execution_time, end_time - start_time)

def check_task_constraints(ut, task_list, output_dict):
    """
    Verify constraints for each individual task are satisfied
    """
    for task in task_list:
        ut.assertIsInstance(task, RealTimeTask)
        if isinstance(task, PeriodicRealTimeTask):
            check_periodic_task_constraints(ut, task, output_dict[task.taskId])
        else: # isinstance(task, DynamicRealTimeTask)
            check_dynamic_task_constraints(ut, task, output_dict[task.taskId])

def check_task_overlap(ut, output_dict, context_switch_overhead):
    """
    Verifys that no tasks overlap and the
    context switching overhead is not violated
    """
    execution_time = get_total_execution_time(output_dict)
    task_execution_list = [0] * (execution_time + context_switch_overhead)
    for _, execution_times in output_dict.items():
        for start_time, end_time in execution_times:
            for i in range(start_time, end_time + context_switch_overhead):
                task_execution_list[i] += 1
    task_execution_list.sort()
    ut.assertLessEqual(task_execution_list[-1], 1)

def check(ut, task_list, context_switch_overhead, plot=False):
    output = get_rtos_static_schedule(task_list, context_switch_overhead)

    check_task_constraints(ut, task_list, output)
    check_task_overlap(ut, output, context_switch_overhead)

    if plot == True:
        plot_graphical_representation(output)

class RtosStaticSchedulingTest(unittest.TestCase):

    def test_simple_periodic(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=10, period=5)
        task_list = [p1]

        check(self, task_list, context_switch_overhead=1)

    def test_periodic_with_nontrivial_end_time(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=8, period=5)
        task_list = [p1]

        check(self, task_list, context_switch_overhead=1)
    
    def test_periodic_single_repetition(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=8, end_time=13, period=10)
        task_list = [p1]

        check(self, task_list, context_switch_overhead=5)

    def test_periodic_context_switching_violation(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=10, period=5)
        task_list = [p1]

        with self.assertRaises(NoRtosStaticScheduleProducible):
            check(self, task_list, context_switch_overhead=3)
    
    def test_intertwined_periodic(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=15, period=7)
        p2 = PeriodicRealTimeTask("P2", start_time=4, execution_time=2, end_time=15, period=7)
        task_list = [p1, p2]

        check(self, task_list, context_switch_overhead=1)

    def test_intertwined_periodic_with_violation(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=15, period=7)
        p2 = PeriodicRealTimeTask("P2", start_time=4, execution_time=2, end_time=15, period=7)
        task_list = [p1, p2]

        with self.assertRaises(NoRtosStaticScheduleProducible):
            check(self, task_list, context_switch_overhead=2)

    def test_sequential_periodic(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=15, period=7)
        p2 = PeriodicRealTimeTask("P2", start_time=15, execution_time=2, end_time=30, period=4)
        task_list = [p1, p2]
        
        check(self, task_list, context_switch_overhead=2)

    def test_sequential_periodic_with_violation(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=17, period=7)
        p2 = PeriodicRealTimeTask("P2", start_time=15, execution_time=2, end_time=30, period=4)
        task_list = [p1, p2]

        with self.assertRaises(NoRtosStaticScheduleProducible):
            check(self, task_list, context_switch_overhead=2)
    
    def test_simple_dynamic(self):
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=1, deadline=6)
        task_list = [d1]
        
        check(self, task_list, context_switch_overhead=1)

    def test_two_dynamic_tasks_with_same_release_time(self):
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=2, deadline=3)
        d2 = DynamicRealTimeTask("D2", release_time=0, execution_time=2, deadline=6)
        task_list = [d1, d2]
        
        check(self, task_list, context_switch_overhead=2)

    def test_two_dynamic_tasks_with_same_release_time_but_violation(self):
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=3, deadline=6)
        d2 = DynamicRealTimeTask("D2", release_time=0, execution_time=3, deadline=6)
        task_list = [d1, d2]
        
        with self.assertRaises(NoRtosStaticScheduleProducible):
            check(self, task_list, context_switch_overhead=2)

    def test_consecutive_dynamic_tasks(self):
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=2, deadline=3)
        d2 = DynamicRealTimeTask("D2", release_time=1, execution_time=2, deadline=6)
        d3 = DynamicRealTimeTask("D3", release_time=2, execution_time=3, deadline=10)
        task_list = [d1, d2, d3]
        
        check(self, task_list, context_switch_overhead=1)

    def test_consecutive_dynamic_tasks_with_violation(self):
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=2, deadline=3)
        d2 = DynamicRealTimeTask("D2", release_time=1, execution_time=2, deadline=6)
        d3 = DynamicRealTimeTask("D3", release_time=2, execution_time=3, deadline=6)
        task_list = [d1, d2, d3]

        with self.assertRaises(NoRtosStaticScheduleProducible):
            check(self, task_list, context_switch_overhead=1)

    def test_dynamic_between_periodic_repetitions(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=12, period=7)
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=2, deadline=6)
        task_list = [p1, d1]

        check(self, task_list, context_switch_overhead=1)

    def test_multiple_dynamic_between_periodic_repetitions(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=20, period=10)
        p2 = PeriodicRealTimeTask("P2", start_time=5, execution_time=2, end_time=25, period=9)
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=1, deadline=10)
        d2 = DynamicRealTimeTask("D2", release_time=10, execution_time=2, deadline=30)
        d3 = DynamicRealTimeTask("D3", release_time=0, execution_time=2, deadline=30)
        task_list = [p1, p2, d1, d2, d3]
        random.shuffle(task_list)

        check(self, task_list, context_switch_overhead=1)

    def test_multiple_dynamic_between_periodic_repetitions_with_violation(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=20, period=10)
        p2 = PeriodicRealTimeTask("P2", start_time=5, execution_time=2, end_time=25, period=9)
        d1 = DynamicRealTimeTask("D1", release_time=0, execution_time=1, deadline=10)
        d2 = DynamicRealTimeTask("D2", release_time=10, execution_time=2, deadline=15)
        d3 = DynamicRealTimeTask("D3", release_time=0, execution_time=2, deadline=25)
        task_list = [p1, p2, d1, d2, d3]
        random.shuffle(task_list)

        with self.assertRaises(NoRtosStaticScheduleProducible):
            check(self, task_list, context_switch_overhead=1)

    def test_complex_sitution(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=50, period=10)
        p2 = PeriodicRealTimeTask("P2", start_time=5, execution_time=2, end_time=100, period=10)
        p3 = PeriodicRealTimeTask("P3", start_time=60, execution_time=3, end_time=80, period=9)
        p4 = PeriodicRealTimeTask("P4", start_time=80, execution_time=2, end_time=120, period=10)
        d1 = DynamicRealTimeTask("D1", release_time=100, execution_time=5, deadline=120)
        d2 = DynamicRealTimeTask("D2", release_time=0, execution_time=6, deadline=100)
        d3 = DynamicRealTimeTask("D3", release_time=20, execution_time=1, deadline=50)
        d4 = DynamicRealTimeTask("D4", release_time=60, execution_time=4, deadline=120)
        task_list = [p1, p2, p3, p4, d1, d2, d3, d4]
        random.shuffle(task_list)

        check(self, task_list, context_switch_overhead=1)

    def test_complex_sitution_with_violation(self):
        p1 = PeriodicRealTimeTask("P1", start_time=0, execution_time=3, end_time=50, period=10)
        p2 = PeriodicRealTimeTask("P2", start_time=5, execution_time=2, end_time=100, period=10)
        p3 = PeriodicRealTimeTask("P3", start_time=60, execution_time=3, end_time=80, period=9)
        p4 = PeriodicRealTimeTask("P4", start_time=80, execution_time=2, end_time=120, period=10)
        d1 = DynamicRealTimeTask("D1", release_time=100, execution_time=5, deadline=120)
        d2 = DynamicRealTimeTask("D2", release_time=0, execution_time=6, deadline=100)
        d3 = DynamicRealTimeTask("D3", release_time=20, execution_time=1, deadline=50)
        d4 = DynamicRealTimeTask("D4", release_time=60, execution_time=4, deadline=100)
        task_list = [p1, p2, p3, p4, d1, d2, d3, d4]
        random.shuffle(task_list)

        with self.assertRaises(NoRtosStaticScheduleProducible):
            check(self, task_list, context_switch_overhead=1)

if __name__ == "__main__":
    unittest.main() 
