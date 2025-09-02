import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
import argparse
from config import system_prompt
from call_function import available_functions, call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    messages = [types.Content(role="user", parts=[types.Part(text=sys.argv[1])])]
    for i in range(20):
        try:
            
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", 
                contents=messages, 
                config=types.GenerateContentConfig(
                    tools=[available_functions], 
                    system_instruction=system_prompt
                    ),
                )
            # for candidate in response.candidates:
            #     messages.append(candidate.content)
                
            if response.text:
                print(f"Final response: {response.text}")
                break
            
            if response.function_calls:
                for function_call in response.function_calls:
                    function_result = call_function(function_call, verbose=True)
                    
                    messages.append(function_call)
                    messages.append(function_result)
                    
                    print(f"Function output: {function_result.parts[0].function_response.response}")
                        
                if "--verbose" in sys.argv:
                    # print(f"User prompt: {sys.argv[1]}")
                    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                    print("Response tokens:", response.usage_metadata.candidates_token_count)
        except Exception as e:
            print(f"Error during iteration {i+1}: {e}")
    else:
        print("Max iterations reached (20) without a final response.")
    


if __name__ == "__main__":
    main()
