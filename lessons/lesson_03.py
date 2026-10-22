emails = [
    "Where is my order?",
    "I want a refund",
    "What are your opening hours?",
    "Can I return this product?",
    "Where is my refund for the order?",
    "I want to cancel my order",
    "Can I cancel my subscription?"
]

def classify_email(message):
    message = message.lower()

    if "refund" in message or "return" in message or "cancel" in message:
        return "COMPLAINT"
    elif "order" in message:
        return "ORDER"
    else:
        return "QUESTION"
for email in emails:
    category = classify_email(email)
    print(category)