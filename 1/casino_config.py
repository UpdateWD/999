# Слито на @Oblako_sxem
# Слито на @Oblako_sxem
# Слито на @Oblako_sxem
import telebot
import sqlite3
from qiwi_payments.kassa import QiwiKassa

cashier = QiwiKassa("e74c00791c075ea5005b2daf6827b8a3")

bot = telebot.TeleBot("1431744138:AAEuZSuRhxWf8ChBtFDcIxc0XgvaYliEAZw")

con = sqlite3.connect("dannie_2.db")
cur = con.cursor()

admin_1 = 1353097202
admin_2 = 1353097202

bot_name = "Worldoffortune_bot"
fake_number = "88005553535"
min_summa = 100
# Слито на @Oblako_sxem
# Слито на @Oblako_sxem
# Слито на @Oblako_sxem
# Слито на @Oblako_sxem
# Работа с бд
def get_status(message):
    con = sqlite3.connect("dannie_2.db")
    cur = con.cursor()
    cur.execute(f"SELECT status FROM users WHERE id = {message.chat.id}")
    status = cur.fetchone()[0]
    return status


def get_balance(message):
    con = sqlite3.connect("dannie_2.db")
    cur = con.cursor()
    cur.execute(f"SELECT balance FROM users WHERE id = {message.chat.id}")
    balance = cur.fetchone()[0]
    return balance


def get_last_popolnenie(message):
    con = sqlite3.connect("dannie_2.db")
    cur = con.cursor()
    cur.execute(f"SELECT last_popolnenie FROM users WHERE id = {message.chat.id}")
    last_popolnenie = cur.fetchone()[0]
    return last_popolnenie


def get_referals(message):
    con = sqlite3.connect("dannie_2.db")
    cur = con.cursor()
    cur.execute(f"SELECT referals FROM users WHERE id = {message.chat.id}")
    referals = cur.fetchone()[0]
    return referals


def get_ref_balance(message):
    con = sqlite3.connect("dannie_2.db")
    cur = con.cursor()
    cur.execute(f"SELECT ref_balance FROM users WHERE id = {message.chat.id}")
    ref_balance = cur.fetchone()[0]
    return ref_balance


def get_ref_link(message):
    ref_link = f"http://t.me/{bot_name}?start={message.chat.id}"
    return ref_link


def get_inf_profil(balance, referals, ref_balance, ref_link):
    inf_profil = f"✅ ЛИЧНЫЙ КАБИНЕТ Слито на @Oblako_sxem ✅\n\n" \
                 f"💵 БАЛАНС 💵\n" \
                 f"{balance}₽\n\n" \
                 f"👥 Ваши рефералы 👥\n" \
                 f"{referals}\n\n" \
                 f"💰 Ваш реферальный баланс 💰\n" \
                 f"{ref_balance}₽\n\n" \
                 f"👤 Ваша реферальная ссылка 👤\n" \
                 f"{ref_link}"
    return inf_profil
