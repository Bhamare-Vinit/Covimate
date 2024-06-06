from tkinter import *
from tkinter import ttk, Scrollbar
import requests
from tkinter import messagebox
from win10toast import ToastNotifier
import customtkinter
from main import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

BLACK = "#303030"
# DIFF_BLACK = "#1F1F1F"
DIFF_BLACK = "#1B1C1E"
FONT = ("Helvetica", 26, "bold")


root = customtkinter.CTk()
root.title("Covid-19")
root.config(padx=30, pady=30)
root.config(bg=BLACK)
# root.eval('tk::PlaceWindow . center')
root.resizable(False, False)
root.iconbitmap('icon.ico')


l = ('World', 'USA', 'Brazil', 'India', 'Russia', 'Peru', 'Chile', 'Mexico', 'South Africa', 'Spain', 'UK', 'Iran', 'Pakistan', 'Italy', 'Saudi Arabia', 'Turkey', 'Germany', 'Bangladesh', 'France', 'Colombia', 'Argentina', 'Canada', 'Qatar', 'Iraq', 'Egypt', 'Indonesia', 'Sweden', 'Ecuador', 'Belarus', 'Kazakhstan', 'Belgium', 'Oman', 'Philippines', 'Kuwait', 'Ukraine', 'UAE', 'Bolivia', 'Netherlands', 'Panama', 'Portugal', 'Dominican Republic', 'Singapore', 'Israel', 'Poland', 'Afghanistan', 'Romania', 'Bahrain', 'Nigeria', 'Armenia', 'Switzerland', 'Guatemala', 'Honduras', 'Azerbaijan', 'Ireland', 'Ghana', 'Japan', 'Algeria', 'Moldova', 'Serbia', 'Austria', 'Nepal', 'Morocco', 'Cameroon', 'Uzbekistan', 'S. Korea', 'Czechia', 'Ivory Coast', 'Denmark', 'Kyrgyzstan', 'Kenya', 'El Salvador', 'Australia', 'Sudan', 'Venezuela',
     'Norway', 'Costa Rica', 'Malaysia', 'North Macedonia', 'Senegal', 'DRC', 'Ethiopia', 'Bulgaria', 'Bosnia and Herzegovina', 'Palestine', 'Finland', 'Haiti', 'Tajikistan', 'French Guiana', 'Guinea', 'Gabon', 'Madagascar', 'Mauritania', 'Luxembourg', 'Djibouti', 'CAR', 'Hungary', 'Croatia', 'Greece', 'Albania', 'Thailand', 'Paraguay', 'Nicaragua', 'Somalia', 'Equatorial Guinea', 'Maldives', 'Mayotte', 'Sri Lanka', 'Malawi', 'Lebanon', 'Cuba', 'Mali', 'Congo', 'South Sudan', 'Estonia', 'Slovakia', 'Iceland', 'Lithuania', 'Guinea-Bissau', 'Slovenia', 'Zambia', 'Cabo Verde', 'Sierra Leone', 'Hong Kong', 'Libya', 'New Zealand', 'Yemen', 'Eswatini', 'Rwanda', 'Mozambique', 'Benin', 'Tunisia', 'Montenegro', 'Jordan', 'Latvia', 'Niger', 'Zimbabwe', 'Liberia', 'Uganda', 'Burkina Faso', 'Namibia', 'Cyprus', 'Uruguay', 'Georgia', 'Chad', 'Andorra', 'Suriname', 'Jamaica', 'Togo', 'Sao Tome and Principe', 'Diamond Princess', 'San Marino', 'Malta', 'Réunion', 'Channel Islands', 'Angola', 'Tanzania', 'Syria', 'Taiwan', 'Botswana', 'Vietnam', 'Mauritius', 'Myanmar', 'Isle of Man', 'Comoros', 'Guyana', 'Burundi', 'Mongolia', 'Lesotho', 'Martinique', 'Eritrea', 'Cayman Islands', 'Guadeloupe', 'Faeroe Islands', 'Gibraltar', 'Cambodia', 'Bermuda', 'Brunei', 'Trinidad and Tobago', 'Bahamas', 'Monaco', 'Aruba', 'Barbados', 'Seychelles', 'Liechtenstein', 'Bhutan', 'Sint Maarten', 'Antigua and Barbuda', 'Turks and Caicos', 'Gambia', 'French Polynesia', 'Macao', 'Saint Martin', 'Belize', 'St. Vincent Grenadines', 'Curaçao', 'Fiji', 'Timor-Leste', 'Grenada', 'New Caledonia', 'Saint Lucia', 'Laos', 'Dominica', 'Saint Kitts and Nevis', 'Falkland Islands', 'Greenland', 'Montserrat', 'Vatican City', 'Papua New Guinea', 'Western Sahara', 'MS Zaandam', 'Caribbean Netherlands', 'British Virgin Islands', 'St. Barth', 'Anguilla', 'Saint Pierre Miquelon', 'China')




