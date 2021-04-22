class RealTimeTask():

    def __init__(self, taskId=None, execution_time=None):
        self.taskId = taskId
        self.execution_time = execution_time

class PeriodicRealTimeTask(RealTimeTask):

    def __init__(self, taskId=None, start_time=None, execution_time=None, end_time=None, period=None):
        super().__init__(taskId, execution_time)
        self.start_time = start_time
        self.period = period
        self.end_time = end_time

class DynamicRealTimeTask(RealTimeTask):

    def __init__(self, taskId=None, release_time=None, execution_time=None, deadline=None):
        super().__init__(taskId, execution_time)
        self.release_time = release_time
        self.deadline = deadline

class NoRtosStaticScheduleProducible(Exception):
    pass