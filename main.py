#package tests for complex structured telegram bots, written in python
#author: Lynnsane

#imports
import asyncio
import commandhandling as command

async def main():
    print('started service succesfully')
    #dictionary object that represents an incoming message, to be expanded upon to support multiple events.
    incomingEvent = dict([("messageType", "command"), ("messageText", "/start"), ("sender", "User"), ("from_id", "1337"), ("chat_id", "12")])
    if incomingEvent["messageType"] == "command":
        await command.callCommands(incomingEvent)

if __name__ == "__main__":
    asyncio.run(main())