from aiogram.dispatcher.filters import Filter
from aiogram.types import Message
from data.texts import Texts


class IsIn(Filter):

    def __init__(self, my_text: str) -> None:
        # get uz,ru,en translations
        self.my_text = Texts().get_list(my_text)

    async def check(self, message: Message):
        # check if text is in the list
        return message.text in self.my_text
