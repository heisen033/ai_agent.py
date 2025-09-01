def run_python_file(working_directory, file_path, args=[]):
    try:
        combined_path = os.path.join(working_directory, file_path)
        full_file_path = os.path.abspath(combined_path)
        full_working_directory_path = os.path.abspath(working_directory)
        
        if not full_file_path.startswith(full_working_directory_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: File "{file_path}" not found.'
        if not full_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
    except Exception as e:
        raise Exception(f"Error: {e}")