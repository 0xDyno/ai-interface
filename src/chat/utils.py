import environ

import openai as ai

from main.utils import load_openai_key

env = environ.Env()
env.read_env("config/.env")


@load_openai_key
def get_answer(prompt, model, temp):
    if model == env("DAVINCI3"):
        max_tokens = 4000
    elif model == env("DAVINCI2"):
        max_tokens = 8000
    else:
        max_tokens = 2000
    
    try:
        response = ai.Completion.create(model=model, prompt=prompt,
                                        temperature=convert_temp(temp), max_tokens=max_tokens)
        return response.choices[0].text
    except (ai.InvalidRequestError, ai.error.RateLimitError) as error:
        return f"Error: {error.error['message']}"
    except ai.OpenAIError:
        return "Sorry, unknown error happened. Try again later or contact support."


def convert_temp(temp):
    """from 100 to 1 & 1 to 0.01, also checks it"""
    if temp > 100:
        temp = 100
    if temp < 0:
        temp = 0
    return temp / 100
    