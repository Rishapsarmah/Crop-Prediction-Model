#######################################################################################################################
#                                                                                                                     #
#                   GROUP MEMBERS:  (Crop Prediction)                                                                 #
#                   Chirantan Bhuyan                                                                                  #
#                   Dhritimoy Majumdar                                                                                #
#                   Jivan Jyoti Bhattacharja                                                                          #
#                   Rishap Sarmah                                                                                     #
#                   Nishant Deka                                                                                      #
#                                                                                                                     #
#######################################################################################################################

from tkinter import *
import pandas as pd
import numpy as np

root=Tk()   # Tkinter object

#----------------------------------------------- DECISION TREE ALGO ---------------------------------------------------
df = pd.read_csv('crop_data_train.csv')
label_nc = df['label']
inputs = df.drop(['label'], axis=1)
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs, label_nc)
#----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------ OUTPUT BOX ----------------------------------------------------------
scvalue = StringVar()
screen = Entry(root, textvariable=scvalue, font="comicsansms 25 bold")
screen.place(x=620, y=600)
Label(root,text="Result :",font="comicsansms 25 bold",bg='#ffe6e6').place(x=490,y=600)
#---------------------------------------------------------------------------------------------------------------------

#------------------------------------- CALCULATE AND DISPLAY RESULT --------------------------------------------------
def calculate():
    indept_vars = [[]]
    indept_vars[0].append(humidity_val.get())
    indept_vars[0].append(temp_val.get())
    indept_vars[0].append(ph_val.get())
    indept_vars[0].append(rainfall_val.get())
    result=model.predict(indept_vars)[0]
    scvalue.set(result)
#----------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------ SCREEN --------------------------------------------------------
screen_width=1520
screen_height=780
root.title("Crop yield Prediction")
root.geometry(f"{screen_width}x{screen_height}")
root.minsize(screen_width,screen_height)
root.maxsize(screen_width,screen_height)
root.configure(background='#ffe6e6')
#---------------------------------------------------------------------------------------------------------------------

#----------------------------------------------- HEADING -------------------------------------------------------------
topic=Label(root,text="CROP YIELD PREDICTION",font="comicsansms 30 bold",bg='#ffe6e6')
topic.pack(pady=10)
#---------------------------------------------------------------------------------------------------------------------

#------------------------------------------------- COLUMNS -----------------------------------------------------------
Label(root,text="TEMPERATURE :",font="comicsansms 25 bold",bg='#ffe6e6').place(x=200,y=150)
Label(root,text="HUMIDITY :",font="comicsansms 25 bold",bg='#ffe6e6').place(x=290,y=230)
Label(root,text="PH :",font="comicsansms 25 bold",bg='#ffe6e6').place(x=405,y=310)
Label(root,text="RAINFALL :",font="comicsansms 25 bold",bg='#ffe6e6').place(x=285,y=390)
#---------------------------------------------------------------------------------------------------------------------

#------------------------------------------------ VARIABLES ----------------------------------------------------------
humidity_val=DoubleVar()
temp_val=DoubleVar()
ph_val=DoubleVar()
rainfall_val=DoubleVar()
#---------------------------------------------------------------------------------------------------------------------

#------------------------------------------------ VALUE ENTRY --------------------------------------------------------
humidity_entry=Entry(root,textvariable=humidity_val,font="comicsansms 25 bold")
temp_entry=Entry(root,textvariable=temp_val,font="comicsansms 25 bold")
ph_entry=Entry(root,textvariable=ph_val,font="comicsansms 25 bold")
rainfall_entry=Entry(root,textvariable=rainfall_val,font="comicsansms 25 bold")
humidity_entry.place(x=500,y=150)
temp_entry.place(x=500,y=230)
ph_entry.place(x=500,y=310)
rainfall_entry.place(x=500,y=390)
#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------- SUBMIT BUTTON --------------------------------------------------
submit_btn=Button(text="SUBMIT",padx=10,pady=5,font="comicsansms 15 bold",command=calculate)
submit_btn.place(x=720,y=500)
#---------------------------------------------------------------------------------------------------------------------

root.mainloop()  # Tkinter Ending