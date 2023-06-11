import telebot
import random
from datetime import datetime
from telebot import types

API_KEY = '5027499993:AAEPS8uoXFhmN4Ezmj5qRq-5AMaExFN4OwQ'
bot = telebot.TeleBot(API_KEY)

# greet_command
@bot.message_handler(commands=['start'])
def get_interest(message):
	# buttons
	markup_inline = types.InlineKeyboardMarkup(row_width = 1)
	item_guide = types.InlineKeyboardButton(text = '📑 Info', callback_data='first')
	item_contacts = types.InlineKeyboardButton(text='⏰ Time', callback_data='yes1')
	item_design = types.InlineKeyboardButton(text='💰 SMM', callback_data='yes3')
	item_call = types.InlineKeyboardButton(text = 'Contact developer', url = 't.me/alikhan_qp')

	markup_inline.add(item_guide, item_contacts, item_design, item_call)
	
	# photo
	bot.send_sticker(message.chat.id, sticker=open('/Users/alikhan/Desktop/gggg/sticker.webp', 'rb'))

	# text + markup_inline + name + bold
	bot.send_message(message.chat.id, f"👋 Welcome to the club <b>{message.from_user.first_name}.</b>\n\n📌Me, <b>helper_bot,</b> made to be a servant.\nClick button under to get information about functions that i have currently\n\n"
									  f"---\nMain menu\n\nSelect category:\n",
					 reply_markup = markup_inline, parse_mode='html')


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
	if call.data == "first":
		markup_inline1 = types.InlineKeyboardMarkup()
		backk = types.InlineKeyboardButton(text='⏪ Back', callback_data='backk')
		markup_inline1.add(backk)

		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
						 "👉You can get information about time and etc. just type word(Ex: time)\n\n/camera1 - room's entrance camera \n/camera2 - access to Amirkhan's camera",
						 reply_markup=markup_inline1)

	elif call.data == "backk":
		markup_inline = types.InlineKeyboardMarkup(row_width=1)
		item_guide = types.InlineKeyboardButton(text='📑 Info', callback_data='first')
		item_contacts = types.InlineKeyboardButton(text='⏰ Time', callback_data='yes1')
		item_design = types.InlineKeyboardButton(text='💰 SMM', callback_data='yes3')
		item_call = types.InlineKeyboardButton(text='Contact developer', url='t.me/alikhan_qp')

		markup_inline.add(item_guide, item_contacts, item_design, item_call)

		# text
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text =
						 "Main menu\n\nSelect category:\n",
						 reply_markup=markup_inline)

	# time
	elif call.data == 'yes1':
		now = datetime.now()
		date_time = now.strftime("📅 %d/%m/%y ⏰ %H:%M:%S")
		bot.send_message(call.message.chat.id, date_time)

# text
@bot.message_handler(content_types = ['text'])
def get_text(message):
	if message.text.lower() in ["hi", "hey", "what's up?", "hello"]:
		bot.send_message(message.chat.id, "Hey there, what's up?")
	elif message.text.lower() in ["good", "nice", "amazing", "well", "alright"]:
		bot.send_message(message.chat.id, "That's good!")
	elif message.text.lower() in ["time", "what's time?", "time?", "date", "date?", "what is time?"]:
		now = datetime.now()
		date_time = now.strftime("📅 %d/%m/%y ⏰ %H:%M:%S")
		bot.send_message(message.chat.id, date_time)
	else:
		rand = random.randint(1, 2)
		if rand == 1:
			bot.send_sticker(message.chat.id, sticker=open('/Users/alikhan/Desktop/gggg/st.webp', 'rb'))
			bot.send_message(message.chat.id, "I don't get you. Try smth else")
		else:
			bot.send_sticker(message.chat.id, sticker=open('/Users/alikhan/Desktop/gggg/st.webp', 'rb'))
			bot.send_message(message.chat.id, "I have not many functios. Try smth else")

# RUN
bot.polling(none_stop=True)
