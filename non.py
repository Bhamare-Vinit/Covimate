import tkinter as tk

# Disclaimer and safety message
DISCLAIMER = "This app is for informational purposes only and should not be used for self-diagnosis or treatment. Always consult a qualified healthcare professional for any health concerns."

def health_check():
    """Calculates health score based on user input and displays a result message."""

    score = 0
    symptom_list = []

    # Get selected symptoms and their points
    for symptom, points in symptoms.items():
        if checkboxes[symptom].get():
            score += points
            symptom_list.append(symptom)

    # Display results based on score
    result_text.set("")  # Clear previous result

    if score >= high_threshold:
        result_text.set(f" You might not be feeling well. {DISCLAIMER}")
        result_emoji.set("")
        for symptom in symptom_list:
            result_text.set(result_text.get() + f"\n- {symptom}")
    else:
        result_text.set(f" You seem to be doing well! {DISCLAIMER}")
        result_emoji.set("")

# Sample symptoms and points (customize based on your needs)
symptoms = {
    "Fever (above 100.4°F)": 3,
    "Headache": 2,
    "Cough": 1,
    "Sore throat": 1,
    "Body aches": 2,
    "Fatigue": 1,
    "Loss of taste or smell": 2,
    "Shortness of breath": 5,
    "Chest pain": 5
}

# High score threshold (adjust as needed)
high_threshold = 8

# Initialize Tkinter window
window = tk.Tk()
window.title("Health Check")

# Disclaimer label
disclaimer_label = tk.Label(window, text=DISCLAIMER, wraplength=300)
disclaimer_label.pack(pady=10)

# Checkboxes for symptoms
checkboxes = {}
for symptom, points in symptoms.items():
    checkbox_var = tk.IntVar(value=0)  # Default unchecked
    checkbox = tk.Checkbutton(window, text=symptom, variable=checkbox_var)
    checkbox.pack(anchor=tk.W)  # Align checkboxes to the left
    checkboxes[symptom] = checkbox_var

# Submit button
submit_button = tk.Button(window, text="Check Your Health", command=health_check)
submit_button.pack(pady=10)

# Result text variable
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 16))
result_label.pack()

# Result emoji variable
result_emoji = tk.StringVar()
result_emoji_label = tk.Label(window, textvariable=result_emoji, font=("Arial", 24))
result_emoji_label.pack()

window.mainloop()