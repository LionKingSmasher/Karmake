class LibrarySetting:
    def __init__(self, execution_program : str = ''):
        self.execution_program = execution_program
        pass

    def get_execution_program(self) -> str:
        return self.execution_program