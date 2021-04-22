from z3 import *
from rtos_static_scheduling_classes import *

def get_rtos_static_schedule(task_list, context_switch_overhead):
    # Split up Dynamic and Periodic Tasks
    periodic_task_list = []
    dynamic_task_list = []
    for i in range(len(task_list)):
        if isinstance(task_list[i], PeriodicRealTimeTask):
            periodic_task_list.append(task_list[i])
        elif isinstance(task_list[i], DynamicRealTimeTask):
            dynamic_task_list.append(task_list[i])

    # Individual Dynamic Task Constraints
    num_dynamic_tasks = len(dynamic_task_list)
    dynamic_start_times = [Int(f"d_ts_{i}") for i in range(num_dynamic_tasks)]
    dynamic_end_times = [Int(f"d_te_{i}") for i in range(num_dynamic_tasks)]
    dynamic_equations = []
    for i in range(num_dynamic_tasks):
        dynamic_equations.extend([
            dynamic_start_times[i] >= dynamic_task_list[i].release_time,
            dynamic_end_times[i] == dynamic_start_times[i] + dynamic_task_list[i].execution_time,
            dynamic_end_times[i] <= dynamic_task_list[i].deadline
        ])
    
    # Individual Periodic Task Constraints
    num_periodic_tasks = len(periodic_task_list)
    all_periodic_start_times = [0] * num_periodic_tasks
    all_periodic_end_times = [0] * num_periodic_tasks
    periodic_equations = []
    for i in range(num_periodic_tasks):
        task = periodic_task_list[i]
        num_repetitions = int((task.end_time - task.start_time) / task.period)
        if (task.start_time + (num_repetitions * task.period) + task.execution_time) <= task.end_time:
            num_repetitions += 1
        periodic_start_times = [Int(f"p_ts_{i}_{j}") for j in range(num_repetitions)]
        periodic_end_times = [Int(f"p_te_{i}_{j}") for j in range(num_repetitions)]
        for j in range(num_repetitions):
            periodic_equations.extend([
                periodic_start_times[j] == task.start_time + (j * task.period),
                periodic_end_times[j] == periodic_start_times[j] + task.execution_time
            ])
        all_periodic_start_times[i] = periodic_start_times
        all_periodic_end_times[i] = periodic_end_times
    
    # Task Relationship Constraints
    # Dynamic Task relationships with all other Dyanmic Tasks and Periodic Tasks
    relationship_equations = []
    for i in range(num_dynamic_tasks):
        fixed_start_time = dynamic_start_times[i]
        fixed_end_time = dynamic_end_times[i]
        for j in range(i + 1, num_dynamic_tasks):
            variable_start_time = dynamic_start_times[j]
            variable_end_time = dynamic_end_times[j]
            relationship_equations.append(
                Or(fixed_start_time >= variable_end_time + context_switch_overhead,
                    fixed_end_time + context_switch_overhead <= variable_start_time)
            )
        for j in range(num_periodic_tasks):
            periodic_start_times = all_periodic_start_times[j]
            periodic_end_times = all_periodic_end_times[j]
            num_repetitions = len(periodic_start_times)
            for k in range(num_repetitions):
                variable_start_time = periodic_start_times[k]
                variable_end_time = periodic_end_times[k]
                relationship_equations.append(
                    Or(fixed_start_time >= variable_end_time + context_switch_overhead,
                        fixed_end_time + context_switch_overhead <= variable_start_time)
                )

    # Periodic Task relationships with other Periodic Tasks
    for i in range(num_periodic_tasks):
        fixed_periodic_start_times = all_periodic_start_times[i]
        fixed_periodic_end_times = all_periodic_end_times[i]
        fixed_num_repetitions = len(fixed_periodic_start_times)
        for j in range(fixed_num_repetitions):
            fixed_start_time = fixed_periodic_start_times[j]
            fixed_end_time = fixed_periodic_end_times[j]

            # Compare repetition with other repetitions within the same periodic task
            for l in range(j + 1, fixed_num_repetitions):
                variable_start_time = fixed_periodic_start_times[l]
                variable_end_time = fixed_periodic_end_times[l]
                relationship_equations.append(
                    Or(fixed_start_time >= variable_end_time + context_switch_overhead,
                        fixed_end_time + context_switch_overhead <= variable_start_time)
                )
            
            # Compare with other periodic tasks and their corresponding repetitions
            for k in range(i + 1, num_periodic_tasks):
                variable_periodic_start_times = all_periodic_start_times[k]
                variable_periodic_end_times = all_periodic_end_times[k]
                variable_num_repetitions = len(variable_periodic_start_times)
                for l in range(variable_num_repetitions):
                    variable_start_time = variable_periodic_start_times[l]
                    variable_end_time = variable_periodic_end_times[l]
                    relationship_equations.append(
                        Or(fixed_start_time >= variable_end_time + context_switch_overhead,
                            fixed_end_time + context_switch_overhead <= variable_start_time)
                    )

    # Solve constraints with Z3 solver
    s = Solver()
    s.add(dynamic_equations + periodic_equations + relationship_equations)
    if s.check() == sat:
        m = s.model()
    else:
        raise NoRtosStaticScheduleProducible()

    # Create output dictionary
    output = dict()
    for i in range(num_dynamic_tasks):
        taskId = dynamic_task_list[i].taskId
        start_time = m.eval(dynamic_start_times[i]).as_long()
        end_time = m.eval(dynamic_end_times[i]).as_long()
        output[taskId] = [(start_time, end_time)]
    for i in range(num_periodic_tasks):
        taskId = periodic_task_list[i].taskId
        output[taskId] = []
        task_start_times = all_periodic_start_times[i]
        task_end_times = all_periodic_end_times[i]
        num_repetitions = len(task_start_times)
        for j in range(num_repetitions):
            start_time = m.eval(task_start_times[j]).as_long()
            end_time = m.eval(task_end_times[j]).as_long()
            output[taskId].append((start_time, end_time))
    
    return output