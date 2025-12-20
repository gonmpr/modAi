import os
from google.genai import types

def get_files_info(working_directory, directory='.'):
    try:
        abs_working_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_path, directory))
        valid_target_dir = os.path.commonpath([abs_working_path, target_dir]) == abs_working_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'



        files_in_dir = []

        for file in os.listdir(target_dir):
            path_to_file = os.path.normpath(os.path.join(target_dir, file))
            file_size = os.path.getsize(path_to_file)
            is_dir = os.path.isdir(path_to_file)
            files_in_dir.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")


        return "\n".join(files_in_dir)

    except Exception as e:
        return f'Error: listing files: {e}'



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="[REQUIRED] Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),

        },
        required=["directory"]
    ),
)
