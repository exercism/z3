# Instructions

This problem is modeled after real-time operating system non-preemptive static 
scheduling, but is also similar to the Job-Shop Scheduling Problem (JSP) with 
only one resource.  This problem assumes that all tasks are known statically.  In 
other words, the release times of all tasks in this problem are known at the beginning 
of the program.  In practice, the release time of tasks are not known at the start of a 
program, and may be generated at any time through I/O, interrupts, etc.

Given a list of tasks with parameters, determine a schedule in which
the tasks can execute sequentially with no overlap.  Since the problem is modeled 
after RTOS process scheduling, we will assume there is a nonzero time required between 
tasks, also known as the context-switching overhead. There are two different types 
of tasks: periodic and dynamic.  Both types have a task ID parameter which is a
string used to differentiate between the different tasks in the task list.

A **periodic task** is defined as a task that executes periodically.  In other words,
the task will execute once every T seconds where T is defined as the period.
A periodic task is defined by the following parameters:
* Start Time - time the first repetition, or instance, of the task starts
* Period - time between the start of the task repetitions
* Execution Time - time each repetition runs for 
* End Time - time the entire task stops getting scheduled

A **dynamic task** is defined as a task that only executes once.
A dynamic task is defined by the following parameters:
* Release Time - first time the task CAN be scheduled (NOT the same as start time)
* Execution Time - time the task runs for 
* Deadline - time in which the task must finish execution by

There are two inputs to the function to be implemented.  The first input is a list of
instances of `RealTimeTask`.  Instances of `RealTimeTask` will either be input as
an instance of `PeriodicRealTimeTask` or `DynamicRealTimeTask` with all task parameters as integers.  
The `isinstance()` built-in Python function can be used to differentiate between the two tasks 
in the list.  The order of the list is irrelevant; look only at the parameters of the tasks.  
The second input is a single integer that specifies the context switching overhead.  The context
switching overhead will always be a non-negative integer.

The output should be a dictionary where the keys are the task ID from RealTimeTask
instances, and the value should be a list of two-tuples.  The format of the two-tuples
are (start time, end time).  Dynamic tasks should only contain one two-tuple in the list,
while periodic tasks may contain more than one.  The order of the two-tuples in the list
does not matter.  If a valid schedule cannot be created from list of the tasks with the 
given context switching overhead, raise a `NoRtosStaticScheduleProducible` exception.  Note 
that the Z3 model results for variables will need to be converted to ints before being output.  If 
the Z3 model result is of type `IntNumRef`, the `as_long()` class method may be used to convert 
to an integer.

An additional function is provided to allow the user to visualize the sequential order
of the tasks.  This function can also be enabled for individual test cases by setting the
`plot` keyword argument to `True` in the `check()` function. A broken horizontal bar plot is 
used to graph and label each task. In order to utilize this function, the Python library 
*matplotlib* must be installed.  Installation details for *matplotlib* can be found 
[here](https://matplotlib.org/stable/users/installing.html).