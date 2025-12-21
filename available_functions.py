from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file

available_functions = types.Tool(
    function_declarations=[
                           schema_get_files_info,
                           schema_get_file_content,
                           schema_write_file,
                           schema_run_python_file,
                          ],
)

function_names = {
    'get_files_info': get_files_info,
    'get_file_content': get_file_content,
    'write_file': write_file,
    'run_python_file': run_python_file,
}

def call_function(function_call, verbose=False):
    global function_names

    if function_call.name not in function_names:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response={"error": f"Unknown function: {function_call.name}"},
            )
        ],
    )


    function_result = function_names[function_call.name](working_directory='./calculator', **function_call.args)



    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")




    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call.name,
            response={"result": function_result},
        )
    ],
)
