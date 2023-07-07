from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


getting_started = ReplyKeyboardMarkup(resize_keyboard=True)
com_bat1 = KeyboardButton(text='/Начать_работу')
com_bat2 = KeyboardButton(text='/Описание')

buttons = ReplyKeyboardMarkup(resize_keyboard=True)

bd1 = KeyboardButton(text='Овен ♈')
bd2 = KeyboardButton(text='Телец ♉')
bd3 = KeyboardButton(text='Близнец ♊')
bd4 = KeyboardButton(text='Рак ♋')
bd5 = KeyboardButton(text='Лев ♈')
bd6 = KeyboardButton(text='Дева ♍')
bd7 = KeyboardButton(text='Весы ♎')
bd8 = KeyboardButton(text='Скорпион ♐')
bd9 = KeyboardButton(text='Стрелец ♐')
bd11 = KeyboardButton(text='Козерог ♑')
bd12 = KeyboardButton(text='Водолей ♒')
bd10 = KeyboardButton(text='Рыбы ♓')

buttons_time = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
but1 = KeyboardButton(text='Сегодня')
but2 = KeyboardButton(text='Завтра')
but3 = KeyboardButton(text='Неделя')
# but4 = KeyboardButton(text='Год')
back = KeyboardButton(text='/Изменить_знак')

getting_started.row(com_bat1, com_bat2)

buttons.row(bd1, bd2, bd3, bd4)
buttons.row(bd5, bd6, bd7, bd8)
buttons.row(bd9, bd10, bd11, bd12)

buttons_time.row(but1, but2)
buttons_time.row(but3)
buttons_time.row(back)