async def command(eventObject):
    return print("Welcome to my lab, {} ".format(eventObject["sender"]))