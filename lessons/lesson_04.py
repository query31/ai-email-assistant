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

categories = []

for email in emails:
    category = classify_email(email)
    categories.append(category)

print(categories)

counts = {
    "ORDER": 0,
    "COMPLAINT": 0,
    "QUESTION": 0,
    "SPAM": 0
}
for category in categories:
    counts[category] += 1

print(counts)
