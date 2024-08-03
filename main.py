from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(bg="light gray")
window.config(pady=20)
window.minsize(width=250, height=250)

#Properties
your_situation = "0"
situation_label = Label()

#Kg label
kg_label = Label(text="Enter your weight(kg)")
kg_label.config(bg="light gray",fg="black")
kg_label.config(pady=10)
kg_label.pack()

#Kg Entry
kg_entry = Entry(width=20,bg="white",fg="black")
kg_entry.focus()
kg_entry.pack()

#Cm label
cm_label = Label(text="Enter your weight(m)")
cm_label.config(bg="light gray",fg="black")
cm_label.config(pady=10)
cm_label.pack()

#Cm Entry
cm_entry = Entry(width=20,bg="white",fg="black")
cm_entry.pack()


#Calculate Button
def calculate_button_clicked():

    global your_situation
    global situation_label

    try:
        user_kg = float(kg_entry.get())
        user_cm = float(cm_entry.get())
        if user_kg and user_cm > 0:
            square_user_cm = user_cm * user_cm
            bmi_score = user_kg / square_user_cm
            if bmi_score >= 40:
                your_situation = "You Are Obese"
            elif 40 > bmi_score >= 25:
                your_situation = "You Are Overwieght"
            elif 25 > bmi_score >= 18.5:
                your_situation = "You Are normal"
            elif 18.5 > bmi_score > 0:
                your_situation = "You Are Underweight"
        else:
            your_situation = "Please enter a pozitive number"
    except ValueError:
        your_situation = "Please enter a number"


    situation_label.destroy()
    change_situation()

calculate_button = Button(text="Calculate",command=calculate_button_clicked)
calculate_button.place(x=85,y=155)

#situation label
def change_situation():
    global situation_label
    situation_label = Label(text=your_situation,font=('Arial', 13),bg="light gray",fg="black")
    situation_label.pack(side="bottom")


mainloop()
