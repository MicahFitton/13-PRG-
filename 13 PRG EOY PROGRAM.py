import random
from tkinter import*
win1 = Tk()
win1.geometry("650x430")
win1.title("Year 10 Maths Quiz.")
win1.configure()
state1 = NORMAL
count = 14
var1 = IntVar()

score = 0
question = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
radiobutton1 = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
radiobutton2 = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
radiobutton3 = ["placeholder1","placeholder2","placeholder3","placeholder4","placeholder5","placeholder6","placeholder7","placeholder8","placeholder9","placeholder10","placeholder11","placeholder12","placeholder13","placeholder14"]
correct = [1,3,2,1,3,1,2,2,3,2,1,2,3,3]
correctans = [0]
useranswer = []
#radiobutton2 = 
#radiobutton3 = 
def startquiz():
    def clear_frame():
        #global counter
        global count
        global state1
        global score
        for widgets in win2.winfo_children():   
            widgets.destroy()
        if count == 4:
            state1 = DISABLED
        count = count-1
        counter = random.randint(0,(count))
        counter1 = counter
        counter2 = random.randint(0,(13))
        counter3 = random.randint(0,(13))
        correct.pop(counter)
        label4 = Button(win2, text = "Question 1",font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
        label5 = Label(win2, text = question[counter],font = "Corbel_Light",fg = "black", bg = "#ffffff",).place(x = 280, y= 120)
        label6 = Button(win2, text = "Next question" ,command=clear_frame,state = state1,font = "Corbel_Light", fg = "black",bg = "#ffffff",padx = 30, pady = 3).place(x =90, y =310 )
        r1 = Radiobutton(win2, text = radiobutton1[counter1],variable= var1, value = 1,font = "times").place(x = 190, y = 200)
        r2 = Radiobutton(win2, text = radiobutton2[counter2],variable = var1,value = 2,font = "times").place(x = 300, y = 200)
        r3 = Radiobutton(win2, text = radiobutton3[counter3],variable = var1, value = 3,font = "times").place(x = 410, y = 200)
        label7 = Label(win2, text = correct[counter1]).place(x = 0, y =0)
        correctans.append(correct[counter])
        useranswer.append(int(var1.get()))
        #if int(var1.get()) == int(correct[counter]):
        #    score = score+1
        #    print(score)
        #if score >= 3:
        #    grade = "NA"
        #elif score >=5:
        #    grade = "A"
        #elif score >=8:
        #    grade = "M"
        #else:
        #    grade = "E"
        question.pop(counter)
        radiobutton1.pop(counter)
        #correct.pop(0)

        print("useranswer: ",useranswer)
        print("correctans: ",correct[counter])
        
    win2 = Toplevel(win1)
    win2.geometry("650x430")
    win2.title("Year 10 Maths Quiz.")
    win2.configure()
    label4 = Button(win2, text = "Question 1",font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
    label5 = Label(win2, text = "PLACEHOLDER",font = "Corbel_Light",fg = "black", bg = "#ffffff",).place(x = 280, y= 120)
    label6 = Button(win2, text = "Next question" ,command=clear_frame,state = state1,font = "Corbel_Light", fg = "black",bg = "#ffffff",padx = 30, pady = 3).place(x =90, y =310 )
    
def endquiz():
    win1.destroy()

label1 = Button(win1, text = "Quiz game" ,font = "Corbel_Light",fg = "black", bg = "#ffffff", padx = 30, pady = 10).place(x = 260, y = 20)
lable2 = Button(win1, text = "Start quiz",command = startquiz, font ="Corbel_Light", fg= "black", bg = "#ffffff", padx = 30, pady = 3).place(x = 90, y= 310)
label3 = Button(win1, text = "End quiz", command = endquiz,font = "Corbel_Light", fg = "black", bg = "#ffffff", padx = 30, pady = 3).place(x = 400, y = 310)


win1.mainloop()
