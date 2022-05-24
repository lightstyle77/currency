from tkinter import *
import requests

window = Tk()
window.geometry("200x200")
window.title("$")
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
lbl = Label(window, text=round(data['Valute']['USD']['Value'], 2))
lbl.grid(column=0, row=0)
lbl.place(relx=.4, rely=.4)
window.mainloop()


