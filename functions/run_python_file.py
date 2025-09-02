import os
import subprocess
import sys

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
        
        command = [sys.executable, full_file_path] + args
        
        output = subprocess.run(command, capture_output=True, text=True, timeout=30, check=False)
        output_parts = []

        if output.stdout.strip():
            output_parts.append("STDOUT: " + output.stdout.strip())
        if output.stderr.strip():
            output_parts.append("STDERR: " + output.stderr.strip())

        if output.returncode != 0:
            output_parts.append(f"Process exited with code {output.returncode}")

        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)    
        
    except Exception as e:
        raise Exception(f"Error: executing Python file: {e}")