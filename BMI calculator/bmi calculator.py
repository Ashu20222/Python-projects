def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_status(bmi):
    if bmi < 18.5:
        return " Underweight "
    elif 18.5 <= bmi < 25:
        return " Normal "
    elif 25 <= bmi < 30:
        return " Overweight "
    else:
        return " Obese "

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
status = bmi_status(bmi)
print("Your BMI is: ", bmi)
print("Your BMI status is: ", status)

if status == "Underweight":
    print("You should eat more and maintain a healthy diet")
elif status == "Normal":
    print("You are in a good shape, Keep up the good work!")
elif status == "Overweight":
    print("You should exercise more and maintain a healthy diet")
else:
    print("You should consult a doctor and maintain a healthy diet")
