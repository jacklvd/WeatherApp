from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
import requests
from PIL import ImageTk, Image
from time import strftime
from datetime import datetime
import os

# store the API
key = os.environ.get('WeatherAPIKey')

# set up the screen or the app gui
screen = Tk()
screen.geometry('800x400')
screen.iconbitmap('assets/Papirus-Team-Papirus-Apps-Weather.ico')
screen.title('My Weather')
screen.resizable(0,0)

try:

    # process the API
    def weather_data(query):
        res = requests.get('https://api.openweathermap.org/data/2.5/weather?'+ query +'&appid=' + key)
        return res.json();

    #Body UI
    Frame(screen, width=800, height= 50, bg='#353535').place(x=0, y=0)

    # search Bar
    img1 = ImageTk.PhotoImage(Image.open('assets/search5.png'))
    def on_enter(e):
        e1.delete(0,'end')
        
    def on_leave(e):
        if e1.get() == '':
            e1.insert(0, 'Search City')

    e1 = Entry(screen, width=21, fg='white', bg='#353535', border=0)
    e1.config(font=('Times New Roman', 12))
    e1.bind('<FocusIn>', on_enter)
    e1.bind('<FocusOut>', on_leave)
    e1.insert(0, 'Search City')
    e1.place(x=620, y=15)

    # date
    a = datetime.today().strftime('%B')
    b = (a.upper())
    month = datetime.now().month

    now = datetime.now()

    c = now.strftime('%B') #time
    month = c[0:3]


    today = datetime.today()
    date = today.strftime('%d')

    # city name
    def label(name):
        Frame(width=500, height=50, bg='#353535').place(x=0, y=0)
        l2 = Label(screen, text=str(name), bg='#353535', fg='white')
        l2.config(font=('Microsoft JhengHei UI Light', 18))
        l2.place(x=20, y=8)
        
        city = name
        query = 'q=' + city 
        w_data = weather_data(query)
        result = w_data
        
        global check
        
        try:
            check = '{}'.format(result['main']['temp']) # check valid city name
            celsius = '{}'.format(result['main']['temp']) # show result in celsius
        except:
            messagebox.showinfo('','    City name not found     ')
        
        counter = (int(float(check))) - 273 # convert into Celsius
        # description = ('{}'.format(result['weather'][0]['description']))
        weather = ('{}'.format(result['weather'][0]['main']))

        now = datetime.now()
        current_time = strftime('%H')
        
        global img

        if int(current_time) < 20 and int(current_time) >= 6 and counter <= 10 and weather == 'Fog' or weather == 'Clear':
            Frame(screen, width=800, height=350, bg='white').place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open('assets/cold.png'))
            Label(screen, image=img, border=0).place(x=170, y=130)
            bcolor = 'white' # background color
            fcolor = 'black' # font color
        
        # sunny weather condition
        elif counter > 10 and weather == 'Clear' or weather == 'Haze':
            Frame(screen, width=800, height=350, bg='#f78954').place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open('assets/sunny1.png'))
            Label(screen, image=img, border=0).place(x=170, y=130)
            bcolor = '#f78954' # background color
            fcolor = 'white' # font color
        
        # cloudy weather condition
        elif counter > 10 and weather == 'Clouds':
            Frame(screen, width=800, height=350, bg='#7492b3').place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open('assets/cloudy1.png'))
            Label(screen, image=img, border=0).place(x=170, y=130)
            bcolor = '#7492b3' # background color
            fcolor = 'white' # font color
        
        # cloud and cold weather condition
        elif counter <= 10 and weather == 'Clouds':
            Frame(screen, width=800, height=350, bg='#7492b3').place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open('assets/cloudcold.png'))
            Label(screen, image=img, border=0).place(x=170, y=130)
            bcolor = '#7492b3' # background color
            fcolor = 'white' # font color

        # cold weather condition
        elif counter > 10 and weather == 'Rain':
            Frame(screen, width=800, height=350, bg='#60789e').place(x=0, y=50)
            img = ImageTk.PhotoImage(Image.open('assets/rain1.png'))
            Label(screen, image=img, border=0).place(x=170, y=130)
            bcolor = '#60789e' # background color
            fcolor = 'white' # font color
            
        else:
            Frame(screen, width=800, height=350, bg='white').place(x=0, y=50)
            Label(screen, image=weather, border=0).place(x=170, y=130)
            label.configure(font=('Microsoft JHengHei UI Light', 23))
            bcolor = 'white' # background color
            fcolor = 'black' # font color                 

        w_data = weather_data(query)
        result = w_data
        
        h = ('Humidity: {}'.format(result['main']['humidity']))
        p = ('Pressure: {}'.format(result['main']['pressure']))        
        t_max = ('Max_temp: {}'.format(result['main']['temp_max']))
        t_min = ('Min temp: {}'.format(result['main']['temp_min']))
        b1 = b = ('Wind Speed: {} m/s'.format(result['wind']['speed']))
        
        l5 = Label(screen, text=str(month +' ' + date), bg=bcolor, fg=fcolor)
        l5.config(font=('Microsoft JHengHei UI Light', 25))
        l5.place(x=330, y=335)
        
        l4 = Label(screen, text=str(h + '%'), bg=bcolor, fg=fcolor)
        l4.config(font=('Microsoft JHengHei UI Light', 11))
        l4.place(x=510, y=135)            
            

        l6 = Label(screen, text=str(p + ' hPa'), bg=bcolor, fg=fcolor)
        l6.config(font=('Microsoft JHengHei UI Light', 11))
        l6.place(x=510, y=175)          

        l7 = Label(screen, text=str(b1), bg=bcolor, fg=fcolor)
        l7.config(font=('Microsoft JHengHei UI Light', 11))
        l7.place(x=510, y=215)
        
        l8 = Label(screen, text=str(counter) + '℃', bg=bcolor, fg=fcolor)
        l8.config(font=('Microsoft JHengHei UI Light', 25))
        l8.place(x=330, y=150)               


    label(name='Cincinnati')

    def cmd1():
        b = str(e1.get())
        label(str(b))        
            
    Button(screen, image=img1, border=0, command=cmd1).place(x=750, y=10)

except:
    Frame(screen, width=800, height=400, bg='white').place(x=0, y=0)
    global imgx
    imgx = ImageTk.PhotoImage(Image.open('assets/nointernet.png'))
    Label(screen, image=imgx, border=0).pack(expand=True)
        
screen.mainloop()