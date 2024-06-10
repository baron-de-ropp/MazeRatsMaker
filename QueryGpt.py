import openai
client = openai.OpenAI()


def query_chatgpt(messages, temperature=0.8, return_json=False):
    max_retries = 3

    for retry in range(max_retries):
        try:
            request_params = {
                'model': 'gpt-4o',
                'messages': messages,
                'temperature': temperature,
                'max_tokens': 2048
            }

            if return_json:
                request_params['response_format'] = { "type": "json_object" }

            response = client.chat.completions.create(**request_params)
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            if retry == max_retries - 1:
                raise e


def main():
    message = [{"role": "user", "content": f"Are you there? Respond with 'y' or 'n' now."}]
    print(query_chatgpt(message))


if __name__ == "__main__":
    main()