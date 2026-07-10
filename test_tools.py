from tools.tool_manager import ToolManager

tm = ToolManager()

project = tm.create_project(
    "AI Phishing SaaS"
)

print(project)

code = tm.generate_code(
    "Write hello world in python"
)

print(code)