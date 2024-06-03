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
            # response = response.json()
            label1.config(text=f"Курс: {response["Valute"][entry1.get()]["Value"]} ₽\n"
                               f"Валюта: {response["Valute"][entry1.get()]["Name"]}")


window = Tk()
window.geometry(f"500x200")
window.title("Курсы валют")
window.iconbitmap(resource_path("exchange_rates.ico"))
window.resizable(False, False)

welcome_text = Label(window, text="Введите буквенный код валюты", font=("Times New Roman", 12, "bold"))
welcome_text.pack(expand=True, anchor="center")

entry1 = Entry(window)
entry1.pack(expand=True, anchor="center")

label1 = Label(window, font=("Times New Roman", 20))
label1.pack(expand=True, anchor="center")

button2 = Button(window, text="Показать обменный курс", command=show_exchange_rate)
button2.pack(expand=True, anchor="center")

window.mainloop()