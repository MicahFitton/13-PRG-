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
question = ["The diameter of a wheel of a rickshaw is 82.6cm. If the wheel makes 130 rotation in one minute, how long will it take for the rickshaw to cover a distance of 30373.2metres? (assume π=22/7)",
            "What is the sum of all natural numbers between 110 and 260 which are divisible by 9?",
            "Matthew throws a dice. What is the probability that he will roll a number more than 2?",
            "In a triangle, ABC, P, Q and R are the midpoints of sides BC, CA, and AB respectively. If AC = 19cm, BC = 24cm and AB = 21cm, find the perimeter of the quadrilateral ARPQ.",
            "A square and an equilateral triangle have the same perimeter. The diagonal of the square is 15cm. Find the area of the triangle."
            "There are 90 numbers. Each number is subtracted from 91 and the mean of the numbers so obtained is found to be -8.8. Find the mean of the given numbers.",
            "A natural number, when increased by 2, equals 195 times its reciprocal. Find the number.",
            "If sinθ + 2cosθ = 1, find the value of 2sinθ - cosθ.",
            "Find the area of the rhombus in which each side is 25cm long and one of whose diagonals is 14cm",
            "The area of a triangle with sides 13cm, 12cm, 5cm is:",
            "Ben plays 11 games of golf and scores the following:79, 70, 83, 76, 88, 70, 83, 88, 74, 89 and 80. Find the mean of his scores?",
            "Paige cut a cylindrically shaped candle, having a diameter and height as 6cm and 12cm respectively, into 4 equal parts. She then took a piece and rolled it into 2 similar balls. What would be the radius of the ball?",
            "A rope is tightly stretched and attached from top of a vertical tower to the ground. The angle made by rope with ground is 45∘.If length of the rope is 10√2m, find height of the tower.",
            "A point of the form (a, 0) lies on the line:"]

radiobutton1 = ["90", "2951", "1/6", "40cm", "150    ", "102.8", "13",
                "1", "672", "30", "73", "5.163cm", "10m ", "x=y"]
radiobutton2 = ["98", "2952", "3/6", "43cm", "50x3^-1", "97.3 ", "17",
                "2", "338", "27", "80", "21.63cm", "10√3", "y=0"]
radiobutton3 = ["87", "2949", "4/6", "45cm", "p-3^-1 ", "99.8 ", "14",
                "0", "336", "34", "85", "2.163cm", "10√2", "x+y=0"]
correct = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]
userans = []

# Randomizer for the questions, creates a list called questions_for_display 
# which is then used in the counter variable to print a certain question lower
questions_for_display = []
for loop in range(11):
    my_rando_int = choice(list(set(range(0, 13)) - set(questions_for_display)))
    questions_for_display.append(my_rando_int)

answerkey = []

# Background image code
background = PhotoImage(file='Background_1.png')
img_label = Label(image=background)


