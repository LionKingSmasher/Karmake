from dbm.ndbm import library
from genericpath import isfile
from .project_setting import ProjectSetting
from .execution_setting import ExecutionSetting
from .library_setting import LibrarySetting
from .run_external_file import *
import os

def object_compile(exec_program : str, source_file : list, objFiles : list) -> bool:
    for i in source_file:
        object_file, _ = os.path.splitext(i)
        object_file = '{0}.o'.format(object_file)
        pid = os.fork()
        if pid == 0:
            os.execv(exec_program, [exec_program, i, '-c', '-o', object_file])
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

def is_file_exist(file : str) -> bool:
    return os.path.isfile('{0}/{1}'.format(os.getcwd(), file))

class Karmake:
    def __init__(self):
        self.prj_setting = ProjectSetting()
        self.exec_setting = ExecutionSetting()
        self.library_setting = LibrarySetting()
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
    
    def set_library_setting(self, lib_setting : LibrarySetting) -> bool:
        if len(lib_setting.get_execution_program()) == 0:
            return False
        
        self.library_setting = lib_setting
    
    def add_execution(self, output : str, source_file : list) -> bool:
        executionFile = self.exec_setting.get_execution_program()
        executionArg  = self.exec_setting.get_execution_arguments()
        objFiles = list()

        if object_compile(executionFile, source_file, objFiles) == False:
            return False
        run_external_file(executionFile, [executionFile, '-o', output] + objFiles)
        
        print('[Program Compile] Compile \'{0}\'... '.format(output), end='')
        if is_file_exist(output):
            print('Complete!!')
        else:
            print('Failed....')
            return False
        return True
    
    def add_library(self, library_name : str, source_files : list) -> bool:
        executionFile = self.exec_setting.get_execution_program()
        library_file = self.library_setting.get_execution_program()
        output_file = 'lib{0}.a'.format(library_name)
        objFiles = list()

        if object_compile(executionFile, source_files, objFiles) == False:
            return False
        run_external_file(library_file, [library_file, 'crv', output_file] + objFiles)
        print('[Library Make] Make \'{0}\'... '.format(output_file), end='')
        if is_file_exist(output_file):
            print('Complete!!')
        else:
            print('Failed....')
            return False
        return True