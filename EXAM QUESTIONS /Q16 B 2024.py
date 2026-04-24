#Please enter name:Oskaras Piskorowski

from datetime import datetime

prompt = input("Please enter prompt:")

if prompt.__contains__("Hello") prompt.__contains__("hello"):
    print("Hi there, how are you?")
elif prompt.__contains__("Name") or prompt.__contains__("name"):
    print("My name is ExamBot, how can I help?")
elif prompt.__contains__("Time") or prompt.__contains__("time"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
elif prompt.__contains__("Weather") or prompt.__contains__("weather"):
    print("It is always sunny in Ireland")
else:
    print('Im sorry, I dont know that one')
