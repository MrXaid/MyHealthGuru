from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def bothome(request):
    return render(request, "chatbot.html")
    
def getResponse(request):
    userMessage = request.GET.get('userMessage', '')
    chatId = int(request.GET.get('chatId'))
    chatEnded = bool(request.GET.get('chatEnded', False))
    chatHistory = request.GET.get('chatHistory', '[]')
    botResponse = f"Chatbot response to '{userMessage}' (Chat ID: {chatId})"
    # Set chatEnded flag based on your logic
    if chatId >= 3:
        chatEnded = True

    # Return the chatbot response and chatEnded flag to the frontend
    response_data = {
        'botResponse': botResponse,
        'chatEnded': chatEnded
    }

    return JsonResponse(response_data)