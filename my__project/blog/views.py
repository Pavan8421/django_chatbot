from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot =ChatBot('chatbot',read_only=False,
                logic_adapters=[
                    {
                    
                    'import_path':'chatterbot.logic.BestMatch',
                    #'default_response':'Sorry I dont know what that means',
                    #'maximun_similarity_thresold':0.90
                    
                    }])

list_to_train =[
    "hi",
    "hi,there",
    "What's your name?",
    "I am just a chatbot",
    "What's your fav food",
    "I like nothing",
    "what's your fav sport",
    "I like all sports",
    "do you have children",
    "no"
]

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request,'blog/index.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
