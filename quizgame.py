import time

# List of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. Jane Austen", "C. Mark Twain", "D. William Shakespeare"],
        "answer": "D"
    }
]

# Initialize score
score = 0
answers_given = []

# Welcome message
print("🧠 Welcome to the Quiz Game!")
print("-----------------------------\n")

# Main quiz loop
for idx, q in enumerate(questions, 1):
    print(f"Q{idx}: {q['question']}")
    for option in q['options']:
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    while user_answer not in ['A', 'B', 'C', 'D']:
        user_answer = input("Please enter a valid option (A/B/C/D): ").strip().upper()
    
    is_correct = user_answer == q['answer']
    answers_given.append({
        "question": q['question'],
        "your_answer": user_answer,
        "correct_answer": q['answer'],
        "result": "Correct" if is_correct else "Wrong"
    })

    if is_correct:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.\n")
    
    time.sleep(1)  # Short pause between questions

# Final score
print("\n🎉 Quiz Over!")
print(f"Your final score is: {score}/{len(questions)}\n")

# Review answers
print("📋 Answer Review:")
print("------------------")
for idx, ans in enumerate(answers_given, 1):
    print(f"Q{idx}: {ans['question']}")
    print(f"Your Answer: {ans['your_answer']} | Correct Answer: {ans['correct_answer']} | Result: {ans['result']}")
    print()

