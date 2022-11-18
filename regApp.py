import tkinter.messagebox
import tkinter
from tkinter import *
import tkinter.messagebox
import tkinter.ttk
from database import *
from style import *
from subprocess import call

def go_to_main():
    call(["python", "main.py"])

def go_to_login():
    call(["python", "startApp.py"])

class regApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry(geometry)
        self.root.resizable(resizable, resizable)
        self.root.configure(bg=bg_color)
        self.root .title("Register Page")
        self.buttonbacktomain = Button(self.root, text="Main Page", borderwidth=0, font=(font_familty, font_size_sm), fg=color_1,
                                       bg=color_3,
                                       width=15, command=lambda:[self.root.destroy(), go_to_main()])
        self.buttonbacktomain.place(x=25, y=20)
        self.buttonReg = Button(self.root, text="Login Page", borderwidth=0, font=(font_familty, font_size_sm),
                                       fg=color_1,
                                       bg=color_3,
                                       width=15, command= lambda:[self.root.destroy(),go_to_login()])
        self.buttonReg.place(x = 550 , y =20)
        self.lbl1 = Label(self.root, text="Welcome.\n You can register here.",
                     font=(font_familty,17), fg= white,bg = color_2  )
        self.lbl1.pack(pady=20)
        self.lbl2 = Label(self.root, text="Username", font=(font_familty,font_size_md),fg= white,bg = color_2 )
        self.lbl2.pack(pady=20)
        self.username = Entry(self.root, width= 50,bg = color_4,font=(font_familty,font_size_sm),fg= color_1)
        self.username.pack(ipady=5)
        self.lbl3 = Label(self.root, text="Phone Number", font=(font_familty,font_size_md),fg= white,bg = color_2 )
        self.lbl3.pack(pady=20)
        self.phone = Entry(self.root, width= 50,bg = color_4,font=(font_familty,font_size_sm),fg= color_1)
        self.phone.pack(ipady=5)
        self.lbl4 = Label(self.root, text="Password", font =(font_familty,font_size_md), fg= white,bg = color_2 )
        self.lbl4.pack(pady=20)
        self.password = Entry(self.root, width= 50,bg = color_4,font=(font_familty,font_size_sm),fg= color_1,show ='*')
        self.password.pack(ipady=5)
        self.lbl5 = Label(self.root, text="Confirm Password", font =(font_familty,font_size_md), fg= white,bg = color_2 )
        self.lbl5.pack(pady=20)
        self.conpassword = Entry(self.root, width= 50,bg = color_4,font=(font_familty,font_size_sm),fg= color_1,show ='*')
        self.conpassword.pack(ipady=5)
        self.button = Button(self.root, text="Register",  borderwidth=0,font=(font_familty, font_size_md), fg=color_3, bg=color_1,
                        width=10,command =self.reg)
        self.button.pack(pady=20)
        self.root.mainloop()

#################################################
    def reg(self):
        self.usernameval =  self.username.get()
        self.phoneval = self.phone.get()
        self.passwordval = self.password.get()
        self.conpasswordval = self.conpassword.get()
        if self.usernameval == '' or self.phoneval == '' or self.passwordval == '' or self.conpasswordval == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
             c.execute("SELECT username FROM userInfo WHERE username = ?", (str(self.usernameval),))
             existusername = c.fetchone()
             if existusername:
                tkinter.messagebox.showinfo("Warning", "Username Is Already Taken.\nPlease Choose Another One.")
             elif self.conpasswordval != self.passwordval:
                tkinter.messagebox.showinfo("Warning", "The passwords did not match.\nPlease Check the confirmation entry.")
             elif len(self.phoneval) < 10:
                tkinter.messagebox.showinfo("Warning", "The phone number must be 10 digits.")
             else:
                 c.execute("INSERT INTO userInfo(username, phonenum, Password) VALUES (?,?,?)",(self.usernameval, self.phoneval, self.passwordval))
                 connection.commit()
                 tkinter.messagebox.showinfo("Success", "You Have Registered Successfully.\nGo To Login Page")

if __name__ == '__main__':
    regApp()