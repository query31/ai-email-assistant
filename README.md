# AI Email Assistant

A beginner-friendly Python project that classifies email messages and creates a simple response.

## Features

- Classifies messages into four categories:
  - `SPAM`
  - `COMPLAINT`
  - `ORDER`
  - `QUESTION`
- Handles uppercase and lowercase text with `lower()`.
- Counts categories during a user session.
- Creates a response based on the detected category.
- Stores each processed email in a session record.
- Accepts multiple emails until the user enters `quit`.
- Validates empty sender and message input.

## How to run

From the project directory, run:

```bash
python3 main.py
```

The program starts the interactive assistant directly. The optional `run_demo()`
function remains in `main.py` for testing and learning purposes.

For each email, enter:

1. Sender
2. Subject
3. Message

Enter `quit` as the sender to end the session.

## Example

```text
Sender (or 'quit'): customer@example.com
Subject: Refund request
Message: I want a refund

Category: COMPLAINT
Response: We are sorry to hear about your issue. Our support team will review it.
```

## Classification rules

| Keywords | Category |
|---|---|
| `free`, `prize`, `reward` | `SPAM` |
| `refund`, `return`, `cancel` | `COMPLAINT` |
| `order` | `ORDER` |
| No matching keyword | `QUESTION` |

When a message contains keywords from multiple categories, the first matching rule wins. The current priority is:

```text
SPAM > COMPLAINT > ORDER > QUESTION
```

## Python topics practiced

- Lists
- Dictionaries
- `if / elif / else`
- `for` and `while` loops
- Functions with `def`
- `return`
- `input()`
- String methods such as `lower()` and `strip()`
- `append()`
- `zip()`
- `enumerate()`
- f-strings
- `break` and `continue`
- The `if __name__ == "__main__":` pattern
