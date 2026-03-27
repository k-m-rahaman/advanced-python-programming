questions = {
    "Capital of India?": "Delhi",
    "5 + 3 = ?": "8",
    "Python is a language? (yes/no)": "yes"
}

score = 0

for q, ans in questions.items():
    user = input(q + " ")
    if user.lower() == ans.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Final Score:", score)
