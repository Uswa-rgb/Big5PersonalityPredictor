import tkinter as tk
import numpy as np
from tkinter import Radiobutton
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk,Image

def clicked(value):
    print(value)


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    intvars = []
    MODES = [
        "Disagree", "Somewhat disagree", "Neutral", "Somewhat Agree", "Agree"
    ]
    QUESTIONS = [
        ". I am the life of the party.", "I don't talk a lot.",
        ". I feel comfortable around people.", "I keep in the background. ",
        ". I start conversations. ", "I have little to say. ",
        ". I talk to a lot of different people at parties.",
        ". I don't like to draw attention to myself.",
        ". I don't mind being the center of attention.",
        ". I am quiet around strangers."
    ]

    def printAllVars(self):
        for var in self.intvars:
            print(var.get())

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        tk.Label(self,text = "BIG FIVE PERSONALITY TEST",font="Helvetica 16 bold italic",pady=20,bg="white").pack(side="top",fill=tk.X,expand=True)
        for i in range(10):
            x = tk.IntVar()
            x.set(3)
            self.intvars.append(x)

        i = 0
        for quest in self.QUESTIONS:
            print(quest)
            label = tk.Label(self,
                             text=str(i+1) + quest,
                             font="Helvetica 14 italic",
                             bg ="white",
                             
                             anchor=tk.W).pack(side="top",
                                               fill=tk.X,
                                               expand=True)
            buttonFrame = tk.Frame(self)
            buttonFrame.pack()
            var = self.intvars[i]
            j = 1
            for mode in self.MODES:
                print(mode)
                rdbtn = Radiobutton(buttonFrame,
                                    text=mode,
                                    variable=var,
                                    font="11",
                                 
                                    value=j,
                                    command=lambda: self.printAllVars())
                rdbtn.pack(side="left",fill=tk.X, anchor=tk.W)
                j += 1
            i += 1

    def getValues(self):
        return self.intvars


class Page2(Page):

    intvars = []
    MODES = [
        "Disagree", "Somewhat disagree", "Neutral", "Somewhat Agree", "Agree"
    ]
    QUESTIONS = [
        ". I get stressed out easily. ",
        ". I am relaxed most of the time.",
        ". I worry about things.",
        ". I seldom feel blue.",
        ". I am easily disturbed.",
        ". I get upset easily.",
        ". I change my mood a lot.",
        ". I have frequent mood swings.",
        ". I get irritated easily.",
        ". I often feel blue.",
    ]

    def printAllVars(self):
        for var in self.intvars:
            print(var.get())

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        for i in range(10):
            x = tk.IntVar()
            x.set(3)
            self.intvars.append(x)
       
        i = 0
        for quest in self.QUESTIONS:
            print(quest)
            label = tk.Label(self,
                             text=str(i+1) + quest,
                             font="Helvetica 14 italic",
                             bg ="white",
                             #relief=tk.SUNKEN,
                             anchor=tk.W).pack(side="top",
                                               fill=tk.X,
                                               expand=True)
            buttonFrame = tk.Frame(self)
            buttonFrame.pack()
            var = self.intvars[i]
            j = 1
            for mode in self.MODES:
                print(mode)
                rdbtn = Radiobutton(buttonFrame,
                                    text=mode,
                                    variable=var,
                                    value=j,
                                    font="11",
                                    command=lambda: self.printAllVars())
                rdbtn.pack(side="left",fill=tk.X, anchor=tk.W)
                j += 1
            i += 1

    def getValues(self):
        return self.intvars


