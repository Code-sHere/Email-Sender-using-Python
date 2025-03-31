import smtplib # it's a library to help the send email 
import con # it's a nem fill to connect the your email and password to connect for the this file 

from tkinter import * #it's a library to make gui interface
from tkinter import messagebox
import tkinter as pop

def send_mail(reciver,message): # it's a email sender function
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) # this is to connect the gmail
        s.starttls()  # starting the function
        s.login(con.sender, con.password)  # its your sender email password variable // and connect the email
        s.sendmail(con.sender, reciver, message) #this function send the email
        s.quit() # stop the function of email sending
        messagebox.showinfo("Done", "Message sent successfully")
        clear_fields() # clear all fileds after correct submition
    except Exception as e:
        messagebox.showerror("Error", str(e)) #its show error on wrong submition

def validation():  # validation of the email correct submition
    email = name.get()
    if email =="" or "@gamil.com" not in email:
        messagebox.showerror("Error"," Plese fill correct eamil")
        clear_fields()
    else:
        send_mail(email, msg.get("1.0",END))

def  clear_fields():  # clear fields function
    name.delete(0, END)
    msg.delete("1.0", END)
window= pop.Tk()

window.configure(background = "#ff1d58")
window.geometry("650x350")

# layout

Label(window,text="Emial sender", font = ('',40), fg="white", bg="#ff1d58").place(x = 78, y =20)

Label(window,text="Send To", font = ('',20), fg="white", bg="#ff1d58").place(x =38, y =78)

Label(window,text="Message", font = ('',20), fg="white", bg="#ff1d58").place(x = 25, y =110)

name = Entry(window, font=('', 17), width=30)
name.place(x =180, y = 78)
msg = Text(window, height = 5, width= 30, font=('', 17))
msg.place(x = 180, y = 110)

Button(window, text=" send ", font=('',20),fg="white",bg="#ff1d58", command=lambda :
       send_mail(name.get(),msg.get("1.0",END))
	   ).place(x = 180, y =250)


window.mainloop()

