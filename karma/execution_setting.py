from multiprocessing.dummy import Array


class ExecutionSetting:
    def __init__(self, execution_program : str = '', execution_arguments : list = []):
        self.execution_program = execution_program
        self.execution_arguments = execution_arguments
        pass

    def get_execution_program(self) -> str:
        return self.execution_program
    
    def get_execution_arguments(self) -> list:
        return self.execution_arguments