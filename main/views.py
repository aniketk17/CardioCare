from django.shortcuts import render
from django.contrib import messages

from joblib import load
model = load('./savedModels/model.joblib')

def home(request):
  return render(request,'homePage.html')

def form_view(request):
  return render(request,'form.html')

def result_view(request):
  if request.method == "POST":
    data = request.POST
    age = float(data.get('age'))
    gender = float(data.get('gender'))
    chest_pain = float(data.get('cp'))
    resting_bp = float(data.get('resting_bp'))
    cholesterol = float(data.get('cholesterol'))
    fasting_blood_sugar = float(data.get('fasting_blood_sugar'))
    resting_ecg = float(data.get('resting_ecg'))
    max_heart_rate = float(data.get('max_heart_rate'))
    exercise_angina = float(data.get('exercise_angina'))
    oldpeak = float(data.get('oldpeak'))
    st_slope = float(data.get('st_slope'))
    
    input_data = [[age, gender, chest_pain, resting_bp, cholesterol, fasting_blood_sugar,
                    resting_ecg, max_heart_rate, exercise_angina, oldpeak, st_slope,0,0]]
    
    prediction = model.predict(input_data)
    print(prediction)
    if not prediction:
        messages.success(request, "No presence of heart disease.")
    else:
        messages.error(request, "We're sorry to inform, but our prediction indicates you might be suffering from a heart disease.")
    
    return render(request, 'result.html')



