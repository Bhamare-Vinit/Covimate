from tkinter import *
import customtkinter as ct
FONT = ("Helvetica", 26, "bold")

self = ct.CTk()
self.title("Self Diagnosis")
self.geometry("920x600")

self.resizable(False, False)

global count
count = 0
Label1 = ct.CTkLabel(self, text="SELF DIAGNOSIS", width=200,
                     height=40, fg_color="green", text_font=FONT, corner_radius=15)
Label1.place(x=100, y=10)


qn1 = ct.CTkLabel(self, text="Select the symptons that you are facing",
                  width=60, height=10, fg_color="green", text_font=FONT, corner_radius=15)
qn1.place(x=20, y=80)

var_c1 = IntVar()
var_c2 = IntVar()
var_c3 = IntVar()
var_c4 = IntVar()
var_c4 = IntVar()
var_c5 = IntVar()
var_c6 = IntVar()
var_c7 = IntVar()
var_c8 = IntVar()
var_c9 = IntVar()
var_c10 = IntVar()
var_c11 = IntVar()
var_c12 = IntVar()
var_c13 = IntVar()
var_c14 = IntVar()
var_c15 = IntVar()
var_c16 = IntVar()



def diagnose():
    global count 
    if var_c1.get() == 1:
        count += 1
    if var_c2.get() == 1:
        count += 1
    if var_c3.get() == 1:
        count += 1
    if var_c4.get() == 1:
        count += 1
    if var_c5.get() == 1:
        count += 1
    if var_c6.get() == 1:
        count += 1
    if var_c7.get() == 1:
        count += 1
    if var_c8.get() == 1:
        count += 1
    if var_c9.get() == 1:
        count += 1
    if var_c10.get() == 1:
        count += 1
    if var_c11.get() == 1:
        count += 1
    if var_c12.get() == 1:
        count += 1
    if var_c13.get() == 1:
        count += 1
    if var_c14.get() == 1:
        count += 1
    if var_c15.get() == 1:
        count += 1
    if var_c16.get() == 1:
        count += 1

    # print(count)
    if count >= 14:
        result_label.configure(text="Covid RIsk is very high")
    elif 10 <= count < 14:
        result_label.configure(text="Covid Risk Level is Medium")
    elif 8 <= count < 10:
        result_label.configure(text="Covid Risk Level is Low")
    elif 0 <= count < 8:
        result_label.configure(text="Covid Risk Level is Very Low")



c1 = ct.CTkCheckBox(self, text="Runny Nose", variable=var_c1,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c1.place(x=20, y=130)

c2 = ct.CTkCheckBox(self, text="High Fever", variable=var_c2,border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c2.place(x=20, y=170)

c3 = ct.CTkCheckBox(self, text="Cough", variable=var_c3,border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c3.place(x=20, y=210)

c4 = ct.CTkCheckBox(self, text="Loss of Taste and Smell", variable=var_c4,border_color="green", border_width=2,fg_color="green",checkmark_color="black")
c4.place(x=20, y=250)

c5 = ct.CTkCheckBox(self, text="Fatigue", variable=var_c5,border_color="green", border_width=2,fg_color="green",checkmark_color="black")
c5.place(x=20, y=290)

c6 = ct.CTkCheckBox(self, text="Sneezing", variable=var_c6,border_color="green", border_width=2,fg_color="green",checkmark_color="black")
c6.place(x=20, y=330)

c7 = ct.CTkCheckBox(self, text="Shortness of Breath", variable=var_c7,border_color="green", border_width=2,fg_color="green",checkmark_color="black")
c7.place(x=20, y=370)

c8 = ct.CTkCheckBox(self, text="Sore Throat", variable=var_c8,border_color="green", border_width=2,fg_color="green",checkmark_color="black")
c8.place(x=20, y=410)

c9 = ct.CTkCheckBox(self, text="High temperature", variable=var_c9,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c9.place(x=200, y=130)

c10 = ct.CTkCheckBox(self, text="Chills and shivers", variable=var_c10,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c10.place(x=200, y=170)

c11 = ct.CTkCheckBox(self, text="Sudden Confusion", variable=var_c11,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c11.place(x=200, y=210)

c12 = ct.CTkCheckBox(self, text="Skin rash", variable=var_c12,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c12.place(x=200, y=250)

c13 = ct.CTkCheckBox(self, text="Red and sore fingers/toes", variable=var_c13,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c13.place(x=200, y=130)

c14 = ct.CTkCheckBox(self, text="Chest pain", variable=var_c14,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c14.place(x=200, y=290)

c15 = ct.CTkCheckBox(self, text="Hoarse voice", variable=var_c15,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c15.place(x=200, y=330)

c16 = ct.CTkCheckBox(self, text="Symptoms persisting more than 1 week", variable=var_c16,
                    border_color="green", border_width=2,fg_color="green",checkmark_color="black")

c16.place(x=200, y=370)


Diag = ct.CTkButton(self, text="Diagnose",fg_color="green",hover_color= "darkgreen",command=diagnose)
Diag.place(x=20, y=450)

def route_home():
    self.destroy()
    import main

homepage_button = ct.CTkButton(self, text="Homepage",fg_color="green",hover_color= "darkgreen",command = route_home)
homepage_button.place(x= 200,y= 450)

result_label = ct.CTkLabel(self, text="",
                           width=700, height=40, corner_radius=12, fg_color="#303030")
result_label.place(x=20, y=510)
self.mainloop()