class Page3(Page):
    intvars = []
    MODES = [
        "Disagree", "Somewhat disagree", "Neutral", "Somewhat Agree", "Agree"
    ]
    QUESTIONS = [
        ". I feel little concern for others.",
        ". I am interested in people.",
        ". I insult people.",
        ". I sympathize with others' feelings.",
        ". I am not interested in other people's problems.",
        ". I have a soft heart.",
        ". I am not really interested in others.",
        ". I take time out for others.",
        ". I feel others' emotions.",
        ". I make people feel at ease.",
    ]

    def printAllVars(self):
        for var in self.intvars:
            print(var.get())

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        for i in range(10):
            x = tk.IntVar()
            x.set(3)
            self.intvars.append(x)

        i = 0
        for quest in self.QUESTIONS:
            print(quest)
            label = tk.Label(self,
                             text=str(i) + quest,
                             font="Helvetica 14 italic",
                             bg ="white",
                             
                             anchor=tk.W).pack(side="top",
                                               fill=tk.X,
                                               expand=True)
            buttonFrame = tk.Frame(self)
            buttonFrame.pack()
            var = self.intvars[i]
            j = 1
            for mode in self.MODES:
                print(mode)
                rdbtn = Radiobutton(buttonFrame,
                                    text=mode,
                                    variable=var,
                                    font="11",
                                    value=j,
                                    command=lambda: self.printAllVars())
                rdbtn.pack(side="left",fill=tk.X, anchor=tk.W)
                j += 1
            i += 1

    def getValues(self):
        return self.intvars


class Page4(Page):
    intvars = []
    MODES = [
        "Disagree", "Somewhat disagree", "Neutral", "Somewhat Agree", "Agree"
    ]
    QUESTIONS = [
        ". I am always prepared.",
        ". I leave my belongings around.",
         ". I pay attention to details.",
        ". I make a mess of things.",
         ". I get chores done right away.",
        ". I often forget to put things back in their proper place.",
        ". I like order.",
        ". I shirk my duties.",
        ". I follow a schedule.",
        ". I am exacting in my work." ]

    def printAllVars(self):
        for var in self.intvars:
            print(var.get())

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        for i in range(10):
            x = tk.IntVar()
            x.set(3)
            self.intvars.append(x)

        i = 0
        for quest in self.QUESTIONS:
            print(quest)
            label = tk.Label(self,
                             text=str(i) + quest,
                             font="Helvetica 14 italic",
                             bg ="white",
                            
                             anchor=tk.W).pack(side="top",
                                               fill=tk.X,
                                               expand=True)
            buttonFrame = tk.Frame(self)
            buttonFrame.pack()
            var = self.intvars[i]
            j = 1
            for mode in self.MODES:
                print(mode)
                rdbtn = Radiobutton(buttonFrame,
                                    text=mode,
                                    font="11",
                                    variable=var,
                                    value=j,
                                    command=lambda: self.printAllVars())
                rdbtn.pack(side="left", fill=tk.X,anchor=tk.W)
                j += 1
            i += 1

    def getValues(self):
        return self.intvars


class Page5(Page):
    intvars = []
    MODES = [
        "Disagree", "Somewhat disagree", "Neutral", "Somewhat Agree", "Agree"
    ]
    QUESTIONS = [
        ". I have a rich vocabulary.",
        ". I have difficulty understanding abstract ideas.",
        ". I have a vivid imagination.",
        ". I am not interested in abstract ideas.", "I have excellent ideas.",
        ". I do not have a good imagination.",
        ". I am quick to understand things.", "I use difficult words.",
        ". I spend time reflecting on things.", "I am full of ideas."
    ]

    def printAllVars(self):
        for var in self.intvars:
            print(var.get())

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        for i in range(10):
            x = tk.IntVar()
            x.set(3)
            self.intvars.append(x)

        i = 0
        for quest in self.QUESTIONS:
            print(quest)
            label = tk.Label(self,
                             text=str(i) + quest,
                             
                             font="Helvetica 14 italic",
                             bg ="white",
                             anchor=tk.W).pack(side="top",
                                               fill=tk.X,
                                               expand=True)
            buttonFrame = tk.Frame(self)
            buttonFrame.pack()
            var = self.intvars[i]
            j = 1
            for mode in self.MODES:
                print(mode)
                rdbtn = Radiobutton(buttonFrame,
                                    text=mode,
                                    variable=var,
                                    font="11",
                                    value=j,
                                    command=lambda: self.printAllVars())
                rdbtn.pack(side="left",fill=tk.X, anchor=tk.W)
                j += 1
            i += 1

    def getValues(self):
        return self.intvars


