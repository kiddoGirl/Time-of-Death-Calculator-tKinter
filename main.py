### Author : Manjubashini ###

import tkinter
import math
from math import log
from datetime import datetime,timedelta

window=tkinter.Tk()
Title=window.title("FORENSIC TIME OF DEATH CALCULATOR")
window["bg"]="pink"

Body_F=tkinter.StringVar()
Time_Death=tkinter.StringVar()
Locality_F=tkinter.StringVar()
Time_Diff=tkinter.StringVar()
After_BT=tkinter.StringVar()


def TIMEOFDEATH():
    Body_Temperature= float(Body_F.get())
    Time_of_Death=Time_Death.get().split(':')
    Locality_Temperature= float(Locality_F.get())
    Time_Difference= int(Time_Diff.get())
    After_Body_Temperature= float(After_BT.get())

    #print(Body_Temperature)
    #print(Time_of_Death)
    #print(Locality_Temperature)
    #print(Time_Difference)
    #print(After_Body_Temperature)

    Normal_Temp=98.6

    c=(Body_Temperature - Locality_Temperature)
    e=((After_Body_Temperature - Locality_Temperature)/c)
    upp=((Normal_Temp - Locality_Temperature)/c) 

    #print(e)
    De= math.log(e)
    Ne=Time_Difference*(log(upp))
    Hour=(Ne/De)
    frac,whole=math.modf(Hour)
    minute=abs(int(60/100*(frac*100)))

    if(Time_of_Death[2]=='PM'):
        if(int(Time_of_Death[0])<12):
            Time_of_Death[0]=int(Time_of_Death[0])+12

    if(Hour<0):
        d=datetime(2022,4,11,int(Time_of_Death[0]),int(Time_of_Death[1])) + timedelta(hours=int(Hour),minutes=minute)#frt , nlchr 
    else:
        d=datetime(2022,4,11,int(Time_of_Death[0]),int(Time_of_Death[1])) - timedelta(hours=int(Hour),minutes=minute)

                                                            
    ans=d.strftime("%I:%M%p")
    Answer=tkinter.Label(window,text="TIMEOFDEATH IS  : "+ans,font=("Calibre",20,"bold"),fg=("purple"),bg=("pink"))
    Answer.place(x=500,y=650) 

  
label=tkinter.Label(window,text="FORENSIC TIME OF DEATH CALCULATOR",font=("calibre",20,"bold"),bg=("pink"))

Body_Temp=tkinter.Label(window,text="BODY TEMPERATURE-FIRST READING",font=("Calibre",10,"bold"),fg=("black"),bg=("pink"))
Body_Temp_entry=tkinter.Entry(window,textvariable=Body_F,font=("Calibre",10,"bold"),bg=("white"))#cr entry for name input

Time_death=tkinter.Label(window,text="TIME OF FIRST READING",font=("calibre",10,"bold"),fg=("black"),bg=("pink"))
Time_death_entry=tkinter.Entry(window,textvariable=Time_Death,font=("calibre",10,"bold"))#cr entry for pass input

Locality_Temp=tkinter.Label(window,text="TEMPERATURE OF THE LOCALITY",font=("calibre",10,"bold"),fg=("black"),bg=("pink"))
Locality_Temp_entry=tkinter.Entry(window,textvariable=Locality_F,font=("calibre",10,"bold"))

Time_Taken=tkinter.Label(window,text="TIME BETWEEN FIRST AND SECOND READING",font=("calibre",10,"bold"),fg=("black"),bg=("pink"))
Time_Taken_entry=tkinter.Entry(window,textvariable=Time_Diff,font=("calibre",10,"bold"))

Body_Temp2=tkinter.Label(window,text="BODY TEMPERATURE-SECOND READING",font=("calibre",10,"bold"),fg=("black"),bg=("pink"))
Body_Temp2_entry=tkinter.Entry(window,textvariable=After_BT,font=("calibre",10,"bold"))


sub_btn=tkinter.Button(window,text="TIMEOFDEATH",font=("calibre",15,"bold"),fg=("grey"),bg=("sky blue"),command=TIMEOFDEATH)

#grid logic

label.place(x=380,y=20)

Body_Temp.place(x=400,y=100)
Body_Temp_entry.place(x=800,y=100)

Time_death.place(x=400,y=200)
Time_death_entry.place(x=800,y=200)
             
Locality_Temp.place(x=400,y=300)
Locality_Temp_entry.place(x=800,y=300)

Time_Taken.place(x=400,y=400)
Time_Taken_entry.place(x=800,y=400)


Body_Temp2.place(x=400,y=500)
Body_Temp2_entry.place(x=800,y=500)

sub_btn.place(x=600,y=580)



window.mainloop()
