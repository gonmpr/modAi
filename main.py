import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSPROMPT
from available_functions import available_functions, call_function



def get_content(usr_input, args=None):
    messages = [types.Content(role="user", parts=[types.Part(text=usr_input)])]


    def generate_content(client):
        nonlocal messages
        nonlocal args

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=SYSPROMPT
                )
        )
        if response.usage_metadata is None:
            raise RuntimeError('FAILED API REQUEST: TIME EXCEED')




        if response.candidates:
            for model_response in response.candidates:
                messages.append(model_response.content)






        calls_response = list()

        if response.function_calls:
            for function_call in response.function_calls:

                called_function = call_function(function_call, True if args.verbose else False)


                if not called_function.parts[0].function_response.response:
                    raise Exception('Error: Fatal error while calling function, response is None')
                else:
                    calls_response.append(called_function.parts[0])

                if args.verbose:
                    print(f"-> {called_function.parts[0].function_response.response}")

        if calls_response:
            messages.append(types.Content(role="user", parts=calls_response))



        if args.verbose:
            print('User prompt:', args.user_prompt)
            print('Prompt tokens:',response.usage_metadata.prompt_token_count)
            print('Response tokens:',response.usage_metadata.candidates_token_count)


        if response.text and not response.function_calls:
            return response.text




    return generate_content




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


    content = get_content(args.user_prompt, args)


    limit = 0



    while limit<20:
        try:
            response = content(client)

            if response:
                print('\n--------------------------------------------\n')
                print('Final response:',response)
                break

            limit += 1

        except Exception as e:
            print(f"Error: fail calling response in while: {e}")


if __name__ == "__main__":
    main()
