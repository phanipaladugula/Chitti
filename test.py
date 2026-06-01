from agent import get_reply

while True:
    text=input("User: ")
    if text=="exit":
        break
    print("AI: ",get_reply(text))
