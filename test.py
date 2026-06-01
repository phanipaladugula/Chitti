from agent import get_reply

while True:
    message=input("User: ")
    if message=="exit":
        break
    print("AI: ",get_reply(message))