# Main question screen
def startquiz():


    win2 = Toplevel(win1)
    win2.geometry("650x430")
    win2.title("Year 10 Maths Quiz.")
    win2.configure()
    button2 = Label(win2, image=background, borderwidth=0).place(x=0, y=0)

    global count

    # Next question Function
    def check_ans():


        #Needs to be done
        for widgets in win2.winfo_children():
                widgets.destroy()
        button3 = Label(win2, image=background, borderwidth=0).place(x=0, y=0)
        global count
        global state1
        counter = (questions_for_display[count] - 1)
        count = count + 1
        answerkey.append(correct[counter])
        userans.append(var1.get())
        qnum = ("Questions", count)
        #Question Buttons
        r1 = Radiobutton(win2, text=radiobutton1[counter], variable=var1, value=1, font="times",bg="#ffffff").place(x=190, y=260)
        r2 = Radiobutton(win2, text=radiobutton2[counter], variable=var1, value=2, font="times",bg="#ffffff").place(x=300, y=260)
        r3 = Radiobutton(win2, text=radiobutton3[counter], variable=var1, value=3, font="times",bg="#ffffff").place(x=410, y=260)
        label7 = Label(win2, text=correct[counter]).place(x = 0,y = 0)
        label4 = Button(win2, text=(qnum),font="times",fg="black", bg="#ffffff", padx=30, pady=10).place(x=260, y=20)
        label5 = Label(win2, text=question[counter], font="times",fg="black", bg="#ffffff",wraplength=280, justify=CENTER).place(x=200, y=120)
        label6 = Button(win2, text="Next question", command=check_ans,state = state1, font="times", 
                        fg="black", bg="#9cc2ff",padx=30, pady=3).place(x=90, y=310 )
        label10 = Label(win2, text=userans).place(x=0, y=60)
        label11 = Label(win2, text=answerkey).place(x=0, y=30)

        
        #Stops the program after 10 questions have been answered
        if count == 11:
            state1 = DISABLED
            for label6 in win2.winfo_children():
                label6.destroy()
            button5= Label(win2, image=background, borderwidth=0,).place(x=0, y=0)
            answerkey.pop(10)

            label8 = Label(win2, text="Press button to view score").place(x=260, y=20)
            label9 = Button(win2, text="Check Score", command=calc_score).place(x=90, y=310)
            label10 = Label(win2, text=userans).place(x=0, y=0)
            label11 = Label(win2, text=answerkey).place(x=0, y=30)
            
    # Calculates the score and displays it on the 1st screen
    def calc_score():

        
        for widgets in win1.winfo_children():   
                widgets.destroy()
        button4= Label(win1, image=background, borderwidth=0,).place(x=0, y=0)

        win2.destroy()
        counter1 = 0
        score = 0
        for loop in range(10):
            if answerkey[counter1] == userans[counter1]:
                score = score +1
            else:
                score = score
            counter1 = counter1 + 1
            print(score)
        
        if score < 4:
            label12 = Label(win1, text="Not achieved").place(x=0, y=0)
        elif score <6:
            label12 = Label(win1, text="Achieved").place(x=0, y=0)        
        elif score <8:
            label12 = Label(win1, text="Merit").place(x=0, y=0)
        elif score <11:
            label12 = Label(win1, text="Excellence").place(x=0,y=0)
        label3 = Button(win1, text="End quiz", command=endquiz,font="times", fg="black", bg="#ffffff", padx=30, pady=3).place(x=400, y=310)  

    # First question code must be kept seperate 
    counter = (questions_for_display[count]-1)    
    count = count+1
    qnum = ("Question "+str(count))
    r1 = Radiobutton(win2, text=radiobutton1[counter], variable=var1, value=1, font="times", bg="#ffffff").place(x=190, y=260) 
    r2 = Radiobutton(win2, text=radiobutton2[counter], variable=var1, value=2, font="times", bg="#ffffff").place(x=300, y=260)
    r3 = Radiobutton(win2, text=radiobutton3[counter], variable=var1, value=3, font="times", bg="#ffffff").place(x=410, y=260)
    label7 = Label(win2, text = correct[counter]).place(x = 0,y = 0)
    label4 = Button(win2, text = ("Question",count), font = "times",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
    label5 = Label(win2, text = question[counter],font = "times", fg = "black", bg = "#ffffff", wraplength=280, justify=CENTER).place(x = 200, y= 120)
    label6 = Button(win2, text = "Next question" ,command=check_ans,state = state1,font = "times", fg = "black",bg = "#9cc2ff",padx = 30, pady = 3).place(x=90,y=310)
 
    #skip function
    def skips():
        global count
        for widgets in win2.winfo_children():   
                widgets.destroy()
        check_ans()

        answerkey.pop(correct[counter])
        userans.pop(counter)
        answerkey.append(correct[counter],13)
    label14 = Button(win2, text = "Skip", command = skips, font = "times" ,padx = 60, pady=3, bg="#9cc2ff", fg = "black").place(x=400, y=310)


# Ends the entire program. 
def endquiz():
    win1.destroy()

# 1st screen labels
button1 = Label(win1, image=background ,borderwidth=0,).place(x=0, y=0)
label1 = Button(win1, text="Quiz game" ,font="times",fg="black", bg="#ffffff", padx=30, pady=10).place(x=260, y=20)
lable2 = Button(win1, text="Start quiz",command=startquiz, state=state1, font="times", fg="black", bg="#9cc2ff", padx=30, pady=3).place(x=90, y=310)
label3 = Button(win1, text="End quiz", command=endquiz,font="times", fg="black", bg="#9cc2ff", padx=30,pady=3).place(x=400, y=310)

# Does tkinter
win1.mainloop()
