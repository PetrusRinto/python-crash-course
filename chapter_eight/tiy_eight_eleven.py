# Patrick 11.11.2025.
# 8-11 Archived Messages.

def send_message(send, sent):
    """
    Simulate sending a message.
    """
    while send:
        message = send.pop()
        print(f"\nSending message:\n{message}")
        sent.append(message)

def sent_message(sent):
    """
    Simulating the messages being sent.
    """
    print("\nThe following messages has been sent:")
    # Looping the messages being sent.
    for message in sent:
        print(f"{message}\n")

send = ["This is a message to all digital entities"]
sent = []

print("\n---WITH COPY---")
print(f"Message currently in sending list:\n{send}")
send_message(send[:], sent)
print(f"\nThe same list after:\n{send}")

print("\n---WITHOUT COPY---")
print(f"Message currently in sending list:\n{send}")
send_message(send, sent)
print(f"\nThe same list after:\n{send}")