import os, subprocess

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

        output_str += f"No output produced\n" if not result.stdout or result.stderr else f"STDOUT: {result.stdout} STDERR: {result.stderr}\n"

        return output_str

    except Exception as e:
        return f"Error: executing Python file: {e}"
