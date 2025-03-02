import tkinter


def 主程序():
    number = 1000.0
    number_str = str(number)
    button_开始.pack_forget()
    aa = 1
    if aa != 10:
        title = "所想的值是否小于" + number_str #输出题目
        label_five = tkinter.Label(window, text=title)  # 标题
        label_five.pack()
        button = tkinter.Button(window, text="    是    ", command=函数1(number))  #创建按钮
        button_no = tkinter.Button(window, text="    否    ")   #创建按钮
        button.place(x='120', y='160')  #显示按钮
        button_no.place(x='200', y='160')   #显示按钮
        print(number)
        aa += 1
    else:
        print('您afsa')

def 函数1(number):
    number = number/2
    return(number)
window = tkinter.Tk()  # 创新窗口实例
window.geometry("400x300")  # 窗口大小
label_one = tkinter.Label(window, text="二分法求值")  # 标题
label_one.pack()  # 显示标题
entry = tkinter.Entry(window)  #创建文本框
label_two = tkinter.Label(window, text="请在心中想一个一千以内的自然数")
label_two.pack()
button_开始 = tkinter.Button(window, text="    开始    ", command=主程序)
button_开始.pack()
# label_there = tkinter.Label(window, text="所想的数是否小于",)
# label_there.pack()

window.mainloop()