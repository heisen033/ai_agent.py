import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)

        if len(os.path.abspath(working_directory)) > len(os.path.abspath(full_path)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        directory_list = ""
        for entity in os.listdir(os.path.abspath(full_path)):
            entity_path = os.path.join(full_path, entity)
            directory_list += f'- {entity}: file_size={os.path.getsize(entity_path)} bytes, is_dir={os.path.isdir(entity_path)}\n'
        print(directory_list)
        return f"Result for {directory}:\n{directory_list}"
    except Exception as e:
        raise Exception(f"Error: {e}")

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)