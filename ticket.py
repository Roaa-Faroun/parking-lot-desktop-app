from imports import *
def go_main(user):
    from mainpofile import getinmain
    getinmain(user)
class tickets:
    def __init__(self,username):
        self.username = username
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Find Your Ticket")
        self.root.resizable(False, False)
        self.root.configure(bg='#477bb3')
        self.button21 = Button(self.root, text="Back", font=("Arial", 15), fg="#fff", bg='red', cursor="cross"
                    , command=lambda:[self.root.destroy(),self.Back()])
        self.button21.place(x=50, y=20)
        self.labelbtn = Label(self.root, text="Your Reservations, " + str(self.username), bg="#da5ae8",
                              font=("Arial", 18), fg="#fff")
        self.labelbtn.place(x = 200 , y = 25)
        c.execute("SELECT * FROM booking WHERE username = ?", (str(self.username),))
        self.infotuple = c.fetchall()
        if self.infotuple:#if user has any booking then....
            import datetime
            today = datetime.date.today()
            from datetime import datetime
            now = datetime.now().time()
            date_time = today.strftime("%Y-%m-%d")
            current_time = now.strftime("%H:%M:00")
            c.execute("SELECT Day,bookingId FROM booking WHERE username = ? ", (str(self.username),))
            gettingdate = c.fetchall() # take the reservation date
            self.col =80
            for i in gettingdate:# i is because there maybe many reservations for the same user, for each reservation, imma check the date
                self.col = self.col + 50
                if date_time > i[0]:#if reserved date has passed , don't show it
                    self.col = self.col - 50
                elif date_time < i[0]: # if date is yet to come, then show it
                    c.execute("SELECT Day,StartTime,endTime,DURATION,fee,spotID FROM booking WHERE bookingId = ? ", (i[1],))
                    self.data = c.fetchall()
                    e = Label(self.root, width=10, text="Date", bg="#081e36", fg='orange',
                              font=('Arial', 12, 'bold'))
                    e.place(x=40, y=80)
                    e = Label(self.root, width=9, text="Start Time", bg="#081e36", fg='orange',
                              font=('Arial', 12, 'bold'))
                    e.place(x=135, y=80)
                    e = Label(self.root, width=9, text="End Time", bg="#081e36", fg='orange',
                              font=('Arial', 12, 'bold'))
                    e.place(x=220, y=80)
                    e = Label(self.root, width=10, text="Duration",bg="#081e36", fg='orange',
                              font=('Arial', 12, 'bold'))
                    e.place(x=315, y=80)
                    e = Label(self.root, width=10, text="Fees",bg="#081e36", fg='orange',
                              font=('Arial', 12, 'bold'))
                    e.place(x=400, y=80)##081e36
                    e = Label(self.root, width=10, text="Spot Num",bg="#081e36", fg='orange',
                              font=('Arial', 12, 'bold'))
                    e.place(x=485, y=80)
                    total_rows = len(self.data) # all rows
                    total_columns = len(self.data[0])  # each row
                    self.r =40
                    for x in range(total_rows):
                        for j in range(total_columns):
                                if type(self.data[x][j]) == str:
                                    e = Label(self.root, width=9, text=str(self.data[x][j]), fg='blue',
                                              font=('Arial', 12, 'bold'))
                                    e.place(x=self.r, y=self.col)
                                    self.r = self.r  + 90

                                else:
                                    if type(self.data[x][j]) == float:
                                        d = f"{self.data[x][j]:.2f}"
                                        e = Label(self.root, width=9, text=str(d), fg='blue',
                                              font=('Arial', 12, 'bold'))
                                        e.place(x=self.r , y=self.col)
                                        self.r  =self.r + 90
                                    else:
                                      e = Label(self.root, width=9, text=str(self.data[x][j]), fg='blue',
                                              font=('Arial', 12, 'bold'))
                                      e.place(x=self.r , y=self.col,)
                                      self.r = self.r + 90
                        self.btn2 = Button(self.root, text="QR Code", font=("Arial", 10),
                                                   fg="#fff", bg='orange', cursor="cross"
                                                   , command=lambda: [self.ticket(i[1])])
                        self.btn2.place(x=(self.r +40), y=self.col)





                elif date_time == i[0]:# if date is today, check the time
                    c.execute("SELECT endTime FROM booking WHERE bookingId = ?  ", (i[1],))
                    gettingtime = c.fetchone()
                    if gettingtime[0] >  current_time:# if time has not passed, do sth
                        c.execute("SELECT Day,StartTime,endTime,DURATION,fee,spotID FROM booking WHERE bookingId = ? ",
                                  (i[1],))
                        self.data = c.fetchall()
                        e = Label(self.root, width=10, text="Date", bg="#081e36", fg='orange',
                                  font=('Arial', 12, 'bold'))
                        e.place(x=40, y=80)
                        e = Label(self.root, width=9, text="Start Time", bg="#081e36", fg='orange',
                                  font=('Arial', 12, 'bold'))
                        e.place(x=135, y=80)
                        e = Label(self.root, width=9, text="End Time", bg="#081e36", fg='orange',
                                  font=('Arial', 12, 'bold'))
                        e.place(x=220, y=80)
                        e = Label(self.root, width=10, text="Duration", bg="#081e36", fg='orange',
                                  font=('Arial', 12, 'bold'))
                        e.place(x=315, y=80)
                        e = Label(self.root, width=10, text="Fees", bg="#081e36", fg='orange',
                                  font=('Arial', 12, 'bold'))
                        e.place(x=400, y=80)  ##081e36
                        e = Label(self.root, width=10, text="Spot Num", bg="#081e36", fg='orange',
                                  font=('Arial', 12, 'bold'))
                        e.place(x=485, y=80)
                        total_rows = len(self.data)  # all rows
                        total_columns = len(self.data[0])  # each row
                        self.r = 40
                        for x in range(total_rows):
                            for j in range(total_columns):
                                if type(self.data[x][j]) == str:
                                    e = Label(self.root, width=9, text=str(self.data[x][j]), fg='blue',
                                              font=('Arial', 12, 'bold'))
                                    e.place(x=self.r, y=self.col)
                                    self.r = self.r + 90

                                else:
                                    if type(self.data[x][j]) == float:
                                        d = f"{self.data[x][j]:.2f}"
                                        e = Label(self.root, width=9, text=str(d), fg='blue',
                                                  font=('Arial', 12, 'bold'))
                                        e.place(x=self.r, y=self.col)
                                        self.r = self.r + 90
                                    else:
                                        e = Label(self.root, width=9, text=str(self.data[x][j]), fg='blue',
                                                  font=('Arial', 12, 'bold'))
                                        e.place(x=self.r, y=self.col, )
                                        self.r = self.r + 90
                            self.btn2 = Button(self.root, text="QR Code", font=("Arial", 10),
                                               fg="#fff", bg='orange', cursor="cross"
                                               , command=lambda: [self.ticket(i[1])])
                            self.btn2.place(x=(self.r + 40), y=self.col)
                    else:
                        self.col = self.col - 50

                else:
                    self.col = self.col - 50

        else:
            e = Label(self.root,  text="NO RESERVATIONS", fg='orange', font=('Arial', 16, 'bold'))
            e.place(x=200, y=100)
        self.root.mainloop()
    def ticket(self,id):
        id = id
        self.root.destroy()
        master = Tk()
        newname = self.username
        master.geometry("700x600")
        master.title("QR CODE")
        master.resizable(False, False)
        master.configure(bg='#477bb3')
        self.button21 = Button(master, text="Back", font=("Arial", 15), fg="#fff", bg='red', cursor="cross"
                    , command=lambda:[master.destroy(),tickets(newname)])
        self.button21.place(x=50, y=20)
        c.execute("SELECT qrid FROM booking WHERE bookingId = ? ", (id,))
        name = c.fetchone()
        from PIL import ImageTk, Image
        name = 'img/' + name[0]
        cd = PhotoImage(file=name)
        code = Label(master)
        code.config(image=cd)
        code.image = cd
        code.place(x=200, y=100)

    def Back(self):
        go_main(self.username)

