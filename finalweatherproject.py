from tkinter import *
from PIL import ImageTk,Image
import requests

def a(weather):
    try:
        City=weather['name']
        Condition=weather['weather'][0]['description']
        Temperature=weather['main']['temp']
        Humidity=weather['main']['humidity']
        final='City:%s\nCondition:%s\nTemperature:%s\nHumidity:%s'%(City,Condition,Temperature,Humidity)
    except:
        final='There is a problem in retreiving information.'
    return final  

#api url https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}

def get_weather(city):
    weather_key='e7b12213a53e62005e4852125cdc968e'
    url='https://api.openweathermap.org/data/2.5/weather'
    parameter={'appid':weather_key,'q':city}
    response=requests.get(url,parameter)
    
    weather=response.json() 
    
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])
    print(weather['main']['humidity'])
    
    l2['text']=a(weather)
    
    
frame=Tk()
frame.geometry('800x500')
frame.title('Weather Forecast')

#labels

l1=Label(frame,text='Enter the city name',fg='white',bg='#000747',font=('Franklin Gothic Heavy',25,'bold','italic'))
l1.place(relx=0.28,rely=0.05)

#entry fields

e1=Entry(frame,bg='#CDE3F6',font=('Franklin Gothic Heavy',25,'italic'))
e1.place(relx=0.26,rely=0.15)

l2=Label(frame,bg='#CDE3F6',font=('Franklin Gothic Heavy',25,'italic'))
l2.place(relx=0.26,rely=0.35,width=400,height=300)

#button

b1=Button(frame,text='Search',font=('Franklin Gothic Heavy',15,'bold','italic'),height=1,bg='#FFFED7',command=lambda:get_weather(e1.get()))
b1.place(relx=0.40,rely=0.25)
'''
#image
img=Image.open(r"./p2.jpg")
img=img.resize((800,500),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(img) 
l3=Label(frame,image=img1)
l3.place(x=0,y=0,width=800,height=500)  

'''

frame.configure(bg='#000747')
frame.mainloop()