class Page6(Page):
    page1 = None
    page2 = None
    page3 = None
    page4 = None
    page5 = None

    def generateResults(self):
        p1selection = self.page1.getValues()
        p2selection = self.page2.getValues()
        p3selection = self.page3.getValues()
        p4selection = self.page4.getValues()
        p5selection = self.page5.getValues()

        selection = {
            "p1": p1selection,
            "p2": p2selection,
            "p3": p3selection,
            "p4": p4selection,
            "p5": p5selection
        }

        userInput = []
        for i in range(1, 6):
            for j in selection[f"p{i}"]:
                userInput.append(j.get())

        inputArr = np.array(userInput)

        negative_values = [
            1, 3, 5, 7, 9, 11, 13, 20, 22, 24, 26, 31, 33, 35, 37, 41, 43, 45
        ]
        for val in negative_values:
            inputArr[val] = 6 - inputArr[val]

        inputArr = inputArr / 5
        #print("inputARRAYYY---------------------------\n", inputArr)

        modInput = np.reshape(inputArr, (1, 50))
        pred = model.predict(modInput)
        classifier = model.predict_classes(modInput)
        #regressor = model.predict_regressor(modInput)
        
        print("CLASSIFIERRRR--------",len(classifier),classifier)
        #print("REGRESSORRR--------",len(regressor),regressor)

        frame = tk.Frame(self,width=100,
                    height=100)
        frame.pack(side = "top" ,fill="x", expand=False)

        # frame2 = tk.Frame(self,width=300,
        #             height=300,
        #             bg='yellow')
        # frame2.pack(side=tk.RIGHT, fill="x", expand=False)

        bottomframe = tk.Frame(self,self,width=200,
                    height=200
                    )
        bottomframe.pack( side = tk.BOTTOM, fill="x", expand=False )

        textLabels = [("extroversion","introversion"),("Social Stability","something"),("Agressiveness","Passive"),("Concientiousness","something"),("Agreeableness","something")]

        label = tk.Label(
            frame,
            text=
            f" Extroversion\t\t: {pred[0][0]*100:.2f}%\n Emoional Stability\t: {pred[0][1]*100:.2f}%\n Agressivness\t\t: {pred[0][2]*100:.2f}%\n Conscientiousness\t: {pred[0][3]*100:.2f}%\n Opennsess\t\t: {pred[0][4]*100:.2f}%\n",
            font = "Helvetica 16 bold italic",
            anchor=tk.W,
            justify=tk.LEFT,
            compound = tk.LEFT,
            padx = 10).pack(side="left", fill=tk.X, expand=False)


        labels = textLabels[classifier[0]]
        values = [pred[0][classifier[0]]*100 , (1-pred[0][classifier[0]])*100]
        actualFigure = plt.figure(figsize = (4,3.4))
        explode = list()
        for k in labels:
            explode.append(0.1)
        pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        #plt.legend(pie[0], labels, loc="upper corner")
        canvas = FigureCanvasTkAgg(actualFigure, frame)
        canvas.get_tk_widget().pack(side="right",anchor = tk.E)   

            # else:
        for i in range(0,5):
            if classifier[0] != i:
                labels = textLabels[i]
                values = [pred[0][i]*100 , (1-pred[0][i])*100]

                actualFigure = plt.figure(figsize = (2.9,2))
                #actualFigure.suptitle("personality Trait", fontsize = 22)

                explode = list()
                for k in labels:
                    explode.append(0.1)

                pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')                

                canvas = FigureCanvasTkAgg(actualFigure, bottomframe)
                canvas.get_tk_widget().pack(side="left",padx=5,pady=5)



        #pie chart 1
        # labels = ["extroversion","introversion"]
        # values = [pred[0][0]*100 , (1-pred[0][0])*100]

        # actualFigure = plt.figure(figsize = (3,3))
        # #actualFigure.suptitle("personality Trait", fontsize = 22)

        # #explode=(0, 0.05, 0, 0)
        # # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. every group needs to have an associated explode value)
        # explode = list()
        # for k in labels:
            # explode.append(0.1)

        # pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        # #plt.legend(pie[0], labels, loc="upper corner")

        # canvas = FigureCanvasTkAgg(actualFigure, frame)
        # canvas.get_tk_widget().pack(side="right",anchor = tk.E)


        # #pie chart 2
        # labels = ["socialStability","neuroticism"]
        # values = [pred[0][1]*100 , (1-pred[0][1])*100]

        # actualFigure = plt.figure(figsize = (2,2))
        # #actualFigure.suptitle("personality Trait", fontsize = 22)

        # #explode=(0, 0.05, 0, 0)
        # # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. every group needs to have an associated explode value)
        # explode = list()
        # for k in labels:
            # explode.append(0.1)

        # pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
    #    # plt.legend(pie[0], labels, loc="upper corner")

        # canvas = FigureCanvasTkAgg(actualFigure, bottomframe)
        # canvas.get_tk_widget().pack(side="left")

        # #pie chart 3
        # labels = ["socialStability","neuroticism"]
        # values = [pred[0][1]*100 , (1-pred[0][1])*100]
        # actualFigure = plt.figure(figsize = (2,2))
        # #actualFigure.suptitle("personality Trait", fontsize = 22)
        # #explode=(0, 0.05, 0, 0)
        # # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. eve
        # explode = list()
        # for k in labels:
            # explode.append(0.1)
        # pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        # #plt.legend(pie[0], labels, loc="upper corner")
        # canvas = FigureCanvasTkAgg(actualFigure, bottomframe)
        # canvas.get_tk_widget().pack(side="left")

        # #pie ahrt 4
        # labels = ["openess","neuroticism"]
        # values = [pred[0][1]*100 , (1-pred[0][1])*100]

        # actualFigure = plt.figure(figsize = (2,2))
        # #actualFigure.suptitle("personality Trait", fontsize = 22)

        # #explode=(0, 0.05, 0, 0)
        # # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. every group needs to have an associated explode value)
        # explode = list()
        # for k in labels:
            # explode.append(0.1)

        # pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        # #plt.legend(pie[0], labels, loc="upper corner")

        # canvas = FigureCanvasTkAgg(actualFigure, bottomframe)
        # canvas.get_tk_widget().pack(side="left")

        # #piechart 5
        # labels = ["socialStability","neuroticism"]
        # values = [pred[0][1]*100 , (1-pred[0][1])*100]

        # actualFigure = plt.figure(figsize = (2,2))
        # #actualFigure.suptitle("personality Trait", fontsize = 22)

        # #explode=(0, 0.05, 0, 0)
        # # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. every group needs to have an associated explode value)
        # explode = list()
        # for k in labels:
            # explode.append(0.1)

        # pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        # #plt.legend(pie[0], labels, loc="upper corner")

        # canvas = FigureCanvasTkAgg(actualFigure, bottomframe)
        # canvas.get_tk_widget().pack(side="left")
        #canvas.show()
        # colors = ['c','m']
        # plt.pie(values,labels=labels,colors=colors)
        # plt.show()
        #print("PAGE 6 INPIUT ARAAAYYYYY",userInput)
        #print(len(userInput))

    def __init__(self, p1, p2, p3, p4, p5, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.page1 = p1
        self.page2 = p2
        self.page3 = p3
        self.page4 = p4
        self.page5 = p5

        bluebutton = tk.Button(self,
                               text="Save",
                               fg="blue",
                               command=lambda: self.generateResults())
        bluebutton.pack(side="bottom")


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(p1, p2, p3, p4, p5, self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self,background="white")
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # print("shaicsa------------------------------------------------------------")
        # print("page1 valuessssss: ",p1.getValues())

        #wrapperFunction(p1selection,p2selection,p3selection,p4selection,p5selection)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Page 4", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Page 5", command=p5.lift)
        b6 = tk.Button(buttonframe, text="Page 6", command=p6.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")

        p1.show()



model = tf.keras.models.load_model("twolayer.model")
if __name__ == "__main__":

    if (model != None):
        print("model loaded successfully")

    root = tk.Tk()
    main=MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1200x600")
    
    root.mainloop()

