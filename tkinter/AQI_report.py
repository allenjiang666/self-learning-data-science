from tkinter import *
import requests
import json

root=Tk()
root.title('Air Quality Report')
root.geometry('300x300')
# root.configure(background='#34495E')
root.resizable(False, False)

zipcode =78209
font_color={
	'Good':'#2ECC71',
	'Moderate':'#F4D03F', 
	'Unhealthy for sensitive group':'#D35400',
	'Unhealthy':'#E74C3C',
	'Very Unhealthy':'#7D3C98 ',
	'Hazardous':'#641E16'
	}

def search(code):
	global api
	zipcode = code
	url=f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=0AE5B32D-634A-401B-8E31-E49889AF5DB7'

	try:
		api_request = requests.get(url)
		api = json.loads(api_request.content)
	except Exception as e:
		api = 'Error..'

	city = Label(root, text=api[0]['ReportingArea'] + api[0]['StateCode'],font=('Arial',15,'italic') )
	city.grid(row=1, column=0, padx=2,ipady=2)
	aqi = Label(root, text=api[0]['AQI'], font=('Arial',45, 'bold'), fg=font_color[api[0]['Category']['Name']])
	aqi.grid(row=2, column=0, ipady=5)
	level = Label(root, text= api[0]['Category']['Name'],font=('Arial',15,'italic bold'), fg=font_color[api[0]['Category']['Name']],width=10)
	level.grid(row=3, column=0)


heading = Label(root, text='Air Quality',width=17, font=('Verdana',25,"bold"))
heading.grid(row=0, column=0)


zip_input = Entry(root, width=5, bd=3, relief=SUNKEN)
zip_input.grid(row=4, column=0, padx=2)
zip_input.insert(0,78209)

search_btn =  Button(root, text="Search by zipcode", command=lambda:search(zip_input.get()))
search_btn.grid(row=5, column=0, ipady=2)

search(78209)
root.mainloop()
