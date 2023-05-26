from aiogram import Bot
from config import BOT_TKN, BASE_URL_BACKEND,ANALYTICS_URL_BACKED
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
import asyncio, logging, datetime
from io import BytesIO
from database import database
from language import language
from keyboards import keyboards, inlineKeyboards
from api_manipulator import SwaggerClient

bot = Bot(token=BOT_TKN)
dp = Dispatcher(bot)

localization = language()
startText, _ = localization.getText() # Получаение русской локализации
keyboards = keyboards(setLang = localization.getLanguage()) # Получаем кейбоарды
inlineKeyboards = inlineKeyboards(setLang = localization.getLanguage()) # Получаем кейбоарды
database = database()

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    query = await database.newUserCheck(uid= message.from_user.id)
    if query == False:
        await message.reply(startText['start_false'], reply_markup=keyboards.mainKeyboard())
    else:
        USER_TKN = query['token']
        STATE = query['state_user']
        LOCALIZATION = query['language']

        # if USER_TKN != 0:
        toAPI = SwaggerClient(base_url=BASE_URL_BACKEND, token=USER_TKN)

        localization.setLanguage(LOCALIZATION)  # Получаение русской локализации
        allText, langKey = localization.getText()
        keyboards.changeLocalization(state=localization.getLanguage())
        inlineKeyboards.changeLocalization(state=localization.getLanguage())

        text = message.text
        if text.lower() == "/start" or text == langKey['reset_key']:
            await database.changeState(0, message.from_user.id)
            STATE = 0
            await message.reply(reply=False, text=allText['start_true'], reply_markup=keyboards.mainKeyboard())
        elif STATE == 0:
            if text == langKey['to_request']:  # Мои отправленные заявки
                TO_REQUEST = [
                    {
                        "company_name": "ИП \"Суворовское\"",
                        "item": "Рис, 1кг",
                        "count": 1000,
                        "about": "Здравствуйте, я бы хотел заказать у вас 1 тонну риса, хочу договориться о доставке в Рязанскую область",
                        "pic": "https://plus.unsplash.com/premium_photo-1674654419403-1a80edb26881?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
                    },
                    {
                        "company_name": "Фермерское хозяйство \"Зеленая поляна\"",
                        "item": "Мед, 500г",
                        "count": 50,
                        "about": "Добрый день, интересует покупка 50 банок натурального меда, желательно разных сортов. Необходима доставка в Москву.",
                        "pic": "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80"
                    },
                    {
                        "company_name": "ООО \"Ферма Успеха\"",
                        "item": "Свежие овощи",
                        "count": 200,
                        "about": "Здравствуйте, хотел бы заказать 200 кг свежих овощей: морковь, картофель, лук. Прошу уточнить возможность доставки в Санкт-Петербург.",
                        "pic": "https://images.unsplash.com/photo-1590779033100-9f60a05a013d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80"
                    },
                    {
                        "company_name": "Колхоз \"Золотая нива\"",
                        "item": "Молоко, 1л",
                        "count": 1000,
                        "about": "Добрый день! Нам нужно закупить 1000 литров свежего коровьего молока. Мы находимся в Краснодарском крае, просим уточнить возможность доставки.",
                        "pic": "https://images.unsplash.com/photo-1611211301828-be4b317d0707?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80"
                    },
                    {
                        "company_name": "ИП \"Золотая рыбка\"",
                        "item": "Морепродукты",
                        "count": 500,
                        "about": "Привет! Хотим приобрести 500 кг разнообразных морепродуктов: креветки, мидии, осьминоги. Необходима доставка в город Калининград.",
                        "pic": "https://images.unsplash.com/photo-1615141982883-c7ad0e69fd62?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80"
                    }
                ]
                from utils import send_message_with_picture, format

                toPaste = {
                    "company_name": allText['request_company_name'],
                    "product": allText['request_product'],
                    "amnount": allText['request_amnount'],
                    "description": allText['request_description'],
                }
                for item in TO_REQUEST:
                    caption, photo = send_message_with_picture(item)
                    caption = format(caption, toPaste)
                    await bot.send_photo(caption=caption,
                                         photo=photo,
                                         chat_id=message.from_user.id,
                                         parse_mode="HTML",
                                         reply_markup=inlineKeyboards.closeMessage()
                                         )
            elif text == langKey['me_request']:  # Рассмотреть заявки
                ME_REQUEST = [
                    {
                        "company_name": "ИП \"Родина\"",
                        "item": "Сыр, 100г",
                        "count": 100,
                        "about": "Здравствуйте, наслышан о вашей компании. Хочу заказать в Рязань. Свяжитесь со мной пожалуйста",
                        "pic": "https://images.unsplash.com/photo-1631379578550-7038263db699?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=874&q=80"
                    },
                    {
                        "company_name": "ООО \"Молочная усадьба\"",
                        "item": "Творог, 500г",
                        "count": 50,
                        "about": "Добрый день! Узнал о вашем вкусном твороге и хотел бы сделать заказ. Живу в Москве. Ожидаю вашего ответа!",
                        "pic": "https://thumbs.dreamstime.com/b/healthy-russian-breakfast-glass-bowl-plain-tvorog-bowl-plain-russian-cottage-cheese-called-tvorog-149363165.jpg"
                    },
                    {
                        "company_name": "Фермерское хозяйство \"Молочный рай\"",
                        "item": "Масло, 250г",
                        "count": 20,
                        "about": "Приветствую! Слышал о вашем натуральном масле и хотел бы приобрести его. Живу в Санкт-Петербурге. Буду ждать от вас сообщения!",
                        "pic": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80"
                    }
                ]
                from utils import send_message_with_picture, format

                toPaste = {
                    "company_name": allText['request_company_name'],
                    "product": allText['request_product'],
                    "amnount": allText['request_amnount'],
                    "description": allText['request_description'],
                }
                for item in ME_REQUEST:
                    caption, photo = send_message_with_picture(item)
                    caption = format(caption, toPaste)
                    await bot.send_photo(caption=caption,
                                         photo=photo,
                                         chat_id=message.from_user.id,
                                         parse_mode="HTML",
                                         reply_markup=inlineKeyboards.closeMessage()
                                         )
            elif text == langKey['settings']:
                checkBox = [
                    query['push'],
                    query['news'],
                    USER_TKN,
                ]

                country = query['language']

                await message.reply(reply=False, text=allText['settings_start'],
                                    reply_markup=inlineKeyboards.settings(checkBox, country))
            elif text.lower() == "/admin":
                myUser = toAPI.getCurrent()
                if 'ADMIN' in myUser['roles']:
                    await database.changeState(3, message.from_user.id)
                    await message.reply(reply_markup=keyboards.adminKeyboard(), text=allText['start_admin'])
            else:
                await message.reply(allText['unknown_command'])
        elif STATE == 1: # enter email addr
            from utils import validate_email, format
            if validate_email(text):
                send = format(allText['auth_text'], {
                    "email": text,
                    "pwd": allText['non_writed'],
                })
                await database.changeEmail(uid=message.from_user.id, state=text)
                await database.changeState(uid=message.from_user.id, state=0)
                await message.reply(reply_markup=inlineKeyboards.getAuthKeyboard(), text=send, parse_mode="HTML")
            else:
                await message.reply(allText['bad_text'])
        elif STATE == 2:
            EMAIL = query['email']
            response = toAPI.signIn(email = EMAIL, password=text)
            if response:
                await database.setToken(state=response['token'], uid=message.from_user.id)
                await database.changeState(state=0, uid=message.from_user.id)

                from utils import format
                toSend = format(allText['success_auth'], {
                    'fullName' : response['fullName']
                })
                await message.reply(parse_mode="HTML",reply=False, reply_markup=keyboards.mainKeyboard(), text=toSend)
            else:
                await message.reply(allText['incorrect_pwd'])
            print(response)
        elif text == langKey['admin_to_main']:
            await database.changeState(3, message.from_user.id)
            STATE = 3
            await message.reply(reply_markup=keyboards.adminKeyboard(), text=allText['start_admin'])
        elif STATE == 3: # IN ADMIN KEYBOARD
            if text == langKey['admin_load']:
                await message.reply(reply_markup=keyboards.admin_load(), text=langKey['admin_load_text'])
            if text == langKey['admin_hotlinemiami']:
                pass
            if text == langKey['admin_uedit']: # Внесение элементов
                await message.reply(parse_mode = "HTML", text = allText['write_dataofuser'], reply_markup=keyboards.resetKeyboard_admin())
                await database.changeState(4, message.from_user.id)

            if text == langKey['admin_stats']:

                # host = "http://192.168.137.96:8080/api/AnaliticsData"
                # import requests, base64
                # data = requests.request(method="get", url=host).json()
                # base64_bytes = data['data'].encode("ascii")
                # message_bytes = base64.b64decode(base64_bytes)
                # # Создание объекта BytesIO и загрузка байтов изображения
                # image_io = BytesIO(message_bytes)
                # await message.reply_photo(photo=image_io)

                # print(data.text)
                pass
            if text == langKey['admin_load_stats']:
                from api_manipulator import analyticsClient
                analytic = analyticsClient(ANALYTICS_URL_BACKED)
                genStats = analytic.getGeneralStats()
                """""""""
                genStats = {
                    'bytes' : 'str',
                    'text' : '',
                }
                """""""""
        elif STATE == 4:
            searched = toAPI.searchEmail(email = text)
            if searched:
                from utils import format

                await message.reply(text=format(allText['admin_input_user'], {
                                                    'fullName' : searched['fullName'],
                                                    'bio' : searched['bio'],
                                                    'roles' : " ".join(searched['roles']),
                                                    'dateRegistration' : datetime.datetime.fromtimestamp(searched['dateRegistration']).strftime("%Y:%m:%d %H:%M"),
                                                }),
                                    reply_markup=inlineKeyboards.getUserChanges(roles=searched['roles'], id=searched['id']), parse_mode="HTML")
            else:
                await message.reply(text = allText['incorrect_email'])

