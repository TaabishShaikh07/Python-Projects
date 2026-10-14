import datetime
import time

name = input("Enter Your Name")
presenthour = datetime.datetime.now().hour

if 5 <= presenthour <= 11:
    print("Good Morning: ", name)
elif 12 <= presenthour <= 17:
    print("Good Afternoon: ", name)
elif 18 <= presenthour <= 20:
    print("Good Evening: ", name)
else:
    print("Good Night: ", name)

print("Welcome To The AI Chatbot")
print("Ask Me The Basic Question Or Type 'Bye' To Exit")

responses = {
     "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
    "functions kya hote hai": "jakar chapter 7 padho"
}

def responseofBot(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
        return "I am not able to tell that yet. Mai jald hi ye sikh lunga" 
    
while True:
    userinput = input("Enter Your Question")
    reply = responseofBot(userinput)
    print("Bot Response: ", reply)

    if "bye" in userinput.lower():
     break