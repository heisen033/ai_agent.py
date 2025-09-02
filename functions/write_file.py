import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        combined_path = os.path.join(working_directory, file_path)
        full_file_path = os.path.abspath(combined_path)
        full_working_directory_path = os.path.abspath(working_directory)
        
        if not full_file_path.startswith(full_working_directory_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        dir_path = os.path.dirname(full_file_path)

        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
                
            with open(full_file_path, "w") as f:
                f.write(content)
                
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        raise Exception(f"Error: {e}")
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to file to be overwritten or created, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be filled in or overwritten into file"
            )
        },
    ),
)