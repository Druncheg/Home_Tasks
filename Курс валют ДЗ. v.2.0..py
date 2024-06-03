# https://www.cbr-xml-daily.ru/daily_json.js

from tkinter import *
import requests
from tkinter.messagebox import showerror
import os, sys

response = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js").json()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def currency_list():
    window1 = Tk()
    window1.geometry(f"100x200+750+200")
    window1.title("Справочник кодов валют")
    window1.iconbitmap(resource_path("exchange_rates.ico"))
    window1.resizable(False, True)

    for i in response["Valute"].keys():
            label_currency_list = Label(window1, text=f"{i}")
            # label_currency_list = Label(window1, text=f"{i, response[i]["Name"]}")
            label_currency_list.pack(expand=True, anchor="center")

def show_exchange_rate():
    exchange_rate = entry1.get()
    if not exchange_rate:
        label1.config(text="")
        showerror("Ошибка", "Строка не может быть пустой!")
    else:
        if entry1.get() not in response["Valute"].keys():
            label1.config(text="")
            showerror("Ошибка", "Указанный код валюты не найден!")
        else:
            label1.config(text=f"Курс: {response["Valute"][entry1.get()]["Value"]} ₽\n"
                               f"Валюта: {response["Valute"][entry1.get()]["Name"]}")


window = Tk()
window.geometry(f"500x200")
window.title("Курсы валют")
window.iconbitmap(resource_path("exchange_rates.ico"))
window.resizable(False, False)

welcome_text = Label(window, text="Введите буквенный код валюты", font=("Times New Roman", 12, "bold"))
welcome_text.pack(expand=True, anchor="center")

button1 = Button(window, text="Справочник кодов валют", command=currency_list)
button1.pack(expand=True, anchor="e", padx=10)

entry1 = Entry(window)
entry1.pack(expand=True, anchor="center")

label1 = Label(window, font=("Times New Roman", 20))
label1.pack(expand=True, anchor="center")

button2 = Button(window, text="Показать обменный курс", command=show_exchange_rate)
button2.pack(expand=True, anchor="center")

window.mainloop()