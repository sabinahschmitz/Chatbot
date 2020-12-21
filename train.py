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
'There are different kinds of discrimination. Gender, age, race, sexuality, religious belief. Which one would you like to talk about?',
'How do I approach my friend about bias',
'Think about...',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

trainer.train([
    'I would like to speak about racism',
    'Ok, let us talk about racism. Racism is not only prevelant amongst radical people, but also with people who do not consider themselves racist. What many minority groups fight against, is the superiority ethos that predominantly white people live by.',

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

