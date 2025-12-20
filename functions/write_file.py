import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_working_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_path, file_path))
        valid_target_file = os.path.commonpath([abs_working_path, target_file]) == abs_working_path

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'


        os.makedirs(os.path.dirname(target_file), exist_ok = True)

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: failed to write file content: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write over a file in a specified file path relative to the working directory, deleting all the old content of the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="[REQUIRED] Path to file to overwrite, relative to the working directory, if the file o the folders in the path doesnt exist, they are automatically made",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="[REQUIRED] content to overwrite into the file",
            ),
        },
        required=["file_path", "content"]
    ),
)
