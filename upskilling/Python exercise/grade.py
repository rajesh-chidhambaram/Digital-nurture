def grade(score):

    if score < 0 or score > 100:
        print("Invalid Score")

    elif score >= 90:
        print("Grade A")

    elif score >= 70:
        print("Grade B")

    else:
        print("Grade C")

score = 88
grade(score)