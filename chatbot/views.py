from django.shortcuts import render, HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only = True, 
              preprocessors=['chatterbot.preprocessors.convert_to_ascii', 
                             'chatterbot.preprocessors.unescape_html',
                             'chatterbot.preprocessors.clean_whitespace'],
             logic_adapters = [
                 {
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'Sorry, I am unable to process your request. Please try again, or contact us for help.',
                     'maximum_similarity_threshold': 0.90
                 }
             ],)

list_to_train = [
    "hii",
    "hello",
    "What are types of heart disease?",
    "1. Arrhythmia\n2. Coronary artery disease\n3. Heart failure\n4. Heart attack\n5. Congenital heart disease\n6. Heart valve disease\n7. Angina\n8. Aortic disease\n9. Atherosclerosis\n10. Cardiomyopathy\n11. Peripheral arterial disease\n12. Stroke\n13. Atrial Fibrillation\n14. Pulmonary hypertension are types of heart disease.",
    "What is Arrhythmia?",
    "Arrhythmias are irregularities in the heartbeat, including when it is too fast or too slow.",
    "What are symptoms of Arrhythmia?",
    "Symptoms may include palpitations, feeling a pause between heartbeats, lightheadedness, passing out, shortness of breath, chest pain, or decreased level of consciousness.",
    "What are treatments for Arrhythmia?",
    "Treatments may include medications, pacemaker insertion, surgery, or urgent treatment with cardioversion or defibrillation.",
    "What are remedies for Arrhythmia?",
    "Remedies include reducing high blood pressure, controlling cholesterol levels, losing excess weight, eating a heart-healthy diet, avoiding tobacco smoke and vaping, and enjoying regular physical activity."
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def chat_bot(request):
    return render(request, 'chatbot.html')

def get_response(request):
    userMessage = request.GET.get('userMessage')
    response = bot.get_response(userMessage)
    return HttpResponse(response)

