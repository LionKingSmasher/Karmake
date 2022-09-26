import os

def run_external_file(execution_program : str = '', arguments : list = []):
    pid = os.fork()
    if pid == 0:
        os.execv(execution_program, arguments)
    else:
        os.wait()