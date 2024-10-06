percentage = float(input())

if percentage < 40:
    print('Fail')
elif percentage >= 40 and percentage < 50:
    print("Passed in Third Division")
elif percentage >= 50 and percentage < 60:
    print("Passed in Second Division")
elif percentage >= 60 and percentage < 75:
    print("Passed in First Division")
elif percentage >= 75 and percentage < 90:
    print("Passed in First Division with Distinction")
elif percentage >= 95 and percentage <= 100:
    print("Congratulations! You're in Merit List")


