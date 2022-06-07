from tkinter import*
from random import choice
win1 = Tk()
win1.geometry("650x430")
win1.title("Year 10 Maths Quiz.")
win1.configure()
state1 = NORMAL
count = 0
var1 = IntVar()

# Questions, Answer in the radiobuttons and the answer key in the correct 
question = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
radiobutton1 = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
radiobutton2 = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
radiobutton3 = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
correct = [1,2,3,1,2,3,1,2,3,1,2,3,1,2]

# Randomizer for the questions, creates a list called questions_for_display which is then used in the counter variable to print a certain question
global questions_for_display
questions_for_display = []
for loop in range (10):
    my_random_int = choice(list(set(range(0, 13)) - set(questions_for_display)))
    questions_for_display.append(my_random_int)

# Main question screen 
def startquiz():
    global win2
    global count
    
    win2 = Toplevel(win1)
    win2.geometry("650x430")
    win2.title("Year 10 Maths Quiz.")
    win2.configure()
    for widgets in win2.winfo_children():   
        widgets.destroy()

    counter = (questions_for_display[count] - 1)
    count = count + 1
    correct  = (questions_for_display[count] - 1)
    r1 = Radiobutton(win2, text = radiobutton1[counter]).place(x = 190, y = 200) 
    r2 = Radiobutton(win2, text=  radiobutton2[counter]).place(x = 300, y= 200)
    r3 = Radiobutton(win2, text = radiobutton3[counter]).place(x = 410, y = 200)
    label7 = Label(win2, text = correct[counter]).place(x = 0,y = 0)
    label4 = Button(win2, text = "Question 1",font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
    label5 = Label(win2, text = "PLACEHOLDER",font = "Corbel_Light",fg = "black", bg = "#ffffff",).place(x = 280, y= 120)
    label6 = Button(win2, text = "Next question" ,command=startquiz,state = state1,font = "Corbel_Light", fg = "black",bg = "#ffffff",padx = 30, pady = 3).place(x =90, y =310 )
    
def check_ans():
    print("hello")

# Ends the entire program. 
def endquiz():
    win1.destroy()

# 
label1 = Button(win1, text = "Quiz game" ,font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
lable2 = Button(win1, text = "Start quiz",command = startquiz, font ="Corbel_Light", fg= "black", bg = "#ffffff", padx = 30, pady = 3).place(x = 90, y= 310)
label3 = Button(win1, text = "End quiz", command = endquiz,font = "Corbel_Light", fg = "black", bg = "#ffffff", padx = 30, pady = 3).place(x = 400, y = 310)


win1.mainloop()
