import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.wm_geometry("900x600")

title = tk.Label(root,text="MODEL ANALYSIS    ",font="Helvetica 16 bold italic",fg = "gray",pady=20).grid(row=0,pady=20,padx=0,column=3,columnspan=2)
#tk.Label(root,text="MODEL ANALYSIS    ",font="Helvetica 16 bold italic",fg = "gray",bg="blue",pady=20).grid(row=0,padx=0,column=4,sticky = tk.E)
image1 = ImageTk.PhotoImage(Image.open("oneLayer_loss_plot_1588616424.7930098.png"))
image2 = ImageTk.PhotoImage(Image.open("oneLayer_accuracy_plot_1588616424.6451762.png"))
image3 = ImageTk.PhotoImage(Image.open("two_loss_plot_1588887461.4619737.png"))
image4 = ImageTk.PhotoImage(Image.open("twolayer1.png"))
image5 = ImageTk.PhotoImage(Image.open("regression_loss_plot_1588700738.6616457.png"))
image6 = ImageTk.PhotoImage(Image.open("regression_accuracy_plot_1588617273.281886.png"))

image7 = ImageTk.PhotoImage(Image.open("oneLayer_loss_plot_1588616424.7930098.png"))
image8 = ImageTk.PhotoImage(Image.open("oneLayer_accuracy_plot_1588616424.6451762.png"))

imageList = [image1,image2,image3,image4,image5,image6,image7,image8]

heading = tk.Label(root,text="ONE LAYER ANN ACCURACY",font=18)
heading.grid(row=1,column=2,columnspan=4,pady=10,rowspan=2)
my_label = tk.Label(image=image1)
my_label.grid(row=3,column=1,columnspan=3,padx=10)
my_label1 = tk.Label(image=image2)
my_label1.grid(row=3,column=4,columnspan=3)

head =["ONE LAYER ANN ACCURACY","TWO LAYER ANN MODEL","REGRESSION MODEL","DECISION TREE"]

def forward(image_number,i):
    global heading
    global my_label
    global my_label1
    global button_forwarad
    global button_back

    heading.grid_forget()
    my_label.grid_forget()
    my_label1.grid_forget()
    
    heading = tk.Label(root,text=head[i+1],font=18) 
    my_label = tk.Label(image=imageList[image_number-1]) 
    my_label1 = tk.Label(image=imageList[image_number])
    

    print("imagein first run",image_number)
    button_forwarad = tk.Button(buttonframe,text=">>",command=lambda:forward(image_number+2,i+1))
    button_back = tk.Button(buttonframe,text="<<",command=lambda:back(image_number-2,i-1))

    if image_number == 7:
        button_forwarad = tk.Button(buttonframe,text=">>",state=tk.DISABLED)
    
    heading.grid(row=1,column=2,columnspan=4,pady=10,rowspan=2)
    my_label.grid(row=3,column=1,columnspan=3,padx=10)
    my_label1.grid(row=3,column=4,columnspan=3)


    button_back.grid(row=5,column=2,columnspan=1)
    button_exit.grid(row=5,column=3,columnspan=1)
    button_forwarad.grid(row=5,column=4,columnspan=1)



def back(image_number,i):
    global heading
    global my_label
    global my_label1
    global button_forwarad
    global button_back

    heading.grid_forget()
    my_label.grid_forget()
    my_label1.grid_forget()
    
    heading = tk.Label(root,text=head[i+1],font=18)
    my_label = tk.Label(image=imageList[image_number-1])
    my_label1 = tk.Label(image=imageList[image_number])

    print("imagein first run",image_number)
    button_forwarad = tk.Button(buttonframe,text=">>",command=lambda:forward(image_number+2,i+1))
    button_back = tk.Button(buttonframe,text="<<",command=lambda:back(image_number-2,i-1))

    if image_number == 1:
        button_back = tk.Button(buttonframe,text="<<",state=tk.DISABLED)
    
    heading.grid(row=1,column=2,columnspan=4,pady=10,rowspan=2)
    my_label.grid(row=3,column=1,columnspan=3,padx=10)
    my_label1.grid(row=3,column=4,columnspan=3)


    button_back.grid(row=5,column=2,columnspan=1)
    button_exit.grid(row=5,column=3,columnspan=1)
    button_forwarad.grid(row=5,column=4,columnspan=1)

buttonframe = tk.Frame(root,bg = "blue")      
buttonframe.grid(row =4,column=3,columnspan=2,pady=20)

button_back = tk.Button(buttonframe,text="<<",command=back,state=tk.DISABLED)
button_exit = tk.Button(buttonframe,text="exit",command=root.quit)
button_forwarad = tk.Button(buttonframe,text=">>",command=lambda:forward(3,0))


button_back.grid(row=5,column=2,columnspan=1)
button_exit.grid(row=5,column=3,columnspan=1)
button_forwarad.grid(row=5,column=4,columnspan=1)

root.mainloop()







