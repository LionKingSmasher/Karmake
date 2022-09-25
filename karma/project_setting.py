class ProjectSetting:
    def __init__(self, project_name : str = "", project_version : str = ""):
        self.project_name    = project_name
        self.project_version = project_version
    
    def get_project_name(self) -> str:
        return self.project_name

    def get_project_version(self) -> str:
        return self.project_version