import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
import argparse


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) > 1:
        messages = [
            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
        ]

        generated_content = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
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
