import requests
import tkinter as tk
from tkinter import messagebox

api_key = "58c4985f734828c66cea872a0018d3a6"

def get_weather():
    city_name = city_entry.get()
    country_code = "IR"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        temperatrue = main['temp']
        weather_description = weather['description']
        wind_speed = wind['speed']

        result_label.config(text=f"شهر: {city_name}\nدما: {temperatrue}°C\nوضیعت هوا: {weather_description}\nسرعت باد: {wind_speed}متر بر ثانیه")
    else:
        messagebox.showerror("faild")
        
root= tk.Tk()
root.title("اب و هوا")

city_label = tk.Label(root, text="نام شهر را وارد کنید:")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(root, text="دریافت اطلاعات", command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
