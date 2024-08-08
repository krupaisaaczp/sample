import json
from django.shortcuts import render
from django.http import JsonResponse
from sklearn.externals import joblib
from .models import ChatHistory

# Load pre-trained model and vectorizer
model = joblib.load('chatbot/models/chatbot_model.pkl')
vectorizer = joblib.load('chatbot/models/vectorizer.pkl')

def index(request):
    return render(request, 'index.html')

def get_response(request):
    if request.method == 'POST':
        user_input = json.loads(request.body).get('message')
        vectorized_input = vectorizer.transform([user_input])
        prediction = model.predict(vectorized_input)[0]
        
        response = {
            'message': prediction
        }
        
        # Save to chat history
        if request.user.is_authenticated:
            ChatHistory.objects.create(user=request.user, message=user_input)
        
        return JsonResponse(response)
