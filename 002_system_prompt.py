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


def chat(messages, system=None, temperature=1.0):

    params = {
        "model": model,
        "max_tokens": 1024,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)

    return message.content[0].text


if __name__ == "__main__":
    my_messages = []

    system_prompt = """
        You are a patient math tutor.
        Do not directly answer a student`s questions.
        Guide them to a solution step by step.
        """

    add_user_message(my_messages, "How do I solve 5x+3=2 for x?")

    answer = chat(my_messages, system=system_prompt)
    print(f"\nanswer: {answer}")

    print("______________________________")

    answer = chat(my_messages)
    print(f"\nanswer: {answer}")
