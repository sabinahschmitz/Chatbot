from chatterbot import ChatBot

# Create object of ChatBot class
bot = ChatBot('Maya',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')

response = bot.get_response('I want to learn more about discrimination')
print("Bot Response:", response)
