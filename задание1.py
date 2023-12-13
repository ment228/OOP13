from tkinter import *#импортируем из библиотеки tkinter все

def close_window():#функция позволяющая закрыть окно
    window.destroy()

window = Tk()#создаем окно
window.title('Проект1')#присваеваем окну имя Проект1
window.geometry('400x100')#задаем разрешение окну

lab = Label(window, text='Моя первая программа', font=('Arial',14))#выводим на окно текст с шрифтом ариал 14 размера
lab.pack()#кнопка посередине

btn = Button(window, text='Закрыть', font=('Arial', 14),command=close_window)#создаем кнопку с текстом с шрифтом ариал 14 размера и присваиваем ей функция
btn.pack()#кнопка посередине

window.mainloop()#завершение программы окна
