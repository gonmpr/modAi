import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def generate_content(client, messages, args=None):

    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=messages,
    )
    if response.usage_metadata is None:
        raise RuntimeError('FAILED API REQUEST: TIME EXCEED')



    if args.verbose:
        print('User prompt:', args.user_prompt)
        print('Prompt tokens:',response.usage_metadata.prompt_token_count)
        print('Response tokens:',response.usage_metadata.candidates_token_count)

    print('Response:',response.text)




def main():

    input_parser = argparse.ArgumentParser(description='modAi is a agentic Ai that screw up your proyects')
    input_parser.add_argument('user_prompt', type=str, help='expecting user prompt')
    input_parser.add_argument('--verbose', action="store_true", help='Enable verbose output')
    args = input_parser.parse_args()


    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError('API KEY NOT FOUND')

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    generate_content(client, messages, args)


if __name__ == "__main__":
    main()
