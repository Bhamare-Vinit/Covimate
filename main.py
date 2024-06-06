from tkinter import *
from main import *
import  customtkinter as ct
BLACK = "#303030"
FONT = ("Helvetica", 16,"bold")

def homepage():
    homepage=Tk()
    homepage.title("HomePage")
    homepage.geometry("920x600")
    homepage.configure(background=BLACK)
    homepage.resizable(False,False)

    def routing_covid_tracker():
        homepage.destroy()
        import main1
        
    def routing_self_diagnose():
        homepage.destroy()
        import self


    Label1= ct.CTkLabel(homepage, text = "HOMEPAGE",fg_color = "#303030",text_font =FONT ,width=500,height=100,bg = "white")
    Label1.pack(padx=10 , pady=10)
    # Label1.configure(background="lightsteelblue")

    sideImage = PhotoImage(file="images/covid.png")     
    sideImageLabel = Label(image=sideImage)
    sideImageLabel.place(x=470,y=95)

    SelfDiagnose=PhotoImage(file="images/self.png")
    SelfDiagnose_Button=ct.CTkButton(homepage,text = "SELF DIAGNOSIS",corner_radius =12,  image=SelfDiagnose,command = routing_self_diagnose)
    SelfDiagnose_Button.place(x=20,y=155)

    Covid_Tracker=PhotoImage(file="images/covid_tracker.png")
    Covid_TrackerButton=ct.CTkButton(homepage,text = "COVID ANALYSER",corner_radius =12,image=Covid_Tracker,command= routing_covid_tracker)
    Covid_TrackerButton.place(x=20,y=355)

    # Vaccine=PhotoImage(file="images/vaccine1.png")
    # VaccineButton=ct.CTkButton(homepage,text = "VACCINE NOTIFIER",corner_radius =12,image=Vaccine,border=0)
    # VaccineButton.place(x=20,y=420)

    Exit=ct.CTkButton(homepage,text="EXIT",hover_color="lightblue" , width = 100,height=45,corner_radius=15)

    Exit.place(x=760, y=550)

    homepage.mainloop()

homepage()