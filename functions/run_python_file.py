import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):

    try:
        abs_working_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_path, file_path))
        valid_target_file = os.path.commonpath([abs_working_path, target_file]) == abs_working_path

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)

        output_str = str()

        if result.returncode != 0:
            output_str += f"Process exited with code {result.returncode}\n"

        output_str += f"No output produced\n" if not (result.stdout or result.stderr) else f"STDOUT: {result.stdout} STDERR: {result.stderr}\n"

        return output_str

    except Exception as e:
        return f"Error: executing Python file: {e}"




schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run a python file in a specified file path relative to the working directory,returning a string informing results of execution",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="[REQUIRED] path to python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items= types.Schema(
                    type=types.Type.STRING,
                ),
                description="[OPTIONAL] Arguments passed to the python file to execute, like 'python example.py [args]' ",
            ),
        },
        required=["file_path"]
    ),
)
