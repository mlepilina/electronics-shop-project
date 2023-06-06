from src.item import Item


class MixinLang:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Метод изменения языка. Язык по умолчанию (при инициализации) - английский (`EN`).
        Всего поддерживается два языка: `EN` и `RU`.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

        return self


class Keyboard(MixinLang, Item):
    """Клавиатура"""
