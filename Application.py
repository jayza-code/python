import customtkinter as ctk
from customtkinter import *
from PIL import Image
import requests as re

set_appearance_mode('dark')
image = Image.open('white magnifing glass.png')

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.icon = CTkImage(dark_image=image)
        self.root.geometry('375x230')
        self.root.minsize(375, 230)
        self.root.maxsize(375, 230)
        self.entry = CTkEntry(master=self.root,
                              placeholder_text='City',
                              font=('Arial', 20),
                              width=275,
                              height=35)
        self.entry.pack(pady=12, padx=10)
        self.entry.place(x=13)
        self.button_search = CTkButton(master=self.root,
                                image=self.icon,
                                fg_color='#434242',
                                text='',
                                width=75,
                                height=33,
                                command=self.button_search_function)
        self.button_search.pack()
        self.button_search.place(x=295, y=1)
        self.label_maxtemperature = CTkLabel(master=self.root,
                                             text='Maximum temperature:',
                                             font=('Comic Sans MS', 23),
                                             text_color='#A2A2A2',
                                             height=50,)
        self.label_maxtemperature.pack()
        self.label_maxtemperature.place(x=1, y=35)
        self.label_mintemperature = CTkLabel(master=self.root,
                                             text='Minimum temperature:',
                                             font=('Comic Sans MS', 23),
                                             text_color='#A2A2A2')
        self.label_mintemperature.pack()
        self.label_mintemperature.place(x=1, y=80)
        self.label_humidity = CTkLabel(master=self.root,
                                       text='Humidity: ',
                                       font=('Comic Sans MS', 23),
                                       text_color='#A2A2A2')
        self.label_humidity.pack()
        self.label_humidity.place(x=1, y=115)
        self.label_wind_speed = CTkLabel(master=self.root,
                                         text='Wind speed:',
                                         font=('Comic Sans MS', 23),
                                         text_color='#A2A2A2')
        self.label_wind_speed.pack()
        self.label_wind_speed.place(x=1, y=150)
        self.label_description = CTkLabel(master=self.root,
                                          text='Description: ',
                                          font=('Comic Sans MS', 23),
                                          text_color='#A2A2A2')
        self.label_description.pack()
        self.label_description.place(x=1, y=185)

        self.root.mainloop()

    def button_search_function(self):
        city = self.entry.get()
        api_key = '495539b81436a6667062cb52de593b11'
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        url =f"{base_url}?appid={api_key}&q={city}"
        response = re.get(url).json()
        max_temp_kelvin = response['main']['temp_max']  # gets temperature in base temperature kelvin
        min_temp_kelvin = response['main']['temp_min']
        max_temp_celsius = kelvin_to_celsius(max_temp_kelvin)
        min_temp_celsius = kelvin_to_celsius(min_temp_kelvin)
        max_temp_celsius = int(round(max_temp_celsius, 1))
        min_temp_celsius = int(round(min_temp_celsius, 1))
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        wind_speed = response['wind']['speed']
        self.label_maxtemperature.configure(text=f"Maximum temperature: {max_temp_celsius}°C")
        self.label_mintemperature.configure(text=f"Minimum temperature: {min_temp_celsius}°C")
        self.label_humidity.configure(text=f"Humidity: {humidity}%")
        self.label_description.configure(text=f"Description: {description}")
        self.label_wind_speed.configure(text=f"Wind speed: {wind_speed}kmp/h")
App()