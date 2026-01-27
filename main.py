import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types, errors

from prompts import system_prompt
from call_function import available_functions


def print_verbose(args, usage):
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    

def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0
        )
    )
    if not response.usage_metadata:
        raise RuntimeError("No usage metadata returned from Gemini API")
    usage = response.usage_metadata

    if args.verbose:
        print_verbose(args, usage)
    
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print("Response:")
        print(response.text)


if __name__ == "__main__":
    main()