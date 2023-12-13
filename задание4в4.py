from tkinter import *
import math as m

def formula():
    x = int(num1.get())
    e = 2
    y = m.sqrt(x)*m.sin(x**2/2)-1.3/((m.sqrt(x)**5)+m.pow(e,3)*x)+2*m.log10(3)*x-1/9
    res = str(int(y))
    lab2.configure(text=res)
root = Tk()#создаем окно
root.title('Кости')#даем имя окну
root.geometry('300x200')#разрешение окна

lab = Label(root,text='подсчет по формуле',font=('Arial',14),fg='Blue')#выписываем текст на окно
lab.grid(column=1,row=0)
#lab.pack()#текст по центру

lba = Label(root, text='x=')
lba.grid(column=0,row=1)
num1 = Entry(root,width=20)
num1.grid(column=1,row=1)

btn = Button(root,text='вычислить',font=('Arial',14),fg='Black',command=formula)#добавляем кнопку на окно с текстом бросить кубик
btn.grid(column=1,row=3)#кнопка по центру

lab = Label(root,text='выражение=',font=('Arial',14),fg='Blue')#выписываем текст на окно
lab.grid(column=1,row=4)

lab2 = Label(root,text='',font=('Arial',14),fg='Blue')#выписываем текст на окно
lab2.grid(column=1,row=5)



root.mainloop()#завершение программы окна