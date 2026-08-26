from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()


client = Anthropic()
model = "claude-sonnet-5"


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stream=True):

    params = {
        "model": model,
        "max_tokens": 1024,
        "messages": messages,
        "temperature": temperature,
        "stream": stream
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)

    return message


def chat_stream(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1024,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        params["system"] = system

    with client.messages.stream(**params) as stream:
        for text in stream.text_stream:
             print(text, end="")

        print("-----------------------")

        final_message = stream.get_final_message()
        print(final_message)



if __name__ == "__main__":
    my_messages = []

    add_user_message(my_messages, "Write a one sentence description of a fake database")

    my_stream = chat(my_messages)

    for event in my_stream:
        print(event)

    print("-----------------------")

    chat_stream(my_messages)

