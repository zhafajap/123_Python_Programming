def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()

        print(f"Sending message: {current_message}")

        sent_messages.append(current_message)


messages = [
    "Keep learning!",
    "Never give up!",
    "Practice makes perfect!"
]

sent_messages = []

send_messages(messages[:], sent_messages)

print("\nOriginal messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)