@dp.callback_query_handler()
async def callback(callback_query: types.CallbackQuery):
    query = await database.newUserCheck(uid= callback_query.from_user.id)
    USER_TKN = query['token']
    STATE = query['state_user']
    LOCALIZATION = query['language']

    localization.setLanguage(LOCALIZATION)  # Получаение русской локализации
    allText, langKey = localization.getText()
    keyboards.changeLocalization(state=localization.getLanguage())
    inlineKeyboards.changeLocalization(state=localization.getLanguage())

    toAPI = SwaggerClient(base_url=BASE_URL_BACKEND, token=USER_TKN)

    if callback_query.data == langKey['push'][1]: # Если нажата кнопка пушов
        checkBox = [
            0 if query['push'] == 1 else 1, # Реверсим при нажатии
            query['news'],
            USER_TKN,
        ]
        if await database.changePush(uid=callback_query.from_user.id, state=checkBox[0]):
            await bot.edit_message_text(reply_markup=inlineKeyboards.settings(checkBox, query['language']),text=langKey['settings'], chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        else:
            await bot.edit_message_text(text="FATAL ERR0R", chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    if callback_query.data == langKey['news'][1]: # Если нажата кнопка пушов
        checkBox = [
            query['push'],
            0 if query['news'] == 1 else 1, # Реверсим при нажатии
            USER_TKN,
        ]

        if await database.changeNews(uid=callback_query.from_user.id, state=checkBox[1]):
            await bot.edit_message_text(reply_markup=inlineKeyboards.settings(checkBox, LOCALIZATION),text=langKey['settings'], chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        else:
            await bot.edit_message_text(text="FATAL ERR0R", chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    if callback_query.data == langKey['set_lang'][1]:
        await bot.edit_message_text(reply_markup=inlineKeyboards.language(),text=allText['access_language'], chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    if callback_query.data == langKey['backto_settings'][1]:
        checkBox = [
            query['push'],
            query['news'],
            USER_TKN,
        ]
        await bot.edit_message_text(reply_markup=inlineKeyboards.settings(checkBox, LOCALIZATION), text=langKey['settings'],
                                    chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    if callback_query.data == langKey['close_ticket'][1]:
        await bot.delete_message(
            chat_id=callback_query.from_user.id,
            message_id=callback_query.message.message_id
        )
    if callback_query.data.startswith("setlang_"):
        value = callback_query.data[len("setlang_"):]
        try:
            if value == "chinese":
                state = 2
                await database.changeLanguage(state=state, uid=callback_query.from_user.id)
            elif value == "america":
                state=1
                await database.changeLanguage(state=state, uid=callback_query.from_user.id)
            else:
                state=0
                await database.changeLanguage(state=state, uid=callback_query.from_user.id)

            localization.setLanguage(state)  # Получаение русской локализации
            newerText, _ = localization.getText()
            keyboards.changeLocalization(state = localization.getLanguage())

            await bot.edit_message_text(
                text=newerText['success_language'],
                chat_id=callback_query.from_user.id,
                message_id=callback_query.message.message_id)
            await bot.send_message(
                text=newerText['start_true'],
                chat_id=callback_query.from_user.id,
                reply_markup=keyboards.mainKeyboard()
            )
        except:
            await bot.edit_message_text(
                                        text="ERR0R",
                                        chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id)
    if callback_query.data == langKey['authorization'][1]:
        from utils import  format
        text = format(allText['auth_text'], {
            "email" : allText['non_writed'],
            "pwd" : allText['non_writed'],
            "status" : "", # wait_input
        })
        await bot.edit_message_text(reply_markup=inlineKeyboards.getAuthKeyboard(),text=text, chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, parse_mode="HTML")
    if callback_query.data.startswith( langKey['email_change'][1] ):
        await database.changeState(state=1, uid=callback_query.from_user.id) # Меняем chat-state 1
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_message(reply_markup=keyboards.resetKeyboard(),text=allText['read_line'], chat_id=callback_query.from_user.id, parse_mode="HTML")
    if callback_query.data.startswith(langKey['pwd_change'][1]):
        await database.changeState(state=2, uid=callback_query.from_user.id)  # Меняем chat-state 2
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_message(reply_markup=keyboards.resetKeyboard(), text=allText['read_line'],
                               chat_id=callback_query.from_user.id, parse_mode="HTML")
    if callback_query.data.startswith("changerole_"):
        value = callback_query.data[len("changerole_"):].split("_")

        client = toAPI.getUserbyID(id=value[1])

        if value[0] in client['roles']:
            client['roles'].remove(value[0])
        else:
            client['roles'].append(value[0])
        toAPI.updateRole(id=value[1], role=client['roles'])

        from utils import format

        await bot.edit_message_text(text=format(allText['admin_input_user'], {
            'fullName': client['fullName'],
            'bio': client['bio'],
            'roles': " ".join(client['roles']),
            'dateRegistration': datetime.datetime.fromtimestamp(client['dateRegistration']).strftime(
                "%Y:%m:%d %H:%M"),
        }),
                            reply_markup=inlineKeyboards.getUserChanges(roles=client['roles'], id=client['id']),
                            parse_mode="HTML", chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id)
        pass

async def main():
    await database.connect("postgresql://username:password@192.168.137.149:5433/tg_bot")
    await dp.start_polling(bot)
    await database.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())