def checkkey(event):
    value = event.widget.get()
    if value == '':
        data = l
    else:
        data = []
        for item in l:
            if value.lower() in item.lower():
                data.append(item)
    update(data)


def update(data):
    lb.delete(0, 'end')
    for item in data:
        lb.insert('end', item)


frame = customtkinter.CTkFrame(
    root, padx=10, pady=10, corner_radius=5, fg_color=BLACK)
frame.config(bg=BLACK)
frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
entry = customtkinter.CTkEntry(
    frame,border_color="green", borderwidth=2, width=200, corner_radius=10)
entry.configure(bd=0)
entry.grid(row=0, column=0, columnspan=2)
entry.bind('<KeyRelease>', checkkey)


lb = Listbox(frame, font=("Calibri", 12), bd=0, background="gray20", highlightthickness=0,
             borderwidth=0, height=25, width=30)
lb.grid(row=1, column=0, columnspan=2, pady=8)
update(l)
lb.config(foreground="white")

sframe = customtkinter.CTkFrame(
    root, padx=10, pady=10, fg_color=BLACK, corner_radius=5)
sframe.config(bg=BLACK)
sframe.grid(row=0, column=1, padx=5, pady=5)


def routing_homepage():
    root.destroy()
    import main
    main.homepage()
    

HomepageButton = customtkinter.CTkButton(sframe, text="Homepage", text_font=FONT, width=250,
                                         height=25, hover_color="#238636", fg_color=DIFF_BLACK, border_width=2, border_color="green",command = routing_homepage)
HomepageButton.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

customtkinter.CTkButton(sframe, text="Cases", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=0, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="TodayCases", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=1, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="Deaths", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=2, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="TodayDeaths", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=3, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="Recovered", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=4, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="Active", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=5, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="Critical", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=6, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="CasesPerOneMillion", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=7, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="DeathsPerOneMillion", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=8, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="TotalTests", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=9, column=0, padx=10, pady=10, sticky=W)
customtkinter.CTkButton(sframe, text="TestsPerOneMillion", fg_color=DIFF_BLACK, border_width=2, border_color="green").grid(
    row=10, column=0, padx=10, pady=10, sticky=W)


Cases = Text(sframe, height=1, width=20, borderwidth=0, font=("Calibri", 12))
Cases.grid(row=0, column=1)
Cases.config(bg=DIFF_BLACK, fg="white")
TodayCases = Text(sframe, height=1, width=20,
                  borderwidth=0, font=("Calibri", 12))
TodayCases.grid(row=1, column=1)
TodayCases.config(bg=DIFF_BLACK, fg="white")
Deaths = Text(sframe, height=1, width=20, borderwidth=0, font=("Calibri", 12))
Deaths.grid(row=2, column=1)
Deaths.config(bg=DIFF_BLACK, fg="white")
TodayDeaths = Text(sframe, height=1, width=20,
                   borderwidth=0, font=("Calibri", 12))
TodayDeaths.grid(row=3, column=1)
TodayDeaths.config(bg=DIFF_BLACK, fg="white")
Recovered = Text(sframe, height=1, width=20,
                 borderwidth=0, font=("Calibri", 12))
Recovered.grid(row=4, column=1)
Recovered.config(bg=DIFF_BLACK, fg="white")
Active = Text(sframe, height=1, width=20, borderwidth=0, font=("Calibri", 12))
Active.grid(row=5, column=1)
Active.config(bg=DIFF_BLACK, fg="white")
Critical = Text(sframe, height=1, width=20,
                borderwidth=0, font=("Calibri", 12))
Critical.grid(row=6, column=1)
Critical.config(bg=DIFF_BLACK, fg="white")
CasesPerOneMillion = Text(sframe, height=1, width=20,
                          borderwidth=0, font=("Calibri", 12))
CasesPerOneMillion.grid(row=7, column=1)
CasesPerOneMillion.config(bg=DIFF_BLACK, fg="white")
DeathsPerOneMillion = Text(sframe, height=1, width=20,
                           borderwidth=0, font=("Calibri", 12))
