from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

Chatbot = ChatBot( 
    "bro",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {'import_path': 'chatterbot.logic.BestMatch',
         'default_response': 'i do not understand :(',
         'maximum_similarity_threshold':0.90
        }
    ],
    database_uri='sqlit:///database.sqle3')

exit_conditions= ("quit","exite","goodbye","bye")
while True:
    query = input("> ")
    if query in exit_conditions: break
    else:
        print(f"know it all:{ChatBot.get_response(query)}")