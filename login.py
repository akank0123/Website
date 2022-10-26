from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

#This is the gui part of frontend how to create the page of otp verification
class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False,False)
        self.n=random.randint(1000,9999)
        self.client=Client("ACd00625708446d429f45e4624ad9fad29","a4c09c8e6058dbc717782bb9e524c4ed")
        self.client.messages.create(to=[""],from_="",body=self.n)


    def Labels(self):
        self.c = Canvas(self,bg= "white",width=400,height=200)
        self.c.place(x=100,y=60)

        self.Login_Title=Label(self,text="OTP Verification",font="bold,20",bg="white")    #login title on top
        self.Login_Title.place(x=210,y=90)

    def Entry(self):
        self.user_Name=Text(self,borderwidth=2,wrap="word",width=29,height=2)
        self.user_Name.place(x=190,y=160)

    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="https://cdn.dribbble.com/users/4950/screenshots/622472/media/abca6e74221aec40458db1e95c1ac422.png?compress=1&resize=400x300")
        self.submitButton=Button(self,image=self.submitButtonImage,command=self.checkOTP,border=0)
        self.submitButton.place(x=208,y=240)

        self.resendOTPImage=PhotoImage(file="https://leaptodigital.com/wp-content/uploads/2019/06/button_resend.png")
        self.resendOTP=Button(self,image=self.resendOTPImage,command=self.resendOTP,border=0)
        self.resendOTP.place(x=200,y=400)


    def checkOTP(self):
        try:
            self.userInput=int(self.user_Name.get(1.0,"end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo","Login Success")
                self.n="Done"

            elif self.n=="Done":
                messagebox.showinfo("showinfo","already Entered the OTP")

            else:
                messagebox.showinfo("showinfo","Wrong OTP")

        except:
            messagebox.showinfo("showinfo","Invalid OTP")


    def resenOTP(self):
        self.n=random.randint(1000,9999)
        self.client=Client("","")
        self.client.messages.create(to=[""],from_="",body=self.n)


if __name__=="__main__":
    window=otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()
