# Arsha/views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, "index.html")

# def BMI(request):
#     bmi_result = None
#     if request.method == 'POST':
#         weight = float(request.POST.get('weight'))
#         height = float(request.POST.get('height')) /100
#         bmi = weight / (height * height)
#         bmi_result = round(bmi, 2)
#     return render(request, "output.html", {"bmi_result": bmi_result})
from django.shortcuts import render

def BMI(request):
    bmi_result = None
    bmi_warning = None
    bmi_difference = None
    weight_difference = None

    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height')) / 100  # Convert cm to meters

        # Calculate BMI (BMI = weight(kg) / height^2(m^2))
        bmi = weight / (height * height)
        bmi_result = round(bmi, 2)

        # Define BMI ranges and corresponding warnings
        bmi_ranges = [
            (float('-inf'), 16.99, "Dangerous Low"),
            (17.0, 18.49, "Low"),
            (18.5, 24.99, "Healthy"),
            (25.0, 29.99, "Medium Risk"),
            (30.0, 34.99, "High Risk"),
            (35.0, float('inf'), "Dangerous High")
        ]

        # Find the corresponding warning for the calculated BMI
        for lower, upper, warning in bmi_ranges:
            if lower <= bmi <= upper:
                bmi_warning = warning
                break

        # Calculate the difference from the healthy BMI range
        if 18.5 <= bmi <= 24.99:
            bmi_difference = 0
        elif bmi < 18.5:
            bmi_difference = round(18.5 - bmi, 2)
        else:
            bmi_difference = round(bmi - 24.99, 2)

        # Calculate the difference in weight required to reach the healthy BMI range
        if bmi_difference != 0:
            target_bmi = 18.5
            target_weight = target_bmi * (height * height)
            weight_difference = round(target_weight - weight, 2)

    return render(request, "output.html", {
        'bmi_result': bmi_result,
        'bmi_warning': bmi_warning,
        'bmi_difference': bmi_difference,
        'weight_difference': weight_difference
    })



