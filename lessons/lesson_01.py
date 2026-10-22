email = {
    "sender": "customer@gmail.com",
    "subject": "Problem with my order",
    "message": "Hello, my order has not arrived yet."   
}

message = email["message"].lower()

if "refund" in message:
    category = "COMPLAINT"
elif "order" in message:
    category = "ORDER"
else:
    category = "QUESTION"

print(category)
