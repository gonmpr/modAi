import os, argparse
from dotenv import load_dotenv
from google import genai




def get_response(client, prompt):


    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )

    if response.usage_metadata is None:
        raise RuntimeError('FAILED API REQUEST: get_response() function error')

    response_and_meta = {'response': response.text,
                         'prompt_tokens': response.usage_metadata.prompt_token_count,
                         'response_tokens': response.usage_metadata.candidates_token_count,
                        }
    return response_and_meta







def main():

    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError('API KEY NOT FOUND')

    client = genai.Client(api_key=api_key)


    input_parser = argparse.ArgumentParser(description='modAi is a agentic Ai that screw up your proyects')
    input_parser.add_argument('user_prompt', type=str, help='expecting user prompt')
    args = input_parser.parse_args()
    prompt = args.user_prompt

    response = get_response(client,prompt)

    print('User prompt:', prompt)
    print('Prompt tokens:',response['prompt_tokens'])
    print('Response tokens:',response['response_tokens'])
    print('Response:',response['response'])

if __name__ == "__main__":
    main()
