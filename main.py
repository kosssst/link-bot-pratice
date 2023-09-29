import telebot
import config
import schedule
import time
import datetime

week = int(input("Enter week: "))

bot = telebot.TeleBot(config.token)

def send(day, pair):
    global week
    if((day == 1) and (pair == 1)):
        if(week == 1):
            week = 2
        else:
            week = 1
    
    pair_text = config.pairs[week-1][day-1][pair-1]
    if pair_text != "":
        success = False
        while not success:
            try:
                bot.send_message(config.chat_id, f"Тиждень: {week}, День: {day}, Пара: {pair}\n\n{pair_text}")
                success = True
            except:
                print(f"[{datetime.datetime.now()}] Error sending message, retrying...")
                time.sleep(2)
        print(f"[{datetime.datetime.now()}] Sent week: {week}, day: {day}, pair: {pair}")
    else:
        print(f"[{datetime.datetime.now()}] Empty pair week: {week}, day: {day}, pair: {pair}")

schedule.every().monday.at("06:25").do(send, day=1, pair=1)
schedule.every().monday.at("08:20").do(send, day=1, pair=2)
schedule.every().monday.at("10:15").do(send, day=1, pair=3)
schedule.every().monday.at("12:10").do(send, day=1, pair=4)
schedule.every().monday.at("14:05").do(send, day=1, pair=5)

schedule.every().tuesday.at("06:25").do(send, day=2, pair=1)
schedule.every().tuesday.at("08:20").do(send, day=2, pair=2)
schedule.every().tuesday.at("10:15").do(send, day=2, pair=3)
schedule.every().tuesday.at("12:10").do(send, day=2, pair=4)
schedule.every().tuesday.at("14:05").do(send, day=2, pair=5)

schedule.every().wednesday.at("06:25").do(send, day=3, pair=1)
schedule.every().wednesday.at("08:20").do(send, day=3, pair=2)
schedule.every().wednesday.at("10:15").do(send, day=3, pair=3)
schedule.every().wednesday.at("12:10").do(send, day=3, pair=4)
schedule.every().wednesday.at("14:05").do(send, day=3, pair=5)

schedule.every().thursday.at("06:25").do(send, day=4, pair=1)
schedule.every().thursday.at("08:20").do(send, day=4, pair=2)
schedule.every().thursday.at("10:15").do(send, day=4, pair=3)
schedule.every().thursday.at("12:10").do(send, day=4, pair=4)
schedule.every().thursday.at("14:05").do(send, day=4, pair=5)

schedule.every().friday.at("06:25").do(send, day=5, pair=1)
schedule.every().friday.at("08:20").do(send, day=5, pair=2)
schedule.every().friday.at("10:15").do(send, day=5, pair=3)
schedule.every().friday.at("12:10").do(send, day=5, pair=4)
schedule.every().friday.at("14:05").do(send, day=5, pair=5)

schedule.every().saturday.at("06:25").do(send, day=6, pair=1)
schedule.every().saturday.at("08:20").do(send, day=6, pair=2)
schedule.every().saturday.at("10:15").do(send, day=6, pair=3)
schedule.every().saturday.at("12:10").do(send, day=6, pair=4)
schedule.every().saturday.at("14:05").do(send, day=6, pair=5)

while True:
    schedule.run_pending()
    time.sleep(1)
