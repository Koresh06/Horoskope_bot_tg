from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from aiogram import types
from keybords import buttons, buttons_time

class FSMadmin(StatesGroup):
    znak = State()
    period = State()

# @dp.message_handler(commands=['Загрузить'], state=None)
async def cm_start(message: types.Message):
    await FSMadmin.znak.set()
    await message.reply('Выбирете знак', reply_markup=buttons)

# @dp.message_handler(content_types=['znak'], state=FSMadmin.znak)
async def load_znak(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['znak'] = message.text
    await FSMadmin.next()
    await message.reply('Теперь выбери период', reply_markup=buttons_time)

# @dp.message_handler(state=FSMadmin.period)
async def load_perod(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['period'] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_znak, state=FSMadmin.znak)
    dp.register_message_handler(load_perod, state=FSMadmin.period)