#!/usr/bin/env python3
from karma.execution_setting import ExecutionSetting
from karma.karmake import Karmake
from karma.project_setting import ProjectSetting
from karma.library_setting import LibrarySetting

if __name__ == "__main__":
    prj_setting = ProjectSetting('test_karmake', '20220925')
    exec_setting = ExecutionSetting('/usr/bin/gcc')
    library_setting = LibrarySetting('/usr/bin/gcc-ar')
    make = Karmake()

    make.set_execution_setting(exec_setting)
    make.set_library_setting(library_setting)
    make.set_project_setting(prj_setting)
    make.add_library('test', ['a.c', 'b.c'])