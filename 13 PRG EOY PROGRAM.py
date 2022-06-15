# Variables which must be initialised at thje start of the program.
from tkinter import*
from random import choice
from PIL import ImageTk, Image  

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
userans = []

# Randomizer for the questions, creates a list called questions_for_display which is then used in the counter variable to print a certain question
questions_for_display = []
for loop in range (11):
    my_random_int = choice(list(set(range(0, 13)) - set(questions_for_display)))
    questions_for_display.append(my_random_int)

answerkey = []





# Main question screen 
def startquiz():

    win2 = Toplevel(win1)
    win2.geometry("650x430")
    win2.title("Year 10 Maths Quiz.")
    win2.configure()
    img1 = PhotoImage(file = "Background_2.png")
    label13 = Label(win2, image = img1 , width = 629, height = 429)
    label13.place(x = 0, y =0)
    
    #Logo.place(x = 0, y = 0)
    global count

    #Next question Function
    def check_ans():
        
        #Needs to be done
        for widgets in win2.winfo_children():   
                widgets.destroy()
        

        global count
        global state1

        counter = (questions_for_display[count] -1)
        count = count + 1
        answerkey.append(correct[counter])
        userans.append(var1.get())

        #Question Buttons
        r1 = Radiobutton(win2, text = radiobutton1[counter], variable= var1, value = 1).place(x = 190, y = 200) 
        r2 = Radiobutton(win2, text=  radiobutton2[counter], variable= var1, value = 2).place(x = 300, y= 200)
        r3 = Radiobutton(win2, text = radiobutton3[counter], variable= var1, value = 3).place(x = 410, y = 200)
        label7 = Label(win2, text = correct[counter]).place(x = 0,y = 0)
        label4 = Button(win2, text = ("Question ",count),font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
        label5 = Label(win2, text = question[counter],font = "Corbel_Light",fg = "black", bg = "#ffffff",).place(x = 280, y= 120)
        label6 = Button(win2, text = "Next question" ,command=check_ans,state = state1,font = "Corbel_Light", fg = "black",bg = "#ffffff",padx = 30, pady = 3).place(x =90, y =310 )
        label10 = Label(win2, text = userans).place(x = 0, y = 60)
        label11 = Label(win2, text = answerkey).place(x = 0, y =30)
        label12 = Button(win2, text = "Skip", command=skips, font = "Corbel_Light").place(x = 0, y = 0)
        
        #Stops the program after 10 questions have been answered
        if count == 11:
            state1 = DISABLED
            for label6 in win2.winfo_children():
                label6.destroy()
            answerkey.pop(10)

            label8 = Label(win2, text= "Press button to view score").place(x= 260, y= 20)
            label9 = Button(win2, text= "Check Score", command = calc_score).place(x= 90, y= 310)
            label10 = Label(win2, text = userans).place(x = 0, y = 0)
            label11 = Label(win2, text = answerkey).place(x = 0, y =30)
            
    # Calculates the score and displays it on the 1st screen
    def calc_score():
        for widgets in win1.winfo_children():   
                widgets.destroy()
    
        win2.destroy()
        counter1 = 0
        score = 0
        for loop in range(10):
            if answerkey[counter1] == userans[counter1]:
                score = score +1
            else:
                score = score
            counter1 = counter1 + 1
        
        if score < 4:
            label12 = Label(win1, text = "Not achieved").place(x = 0, y = 0)
        elif score <6:
            label12 = Label(win1, text = "Achieved").place(x = 0, y = 0)        
        elif score <8:
            label12 = Label(win1, text = "Merit").place(x = 0, y = 0)
        elif score <10:
            label12 = Label(win1, text = "Excellence").place(x = 0, y = 0)
        label3 = Button(win1, text = "End quiz", command = endquiz,font = "Corbel_Light", fg = "black", bg = "#ffffff", padx = 30, pady = 3).place(x = 400, y = 310)
    
    # Skip function
    def skips():
        for widgets in win2.winfo_children():   
                widgets.destroy()
        count = count-1
        check_ans()
        answerkey.pop(correct[counter])
        userans.pop(counter)

    # First question code must be kept seperate 
    counter = (questions_for_display[count]-1)    
    answerkey.append(correct[counter])
    
    count = count+1
    
    r1 = Radiobutton(win2, text = radiobutton1[counter], variable= var1, value = 1).place(x = 190, y = 200) 
    r2 = Radiobutton(win2, text=  radiobutton2[counter], variable= var1, value = 2).place(x = 300, y= 200)
    r3 = Radiobutton(win2, text = radiobutton3[counter], variable= var1, value = 3).place(x = 410, y = 200)
    label7 = Label(win2, text = correct[counter]).place(x = 0,y = 0)
    label4 = Button(win2, text = ("Question ",count),font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
    label5 = Label(win2, text = question[counter],font = "Corbel_Light",fg = "black", bg = "#ffffff",).place(x = 280, y= 120)
    label6 = Button(win2, text = "Next question" ,command=check_ans,state = state1,font = "Corbel_Light", fg = "black",bg = "#ffffff",padx = 30, pady = 3).place(x=90,y=310)
    #label12 = Button(win2, text = "Skip", command=skips, font = "Corbel_Light").place(x = 0, y = 0)


# Ends the entire program. 
def endquiz():

    win1.destroy()

# 1st screen labels
label1 = Button(win1, text = "Quiz game" ,font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
lable2 = Button(win1, text = "Start quiz",command = startquiz, state = state1, font ="Corbel_Light", fg= "black", bg = "#ffffff", padx = 30, pady = 3).place(x = 90, y= 310)
label3 = Button(win1, text = "End quiz", command = endquiz,font = "Corbel_Light", fg = "black", bg = "#ffffff", padx = 30, pady = 3).place(x = 400, y = 310)



# Does tkinter
win1.mainloop()