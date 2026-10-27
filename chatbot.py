
import json
import re
from pathlib import Path


# ---------- Terminal Colors ----------
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
BLUE = "\033[94m"


# ---------- Load FAQ Data ----------
def load_faq_data():
    file_path = Path(__file__).parent / "faq.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"{RED}Error: faq.json was not found.{RESET}")
        return {"greetings": [], "faqs": []}

    except json.JSONDecodeError:
        print(f"{RED}Error: faq.json contains invalid JSON.{RESET}")
        return {"greetings": [], "faqs": []}


data = load_faq_data()


# ---------- Display Design ----------
def show_header():
    print(CYAN + BOLD)
    print("=" * 55)
    print("          DATHEON INTERNSHIP ASSISTANT")
    print("=" * 55)
    print(RESET)
    print("  Welcome! I am your virtual support assistant.")
    print("  Ask me about internships, submissions, or certificates.")
    print(f"\n  {YELLOW}Type 'help' to see topics or 'exit' to quit.{RESET}")
    print(CYAN + "-" * 55 + RESET)


def show_topics():
    print(f"\n{BLUE}{BOLD} AVAILABLE TOPICS {RESET}")
    print("-" * 35)
    print("  1. Business hours")
    print("  2. Internship project submission")
    print("  3. Certificate delivery")
    print("  4. General greetings")
    print("-" * 35)


def display_response(response):
    print(f"\n{GREEN}{BOLD}  ASSISTANT{RESET}")
    print(f"  {GREEN}{response}{RESET}")
    print(CYAN + "-" * 55 + RESET)


# ---------- Chatbot Logic ----------
def get_response(user_input):
    text = re.sub(r"\s+", " ", user_input.lower()).strip()

    if not text:
        return "Please enter a question so I can help you."

    if re.fullmatch(r"(exit|quit|bye)", text):
        return None

    if text == "help":
        show_topics()
        return "Choose a topic and ask me a question."

    # Greeting recognition
    greetings = data.get("greetings", [])

    for greeting in greetings:
        pattern = r"\b" + re.escape(greeting.lower()) + r"\b"

        if re.search(pattern, text):
            return (
                "Hello! Welcome to Datheon Internship Support. "
                "How can I help you today?"
            )

    # FAQ keyword matching
    faqs = data.get("faqs", [])

    keywords = {
        "hours": [
            "hours", "operation", "operating hours",
            "open", "opening time", "closing time"
        ],
        "submission": [
            "submit", "submission", "github", "repository",
            "project link", "student workspace"
        ],
        "certificate": [
            "certificate", "certificates", "code review",
            "receive my certificate", "certificate delivery"
        ]
    }

    for topic, topic_keywords in keywords.items():
        if any(keyword in text for keyword in topic_keywords):
            for faq in faqs:
                question = faq.get("question", "").lower()

                if topic == "hours" and "hours" in question:
                    return faq.get("answer", "Answer unavailable.")

                if topic == "submission" and (
                    "submit" in question or "project" in question
                ):
                    return faq.get("answer", "Answer unavailable.")

                if topic == "certificate" and (
                    "certificate" in question
                ):
                    return faq.get("answer", "Answer unavailable.")

    # Match a complete FAQ question if possible
    for faq in faqs:
        question = faq.get("question", "").lower()

        if text in question or question in text:
            return faq.get("answer", "Answer unavailable.")

    return (
        "Sorry, I couldn't understand your question.\n"
        "Try asking about business hours, project submission, "
        "or certificates. Type 'help' for the topic list."
    )


# ---------- Main Program ----------
def main():
    show_header()

    while True:
        try:
            user_input = input(f"\n{CYAN}{BOLD}  YOU > {RESET}").strip()
            response = get_response(user_input)

            if response is None:
                print(f"\n{YELLOW}{BOLD}")
                print("  Thank you for using Datheon Assistant!")
                print("  Goodbye! Have a great day.")
                print(RESET)
                print(CYAN + "=" * 55 + RESET)
                break

            display_response(response)

        except (KeyboardInterrupt, EOFError):
            print(f"\n{YELLOW}\n  Chat session ended. Goodbye!{RESET}")
            break

        except Exception as error:
            print(f"\n{RED}  An error occurred: {error}{RESET}")


if __name__ == "__main__":
    main()
