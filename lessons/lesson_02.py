emails = [
    "Where is my order?",
    "I want a refund",
    "What are your opening hours?"
]

for email in emails:
    message = email.lower()

    if "order" in message:
        category = "ORDER"
    elif "refund" in message:
        category = "COMPLAINT"
    else:
        category = "QUESTION"
    print(category)