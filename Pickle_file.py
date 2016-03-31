import pickle
import re
import Model



def showAllDays():
	if (len(Model.diary) == 0):
		print ("Error! Diary is empty")
	else:
		for i in Model.diary:
			i.displayDayInfo()
			print ("------------------------")
	
def addDay(date, temperature, clouds, pressure):
	for i in Model.diary:
		if i.date == date:
			print("Error! Date already exists")
			break
	else:
		Model.diary.append(Model.CalendarDay(date, temperature, clouds, pressure))

def checkingDate(date):
	if ((date[0] == "1") or (date[0] == "2")):
		p = re.compile(r"^[0-2][0-9][.][01][0-9][.][12][09][0-9][0-9]$")
	else:
		p = re.compile(r"^[03][0-1][.][01][0-9][.][12][09][0-9][0-9]$")
	if p.search(date):
		return 1
	else:
		return 0

def checkingTemperature(temperature):
	a = int(temperature)
	if ((a >= -60) and (a <= 60)):
		return 1
	else:
		return 0

def checkingClouds(clouds):
	reserved_clouds = ['clear', 'sunny', 'cloudy', 'fog', 'rain']
	for i in reserved_clouds:
		if i == clouds:
			return 1
	else:
		return 0

def checkingPressure(pressure):
	a = int(pressure)
	if ((a >= 700) and (a <= 800)):
		return 1
	else:
		return 0