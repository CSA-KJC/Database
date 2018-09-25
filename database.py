##                 GNU GENERAL PUBLIC LICENSE
##                   Version 3, 29 June 2007
##
##Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
##Everyone is permitted to copy and distribute verbatim copies
##of this license document, but changing it is not allowed.
##
##                        Preamble
##
##The GNU General Public License is a free, copyleft license for
##software and other kinds of works.
##
##The licenses for most software and other practical works are designed
##to take away your freedom to share and change the works.  By contrast,
##the GNU General Public License is intended to guarantee your freedom to
##share and change all versions of a program--to make sure it remains free
##software for all its users.  We, the Free Software Foundation, use the
##GNU General Public License for most of our software; it applies also to
##any other work released this way by its authors.  You can apply it to
##your programs, too.

#Katie Chiu
#Database. Last update 9/24/18


from tkinter import *
from tkinter import ttk


class App:
    def restart(self, event):  # leaves combobox blank
        event.widget.master.focus_set()

    def __init__(self, root):
        frame = Frame(root)  # entries frame
        frame.pack(anchor="w")
        self.z = StringVar()  # value for username
        self.z.set("")
        self.userlabel = Label(frame, text="Username:")  # username
        self.userlabel.pack(anchor="w")
        self.username = Entry(frame, textvariable=self.z, width=20)  # username entry
        self.username.pack(anchor="w")
        self.x = StringVar()  # value for password
        self.x.set("")
        self.passwordlabel = Label(frame, text="Password:")
        self.passwordlabel.pack(anchor="w")
        self.password = Entry(frame, textvariable=self.x, width=20, show="*")  # password entry
        self.password.pack(anchor="w")

        frame1 = Frame(root)  # radiobuttons frame
        frame1.pack(anchor="w")
        self.y = StringVar()  # value for radiobuttons
        self.y.set(0)  # deselects buttons
        self.male = Radiobutton(frame1, text="Male", variable=self.y, value="male")  # male radiobutton
        self.male.pack(anchor="w")
        self.female = Radiobutton(frame1, text="Female", variable=self.y, value="female")  # female radiobutton
        self.female.pack(anchor="w")

        frame2 = Frame(root)  # checkbuttons frame
        frame2.pack(anchor="w")
        self.type=Label(frame2, text="User Type:")
        self.type.pack(anchor="w")
        self.onevar = StringVar()  # value for checkbutton
        self.onevar.set(0)  # deselect checkbuttons
        self.admin = Checkbutton(frame2, text="Admin", variable=self.onevar, onvalue="Admin",
                                 offvalue="0")  # admin checkbutton
        self.admin.pack(anchor="w")
        self.user = Checkbutton(frame2, text="User", variable=self.onevar, onvalue="User",
                                offvalue="0")  # user checkbutton
        self.user.pack(anchor="w")
        self.guest = Checkbutton(frame2, text="Guest", variable=self.onevar, onvalue="Guest",
                                 offvalue="0")  # guest checkbutton
        self.guest.pack(anchor="w")

        frame3 = Frame(root)  # combobox frame
        frame3.pack(anchor="w")
        self.section = StringVar()  # combobox value
        self.section.set("")
        self.box = ttk.Combobox(frame3, state="readonly", textvariable=self.section)  # combobox
        self.box["values"] = ["IT", "HR", "Sales", "Maintenance", "Other"]  # values
        self.box.pack()
        self.box.bind("<<ComboboxSelected>>")  # applies selected value
        self.box.bind("<FocusIn>", self.restart)

        frame4 = Frame(root)  # frame for buttons
        frame4.pack(anchor="w")
        self.clear = Button(frame4, text="Clear", command=self.none)  # clear button
        self.clear.pack(anchor="w")
        self.submit = Button(frame4, text="Submit", command=self.submit)  # submit button
        self.submit.pack(anchor="w")

        frame5 = Frame(root)  # frame for label
        frame5.pack(anchor="w")
        self.final = Label(frame5)
        self.final.pack()

    def none(self):  # clear function
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.y.set(0)
        self.onevar.set(0)
        self.section.set("")
        self.box.bind("<FocusIn>", self.restart)

    def submit(self):  # write in file
        allusers=[]
        allusers.append(self.z.get())
        allusers=("").join(allusers)
        check=open("usernames.txt","r")
        line=check.readline()
        while line:
            line=list(line)
            del line[-1]
            line=("").join(line)
            break
        while line:
            if line==allusers:
                self.final.config(text="User already exists")
                self.username.delete(0, END)  # clears values
                self.password.delete(0, END)
                self.y.set(0)
                self.onevar.set(0)
                self.section.set("")
                self.box.bind("<FocusIn>", self.restart)
                break
            else:
                line=check.readline()
        if line!=allusers:
            final=open("usernames.txt","a")
            final.write(allusers)
            final.write("\n")
            final.close()
        if self.z.get() != "" and self.x.get() != "" and self.y.get() != "0" and self.onevar.get() != "0" and self.section.get() != "" and line!=allusers:
            self.final.config(text="User Created")
            values = [str(self.z.get()), str(self.x.get()), str(self.y.get()), str(self.onevar.get()),str(self.section.get())]  # gets all values
            files = open("users.txt", "a")
            for x in values:  # writes to file
                files.write(x)
                files.write(",")
            files.write("\n")
            files.close()
            self.username.delete(0, END)  # clears values
            self.password.delete(0, END)
            self.y.set(0)
            self.onevar.set(0)
            self.section.set("")
            self.box.bind("<FocusIn>", self.restart)
        elif self.z.get()=="" or self.x.get()=="" or self.y.get()=="0" or self.onevar.get()=="0" or self.section.get()=="":
            if line!=allusers:
                self.final.config(text="Error")
                self.username.delete(0, END)  # clears values
                self.password.delete(0, END)
                self.y.set(0)
                self.onevar.set(0)
                self.section.set("")
                self.box.bind("<FocusIn>", self.restart)
        check.close()
        



root = Tk()
app = App(root)
start1=open("usernames.txt","a")
start1.close()
start=open("users.txt","a")
start.close()
root.title("Create User")
root.geometry("150x325")
root.resizable(width=False, height=False)
root.mainloop()
root.destroy()
