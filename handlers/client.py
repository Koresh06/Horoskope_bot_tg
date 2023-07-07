from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from keybords import buttons, buttons_time, getting_started
from bs4 import BeautifulSoup
import requests
import json


HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

class FSMadmin(StatesGroup):
    znak = State()
    period = State()


async def start_command(message: types.Message):
    await message.answer('Вас приветствует бот-гороскоп\nВыберете одну из команд (Начать_работу, Описание)', reply_markup=getting_started)


async def cm_start(message: types.Message):
    await FSMadmin.znak.set()
    await message.answer('Выбирете знак', reply_markup=buttons)

async def load_znak(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['znak'] = message.text
    await FSMadmin.next()
    await message.answer('Теперь выбери период', reply_markup=buttons_time)

async def load_perod(message: types.Message, state=FSMContext):
    if message.text == '/Изменить_знак':
        await state.finish()
        cm_start()
    else:
        async with state.proxy() as data:
            data['period'] = message.text
        async with state.proxy() as data:
            with open('handlers/data.json', 'r', encoding='utf-8') as file:
                href_dict = json.load(file)
            if (data['period']) == 'Сегодня':
                await message.answer(f"{'*' * 50}\n\n{get_content(get_html(href_dict[data['znak']][0]['Гороскоп на сегодня']))}\n\n{'*' * 50}")
            elif (data['period']) == 'Завтра':
                await message.answer(f"{'*' * 50}\n\n{get_content(get_html(href_dict[data['znak']][1]['Гороскоп на завтра']))}\n\n{'*' * 50}")
            elif (data['period']) == 'Неделя':
                await message.answer(f"{'*' * 50}\n\n{get_content(get_html(href_dict[data['znak']][2]['Гороскоп на неделю']))}\n\n{'*' * 50}")
            # elif (data['period']) == 'Год':
            #     await message.answer(get_content(get_html(href_dict[data['znak']][3]['Гороскоп на год'])))
            else:
                await message.answer('Указано неверное значение')
        await state.finish()


async def discriphion_bot(message: types.Message):
    await message.answer('Описание бота...')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(cm_start, commands=['Начать_работу', 'Изменить_знак'], state=None)
    dp.register_message_handler(load_znak, state=FSMadmin.znak)
    dp.register_message_handler(load_perod, state=FSMadmin.period)
    dp.register_message_handler(discriphion_bot, commands=['Описание'])




def get_html(url):
    res = requests.get(url, headers=HEADERS)
    return res.text

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('div', class_='eje_block').find('p').get_text()
    
    return(items)






