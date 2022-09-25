from genericpath import isfile
from karma.project_setting import ProjectSetting
from karma.execution_setting import ExecutionSetting
import os

class Karmake:
    def __init__(self):
        self.prj_setting = ProjectSetting()
        self.exec_setting = ExecutionSetting()
        pass

    def set_project_setting(self, prj_setting : ProjectSetting) -> bool:
        if len(prj_setting.get_project_name()) == 0:
            return False
        elif len(prj_setting.get_project_version()) == 0:
            return False
        
        self.prj_setting = prj_setting

        return True

    def set_execution_setting(self, exec_setting : ExecutionSetting) -> bool:
        if len(exec_setting.get_execution_program()) == 0:
            return False
        
        self.exec_setting = exec_setting
        return True
    
    def add_execution(self, output : str, source_file : list) -> bool:
        executionFile = self.exec_setting.get_execution_program()
        executionArg  = self.exec_setting.get_execution_arguments()
        objFiles = list()

        for i in source_file:
            object_file, _ = os.path.splitext(i)
            object_file = '{0}.o'.format(object_file)
            pid = os.fork()
            if pid == 0:
                os.execv(executionFile, [executionFile, i, '-c', '-o', object_file])
            else:
                os.wait()
            objFiles.append(object_file)
            print('[Object Compile] {0} => {1} '.format(i, object_file), end='')
            if os.path.isfile('{0}/{1}'.format(os.getcwd(), object_file)):
                print('Complete!!')
            else:
                print('Failed....')
                return False
            pass

        pid = os.fork()
        if pid == 0:
            os.execv(executionFile, [executionFile, '-o', output] + objFiles)
        else:
            os.wait()
        
        print('[Program Compile] Compile \'{0}\'... '.format(output), end='')
        if os.path.isfile('{0}/{1}'.format(os.getcwd(), output)):
            print('Complete!!')
        else:
            print('Failed....')
            return False
        return True