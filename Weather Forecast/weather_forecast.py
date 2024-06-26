# Weather forecast
import tkinter, requests
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO

# Define window
root = tkinter.Tk()
root.title('Weather Forecast')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0, 0)

# Define fonts and colors
sky_color = '#76c3ef'
grass_color = '#aad207'
output_color = '#dcf0fb'
input_color = '#ecf2ae'
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

# Define Functions
def search():
    """Use open weather api to look up current weather conditions given a city/ city, country"""
    global response

    # Get API response
    # URL and my api key.... USE YOUR OWN API KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = '4d409dcb88adf71d46b7089994226e3b'

    # Search by appropriate query, entry city name or zip
    if search_method.get() == 1:
        querystring = {'q': city_entry.get(), 'appid': api_key, 'units': 'metric'}
    elif search_method.get() == 2:
        querystring = {'zip': city_entry.get(), 'appid': api_key, 'units': 'metric'}

    # Call API
    response = requests.request('GET', url, params=querystring)
    response = response.json()

    # Example response return
    """{'coord': {'lon': 32.5822, 'lat': 0.3163}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 
    'main': {'temp': 294.81, 'feels_like': 294.47, 'temp_min': 294.81, 'temp_max': 294.81, 'pressure': 1012, 'humidity': 55, 'sea_level': 1012, 'grnd_level': 882}, 'visibility': 10000, 
    'wind': {'speed': 1.78, 'deg': 66, 'gust': 2.84}, 'clouds': {'all': 98}, 'dt': 1702456482, 'sys': {'type': 1, 'id': 2642, 'country': 'UG', 'sunrise': 1702438839, 
    'sunset': 1702482407}, 'timezone': 10800, 'id': 232422, 'name': 'Kampala', 'cod': 200}"""

    get_weather()
    get_icon()

def get_weather():
    """Grab information from API response and update out weather labels."""
    # Gather the data to be used from the API response
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']

    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    # Update output labels
    city_info_label.config(text=city_name + "(" + city_lat + "," + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config(text="weather: " + main_weather + "," + description, font=small_font, bg=output_color)
    temp_label.config(text='Temperature: ' + temp + " C", font=small_font, bg=output_color)
    feels_label.config(text='Feels like: ' + feels_like + " C", font=small_font, bg=output_color)
    temp_min_label.config(text='Min Temperature: ' + temp_min + " C", font=small_font, bg=output_color)
    temp_max_label.config(text='Max Temperature: ' + temp_max + " C", font=small_font, bg=output_color)
    humidity_label.config(text='Humidity: ' + humidity, font=small_font, bg=output_color)

def get_icon():
    """Get the appropriate weather icon from API response"""
    global img

    # Get the icon id from the API response
    icon_id = response['weather'][0]['icon']

    # Get the icon from the correct website
    url = 'https://openweathermap.org/img/wn/{icon}@2x.png'.format(icon=icon_id)

    # Make a request at the url to download the icon; stream= True automatically Download
    icon_response = requests.get(url, stream=True)

    # Turn into form that tkinter/python can use
    img_data = icon_response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    # Update label
    photo_label.config(image=img)

# Define layout
# Create Frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

# Output frame layout
city_info_label = tkinter.Label(output_frame, bg=output_color)
weather_label = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feels_label = tkinter.Label(output_frame, bg=output_color)
temp_min_label = tkinter.Label(output_frame, bg=output_color)
temp_max_label = tkinter.Label(output_frame, bg=output_color)
humidity_label = tkinter.Label(output_frame, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)



city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

# Input Frame layout
# Create input frame button and entry
city_entry  = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text='Submit', font='large_font', bg=input_color, command=search)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text='Search by City Name', variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text='Search by zipcode', variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10, 0))
submit_button.grid(row=0, column=1, padx=10, pady=(10, 0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=5, pady=2)

# Run root windows mainloop
root.mainloop()