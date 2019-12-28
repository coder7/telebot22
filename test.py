import telebot

TOKEN = ''

bot = telebot.TeleBot('')

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Instagram', 'Telegram')
keyboard.row('Информация', 'Связь')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.from_user.id, 'Привет!', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def command_help(message1):
    bot.send_message(message1.from_user.id, "Как я могу помочь тебе?")#написать норм помощь!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text == 'Instagram':
		keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
		keyboard1.row('Подписчики', 'Лайки')
		keyboard1.row('Выход')
		bot.send_message(message.from_user.id, 'Выбери вид накрутки:', reply_markup=keyboard1)
	if message.text == 'Подписчики':
		bot.send_message(message.from_user.id, 'Временно не доступно!!!')
	elif message.text == 'Лайки':
		bot.send_message(message.from_user.id, 'Временно не доступно!!!')
	#elif message.text == 'Выход':
		#bot.send_message(message.from_user.id, 'Привет!', reply_markup=keyboard)


	if message.text == 'Telegram':
		keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
		keyboard2.row('Подписчики!', 'Просмотры!')
		keyboard2.row('Выход')
		bot.send_message(message.from_user.id, 'Выбери вид накрутки:', reply_markup=keyboard2)
	if message.text == 'Подписчики!':
		bot.send_message(message.from_user.id, """
=============================
Подписчики Telegram
=============================
Для начала подсчитайте стоимость вашего заказа:
Подписчик = 0.15₽
Например: 1к = 150₽
=============================
Оплата:
Киви - +380688509012
В комментариях укажите: 
(количество/ссылка на канал)
Например: 1000/@djhhiehdh
=============================
Канал должен быть открытым!!!
Заказы принимаем только от 1000 подписчиков!!!
=============================
Ожидайте выполнения!
=============================""")
	elif message.text == 'Просмотры!':
		bot.send_message(message.from_user.id, 'Временно не доступно!!!')
	elif message.text == 'Выход':
		bot.send_message(message.from_user.id, 'Привет!', reply_markup=keyboard)


	if message.text == 'Информация':
		bot.send_message(message.from_user.id, """
Подписчики Telegram:

• Цена: 0.15 ₽ / 1 подписчик
• Неактивные, без отписок
• Живых нет и не будет
• Максимум 500К на 1 канал
• Скорость 3-5К/час (иногда бывает ниже)
• Принимаются каналы только открытые!""", reply_markup=keyboard)


	if message.text == 'Связь':
		bot.send_message(message.from_user.id, """
Прочитайте справку в меню			
«Информация».Она короткая.
Бот не продаётся, скидок нет. На
вопросы, не касающиеся работы бота, не 
отвечаю.

Если есть вопрос - пишите сюда 
@piarman сразу вопрос одним
сообщением. Можно без приветствий.""", reply_markup=keyboard)



bot.polling()