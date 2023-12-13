from tkinter import *#импортируем из библиотеки tkinter все

def clicked():#функция позволяющая закрыть окно
    lab.configure(text='первые и не последние!', font=('Arial',14), fg='black')

def close_window():#функция позволяющая закрыть окно
    window.destroy()

window = Tk()#создаем окно
window.title('Проект2')#присваеваем окну имя Проект1
window.geometry('400x100')#задаем разрешение окну

lab = Label(window, text='первые успехи!', font=('Georgia',17), fg='red')#выводим на окно текст с шрифтом ариал 14 размера
lab.grid(column=1,row=0)#кнопка посередине

btn = Button(window, text='приветствие', font=('Arial', 14),command=clicked)#создаем кнопку с текстом с шрифтом ариал 14 размера и присваиваем ей функцию
btn.grid(column=0,row=1)#кнопка посередине

btn1 = Button(window, text='Закрыть', font=('Arial', 14),command=close_window)#создаем кнопку с текстом с шрифтом ариал 14 размера и присваиваем ей функцию
btn1.grid(column=2,row=1)#кнопка посередине

window.mainloop()#завершение программы окна
