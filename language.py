""""""""""
SWITCH DECLARATION

0 - Русский
1 - Американский
2 - Китайский

"""""""""""

class language:
    def __init__(self, lang=0):
        self.switch = lang

    def getText(self):
        if self.switch == 0:  # Русский
            text = {
                "start_true": "Привет фермер!",
                "start_false": "Привет фермер,\nзайди в свой аккаунт в настройках!",
                "settings": "Настройки",
                "unknown_command": "Неизвестная команда... 🤔",
                "settings_start": "Твои настройки",
                "access_language": "Список возможных языков:",
                "success_language" : "Успешно изменен язык!",

                "request_company_name" : "Название компании",
                "request_product" : "Наименование продукта",
                "request_amnount" : "Количество",
                "request_description" : "Запрос",
                "non_writed" : "Не записан",
                "wait_input" : "<b>Ожидается ввод</b>",
                "bad_text" : "Некорректное значение, попробуйте еще раз",
                "read_line" : "Ожидаю вашего ввода...",
                "incorrect_pwd": "Неверный пароль!",
                "incorrect_email": "Неверный email!",
                "write_dataofuser" : "Напишите <code>email</code> пользователя",
                "start_admin" : "Админская панель:",
                "success_auth" : "<b>{fullName}</b>!\n\nДобро пожаловать в вспомогательный бот!",
                "auth_text" : "Ваш e-mail: <b>{email}</b>\nВаш пароль: <b>{pwd}</b>",
                "admin_input_user" : "<b>{fullName}</b>\n\n<i>{bio}</i>\n\nРегистрация: <code>{dateRegistration}</code>\nРоли: <b>{roles}</b>\n\n<i>Напишите еще email или выйдите из меню</i>",
            }
            keyboards = {
                # Admin keyboards
                "admin_load" : "Выгрузка",
                "admin_hotlinemiami" : "Горячая линия",
                "admin_uedit" : "Внесение изменений",
                "admin_stats" : "Статистики",

                "admin_load_stats" : "Статистика",
                "admin_load_geo" : "География",
                "admin_load_product" : "Виды товара",
                "admin_load_text" : "Выгрузка различных значений",
                # "admin_stats_farmers" : "Рейтинг и отзывы фермера",

                "admin_to_main" : "⬅️ АП",

                "reset_key" : "↩️ Вернуться в меню",
                "email_change" : ["Нажмите для ввода e-mail", "change_email_"],
                "pwd_change" : ["Нажмите для ввода пароля", "change_pwd_"],
                "in_settings": [
                    "Ваши настройки:\n",
                    "{you_name}",
                ],
                "close_ticket" : [
                    "❌ Закрыть заявку",
                    "closeticket", # todo {id}, and format
                ],
                "settings" : "Настройки",
                "me_request": "Рассмотреть заявки",
                "set_lang": ["Настройки языка {langEmj}", "set_lang"],
                "to_request": "Мои заявки",
                # В настройках Inline
                "push": [
                    "Уведомления",
                    "pushes",
                ],
                "news": [
                    "Новости",
                    "news",
                ],
                "authorization": [
                    "Авторизация",
                    "auth",
                ],
                "chinese" : [
                    "Китайский 🇨🇳",
                    "setlang_chinese"
                ],
                "american": [
                    "Американский 🇺🇲",
                    "setlang_america"
                ],
                "russian": [
                    "Русский " + "🇷🇺",
                    "setlang_russian"
                ],
                "backto_settings": [
                    "⬅️ Настройки",
                    "go_settings"
                ]
            }
        elif self.switch == 1:  # Американский
            text = {
                "start_true": "Hello farmer!",
                "start_false": "Hello farmer,\nlog into your account in settings!",
                "settings": "Settings",
                "unknown_command": "Unknown command... 🤔",
                "settings_start": "Your settings",
                "access_language": "List of available languages:",
                "success_language": "Language successfully changed!",
                "request_company_name": "Company name",
                "request_product": "Product name",
                "request_amnount": "Quantity",
                "request_description": "Request",
                "non_writed": "Not written",
                "wait_input": "<b>Waiting for input</b>",
                "bad_text": "Incorrect value, please try again",
                "read_line": "Waiting for your input...",
                "incorrect_pwd": "Incorrect password!",
                "incorrect_email": "Incorrect email!",
                "write_dataofuser": "Write user's <code>email</code>",
                "start_admin": "Admin panel:",
                "success_auth": "<b>{fullName}</b>!\n\nWelcome to the assistant bot!",
                "auth_text": "Your e-mail: <b>{email}</b>\nYour password: <b>{pwd}</b>",
                "admin_input_user": "<b>{fullName}</b>\n\n<i>{bio}</i>\n\nRegistration: <code>{dateRegistration}</code>\nRoles: <b>{roles}</b>\n\n<i>Write another email or exit the menu</i>",
            }
            keyboards = {
                # Admin keyboards
                "admin_load": "Load",
                "admin_hotlinemiami": "Hotline Miami",
                "admin_uedit": "Editing",
                "admin_stats": "Statistics",
                "admin_load_stats": "Statistics",
                "admin_load_geo": "Geography",
                "admin_load_product": "Product types",
                "admin_load_text": "Unload various values",
                # "admin_stats_farmers": "Farmer's rating and reviews",
                "admin_to_main": "⬅️ AP",
                "reset_key": "↩️ Back to menu",
                "email_change": ["Click to enter e-mail", "change_email_"],
                "pwd_change": ["Click to enter password", "change_pwd_"],
                "in_settings": [
                    "Your settings:\n",
                    "{you_name}",
                ],
                "close_ticket": [
                    "❌ Close ticket",
                    "closeticket",  # todo {id}, and format
                ],
                "settings": "Settings",
                "me_request": "Review requests",
                "set_lang": ["Language settings {langEmj}", "set_lang"],
                "to_request": "My requests",
                # In Inline settings
                "push": [
                    "Notifications",
                    "pushes",
                ],
                "news": [
                    "News",
                    "news",
                ],
                "authorization": [
                    "Authorization",
                    "auth",
                ],
                "chinese": [
                    "Chinese 🇨🇳",
                    "setlang_chinese"
                ],
                "american": [
                    "American 🇺🇲",
                    "setlang_america"
                ],
                "russian": [
                    "Russian " + "🇷🇺",
                    "setlang_russian"
                ],
                "backto_settings": [
                    "⬅️ Settings",
                    "go_settings"
                ]
            }

        elif self.switch == 2:  # Китайский
            text = {
                "start_true": "你好，农民！",
                "start_false": "你好，农民，请在设置中登录你的账户！",
                "settings": "设置",
                "unknown_command": "未知命令... 🤔",
                "settings_start": "你的设置",
                "access_language": "可用语言列表：",
                "success_language": "语言已成功更改！",
                "request_company_name": "公司名称",
                "request_product": "产品名称",
                "request_amnount": "数量",
                "request_description": "请求",
                "non_writed": "未填写",
                "wait_input": "<b>等待输入</b>",
                "bad_text": "无效的值，请重试",
                "read_line": "等待您的输入...",
                "incorrect_pwd": "密码错误！",
                "incorrect_email": "电子邮件错误！",
                "write_dataofuser": "写入用户的 <code>电子邮件</code>",
                "start_admin": "管理员面板：",
                "success_auth": "<b>{fullName}</b>！\n\n欢迎使用助手机器人！",
                "auth_text": "您的电子邮件：<b>{email}</b>\n您的密码：<b>{pwd}</b>",
                "admin_input_user": "<b>{fullName}</b>\n\n<i>{bio}</i>\n\n注册日期：<code>{dateRegistration}</code>\n角色：<b>{roles}</b>\n\n<i>请输入另一个电子邮件或退出菜单</i>",
            }
            keyboards = {
                # 管理员键盘
                "admin_load": "装载",
                "admin_hotlinemiami": "热线迈阿密",
                "admin_uedit": "编辑",
                "admin_stats": "统计",
                "admin_load_stats": "统计",
                "admin_load_geo": "地理",
                "admin_load_product": "产品类型",
                "admin_load_text": "卸载各种值",
                # "admin_stats_farmers": "农民评级和评论",
                "admin_to_main": "⬅️ AP",
                "reset_key": "↩️ 返回菜单",
                "email_change": ["点击输入电子邮件", "change_email_"],
                "pwd_change": ["点击输入密码", "change_pwd_"],
                "in_settings": [
                    "您的设置：\n",
                    "{you_name}",
                ],
                "close_ticket": [
                    "❌ 关闭请求",
                    "closeticket",  # todo {id}, and format
                ],
                "settings": "设置",
                "me_request": "查看请求",
                "set_lang": ["语言设置 {langEmj}", "set_lang"],
                "to_request": "我的请求",
                # 内联设置
                "push": [
                    "通知",
                    "pushes",
                ],
                "news": [
                    "新闻",
                    "news",
                ],
                "authorization": [
                    "授权",
                    "auth",
                ],
                "chinese": [
                    "中文 🇨🇳",
                    "setlang_chinese"
                ],
                "american": [
                    "美国人 🇺🇲",
                    "setlang_america"
                ],
                "russian": [
                    "俄罗斯人 " + "🇷🇺",
                    "setlang_russian"
                ],
                "backto_settings": [
                    "⬅️ 设置",
                    "go_settings"
                ]
            }
        else:
            text = {}
            keyboards = {}

        return text, keyboards

    def getLanguage(self):
        return self.switch
    def setLanguage(self, state):
        self.switch = state
