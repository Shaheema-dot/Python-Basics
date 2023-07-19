import tkinter as tk
from tkinter import StringVar

window= tk.Tk()
window.geometry("850x600")
window.title("BMI Calculator")
window.columnconfigure([0,1,2], weight=1, minsize=55)
window.rowconfigure([0,1,2], weight=1, minsize=20)
weight = StringVar()
height = StringVar()
weight.set(0)

lbl = tk.Label(window, fg="dark blue",text="BMI Calculator", font=("Helvetica", 26, "bold"))
lbl.grid(row=0, column=0, columnspan=3)

input_frame = tk.Frame(window, relief=tk.RAISED)
input_frame.grid(row=1, column=0 ,padx=5, pady=5)

output_frame = tk.Frame(window, relief=tk.RAISED)
output_frame.grid(row=1, column=1, padx=5, pady=5)


lbl_height = tk.Label(input_frame, text="Height (in cm):",fg='green',font=("Tmes", 20),pady=50)
lbl_height.grid(row=1, column=0, sticky='e', padx=20)
enter_height = tk.Spinbox(input_frame, font=("Times", 20), from_=100.0, to=250.0, textvariable=height)
enter_height.grid(row=1, column=1, sticky='w')

lbl_weight = tk.Label(input_frame, text="Weight (in kg):",fg='green',font=("Tmes", 20))
lbl_weight.grid(row=2, column=0, sticky='e', padx=20,pady=30)
enter_weight = tk.Entry(input_frame, font=("Times", 20),textvariable=weight)
enter_weight.grid(row=2, column=1, sticky='w')

def calculate_bmi():
    global height, weight 
    height = float(height.get())/100
    weight = float(weight.get())
    bmi = weight / (height ** 2)
    lbl_bmi_txt = tk.Label(output_frame, text="BMI", fg="green",font=("Times", 25)).grid(row=1, column=2)
    lbl_bmi_val = tk.Label(output_frame, text="45.56", bg="dark blue",fg="white", font=("Times", 30, "bold"), padx=50, pady=20)
    lbl_bmi_val.grid(row=2, column=2,pady=20)
    lbl_bmi_val['text'] = round(bmi,2)
    bmi_status = tk.Label(output_frame, text=get_bmi_status(bmi), bg="green", fg="white", font=("Arial", 15),padx=40,pady=20)
    bmi_status.grid(row=3, column=2,stick='w',pady=50)
    
def get_bmi_status(bmi):
    if bmi <= 15:
        return "Severe Thinness"
    elif 15 < bmi <= 16:
        return "Moderate Thinness"
    elif 16 < bmi < 18.5:
        return "Mild Thinness"
    elif 18.5 <= bmi <= 25:
        return "Normal"
    elif 25 < bmi <= 30:
        return "Overweight"
    elif 30 < bmi <= 35:
        return "Obese Class I"
    elif 35 < bmi <= 40:
        return "Obese Class II"
    else:
        return "Obese Class III"

button_calculate = tk.Button(input_frame,bg="dark blue", fg='white', bd=12, text="Calculate BMI", font=("Helvetica", 20),command=calculate_bmi)
button_calculate.grid(row=4, column=1, sticky='w', pady=50,padx=10)
window.mainloop()

