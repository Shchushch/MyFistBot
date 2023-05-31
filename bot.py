import logging
import pandas as pd
import lxml
import os
import datetime

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('logger')
fh = logging.FileHandler('log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(fh)

#TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

path = 'https://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/'
translator = pd.read_html(path,index_col=1,header=0)[0].drop(columns='N п/п')['Рекомендуемая транслитерация'].to_dict()
translator['Ь'] = ''
#translator = translator.drop(columns='N п/п')['Рекомендуемая транслитерация']
print(translator)
def translate(message):
    translated = ''
    for char in message.upper():
        translated += translator.get(char, char)
    translated=translated[0]+translated[1:].lower()
    if translated=='Puvlik':
        return 'Пошёл нахуй <3'
    else:
        return translated


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Салам пополам, {user_name}!\n Чем я тут занимаюсь?\nЯ блюжу закон, т.е. помогаю с транслитерацией имён в соответствии с Приказом МИД России от 12.02.2020 № 2113'
    
    logger.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def send_translated(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = translate(message.text)
    
    logger.info(f'{datetime.datetime.now()} {user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, text)
    #await bot.send_message(user_id, text)    

if __name__ == '__main__':
    executor.start_polling(dp)