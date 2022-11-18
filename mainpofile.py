from imports import *
from profile import profile
from booking import booking
from reservation import reservationinfo
from ticket import tickets

def go_to_login():
    call(["python", "startApp.py"])
def to_booking(username):
    booking(username)
    # call(["python", "startApp.py"])
def to_ticket(username):
    tickets(username)
    # call(["python", "startApp.py"])
def  to_profile(username):
    profile(username)
    # call(["python", "startApp.py"])
def reservation_info(username):
    reservationinfo(username)
    # call(["python", "startApp.py"])

newimg = cv2.imread('img/book.png')
newimg = cv2.resize(newimg, (100, 100))
cv2.imwrite("img/book.png", newimg)
newimg = cv2.imread('img/ticket.png')
newimg = cv2.resize(newimg, (100, 100))
cv2.imwrite("img/ticket.png", newimg)
newimg = cv2.imread('img/prof.png')
newimg = cv2.resize(newimg, (100, 100))
cv2.imwrite("img/prof.png", newimg)

newimg = cv2.imread('img/info.png')
newimg = cv2.resize(newimg, (100, 100))
cv2.imwrite("img/info.png", newimg)



def getinmain(username):
    username = username
    print(username)

    global root
    root = Tk()
    root.geometry(geometry)
    root.title("Main Page")
    root.resizable(resizable, resizable)
    root.configure(bg=bg_color)
    from PIL import ImageTk, Image
    img0 = Image.open("img/back.png")
    img0 = img0.resize((700, 200))
    img = ImageTk.PhotoImage(img0)
    l = Label(image=img)
    l.place(x=0, y=0)
    buttonbacktomain = Button(root, borderwidth=0, text="Logout", font=(font_familty, font_size_sm), fg=color_1,
                                   bg="orange",
                                   width=15, command=lambda: [root.destroy(), go_to_login()])
    buttonbacktomain.place(x=10, y=20)
    label2 = Label(root, text="Welcome "+ username , font=(font_familty, 30), fg="#000090", bg=color_3)
    label2.pack(pady=50)

    icon = PhotoImage(file='img/book.png')
    icon2 = PhotoImage(file='img/ticket.png')
    icon3 = PhotoImage(file='img/prof.png')
    icon4 =  PhotoImage(file='img/info.png')

    frame1 = Frame(root,bg=bg_color)
    frame1.place(x=100, y=250)
    frame2 = Frame(root,bg=bg_color)
    frame2.place(x=500, y=250)

    button1 = Button(frame1, text="book",cursor = "cross",font=(font_familty, 30), fg="#000090", bg=bg_color,
                     borderwidth=0, command=lambda:[root.destroy(),to_booking(username)])
    button1.config(image=icon)
    button1.image = icon
    button1.pack()
    labelbut1 = Label(frame1, text="Book Spot", bg=color_2, font=(font_familty, font_size_md), fg="#000090")
    labelbut1.pack()

    labelbu = Label(frame1, text="", bg=color_2, font=(font_familty, font_size_md), fg="#000090")
    labelbu.pack()
    button12 = Button(frame1, text="Your Ticket",cursor = "cross", font=(font_familty, 30), fg="#000090", bg=bg_color,
                      borderwidth=0, command=lambda:[root.destroy(),to_ticket(username)])
    button12.config(image=icon2)
    button12.image = icon2
    button12.pack()
    labelbut12 = Label(frame1, text="Your Ticket", bg=color_2, font=(font_familty, font_size_md), fg="#000090")
    labelbut12.pack()
    button2 = Button(frame2, text="Profile", font=(font_familty, 30),cursor = "cross", fg="#000090", bg=bg_color,
                     borderwidth=0, command=lambda: [root.destroy(), to_profile(username)])
    button2.config(image=icon3)
    button2.image = icon3
    button2.pack()
    labelbut2 = Label(frame2, text="Profile", bg=color_2, font=(font_familty, font_size_md), fg="#000090",cursor = "cross" )
    labelbut2.pack()
    labelbut = Label(frame2, text="", bg=color_2, font=(font_familty, font_size_md), fg="#000090")
    labelbut.pack()
    button21 = Button(frame2, text="Info", font=(font_familty, 30), fg="#000090", bg=bg_color,
                      borderwidth=0,cursor = "cross" , command=lambda:[root.destroy(),reservation_info(username)])
    button21.config(image=icon4)
    button21.image = icon4
    button21.pack()
    labelbut21 = Label(frame2, text="Info", bg=color_2, font=(font_familty, font_size_md), fg="#000090")
    labelbut21.pack()
    root.mainloop()
# if __name__ == '__main__':
#     pass
#     #getinmain(startApp.username)