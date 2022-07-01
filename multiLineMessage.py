
from message import Message


class MultiLineMessage(object):


    def __init__(self, message=Message("")):
        self._myMessages=[]
        if message.texte!="":
            self._myMessages.append([message])


    @property
    def myMessages(self):
        return self._myMessages

    def __add__(self, messages):
        if isinstance(messages, Message):
            self._myMessages.append([messages])
        elif isinstance(messages, MultiLineMessage):
            self._myMessages.extend(messages.myMessages)
        elif isinstance(messages, str):
            self._myMessages.append(Message(messages))


    def __mul__(self, message):
        self._myMessages[-1]=self._myMessages[-1].append(message)