#导入图片要先下一个illow库输入一个P就会跳入，(好神奇啊)，ip也可以，在windows里下
#一定要中文输入法pip,pillow
#Tkinter  是 Python 标准库中的一个模块，用于创建图形用户界面（GUI）应用程序。
#Tkinter  提供了一组工具和组件，如按钮、文本框、标签、菜单等，允许开发者使用 Python 编程语言来构建具有交互性的窗口界面。
#它基于  Tk  工具包，是一个跨平台的 GUI 框架，可以在 Windows、Mac 和 Linux 等操作系统上运行。

from PIL import Image, ImageTk
import tkinter as tk
def show_gif():
    #找到位置
    image1 = Image.open("D:\杜甫ppt\羊-C.jpg")
    #转换为kinke  tkinker可用格式
    tk_image = ImageTk.PhotoImage(image1)
    #创建一个thinker的标签，并设置其图像转化后的gif图像
    label = tk.Label(root, image=tk_image)
    #移动到指定位置
    label.place(x = 100,y = 0)
    
    image2 = Image.open("D:\杜甫ppt\狼-C.jpg") 
    tk_image2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(root, image=tk_image2)
    label2.place(x = 0,y = 0)
    
    image3 = Image.open("D:\杜甫ppt\菜-C.jpg") 
    tk_image3 = ImageTk.PhotoImage(image3)
    label3 = tk.Label(root, image=tk_image3)
    label3.place(x = 0,y = 100)
    
    image4 = Image.open("D:\杜甫ppt\船-C.jpg") 
    tk_image4 = ImageTk.PhotoImage(image4)
    label4 = tk.Label(root, image=tk_image4)
    label4.place(x = 100,y = 10)
    #
    root.mainloop()
root = tk.Tk()
show_gif()
