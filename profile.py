from imports import *
def go_main(user):
    from mainpofile import getinmain
    getinmain(user)

class profile:
    def __init__(self,username):
        self.user = username
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Profile")
        self.root.resizable(False, False)
        self.root.configure(bg='#477bb3')
        connection = sqlite3.connect('parkinglot.db')
        c = connection.cursor()
        c.execute("SELECT * FROM userInfo WHERE username = ?", (str(self.user),))
        self.infotuple = c.fetchone()
        self.id = self.infotuple[0]
        self.button26 = Button(self.root, text="Change Info",
                               font=(font_familty, 15), fg=white, bg='green',cursor = "cross"
                         , command=lambda:[self.root.destroy(),self.changes()])

        self.button26.place(x=550, y=20)

        self.button25= Button(self.root, text="Back", font=(font_familty, 15), fg=white, bg='red', cursor="cross"
                    , command=lambda:[self.root.destroy(),self.Back()])
        self.button25.place(x=50, y=20)

        self.labelbtn = Label(self.root, text="Username: " + self.infotuple[1], bg="#477bb3",
                              font=(font_familty, 15), fg=white)

        self.labelbtn.place(x = 50 , y = 80)

        self.labelbtn = Label(self.root, text="Phone Number : " + self.infotuple[2],
                              bg="#477bb3", font=(font_familty, 15), fg=white)
        self.labelbtn.place(x=50, y=130)


        self.button22 = Button(self.root, text="Change Password Here", bg="#477bb3", font=(font_familty, 15), fg="#081e36"
                       ,borderwidth=0,cursor = "cross" ,
                               command=lambda:[self.root.destroy(),self.changepassword()])
        self.button22.place(x=50, y=180)
        self.button255 = Button(self.root, text="Delete Your Account", bg="red", font=(font_familty, 15), fg=white
                       ,cursor = "cross" ,  command=lambda:[self.root.destroy(),
                                                                            self.Delete()])
        self.button255.place(x=50, y=230)


        self.root.mainloop()

    def changes(self):
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Change Data")
        self.root.resizable(False, False)
        self.root.configure(bg='#477bb3')
        self.buttonbacktomain = Button(self.root, text="Profile Page", borderwidth=0,
                                       font=(font_familty, 10), fg="#081e36",
                                       bg="#f5f5f5",
                                       width=15, command=lambda: [self.root.destroy(), profile(self.user)])
        self.buttonbacktomain.place(x=25, y=20)
        self.lbl1 = Label(self.root, text="\nYou can update your info here.",
                          font=(font_familty, 17), fg=white, bg="#477bb3")
        self.lbl1.pack(pady=20)
        self.lbl2 = Label(self.root, text="Username", font=(font_familty, 15), fg=white, bg="#477bb3")
        self.lbl2.pack(pady=20)
        self.username = Entry(self.root, width=50, bg="#f5a467", font=(font_familty, 10), fg="#081e36")
        self.username.pack(ipady=5)
        self.lbl3 = Label(self.root, text="Phone Number", font=(font_familty, 15), fg=white, bg="#477bb3")
        self.lbl3.pack(pady=20)
        self.phone = Entry(self.root, width=50, bg="#f5a467", font=(font_familty, 10), fg="#081e36")
        self.phone.pack(ipady=5)
        self.button = Button(self.root, text="Save", borderwidth=0, font=(font_familty, 15), fg="#f5f5f5", bg="#081e36",
                             width=10, command=self.saveChanges)
        self.button.pack(pady=20)
        self.root.mainloop()

    def saveChanges(self):
        self.usernameval = self.username.get()
        self.phoneval = self.phone.get()
        if self.usernameval == '' and self.phoneval == '':
            tkinter.messagebox.showinfo("Warning", "Try Again. Fill the boxes")
        else:
            if self.usernameval == '':
                # c.execute("SELECT username from userInfo WHERE Userid = ?", (self.id,))
                # username = c.fetchone()
                # print(username)
                if len(self.phoneval) == 10:
                    c.execute("UPDATE userInfo SET phonenum = (?) Where Userid = ?", (str(self.phoneval), self.id,))
                    connection.commit()
                    tkinter.messagebox.showinfo("Success", "phonenumber has been changed")
                    self.root.destroy()
                    profile(self.user)
                else:
                    tkinter.messagebox.showinfo("Failed", "your phonenumber has more or less than 10 digits")

            elif self.phoneval == '':
                c.execute("SELECT username FROM userInfo WHERE username = ? ", (str(self.usernameval),))
                self.checkuser = c.fetchone()
                if not self.checkuser:
                    c.execute('select bookingId from booking where username = ?', (self.user,))
                    ids = c.fetchone()
                    print(ids)
                    if ids:
                        for i in ids:

                            c.execute("UPDATE booking SET username = (?) Where bookingId = ?",(self.usernameval, i,))
                            connection.commit()
                    c.execute("UPDATE userInfo SET username = (?) Where Userid = ?",
                              (self.usernameval, self.id,))
                    connection.commit()
                    tkinter.messagebox.showinfo("Success", "Username has been changed")
                    self.root.destroy()
                    profile(self.usernameval)

                else:
                    tkinter.messagebox.showinfo("Failed", "Username is Taken.Try again")
            else:
                c.execute("SELECT username FROM userInfo WHERE username = ? ", (str(self.usernameval),))
                self.usercheck = c.fetchone()
                if not self.usercheck:
                    if len(self.phoneval) == 10:
                        c.execute('select bookingId from booking where username = ?', (self.user,))
                        ids = c.fetchone()
                        for i in ids:
                            c.execute("UPDATE booking SET username = (?) Where bookingId = ?",
                                      (self.usernameval, i,))
                            connection.commit()
                        c.execute("UPDATE userInfo SET username = (?),phonenum = (?) Where Userid = ?",
                                  (self.usernameval,str(self.phoneval), self.id,))
                        connection.commit()
                        tkinter.messagebox.showinfo("Success", "Username and phone num have been changed")
                        self.root.destroy()
                        profile(self.usernameval)

                    else:
                        tkinter.messagebox.showinfo("Warning", "phonenumber has more or less than 10 digits")

                else:
                    tkinter.messagebox.showinfo("Warning", "username is already taken")

    def changepassword(self):
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Change Data")
        self.root.resizable(False, False)
        self.root.configure(bg='#477bb3')
        c.execute("SELECT username FROM userInfo WHERE username = ?", (str(self.user),))
        self.infotuple = c.fetchone()
        self.name = self.infotuple[0]
        c.execute("SELECT username FROM userInfo WHERE username = ?", (str(self.user),))
        self.infotuple = c.fetchone()
        self.num = self.infotuple[0]
        self.buttonbacktomain = Button(self.root, text="Profile Page", borderwidth=0,
                                       font=(font_familty, 10), fg="#081e36",
                                       bg="#f5f5f5",
                                       width=15, command=lambda: [self.root.destroy(), profile(self.user)])
        self.buttonbacktomain.place(x=25, y=20)
        self.lbl1 = Label(self.root, text="\nYou can change your password here.",
                          font=(font_familty, 17), fg=white, bg="#477bb3")
        self.lbl1.pack(pady=20)

        self.lbl2 = Label(self.root, text="Old Password", font=(font_familty, 15), fg=white, bg="#477bb3")
        self.lbl2.pack(pady=20)
        self.oldpass = Entry(self.root, width=50, bg="#f5a467", font=(font_familty, 10), fg="#081e36", show="*")
        self.oldpass.pack(ipady=5)
        self.lbl3 = Label(self.root, text="New Password", font=(font_familty, 15), fg=white, bg="#477bb3")
        self.lbl3.pack(pady=20)
        self.newpass = Entry(self.root, width=50, bg="#f5a467", font=(font_familty, 10), fg="#081e36", show="*")
        self.newpass.pack(ipady=5)
        self.lbl3 = Label(self.root, text="Confirm Password", font=(font_familty, 15), fg=white, bg="#477bb3")
        self.lbl3.pack(pady=20)
        self.confpass = Entry(self.root, width=50, bg="#f5a467", font=(font_familty, 10), fg="#081e36", show="*")
        self.confpass.pack(ipady=5)
        self.button = Button(self.root, text="Save", borderwidth=0, font=(font_familty, 15), fg="#f5f5f5", bg="#081e36",
                             width=10, command=self.savepassChanges)
        self.button.pack(pady=20)
        self.root.mainloop()

    def savepassChanges(self):

        self.old = self.oldpass.get()
        self.new = self.newpass.get()
        self.conf = self.confpass.get()

        if self.old == '' or self.new == '' or self.conf == '':
            tkinter.messagebox.showinfo("Warning", "Try Again. Fill ALL boxes")
        else:
            c.execute("SELECT Password FROM userInfo WHERE username = ?", (str(self.user),))
            self.infotuple = c.fetchone()
            self.password = self.infotuple[0]
            if self.password == self.old:
                if self.new == self.conf:
                    c.execute("UPDATE userInfo SET Password = ? Where username = ?", (str(self.new), self.user,))
                    connection.commit()
                    tkinter.messagebox.showinfo("Success", "Password has been changed")
                else:
                    tkinter.messagebox.showinfo("Success", "your new password isn't matching the confirmation password")
            else:
                tkinter.messagebox.showinfo("Failed", "Your Old Password isn't correct.\nTry again")


    def seePaymentsAndSpots(self):
        pass


    def Delete(self):
        self.rootw = Tk()
        self.rootw.geometry("700x600")
        self.rootw.title("Delete Account")
        self.rootw.resizable(False, False)
        self.rootw.configure(bg='#477bb3')
        self.buttonbacktomain = Button(self.rootw, text="Profile Page", borderwidth=0,
                                       font=(font_familty, 10), fg="#081e36",
                                       bg="#f5f5f5",
                                       width=15, command=lambda: [self.rootw.destroy(), profile(self.user)])
        self.buttonbacktomain.place(x=25, y=20)
        self.lbl1 = Label(self.rootw, text="\nYou can delete your account here.",
                          font=(font_familty, 17), fg=white, bg="#477bb3")
        self.lbl1.pack(pady=20)
        self.lbl2 = Label(self.rootw, text="Password", font=(font_familty, 15), fg=white, bg="#477bb3")
        self.lbl2.pack(pady=20)
        self.Password = Entry(self.rootw, width=50, bg="#f5a467", font=(font_familty, 10), fg="#081e36", show="*")
        self.Password.pack(ipady=5)
        self.lbl3 = Label(self.rootw, text="Confirm Password", font=(font_familty, 15), fg=white, bg="#477bb3")
        self.lbl3.pack(pady=20)
        self.Confirm = Entry(self.rootw, width=50, bg="#f5a467", font=(font_familty, 10), fg="#081e36", show="*")
        self.Confirm.pack(ipady=5)
        self.buttondlt = Button(self.rootw, text="Delete here",
                             font=(font_familty, 15), fg="#f5f5f5", bg="red",
                             width=10, command=self.deleteaccount)
        self.buttondlt.pack(pady=20)
        self.rootw.mainloop()


    def deleteaccount(self):
        self.passwo = self.Password.get()
        self.conf = self.Confirm.get()

        if self.passwo == '' or self.conf == '':
            tkinter.messagebox.showinfo("Warning", "Fill ALL boxes")
        else:
            c.execute("SELECT Password FROM userInfo WHERE username = ?", (str(self.user),))
            self.infotuple = c.fetchone()
            self.password = self.infotuple[0]
            if self.passwo == self.conf:
                if self.password == self.passwo:
                    c.execute("Delete FROM userInfo WHERE username = ?", (self.user,))
                    connection.commit()
                    self.rootw.destroy()
                    tkinter.messagebox.showinfo("Success", "Account Deleted")
                    # main()

                else:
                    tkinter.messagebox.showinfo("Failed", "Your Password isn't correct.\nTry again")
            else:
                tkinter.messagebox.showinfo("Failed", "our password isn't matching the confirmation password")


    def Back(self):
        go_main(self.user)
