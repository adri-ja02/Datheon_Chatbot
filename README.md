# Rule-Based Interactive Terminal Chatbot

## Project Overview

This project is a rule-based interactive chatbot developed using Python. It acts as a simple customer support assistant that responds to user queries using predefined keywords, regular expressions, and FAQ data.

The chatbot can answer questions about business hours, product information, delivery, returns, payments, warranties, and customer support. It also supports multiple intents in a single message and provides fallback responses for unrecognized queries.

## Features

- **Greeting Recognition:** Responds to greetings such as hello, hi, and hey.
- **Business Hours:** Provides information about opening and closing hours.
- **Product FAQs:** Answers predefined questions about delivery, returns, payments, warranties, and products.
- **Contact Information:** Provides customer support contact details.
- **Multi-Intent Recognition:** Handles multiple supported topics in one message.
- **Fallback Handling:** Gives a helpful response when it cannot recognize a question.
- **Exit Commands:** Ends the conversation when the user types `bye`, `exit`, or `quit`.
- **Error Handling:** Handles missing or invalid FAQ data and unexpected terminal interruptions.

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- JSON (`json`)
- pathlib (`pathlib`)

## Project Structure

```text
task4-chatbot/
├── chatbot.py
├── faq.json
└── README.md
```

### File Description

- `chatbot.py`: Contains the chatbot logic, intent recognition, response generation, and error handling.
- `faq.json`: Stores business information and predefined frequently asked questions.
- `README.md`: Documents the project and explains how to run it.

## Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another code editor.
- A terminal or command prompt.

No additional Python packages are required because the project uses built-in Python libraries.

## How to Run the Project

1. Download or clone the project repository.
2. Open the project folder in Visual Studio Code.
3. Make sure `chatbot.py` and `faq.json` are in the same folder.
4. Open the integrated terminal by selecting **Terminal → New Terminal**.
5. Run the following command:

```bash
python chatbot.py
```

If the command does not work on Windows, try:

```bash
py chatbot.py
```

6. Type a question and press Enter to interact with the chatbot.
7. Type `bye`, `exit`, or `quit` to end the conversation.

## Example Interaction

```text
Welcome to TechStore Assistant!
Ask about business hours, products, or support.
Type 'bye', 'exit', or 'quit' to leave.

You: hello
Bot: Hello! Welcome to TechStore.

You: How long does delivery take?
Bot: Standard delivery usually takes 3 to 5 business days.

You: What are your business hours?
Bot: Monday to Saturday, 9:00 AM to 8:00 PM. Sunday is closed.

You: bye
Bot: Thank you for chatting. Goodbye!
```

*Note: The example responses assume the sample business information in `faq.json`.*

## Customization

You can customize the chatbot by editing `faq.json`. Update the business name, operating hours, contact information, and FAQ entries to suit your preferred business.

Each FAQ entry contains keywords, a question, and an answer. The chatbot uses the keywords to identify relevant user queries.

## Limitations

- Responses are based on predefined rules rather than machine learning.
- The chatbot cannot reliably answer questions outside its configured topics.
- Its responses depend on the keywords and FAQ information provided.
- It does not connect to a live database or external customer support system.

## Future Improvements

- Add more FAQ categories and keyword patterns.
- Improve typo handling and intent recognition.
- Add automated unit tests.
- Develop a graphical user interface.
- Connect the chatbot to a product database.

## Author

Developed a Rule-Based Interactive Terminal Assistant / Chatbot.
