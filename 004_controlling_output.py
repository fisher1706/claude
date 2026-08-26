from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()


client = Anthropic()
model = "claude-sonnet-4-5"


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stop_sequences=None):

    params = {
        "model": model,
        "max_tokens": 1024,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)

    return message.content[0].text


if __name__ == "__main__":
    my_messages = []

    add_user_message(my_messages, "Generate a very short event bridge rule as json")
    add_assistant_message(my_messages, "```json")

    print(my_messages)

    answer = chat(my_messages, stop_sequences=["```"])
    print(f"\nanswer: {answer}")


