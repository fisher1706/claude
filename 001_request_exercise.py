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


def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=messages
    )

    return message.content[0].text

if __name__ == "__main__":
    my_messages = []

    
    while True:
        user_input = input("> ")
        print(user_input)

        add_user_message(my_messages, user_input)

        answer = chat(my_messages)
        add_assistant_message(my_messages, answer)

        print("---")

        print(answer)

        print("---")