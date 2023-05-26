from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from language import language
from utils import format, getEmoj
class keyboards():
    def __init__(self, setLang = 0):
        self.localization = language(setLang)
        _, self.keyboardLang = self.localization.getText()  # Получаение требоваемой локализации
    def changeLocalization(self, state):
        self.localization.setLanguage(state)  # Получаение русской локализации
        _, self.keyboardLang = self.localization.getText()

    def mainKeyboard(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(self.keyboardLang['me_request']), KeyboardButton(self.keyboardLang['to_request']))
        markup.row(KeyboardButton(self.keyboardLang['settings']))
        return markup
    def resetKeyboard(self): # goto /start
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(KeyboardButton(self.keyboardLang['reset_key']))
        return markup
    def adminKeyboard(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(KeyboardButton(self.keyboardLang['admin_hotlinemiami']))
        markup.row(KeyboardButton(self.keyboardLang['admin_load']), KeyboardButton(self.keyboardLang['admin_stats']))
        markup.row(KeyboardButton(self.keyboardLang['admin_uedit']))
        markup.row(KeyboardButton(self.keyboardLang['reset_key']))
        return markup
    def admin_load(self): # goto /admin
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(KeyboardButton(self.keyboardLang['admin_load_stats']), KeyboardButton(self.keyboardLang['admin_load_geo']))
        markup.row(KeyboardButton(self.keyboardLang['admin_to_main']),KeyboardButton(self.keyboardLang['admin_load_product']))
        return markup
    def resetKeyboard_admin(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row( self.keyboardLang['admin_to_main'] )
        return markup
class inlineKeyboards():
    def __init__(self, setLang=0):
        self.localization = language(setLang)
        _, self.keyboardLang = self.localization.getText()  # Получаение требоваемой локализации

    def changeLocalization(self, state):
        self.localization.setLanguage(state)  # Получаение русской локализации
        _, self.keyboardLang = self.localization.getText()
    def settings(self, checkBox, country = 0):
        push = self.keyboardLang['push'][0] + " ✅" if checkBox[0] == 1 else self.keyboardLang['push'][0] + " ❌"
        news = self.keyboardLang['news'][0] + " ✅" if checkBox[1] == 1 else self.keyboardLang['news'][0] + " ❌"
        auth = self.keyboardLang['authorization'][0] + " ✅" if checkBox[2] != 0 else self.keyboardLang['authorization'][0]

        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
                    InlineKeyboardButton(push, callback_data=self.keyboardLang['push'][1]),
                    InlineKeyboardButton(news, callback_data=self.keyboardLang['news'][1])
                   )
        markup.add(InlineKeyboardButton(format(self.keyboardLang['set_lang'][0], { "langEmj" : getEmoj(country)}), callback_data=self.keyboardLang['set_lang'][1]))
        markup.add(InlineKeyboardButton(auth, callback_data=self.keyboardLang['authorization'][1]))
        return markup
    def language(self):
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton(self.keyboardLang['russian'][0],
                                        callback_data=self.keyboardLang['russian'][1]))
        markup.add(InlineKeyboardButton(self.keyboardLang['chinese'][0],
                                        callback_data=self.keyboardLang['chinese'][1]))
        markup.add(InlineKeyboardButton(self.keyboardLang['american'][0],
                                        callback_data=self.keyboardLang['american'][1]))
        markup.add(InlineKeyboardButton(self.keyboardLang['backto_settings'][0],
                                        callback_data=self.keyboardLang['backto_settings'][1]))
        return markup
    def closeMessage(self):
        # todo сделать обработку id что бы мы понимали какой тикет закрывать
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton(self.keyboardLang['close_ticket'][0],
                                        callback_data=self.keyboardLang['close_ticket'][1]))
        return markup
    def getAuthKeyboard(self):
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton(self.keyboardLang['email_change'][0],
                                        callback_data=self.keyboardLang['email_change'][1]))
        markup.add(InlineKeyboardButton(self.keyboardLang['pwd_change'][0],
                                        callback_data=self.keyboardLang['pwd_change'][1]))
        markup.add(InlineKeyboardButton(self.keyboardLang['backto_settings'][0],
                                        callback_data=self.keyboardLang['backto_settings'][1]))
        return markup
    def getUserChanges(self, roles, id):
        USER_ROLE = "USER ✅" if "USER" in roles else "USER ❌"
        FARMER_ROLE = "FARMER ✅" if "FARMER" in roles else "FARMER ❌"
        ADMIN_ROLE = "ADMIN ✅" if "ADMIN" in roles else "ADMIN ❌"

        markup = InlineKeyboardMarkup(row_width=3)
        markup.add(InlineKeyboardButton(text=USER_ROLE,callback_data="changerole_USER_"+str(id)),
                   InlineKeyboardButton(text=FARMER_ROLE,callback_data="changerole_FARMER_"+str(id)),
                   InlineKeyboardButton(text=ADMIN_ROLE,callback_data="changerole_ADMIN_"+str(id)))


        return markup