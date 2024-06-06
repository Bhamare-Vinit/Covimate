import tkinter as tk
from tkinter import messagebox

class HealthDiagnosisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Health Diagnosis App")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(master)
        self.frame = tk.Frame(self.canvas)
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure(canvas))

        self.questions = {
            "Fever": {"High": 5, "Low": 2},
            "Cough": {"Dry": 3, "Wet": 4, "None": 0},
            "Headache": {"Mild": 1, "Moderate": 3, "Severe": 5},
            "Fatigue": {"Mild": 2, "Moderate": 4, "Severe": 6},
            "Sore throat": {"Yes": 3, "No": 0},
            "Body aches": {"Yes": 4, "No": 0},
            "Shortness of breath": {"Yes": 5, "No": 0},
            "Chills": {"Yes": 4, "No": 0},
            "Loss of taste or smell": {"Yes": 5, "No": 0},
            "Nausea or vomiting": {"Yes": 3, "No": 0}
        }

        self.selected_answers = {}

        self.create_checkboxes()
        self.create_submit_button()

    def create_checkboxes(self):
        row = 0
        for question, options in self.questions.items():
            tk.Label(self.frame, text=question).grid(row=row, column=0, sticky="w")
            row += 1
            self.selected_answers[question] = {}
            for option, points in options.items():
                var = tk.IntVar()
                checkbox = tk.Checkbutton(self.frame, text=option, variable=var)
                checkbox.var = var
                checkbox.grid(row=row, column=0, sticky="w")
                self.selected_answers[question][option] = checkbox
                row += 1

        # Creating a placeholder label for spacing
        tk.Label(self.frame, text="").grid(row=row, column=0)

    def create_submit_button(self):
        submit_button = tk.Button(self.master, text="Submit", command=self.submit)
        submit_button.pack(side="bottom", pady=10)

    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def submit(self):
        total_points = sum(value.var.get() * self.questions[key][option] for key, options in self.selected_answers.items() for option, value in options.items())
        if total_points >= 25:
            messagebox.showinfo("Diagnosis Result", "You are not okay! 😷")
        else:
            messagebox.showinfo("Diagnosis Result", "You are okay! 😀")

def main():
    root = tk.Tk()
    app = HealthDiagnosisApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

