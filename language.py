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

                "admin_uedit_text" : "Выберите параметр для редактирования",
                "request_company_name" : "Название компании",
                "request_product" : "Наименование продукта",
                "request_amnount" : "Количество",
                "request_description" : "Запрос",
                "non_writed" : "Не записан",
                "gotoCurseList" : "Вернуться в ",
                "wait_input" : "<b>Ожидается ввод</b>",
                "bad_text" : "Некорректное значение, попробуйте еще раз",
                "read_line" : "Ожидаю вашего ввода...",
                "incorrect_pwd": "Неверный пароль!",
                "incorrect_email": "Неверный email!",
                "write_dataofuser" : "Напишите <code>email</code> пользователя",
                "start_admin" : "Админская панель:",
                "errorDeleting" : "Неудачное удаление",
                "sucessfull_deleted" : "Удачное удаление",
                "success_auth" : "<b>{fullName}</b>!\n\nДобро пожаловать в вспомогательный бот!",
                "auth_text" : "Ваш e-mail: <b>{email}</b>\nВаш пароль: <b>{pwd}</b>",
                "admin_input_user" : "<b>{fullName}</b>\n\n<i>{bio}</i>\n\nРегистрация: <code>{dateRegistration}</code>\nРоли: <b>{roles}</b>\n\n<i>Напишите еще email или выйдите из меню</i>",
                "EKO" : "Эко",
                "POST" : "Пост",
                "HALAL" : "Халяль",
                "notDeliverys" : "Доставок нет!",
                "card_deliverys" :  "<b>[{product_name}]</b>\n\n" +
                                    "<b>[Описание]</b> {product_description}\n" +
                                    "<b>[ТЭГИ]</b> <code>{product_tags}</code>\n" +
                                    "<b>[Количество]</b> {count} {product_unit}\n\n" +
                                    "<b>[Тип оплаты]</b>: {paymentType}\n\n" +
                                    "<b>[ДОСТАВКА]</b>\n{date}\n" +
                                    "Из: {adressFrom}\n" +
                                    "В: {adressTo}\n",
                'tags_kg' : "КГ",
                'tags_pieces' : "Штук",

                'tags_SBP' : "СБП",
                'tags_CARD' : "Банковская карта",
                'tags_CASH' : "Наличные",
            }
            keyboards = {
                # Admin keyboards
                "diliveres" : "Доставки",
                "product" : "Продукты",
                "course" : "Курсы",
                "user" : "Пользователи",

                "admin_course_deleteCourse" : [
                    "Удалить",
                    "delete_course_"
                ],
                "admin_course_editLink" : [
                    "Изменить ссылку",
                    "editlink_course_"
                ],
                "admin_course_header": [
                    "Изменить заголовок",
                    "editheader_course_"
                ],
                "admin_course_description": [
                    "Изменить описание",
                    "editdescription_course_"
                ],

                "admin_courses_getText" : "Ссылка: {link}\nЗаголовок: {header}\nОписание: {description}",
                "admin_courses_getEmpty" : "Никаких курсов нет!",

                "admin_courses_getAll" : "Все курсы",
                "admin_courses_getbyid" : "Редактировать курс",
                "admin_courses_addCourse" : "Добавить курс",

                "wait_input_description" : "Ожидаю описание",
                "wait_input_link" : "Ожидаю ссылку",
                "wait_input_header" : "Ожидаю заголовок",

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
                "admin_to_uedit" : "⬅️ Категории",
                "admin_to_uedit_course" : "⬅️ Курсы",

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
                "start_true": "Hello, farmer!",
                "start_false": "Hello, farmer,\nlog into your account in the settings!",
                "settings": "Settings",
                "unknown_command": "Unknown command... 🤔",
                "settings_start": "Your settings",
                "access_language": "List of available languages:",
                "success_language": "Language successfully changed!",

                "admin_uedit_text": "Select a parameter to edit",
                "request_company_name": "Company name",
                "request_product": "Product name",
                "request_amnount": "Amount",
                "request_description": "Request",
                "non_writed": "Not written",
                "gotoCurseList": "Return to ",
                "wait_input": "<b>Waiting for input</b>",
                "bad_text": "Invalid value, please try again",
                "read_line": "Waiting for your input...",
                "incorrect_pwd": "Incorrect password!",
                "incorrect_email": "Incorrect email!",
                "write_dataofuser": "Write the user's <code>email</code>",
                "start_admin": "Admin panel:",
                "errorDeleting": "Unsuccessful deletion",
                "sucessfull_deleted": "Successful deletion",
                "success_auth": "<b>{fullName}</b>!\n\nWelcome to the assistant bot!",
                "auth_text": "Your e-mail: <b>{email}</b>\nYour password: <b>{pwd}</b>",
                "admin_input_user": "<b>{fullName}</b>\n\n<i>{bio}</i>\n\nRegistration: <code>{dateRegistration}</code>\nRoles: <b>{roles}</b>\n\n<i>Write another email or exit the menu</i>",
                "EKO": "Eco",
                "POST": "Post",
                "HALAL": "Halal",
                "notDeliverys": "No deliveries!",
                "card_deliverys": "<b>[{product_name}]</b>\n\n" +
                                  "<b>[Description]</b> {product_description}\n" +
                                  "<b>[Tags]</b> <code>{product_tags}</code>\n" +
                                  "<b>[Amount]</b> {count} {product_unit}\n\n" +
                                  "<b>[Payment type]</b>: {paymentType}\n\n" +
                                  "<b>[DELIVERY]</b>\n{date}\n" +
                                  "From: {adressFrom}\n" +
                                  "To: {adressTo}\n",
                'tags_kg': "KG",
                'tags_pieces': "Pieces",

                'tags_SBP': "SBP",
                'tags_CARD': "Card",
                'tags_CASH': "Cash",
            }
            keyboards = {
                # Admin keyboards
                "diliveres": "Deliveries",
                "product": "Products",
                "course": "Courses",
                "user": "Users",

                "admin_course_deleteCourse": [
                    "Delete",
                    "delete_course_"
                ],
                "admin_course_editLink": [
                    "Edit link",
                    "editlink_course_"
                ],
                "admin_course_header": [
                    "Edit header",
                    "editheader_course_"
                ],
                "admin_course_description": [
                    "Edit description",
                    "editdescription_course_"
                ],

                "admin_courses_getText": "Link: {link}\nHeader: {header}\nDescription: {description}",
                "admin_courses_getEmpty": "No courses yet!",

                "admin_courses_getAll": "All courses",
                "admin_courses_getbyid": "Edit course",
                "admin_courses_addCourse": "Add course",

                "wait_input_description": "Waiting for description",
                "wait_input_link": "Waiting for link",
                "wait_input_header": "Waiting for header",

                "admin_load": "Load",
                "admin_hotlinemiami": "Hotline",
                "admin_uedit": "Edit",
                "admin_stats": "Statistics",

                "admin_load_stats": "Statistics",
                "admin_load_geo": "Geography",
                "admin_load_product": "Product types",
                "admin_load_text": "Load different values",
                # "admin_stats_farmers" : "Farmer ratings and reviews",

                "admin_to_main": "⬅️ AP",
                "admin_to_uedit": "⬅️ Categories",
                "admin_to_uedit_course": "⬅️ Courses",

                "reset_key": "↩️ Return to menu",
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
                # Inline settings
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
                "start_true": "你好，农夫！",
                "start_false": "你好，农夫，\n在设置中登录你的帐户！",
                "settings": "设置",
                "unknown_command": "未知的命令... 🤔",
                "settings_start": "您的设置",
                "access_language": "可用语言列表：",
                "success_language": "语言已成功更改！",

                "admin_uedit_text": "选择要编辑的参数",
                "request_company_name": "公司名称",
                "request_product": "产品名称",
                "request_amnount": "数量",
                "request_description": "请求",
                "non_writed": "未填写",
                "gotoCurseList": "返回 ",
                "wait_input": "<b>等待输入</b>",
                "bad_text": "无效的值，请重试",
                "read_line": "等待您的输入...",
                "incorrect_pwd": "密码错误！",
                "incorrect_email": "电子邮件错误！",
                "write_dataofuser": "请填写用户的 <code>电子邮件</code>",
                "start_admin": "管理员面板：",
                "errorDeleting": "删除失败",
                "sucessfull_deleted": "删除成功",
                "success_auth": "<b>{fullName}</b>！\n\n欢迎使用助手机器人！",
                "auth_text": "您的电子邮件：<b>{email}</b>\n您的密码：<b>{pwd}</b>",
                "admin_input_user": "<b>{fullName}</b>\n\n<i>{bio}</i>\n\n注册： <code>{dateRegistration}</code>\n角色： <b>{roles}</b>\n\n<i>写入另一个电子邮件或退出菜单</i>",
                "EKO": "环保",
                "POST": "邮政",
                "HALAL": "清真",
                "notDeliverys": "没有交付！",
                "card_deliverys": "<b>[{product_name}]</b>\n\n" +
                                  "<b>[Description]</b> {product_description}\n" +
                                  "<b>[Tags]</b> <code>{product_tags}</code>\n" +
                                  "<b>[Amount]</b> {count} {product_unit}\n\n" +
                                  "<b>[Payment type]</b>: {paymentType}\n\n" +
                                  "<b>[DELIVERY]</b>\n{date}\n" +
                                  "From: {adressFrom}\n" +
                                  "To: {adressTo}\n",
                'tags_kg': "公斤",
                'tags_pieces': "件",

                'tags_SBP': "银行卡",
                'tags_CARD': "信用卡",
                'tags_CASH': "现金",
            }
            keyboards = {
                # Admin keyboards
                "diliveres": "送货",
                "product": "产品",
                "course": "课程",
                "user": "用户",

                "admin_course_deleteCourse": [
                    "删除",
                    "delete_course_"
                ],
                "admin_course_editLink": [
                    "编辑链接",
                    "editlink_course_"
                ],
                "admin_course_header": [
                    "编辑标题",
                    "editheader_course_"
                ],
                "admin_course_description": [
                    "编辑描述",
                    "editdescription_course_"
                ],

                "admin_courses_getText": "链接：{link}\n标题：{header}\n描述：{description}",
                "admin_courses_getEmpty": "尚无课程！",

                "admin_courses_getAll": "所有课程",
                "admin_courses_getbyid": "编辑课程",
                "admin_courses_addCourse": "添加课程",

                "wait_input_description": "等待描述",
                "wait_input_link": "等待链接",
                "wait_input_header": "等待标题",

                "admin_load": "加载",
                "admin_hotlinemiami": "热线",
                "admin_uedit": "编辑",
                "admin_stats": "统计",

                "admin_load_stats": "统计信息",
                "admin_load_geo": "地理",
                "admin_load_product": "产品类型",
                "admin_load_text": "加载不同的值",
                # "admin_stats_farmers" : "农民评分和评价",

                "admin_to_main": "⬅️ AP",
                "admin_to_uedit": "⬅️ 类别",
                "admin_to_uedit_course": "⬅️ 课程",

                "reset_key": "↩️ 返回菜单",
                "email_change": ["单击输入电子邮件", "change_email_"],
                "pwd_change": ["单击输入密码", "change_pwd_"],
                "in_settings": [
                    "您的设置：\n",
                    "{you_name}",
                ],
                "close_ticket": [
                    "❌ 关闭工单",
                    "closeticket",  # todo {id}, and format
                ],
                "settings": "设置",
                "me_request": "审查请求",
                "set_lang": ["语言设置 {langEmj}", "set_lang"],
                "to_request": "我的请求",
                # Inline settings
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
