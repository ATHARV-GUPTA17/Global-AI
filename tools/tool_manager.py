from tools.file_tool import *
from tools.project_tool import *
from tools.code_tool import *

class ToolManager:

    def create_project(self,name):
        return create_project(name)

    def generate_code(self,prompt):
        return generate_code(prompt)

    def write(self,path,content):
        return write_file(path,content)

    def read(self,path):
        return read_file(path)