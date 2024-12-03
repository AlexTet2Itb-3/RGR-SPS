import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('7062669153:AAGFUmrsCDQNbWlAvkxwJRKPHBuHWo3rjcM')

@botTimeWeb.message_handler(commands=['start'])
def start_bot(message):
    first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о нашей компании?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    markup.add(button_yes)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.message_handler(commands=['question'])
def question_handler(message):
    question_mess = "Если у вас есть вопросы, вы можете обратиться к нашему специалисту по следующей ссылке: [Чат со специалистом](https://t.me/arsenmarkarian)"
    botTimeWeb.send_message(message.chat.id, question_mess, parse_mode='Markdown')

@botTimeWeb.message_handler(commands=['suggestion'])
def suggestion_handler(message):
    suggestion_link = "https://vk.com/kmizulina"
    botTimeWeb.send_message(message.chat.id, f"Вы можете оставить свои предложения по улучшению здесь: {suggestion_link}")

@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.data == "yes":
        second_mess = "Мы облачная Для Удобрений Рога и Копыта. Более детально можешь ознакомиться с нами на нашем сайте!"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://timeweb.cloud/"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

# Запуск бота
botTimeWeb.infinity_polling()

