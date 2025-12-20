import os
from config import MAXCHARS


def get_file_content(working_directory, file_path):
    try:
        abs_working_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_path, file_path))
        valid_target_file = os.path.commonpath([abs_working_path, target_file]) == abs_working_path

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'



        with open(target_file, "r") as f:
            file_content = f.read(MAXCHARS)

            if f.read(1):
                file_content += f'[ ...file "{file_path}" truncated at {MAXCHARS} characters ]'

        return file_content

    except Exception as e:
        return f"Error: failed to read file content: {e}"

