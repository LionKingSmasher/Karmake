#!/usr/bin/env python3
from karma.execution_setting import ExecutionSetting
from karma.karmake import Karmake
from karma.project_setting import ProjectSetting

if __name__ == "__main__":
    prj_setting = ProjectSetting('test_karmake', '20220925')
    exec_setting = ExecutionSetting('/usr/bin/gcc')
    make = Karmake()

    make.set_execution_setting(exec_setting)
    make.set_project_setting(prj_setting)
    make.add_execution('test', ['main.c', 'test.c'])