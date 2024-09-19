def calculate_bmi(weight, height):
    """Calculate BMI using weight in kg and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Determine category
category = bmi_category(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
