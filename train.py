from chatbot import bot
from chatterbot.trainers import ChatterBotCorpusTrainer
# Import ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'How are you?',
'Cannot complain, I am a bot',
'How smart are you?',
'As smart as you make me',
'I want to learn more about discrimination',
'Please tell me more',
'What is discrimination',
'Discrimination is..',
'How do I approach my friend about bias',
'Think about...',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

name = input("What's your name?: ")
print("Welcome to the Maya's Unbias Bot! Let me know how can I help you?")
while True:
    request = input(name+':')
    if request == 'Bye' or request == 'bye':
        print('Maya: Bye')
        break
    else: 
        response=bot.get_response(request)
        print('Maya:',response)

#comment

