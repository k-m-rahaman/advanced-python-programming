import datetime

name = None

def get_time_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

print("🤖 SmartBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    # Greeting
    if user in ["hello", "hi", "hey"]:
        print(f"Bot: {get_time_greeting()}!")

    # Ask name
    elif "my name is" in user:
        name = user.split("my name is")[-1].strip()
        print(f"Bot: Nice to meet you, {name}!")

    elif "what is my name" in user:
        if name:
            print(f"Bot: Your name is {name}.")
        else:
            print("Bot: I don't know your name yet.")

    # Basic conversation
    elif "how are you" in user:
        print("Bot: I'm doing great! How about you?")

    elif "your name" in user:
        print("Bot: I'm SmartBot, your Python assistant 🤖")

    # Math feature (simple)
    elif "add" in user:
        try:
            nums = [int(s) for s in user.split() if s.isdigit()]
            print("Bot: Result =", sum(nums))
        except:
            print("Bot: Couldn't calculate.")

    # Time feature
    elif "time" in user:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", now)

    # Help
    elif "help" in user:
        print("""
Bot Commands:
- hello / hi
- my name is <name>
- what is my name
- how are you
- add numbers (e.g., add 5 10)
- time
- bye
        """)

    # Exit
    elif user == "bye":
        print("Bot: Goodbye! Have a great day 👋")
        break

    # Default
    else:
        print("Bot: Hmm... I didn't understand that. Type 'help' to see options.")