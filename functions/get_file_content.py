
import os
from config import FILE_CONTENTS_LIMIT

def get_file_content(working_directory, file_path):
    try:
        combined_path = os.path.join(working_directory, file_path)
        full_file_path = os.path.abspath(combined_path)
        full_working_directory_path = os.path.abspath(working_directory)
        
        if not full_file_path.startswith(full_working_directory_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_file_path, "r") as f:
            content = f.read()

        if len(content) > FILE_CONTENTS_LIMIT:
            file_content_string = content[:FILE_CONTENTS_LIMIT] + f'[...File "{file_path}" truncated at {FILE_CONTENTS_LIMIT} characters]'
        else:
            file_content_string = content

        return file_content_string
    
    except Exception as e:
        raise Exception(f"Error: {e}")