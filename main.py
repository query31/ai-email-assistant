emails = [
    "Where is my order?",
    "I want a refund",
    "What are your opening hours?",
    "Can I return this product?",
    "Where is my refund for the order?",
    "I want to cancel my order",
    "Can I cancel my subscription?",
    "You won a free prize!",
    "Click here to claim your reward"
]

def classify_email(message):
    message = message.lower()
    if "free" in message or "prize" in message or "reward" in message:
        return "SPAM"
    elif "refund" in message or "return" in message or "cancel" in message:
        return "COMPLAINT"
    elif "order" in message:
        return "ORDER"
    else:
        return "QUESTION"


def classify_emails(emails):
    categories = []
    for email in emails:
        category = classify_email(email)
        categories.append(category)
    return categories


def count_categories(categories):
    counts = {
        "ORDER": 0,
        "COMPLAINT": 0,
        "QUESTION": 0,
        "SPAM": 0
    }
    for category in categories:
        counts[category] += 1

    return counts


def create_response(category):
    if category == "SPAM":
        return "This message was classified as spam and will not be processed."
    elif category == "COMPLAINT":
        return "We are sorry to hear about your issue. Our support team will review it."
    elif category == "ORDER":
        return "Thank you for contacting us about your order. We will review your request."
    else:
        return "Thank you for your question. Our support team will get back to you soon."


def run_demo():
    print("Demo classification")
    print("-------------------")
    categories = classify_emails(emails)

    for number, (email, category) in enumerate(zip(emails, categories), start=1):
        print(f"{number}: {email} => {category}")

    counts = count_categories(categories)
    print("\nDemo category counts")
    for category in counts:
        print(category, counts[category])


def run_assistant():
    print("\nAI Email Assistant")
    print("------------------")
    print("Enter 'quit' as the sender to end the session.\n")

    records = []
    counts = count_categories([])

    while True:
        sender = input("Sender (or 'quit'): ").strip()
        if sender.lower() == "quit":
            print("Exiting the program.")
            break

        if sender == "":
            print("Please enter a sender.\n")
            continue

        subject = input("Subject: ").strip()
        if subject == "":
            print("Please enter a subject.\n")
            continue
        message = input("Message: ").strip()

        if message == "":
            print("Please enter a message.\n")
            continue

        new_category = classify_email(message)
        counts[new_category] += 1

        response = create_response(new_category)
        email_record = {
            "sender": sender,
            "subject": subject,
            "message": message,
            "category": new_category,
            "response": response
        }
        records.append(email_record)
        print(f"\nCategory: {new_category}")
        print(f"Response: {response}")
        print(f"Updated counts: {counts}\n")

    print("\nSession records")
    print("---------------")
    if not records:
        print("No emails were processed.")
    else:
        for record in records:
            print(
                f"Sender: {record['sender']}, Subject: {record['subject']}, "
                f"Message: {record['message']}, Category: {record['category']}, "
                f"Response: {record['response']}"
            )

if __name__ == "__main__":
    run_assistant()
