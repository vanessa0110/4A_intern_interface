# import if libraries
from tkinter import *
from PIL import ImageTk, Image
import csv
import pandas as pd
#import plotly.graph_objs as go
import io
#import plotly.express as px
#import plotly.io as pio
#from plotly.offline import plot
from tkhtmlview import HTMLLabel
from tkinter import ttk
import tkinter.font as tkFont
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt




#avoid to write it always
#avoid to write it always
link ='C:\\Users\\User\\Documents\\Stage_4A_Vanessa\\Interface\\Images'
logo = link + '\\openBCI.ico'



###################################################################################################################
#-------------------------------------------------WINDOW 1---------------------------------------------------------
# the function of the first window we open. When we click on the button it create a new window with this information into
def window_1():
    other = Toplevel()
    other.title("Raw data") #we change the title of the new window 
    other.geometry("1300x1600")
    other.iconbitmap(logo)
    

    
        
    # create a main frame
    main_frame =  Frame(other)
    main_frame.pack(fill=BOTH, expand=1)

    # create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrollbar to the canvas 
    my_scrollbarv = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbarv.pack(side=RIGHT, fill=Y)
    my_scrollbarh = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
    my_scrollbarh.pack(side=TOP,fill=X)
    
    # configure the canvas
    my_canvas.configure(yscrollcommand = my_scrollbarv.set)
    my_canvas.configure(xscrollcommand = my_scrollbarh.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")) )

    # create an other frame inside the canvas
    second_frame = Frame(my_canvas)

    # add the new frame to a window in the canvas 
    my_canvas.create_window((0,0), window= second_frame, anchor="nw")
    second_frame.config(width=1600, height=1200)


    ## the code here : 
    #------------------ Image of nomenclature --------------------------------------------------
    global my_img1
    image = Image.open(link + "\\head__1_-removebg-preview.png")
    image = image.resize((200, 250))
    my_img1 = ImageTk.PhotoImage(image)
    my_label = Label(second_frame, image=my_img1)
    my_label.place(x=550,y=0)

    #---------------- Graphic -----------------------------------------------------------------
    road = 'C:\\Users\\User\\Documents\\Stage_4A_Vanessa\\doc_matlab'
    raw_data = pd.read_csv(road +'/2021911-19-2-data.csv', delimiter=',',index_col=0)
    event_data = pd.read_csv(road+'\\2021911-19-2-events.csv', delimiter=',')
    
    fig, ax = plt.subplots()
    sns.set(rc={'figure.figsize':(12,4)})
    sns.lineplot(data=raw_data)
    
    # Access the current axes object
    ax = plt.gca()

    #ajustthe x limit
    #plt.xlim(400* 1000000, 410* 1000000)

    # Get the current x-axis tick labels
    xticks = ax.get_xticks()
    # Convert the tick values from milliseconds to seconds
    xticks_seconds = [tick / 1000000 for tick in xticks]
    # Set the new tick labels on the x-axis
    ax.set_xticklabels(xticks_seconds)
   
    ######################################################## a revoir----------------------------
    #x_min, x_max = ax.get_xlim()
    #def nexxt(x_min,x_max):
    #    plt.xlim(x_min+50,x_max+50)

    #next = Button(second_frame, text='>', command=nexxt(400,500))
    #next.place(x=500,y=700)
    #################################################################----------------------------
    
    
    
    #recupere valeur max pr x
    x_min, x_max = ax.get_xlim()
    # Ajouter les lignes verticales
    for i in range(event_data.shape[0]):
        x_value = event_data.iloc[i, 0]
        if x_value >= x_min and x_value <= x_max:
            if event_data.iloc[i,1]=="IMGTASK_LA" :
                plt.axvline(x=x_value, color='darkcyan', linewidth=1)
                #plt.legend(['IMGTASK_LA'], bbox_to_anchor=(0.5, 1.15), loc='upper center')
            elif event_data.iloc[i,1]=="IMGTASK_RA" :
                plt.axvline(x=x_value, color='blue', linewidth=1)
            elif event_data.iloc[i,1]=="IMGTASK_AT" :
                plt.axvline(x=x_value, color='black', linewidth=1)
            elif event_data.iloc[i,1]=="OE" :
                plt.axvline(x=x_value, color='orange', linewidth=1)
            elif event_data.iloc[i,1]=="CE" :
                plt.axvline(x=x_value, color='pink', linewidth=1)
            elif event_data.iloc[i,1]=="IMGTASK_START" :
                plt.axvline(x=x_value, color='red', linewidth=1)
        
    # Add the canvas to the frame
    canvas = FigureCanvasTkAgg(fig, master=second_frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=50, y=250)

    

    #---------------------------- we create a button to close the window when we finish in an exact place ------------------------
    exit = Button(second_frame, text="Close the window", command=other.destroy)
    bold_font = tkFont.Font(weight="bold")
    exit.configure(font=bold_font)
    exit.place(x=550,y=700)

    other.mainloop()



