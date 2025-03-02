import tkinter

window = tkinter.Tk()  # 创新窗口实例
window.geometry("400x300")
label_one = tkinter.Label(window, text="实训3-1:温度转换")  # 标题
# label_one.place(x=60, y=0)
label_one.pack()  # 显示标题
label_two = tkinter.Label(window, text="请输入摄氏度:", )
label_two.place(x=70, y=50)
# label_two.pack()


entry1 = tkinter.Entry(window)  # 添加文本框1
entry1.place(x=160, y=50)


def get_data():
    get_data1 = entry1.get()  # 获取数据
    get_data1 = float(get_data1)
    get_data1 = get_data1 * 9 / 5 + 32  # 计算
    label_get = tkinter.Label(window, text=get_data1)  # 输出
    label_get.place(x='150', y='200')


button = tkinter.Button(window, text="计算", command=get_data)
button.place(x='150', y='100')
# entry1.pack()  # 将文本框添加到窗口中
# entry2 = tkinter.Entry(window)  # 添加文本框2
# entry2.pack()  # 将文本框添加到窗口中


window.mainloop()  # 进入消息循环
