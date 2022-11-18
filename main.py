from style import *
from tkinter import *
from regApp import regApp
from startApp import startApp

def main():
    global root
    root = Tk()
    root.geometry(geometry)
    root.title("Welcome Page")
    root.resizable(resizable, resizable)
    root.configure(bg=bg_color)

    from PIL import ImageTk, Image
    img0 = Image.open('img/Parking-Lot-of-deas.jpg')
    img0 = img0.resize((700, 200))
    img = ImageTk.PhotoImage(img0)
    l = Label(image=img)
    l.place(x=0, y=0)
    label2 = Label(root, text="Welcome To Our Parking Lot", font=("Arial", 30), fg="#000090", bg="#f5f5f5")
    label2.pack(pady=50)

    frame1 = Frame(root)
    frame1.place(x=100, y=300)
    frame2 = Frame(root)
    frame2.place(x=400, y=300)
    button1 = Button(frame1, text="Register", font=("Arial", 30), fg="#000090", bg="#f5f5f5", width=10,
                         borderwidth=0, command=lambda:[root.destroy(),regApp()])
    button1.pack()
    button2 = Button(frame2, text="Login", font=("Arial", 30), fg="#f5f5f5", bg="#000090", width=10,
                         borderwidth=0, command=lambda:[root.destroy(),startApp()])
    button2.pack()
    root.mainloop()

if __name__ == '__main__':
    main()