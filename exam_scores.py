# exam_scores.py

def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def provide_feedback(average):
    if average >= 85:
        print("Feedback: Excellent")
    elif 70 <= average < 85:
        print("Feedback: Good")
    else:
        print("Feedback: Needs Improvement")

def main():
    score1 = float(input("Enter your score for Subject 1: "))
    score2 = float(input("Enter your score for Subject 2: "))
    score3 = float(input("Enter your score for Subject 3: "))

    average = calculate_average(score1, score2, score3)
    print(f"Your average score is: {average:.2f}")
    provide_feedback(average)

if __name__ == "__main__":
    main()
