from imports import *
from mainpofile import getinmain
def go_to_main():
    call(["python", "main.py"])

def go_to_registration():
    call(["python", "regApp.py"])
def get_in_main(user):
    getinmain(user)
    # call(["python", "mainpofile.py  "])

class startApp:

    def __init__(self):
        self.master = Tk()
        self.master.geometry(geometry)
        self.master.resizable(resizable, resizable)
        self.master.configure(bg=bg_color)
        self.master.title("Login Page")
        self.buttonbacktomain = Button(self.master, borderwidth=0,text="Main Page", font=(font_familty, font_size_sm), fg=color_1,
                                       bg=color_3,
                                       width=15,command = lambda:[self.master.destroy(),go_to_main()])
        self.buttonbacktomain.place(x=10, y=20)
        self.buttonLog = Button(self.master, text="Register Page", borderwidth=0, font=(font_familty, font_size_sm),
                                       fg=color_1,
                                       bg=color_3,
                                       width=15, command= lambda:[self.master.destroy(),go_to_registration()])
        self.buttonLog.place(x=550, y=20)
        self.lbl1 = Label(self.master, text="Welcome back.\n\n You can Login by entering your username and password",
                     font=(font_familty,17), fg= white,bg = color_2  )
        self.lbl1.pack(pady=50)
        self.lbl2 = Label(self.master, text="Username", font=(font_familty,font_size_md),fg= white,bg = color_2 )
        self.lbl2.pack(pady=20)
        self.username = Entry(self.master, width= 50,bg = color_4,font=(font_familty,font_size_sm),fg= color_1)
        self.username.pack(ipady=5)
        self.lbl3 = Label(self.master, text="Password", font =(font_familty,font_size_md), fg= white,bg = color_2 )
        self.lbl3.pack(pady=20)
        self.password = Entry(self.master, width= 50,bg = color_4,font=(font_familty,font_size_sm),fg= color_1,show ='*')
        self.password.pack(ipady=5)
        self.button = Button(self.master, borderwidth=0, text="Login", font=(font_familty, font_size_md), fg=color_3, bg=color_1,
                        width=10,command =self.login)
        self.button.pack(pady=20)
        self.master.mainloop()


    def login(self):
        global getData
        global ids
        ids =[]
        self.usernameval = self.username.get()
        self.passwordval = self.password.get()


        if self.usernameval == '' or self.passwordval == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
             c.execute("SELECT username FROM userInfo WHERE username = ?", (str(self.usernameval),))
             existusername = c.fetchone()
             if existusername:
                 c.execute("SELECT Password FROM userInfo WHERE username=?", (str(self.usernameval),))
                 checkPass = c.fetchone()
                 if checkPass[0] == self.passwordval:
                     c.execute("SELECT userId FROM userInfo WHERE username=?", (str(self.usernameval),))
                     self.getData= c.fetchall()
                     ids.append(self.getData)
                     # startApp.username = self.usernameval

                     self.master.destroy()

                     get_in_main(self.usernameval)

                 else:
                     tkinter.messagebox.showinfo("Warning", "Wrong Password.\n Try Again.")
             else:
                 tkinter.messagebox.showinfo("Warning", "Username Does Not Exist. Try Registering First")

if __name__ == '__main__':
    my_app = startApp()
    user = my_app.usernameval