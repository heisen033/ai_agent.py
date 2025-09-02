import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
import argparse
from config import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

def main():
    if len(sys.argv) > 1:
        messages = [
            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
        ]

        generated_content = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages, 
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
            )
        if generated_content.function_calls:
            for function_call in generated_content.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")
        print(generated_content.text)
        if "--verbose" in sys.argv:
            print(f"User prompt: {sys.argv[1]}")
            print("Prompt tokens:", generated_content.usage_metadata.prompt_token_count)
            print("Response tokens:", generated_content.usage_metadata.candidates_token_count)
    else:
        print("Error: Something went wrong.", file=sys.stderr)
        sys.exit(1)
    


if __name__ == "__main__":
    main()
