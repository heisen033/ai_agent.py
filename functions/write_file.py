import os

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