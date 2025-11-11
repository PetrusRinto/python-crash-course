# Patrick 11.11.2025.
# 8-10 Sending Messages.

def send_message(unsent, sent):
    """
    Simulate sending a message.
    """
    while unsent:
        message = unsent.pop()
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

text = input("Send a message: ")
unsent = [text]
sent = []

send_message(unsent, sent)
sent_message(sent)