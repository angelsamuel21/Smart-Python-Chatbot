def chatbot():
    import random
    import datetime
    import wikipedia as wp
    from wikipedia.exceptions import DisambiguationError, PageError
    import qrcode as qr
    import os

    print("🤖 Bot: Hello! Type 'menu' to see what I can do, or 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # Greeting logic based on time
        current_hour = datetime.datetime.now().hour
        if user_input in ["hello", "hi", "hey", "hmm", "hm"]:
            if 5 <= current_hour < 12:
                greeting = "Good morning! ☀️"
            elif 12 <= current_hour < 18:
                greeting = "Good afternoon! 🌤"
            else:
                greeting = "Good evening! 🌙"

            responses = [
                f"Bot: Hey there! {greeting} How are you today?",
                f"Bot: Hello! {greeting} How can I help you?",
                f"Bot: Hi! {greeting} What would you like to do today?",
            ]
            print(random.choice(responses))

        # Sad response
        elif user_input in ["sad", "feeling sad", "not happy", "bad day"]:
            comforting_lines = [
                "Use today as a pause, not a stop. You’re stronger than you think. 💪",
                "Even cloudy days bring rainbows later. 🌈",
                "It’s okay to not be okay. Better days are already on their way. 🌤",
                "You’ve survived 100% of your bad days so far — that’s a perfect record! 💯",
                "One bad day can’t erase all your good moments. Keep going. 🌻"
            ]
            print(random.choice(comforting_lines))

        # Menu section
        elif "menu" in user_input:
            print("\n📜 Here's what I can do:\n")
            print("1. Learn anything using Wikipedia")
            print("2. Solve basic math problems")
            print("3. Read motivational quotes")
            print("4. Create QR codes")
            print("5. Know current date & time")
            print("6. Generate OTP")
            print("7. Calculate your age\n")

        # Learn topic
        elif "learn" in user_input:
            topic = input("Enter topic name: ").title()
            try:
                summary = wp.summary(topic, sentences=3)
                print(f"\n📚 Here's what I found about '{topic}':\n{summary}\n")
            except DisambiguationError as e:
                print("This topic is ambiguous. Try one of these options:", e.options[:5])
            except PageError:
                print("Sorry, I couldn't find that topic. Please try again.")
            except Exception:
                print("Sorry, something went wrong. Please try again.")

        # Current date and time
        elif "date" in user_input or "time" in user_input:
            now = datetime.datetime.now()
            print("📅 Current Date and Time:", now.strftime("%A, %d %B %Y - %I:%M %p"))

        # Solve math problems (using safe eval)
        elif "solve" in user_input or "math" in user_input:
            print("\n🧮 You can solve any simple math expression here.")
            expression = input("Enter Expression (e.g., 2+3*4): ")
            try:
                # Safe eval: only math operations, no built-ins
                result = eval(expression, {"__builtins__": None}, {})
                print("✅ Result:", result)
            except Exception:
                print("❌ Invalid expression. Please try again.")

        # Quotes
        elif "quote" in user_input or "motivate" in user_input:
            quotes = [
                "Believe in yourself and all that you are! 🌟",
                "The harder you work, the luckier you get.",
                "Push yourself — no one else is going to do it for you.",
                "Great things never come from comfort zones.",
                "Dream big, start small, act now! 🚀"
            ]
            print("💡 Quote of the Day:", random.choice(quotes))

        # Calculate age
        elif "age" in user_input:
            try:
                birth_year = int(input("Enter your birth year (e.g., 2003): "))
                current_year = datetime.datetime.now().year
                age = current_year - birth_year
                print(f"🎂 You are approximately {age} years old.")
            except ValueError:
                print("❌ Please enter a valid year.")

        # Create QR code
        elif "qr" in user_input or "createqr" in user_input:
            data = input("Enter data for QR: ")
            filename = input("Enter filename (without extension): ") + ".png"
            qr_img = qr.make(data)
            qr_img.save(filename)
            print("✅ QR saved successfully.")
            print("📁 Saved at:", os.path.abspath(filename))

        # Generate OTP
        elif "otp" in user_input or "generateotp" in user_input:
            otp = random.randint(100000, 999999)
            print("🔐 Your OTP is:", otp)

        # Exit
        elif user_input in ["bye", "exit", "quit", "q"]:
            print("👋 Thank you for using my chatbot! Have a great day!")
            break

        # Unknown input
        else:
            unsure_responses = [
                "Hmm, I didn’t quite get that. Try 'menu' to see what I can do.",
                "Sorry, I’m still learning. Maybe try another keyword?",
                "I’m not sure how to respond to that, but I’m here to help!",
            ]
            print(random.choice(unsure_responses))


# Run chatbot
chatbot()
