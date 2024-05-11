from tkinter import *

root = Tk()
root.geometry("300x250")
 
root.mainloop()

# list1 = Listbox(window, height=25, width=65)

# # создаём надписи для полей ввода и размещаем их по сетке
# l1 = Label(window, text="Название") 
# l1.grid(row=0, column=0) 

# l2 = Label(window, text="Стоимость")
# l2.grid(row=0, column=2)

# l3 = Label(window, text="Комментарий")
# l3.grid(row=1, column=0)

# # создаём поле ввода названия покупки, говорим, что это будут строковые переменные и размещаем их тоже по сетке
# product_text = StringVar()
# e1 = Entry(window, textvariable=product_text)
# e1.grid(row=0, column=1)

# # то же самое для комментариев и цен
# price_text = StringVar() 
# e2 = Entry(window, textvariable=price_text)
# e2.grid(row=0, column=3)

# comment_text = StringVar() 
# e3 = Entry(window, textvariable=comment_text)
# e3.grid(row=1, column=1)

# # создаём список, где появятся наши покупки, и сразу определяем его размеры в окне
# list1 = Listbox(window, height=25, width=65) 
# list1.grid(row=2, column=0, rowspan=6, columnspan=2) 

# # на всякий случай добавим сбоку скролл, чтобы можно было быстро прокручивать длинные списки
# sb1 = Scrollbar(window) 
# sb1.grid(row=2, column=2, rowspan=6)

# # привязываем скролл к списку
# list1.configure(yscrollcommand=sb1.set) 
# sb1.configure(command=list1.yview)

# # создаём кнопки действий и привязываем их к своим функциям
# # кнопки размещаем тоже по сетке
# b1 = Button(window, text="Посмотреть все", width=12, command=print('view_command')) 
# b1.grid(row=2, column=3) #size of the button

# b2 = Button(window, text="Поиск", width=12, command=print('search_command'))
# b2.grid(row=3, column=3)

# b3 = Button(window, text="Добавить", width=12, command=print('add_command'))
# b3.grid(row=4, column=3)

# b4 = Button(window, text="Обновить", width=12, command=print('update_command'))
# b4.grid(row=5, column=3)

# b5 = Button(window, text="Удалить", width=12, command=print('delete_command'))
# b5.grid(row=6, column=3)

# b6 = Button(window, text="Закрыть", width=12, command=print('on_closing'))
# b6.grid(row=7, column=3)