DeathsPerOneMillion.grid(row=8, column=1)
DeathsPerOneMillion.config(bg=DIFF_BLACK, fg="white")
TotalTests = Text(sframe, height=1, width=20,
                  borderwidth=0, font=("Calibri", 12))
TotalTests.grid(row=9, column=1)
TotalTests.config(bg=DIFF_BLACK, fg="white")
TestsPerOneMillion = Text(sframe, height=1, width=20,
                          borderwidth=0, font=("Calibri", 12))
TestsPerOneMillion.grid(row=10, column=1)
TestsPerOneMillion.config(bg=DIFF_BLACK, fg="white")


def select():

    global entry
    global Cases
    global TodayCases
    global Deaths
    global TodayDeaths
    global Recovered
    global Active
    global Critical
    global CasesPerOneMillion
    global DeathsPerOneMillion
    global TotalTests
    global TestsPerOneMillion

    entry.delete(0, END)
    entry.insert(0, lb.get(ANCHOR))

    cname = str(lb.get(ANCHOR))

    url = f'https://coronavirus-19-api.herokuapp.com/countries/{cname}'
    r = requests.get(url)
    data = r.json()

    Cases.configure(state='normal')
    TodayCases.configure(state='normal')
    Deaths.configure(state='normal')
    TodayDeaths.configure(state='normal')
    Recovered.configure(state='normal')
    Active.configure(state='normal')
    Critical.configure(state='normal')
    CasesPerOneMillion.configure(state='normal')
    DeathsPerOneMillion.configure(state='normal')
    TotalTests.configure(state='normal')
    TestsPerOneMillion.configure(state='normal')

    Cases.delete(1.0, END)
    TodayCases.delete(1.0, END)
    Deaths.delete(1.0, END)
    TodayDeaths.delete(1.0, END)
    Recovered.delete(1.0, END)
    Active.delete(1.0, END)
    Critical.delete(1.0, END)
    CasesPerOneMillion.delete(1.0, END)
    DeathsPerOneMillion.delete(1.0, END)
    TotalTests.delete(1.0, END)
    TestsPerOneMillion.delete(1.0, END)

    Cases.insert(END, str(data["cases"]))
    TodayCases.insert(END, str(data["todayCases"]))
    Deaths.insert(END, str(data["deaths"]))
    TodayDeaths.insert(END, str(data["todayDeaths"]))
    Recovered.insert(END, str(data["recovered"]))
    Active.insert(END, str(data["active"]))
    Critical.insert(END, str(data["critical"]))
    CasesPerOneMillion.insert(END, str(data["casesPerOneMillion"]))
    DeathsPerOneMillion.insert(END, str(data["deathsPerOneMillion"]))
    TotalTests.insert(END, str(data["totalTests"]))
    TestsPerOneMillion.insert(END, str(data["testsPerOneMillion"]))

    Cases.configure(state='disabled')
    TodayCases.configure(state='disabled')
    Deaths.configure(state='disabled')
    TodayDeaths.configure(state='disabled')
    Recovered.configure(state='disabled')
    Active.configure(state='disabled')
    Critical.configure(state='disabled')
    CasesPerOneMillion.configure(state='disabled')
    DeathsPerOneMillion.configure(state='disabled')
    TotalTests.configure(state='disabled')
    TestsPerOneMillion.configure(state='disabled')

# def notify():
#     global notify
#     ncname = str(lb.get(ANCHOR))
#     if len(ncname) == 0:
#         messagebox.showerror('Country', 'Select your Country')
#     else:
#         nurl = f'https://coronavirus-19-api.herokuapp.com/countries/{ncname}'
#         nr = requests.get(nurl)
#         ndata = nr.json()
#         ntext = f"Confirmed Cases : {ndata['cases']} \nDeaths : {ndata['deaths']} \nRecovered : {ndata['recovered']}"
#         toast = ToastNotifier()
#         toast.show_toast(f'{ncname} Covid-19 Updates',
#                             ntext, duration=10, icon_path="icon.ico")
               

search = customtkinter.CTkButton(frame, text="Show", width=150,height=35, corner_radius=15, fg_color="#238636",
                                 border_width=3, border_color="green",text_font=("Helvetica", 22, "bold"), text_color="white", command=select)
search.grid(row=3, column=0, pady=15, columnspan=1)

# notify = customtkinter.CTkButton(frame, text="Notify", width=45, corner_radius=15, border_width=3, border_color="#238636",
#                                  command=notify)
# notify.grid(row=3, column=1, pady=10, columnspan=1)

root.mainloop()
