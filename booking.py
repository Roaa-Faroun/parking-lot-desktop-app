from imports import *
from constants import spot, fee
def go_main(user):
    from mainpofile import getinmain
    getinmain(user)
class booking:
    def __init__(self,username):
        self.user = username
        self.root = Tk()
        self.root.geometry(geometry)
        self.root.title("Profile")
        self.root.resizable(resizable, resizable)
        self.root.configure(bg=bg_color)

        c.execute("SELECT * FROM userInfo WHERE username = ?", (str(self.user),))
        self.infotuple = c.fetchone()
        self.button25= Button(self.root, text="Back", font=(font_familty, font_size_md), fg=white, bg='red', cursor="cross"
                    , command=lambda:[self.root.destroy(),self.Back()])
        self.button25.place(x=50, y=20)
        self.labelbtn = Label(self.root, text="Date: ", bg=color_2,
                              font=(font_familty, font_size_md), fg=white)

        self.labelbtn.place(x = 50 , y = 80)
        self.date = DateEntry(self.root, selectmode='day')
        self.date.place(x = 190 , y = 85)
        self.labelbtn = Label(self.root, text="Start Time : ",
                              bg=color_2, font=(font_familty, font_size_md), fg=white)
        self.labelbtn.place(x=50, y=130)
        self.Start = Entry(self.root, width=10, bg=white, font=(font_familty, font_size_sm), fg=color_1)
        self.Start.place(x=190, y=135)
        self.labelbtn = Label(self.root, text="Leaving Time:",
                              bg=color_2, font=(font_familty, font_size_md), fg=white)
        self.labelbtn.place(x=50, y=180)
        self.leave = Entry(self.root, width=10, bg=white, font=(font_familty, font_size_sm), fg=color_1)

        self.leave.place(x=190, y=185)



        self.button255 = Button(self.root, text="Reserve", bg="green", font=(font_familty, font_size_md), fg=white
                       ,cursor = "cross" ,  command=lambda:[self.reserve()])
        self.button255.place(x=50, y=230)
        self.root.mainloop()

    def reserve(self):
        self.dateresrve = self.date.get()
        self.leavetime = self.leave.get()
        self.Starttime = self.Start.get()
        if self.dateresrve == '' or self.leavetime == '' or self.Starttime == '':
            tkinter.messagebox.showinfo("Warning", "Try Again. Fill the boxes")
        else:
            import datetime
            today = datetime.date.today()
            newdate = datetime.datetime.strptime(self.dateresrve, '%m/%d/%y')
            newdate = datetime.datetime.date(newdate)
            if newdate == today:
                from datetime import datetime
                d1 = datetime.now()
                now = datetime.now().time()
                current_time = now.strftime("%H:%M")
                import datetime
                starttime = datetime.datetime.strptime(self.Starttime, "%H:%M").time()
                leavetime = datetime.datetime.strptime(self.leavetime, "%H:%M").time()
                minDuration = 30.0


                if starttime > now:
                    timedateSTART = datetime.datetime.combine(newdate, starttime)
                    timedateLEAVE = datetime.datetime.combine(newdate, leavetime)
                    if leavetime > starttime:
                        duration = timedateLEAVE - timedateSTART
                        duration = duration.seconds/60

                        if duration < minDuration:
                            tkinter.messagebox.showinfo("Failed", "less than 30 min.")
                        elif duration >= minDuration:
                            c.execute("select spotID from booking where StartTime = ? and endTime = ? and Day = ? ", (str(starttime),str(leavetime), str(newdate)),)
                            isfreespot = c.fetchall()
                            if isfreespot:
                                lst = list(set(spot) - set(isfreespot))
                                myspot =lst[0]
                            else:
                                myspot = spot[0]
                            self.fee = fee * (duration / 30)
                            qr = qrcode.QRCode(
                                version=1,
                                box_size=10,
                                border=5)
                            randomnum = str(random.randint(0, 1000000))
                            strtext = str(newdate) + str(starttime) + self.user + randomnum
                            strtext = ''.join(filter(str.isalnum, strtext))
                            name = strtext + '.png'
                            self.qr = name
                            qr.add_data(name + self.user +str(newdate)+str(starttime) + str(leavetime) )
                            qr.make(fit=True)
                            img = qr.make_image(fill='black', back_color='white')
                            img.save('img/' + name)
                            c.execute("INSERT INTO booking(username"
                                      ", Day,StartTime,"
                                      " endTime,DURATION,fee,spotID,qrid) VALUES (?,?,?,?,?,?,?,?)",(self.user,str(newdate), str(starttime), str(leavetime),duration,self.fee,myspot,self.qr))
                            connection.commit()
                            tkinter.messagebox.showinfo("Success", "Reserved")
                            self.root.destroy()
                            booking(self.user)

                elif starttime < now:
                        tkinter.messagebox.showinfo("Warning", "Cannot reserve. Choose valid time")


            elif newdate < today:
                tkinter.messagebox.showinfo("Warning", "Old date")

            elif newdate > today:
                from datetime import datetime
                d1 = datetime.now()
                now = datetime.now().time()
                current_time = now.strftime("%H:%M")
                import datetime
                starttime = datetime.datetime.strptime(self.Starttime, "%H:%M").time()
                leavetime = datetime.datetime.strptime(self.leavetime, "%H:%M").time()
                minDuration = 30.0
                timedateSTART = datetime.datetime.combine(newdate, starttime)
                timedateLEAVE = datetime.datetime.combine(newdate, leavetime)
                if leavetime > starttime:
                    duration = timedateLEAVE - timedateSTART
                    duration = duration.seconds / 60

                    if duration < minDuration:
                        tkinter.messagebox.showinfo("Failed", "less than 30 min.")
                    elif duration >= minDuration:
                        c.execute("select spotID from booking where StartTime = ? and endTime = ? and Day = ? ",
                                  (str(starttime), str(leavetime), str(newdate)), )
                        isfreespot = c.fetchone()
                        if isfreespot:
                            lst = list(set(spot) - set(isfreespot))
                            myspot = lst[0]
                        else:
                            myspot = spot[0]
                        self.fee = fee * (duration / 30)
                        qr = qrcode.QRCode(
                            version=1,
                            box_size=10,
                            border=5)
                        randomnum = str(random.randint(0, 1000000))
                        strtext = str(newdate) + str(starttime) + self.user + randomnum
                        strtext = ''.join(filter(str.isalnum, strtext))
                        name = strtext + '.png'
                        self.qr = name
                        qr.add_data(name + self.user + str(newdate) + str(starttime) + str(leavetime))
                        qr.make(fit=True)
                        img = qr.make_image(fill='black', back_color='white')
                        img.save('img/' + name)
                        c.execute("INSERT INTO booking(username"
                                  ", Day,StartTime,"
                                  " endTime,DURATION,fee,spotID,qrid) VALUES (?,?,?,?,?,?,?,?)",
                                  (self.user, str(newdate), str(starttime), str(leavetime), duration, self.fee, myspot,self.qr))
                        connection.commit()
                        tkinter.messagebox.showinfo("Success", "Reserved")

    def Back(self):
         go_main(self.user)
