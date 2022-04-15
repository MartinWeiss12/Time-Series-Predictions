#!/usr/bin/env python3
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error 
from sklearn.svm import SVR

#data import
credentialsCSV = pd.read_csv(r'/Users/martinweiss/Desktop/Python/Brivo DS/ShireData/credentials.csv') #CHANGE TO YOUR PATH
doorsCSV = pd.read_csv(r'/Users/martinweiss/Desktop/Python/Brivo DS/ShireData/doors.csv') #CHANGE TO YOUR PATH
eventTypesCSV = pd.read_csv(r'/Users/martinweiss/Desktop/Python/Brivo DS/ShireData/event_types.csv') #CHANGE TO YOUR PATH
eventLogCSV = pd.read_csv(r'/Users/martinweiss/Desktop/Python/Brivo DS/ShireData/events_log.csv') #CHANGE TO YOUR PATH
schedulesCSV = pd.read_csv(r'/Users/martinweiss/Desktop/Python/Brivo DS/ShireData/schedules.csv') #CHANGE TO YOUR PATH
sitesCSV = pd.read_csv(r'/Users/martinweiss/Desktop/Python/Brivo DS/ShireData/sites.csv') #CHANGE TO YOUR PATH
usersCSV = pd.read_csv(r'/Users/martinweiss/Desktop/Python/Brivo DS/ShireData/users.csv') #CHANGE TO YOUR PATH

usersLength = len(usersCSV)
userInfo = {}

for i in range (usersLength):	
	usersList = usersCSV['name'].tolist()
	users = np.array(usersList)
	userName = users[i]
	userIDList = usersCSV['id'].tolist()
	userIDs = np.array(userIDList)
	userID = userIDs[i]
	userInfo[userName.format(i)] = userID
userIDKeys = list(userInfo.keys())

for a, b in userInfo.items():
	userCount = 1	
	
for c, d in userInfo.items():
	userNameID = "userNameID" 
	userCount = userCount + 1
	userNameID = userNameID + str(userCount)
	userNameID = userInfo[c]
	
userDoorOpenList = eventLogCSV['event_type_id'].tolist()
userDoorOpenArray = np.array(userDoorOpenList)
userDoorOpen = userDoorOpenArray[i]
eventsLogLength =  len(eventLogCSV)	
userIDTimeInList = eventLogCSV['user_id'].tolist()
userIDTimeInAray = np.array(userIDTimeInList)
userIDTimeIn = userIDTimeInAray[i]
enterTimesList = eventLogCSV['event_time'].tolist()
enterTimesArray = np.array(enterTimesList)		
enterTimes = enterTimesArray[i]
count = 1
earlyBirdFrodo = 0
earlyBirdAragorn = 0
earlyBirdGandalf = 0
earlyBirdLegolas = 0
earlyBirdArwen = 0
earlyBirdGimli = 0
earlyBirdBilbo = 0
earlyBirdEverard = 0
nightOwlFrodo = 0
nightOwlAragorn = 0
nightOwlGandalf = 0
nightOwlLegolas = 0
nightOwlArwen = 0
nightOwlGimli = 0
nightOwlBilbo = 0
nightOwlEverard = 0
frodoWeekday = []
aragornWeekday = []
gandalfWeekday = []
legolasWeekday = []
arwenWeekday = []
gimliWeekday = []
bilboWeekday = []
everardWeekday = []
weekdaysArray = ["Sunday","Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday"]
frodoCount = 0
aragornCount = 0
gandalfCount = 0
legolasCount = 0
arwenCount = 0
gimliCount = 0
bilboCount = 0
everardCount = 0
frodoCountList= []
aragornCountList = []
gandalfCountList = []
legolasCountList = []
arwenCountList = []
gimliCountList = []
bilboCountList = []
everardCountList = []
frodoTimeList = []
aragornTimeList= []
gandalfTimeList = []
legolasTimeList = []
arwenTimeList= []
gimliTimeList = []
bilboTimeList = []
everardTimeList = []

for j in range (eventsLogLength):
	doorOpen = "doorOpen" 
	doorOpen = doorOpen + str(count)
	doorOpen = userDoorOpenArray[j]	
	doorOpen = doorOpen
	eventYear = "evenYear" 
	eventYear = eventYear + str(count)
	eventYear = enterTimesArray[j]	
	eventYear = eventYear[0:4]	
	eventYear = int(eventYear)
	eventDay = "eventDay" 	
	eventDay = eventDay + str(count)
	eventDay = enterTimesArray[j]
	eventDay = eventDay[8:10]
	eventDay = int(eventDay)
	eventMonth = "eventMonth" 
	eventMonth = eventMonth + str(count)
	eventMonth = enterTimesArray[j]
	eventMonth = eventMonth[5:7]
	eventMonth = int(eventMonth)
	eventTime = "eventTime" 
	count = count + 1
	eventTime = eventTime + str(count)
	eventTime = enterTimesArray[j]
	enterHour = eventTime[11:13]
	userIDInFile = "userIDInFile" 
	userIDInFile = userIDInFile + str(count)
	userIDInFile = userIDTimeInAray[j]
	leapYearArray = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	eventYear -= eventMonth < 3
	
	if (userIDInFile == (userInfo[userIDKeys[0]])):
		while(doorOpen == 0):
			frodoWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)
			frodoCount = frodoCount + 1
			frodoCountList.append(frodoCount)
			frodoTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:
				nightOwlFrodo = nightOwlFrodo + 1
			else:
				earlyBirdFrodo = earlyBirdFrodo + 1	
			break
				
	if (userIDInFile == (userInfo[userIDKeys[1]])):
		while(doorOpen == 0):
			aragornWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)	
			aragornCount = aragornCount + 1
			aragornCountList.append(aragornCount)
			aragornTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:
				nightOwlAragorn = nightOwlAragorn + 1
			else:
				earlyBirdAragorn = earlyBirdAragorn + 1	
			break
			
	if (userIDInFile == (userInfo[userIDKeys[2]])):
		while(doorOpen == 0):
			gandalfWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)			
			gandalfCount = gandalfCount + 1	
			gandalfCountList.append(gandalfCount)
			gandalfTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:				
				nightOwlGandalf = nightOwlGandalf + 1
			else:
				earlyBirdGandalf = earlyBirdGandalf + 1	
			break
				
	if (userIDInFile == (userInfo[userIDKeys[3]])):
		while(doorOpen == 0):
			legolasWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)
			legolasCount = legolasCount + 1
			legolasCountList.append(legolasCount)
			legolasTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:
				nightOwlLegolas = nightOwlLegolas + 1
			else:
				earlyBirdLegolas = earlyBirdLegolas + 1
			break
		
	if (userIDInFile == (userInfo[userIDKeys[4]])):
		while(doorOpen == 0):
			arwenWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)
			arwenCount = arwenCount + 1
			arwenCountList.append(arwenCount)
			arwenTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:
				nightOwlArwen = nightOwlArwen + 1
			else:
				earlyBirdArwen = earlyBirdArwen + 1
			break
		
	if (userIDInFile == (userInfo[userIDKeys[5]])):
		while(doorOpen == 0):
			gimliWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)
			gimliCount = gimliCount + 1
			gimliCountList.append(gimliCount)
			gimliTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:
				nightOwlGimli = nightOwlGimli + 1
			else:
				earlyBirdGimli = earlyBirdGimli + 1
			break
		
	if (userIDInFile == (userInfo[userIDKeys[6]])):
		while(doorOpen == 0):
			bilboWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)
			bilboCount = bilboCount + 1
			bilboCountList.append(bilboCount)
			bilboTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:
				nightOwlBilbo = nightOwlBilbo + 1
			else:
				earlyBirdBilbo = earlyBirdBilbo + 1
			break
			
	if (userIDInFile == (userInfo[userIDKeys[7]])):
		while(doorOpen == 0):
			everardWeekday.append((eventYear + int(eventYear/4) - int(eventYear/100) + int(eventYear/400) +  leapYearArray[eventMonth - 1] + eventDay) % 7)
			everardCount = everardCount + 1
			everardCountList.append(everardCount)
			everardTimeList.append(enterHour)
			if enterHour in ['17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05']:
				nightOwlEverard = nightOwlEverard + 1
			else:
				earlyBirdEverard = earlyBirdEverard + 1
			break

	if (nightOwlFrodo > earlyBirdFrodo):
		earlyBirdBoolFrodo = True
	else:
		earlyBirdBoolFrodo = False
		
	if (nightOwlAragorn > earlyBirdAragorn):
		earlyBirdBoolAragorn = True
	else:
		earlyBirdBoolAragorn = False
		
	if (nightOwlGandalf > earlyBirdGandalf):
		earlyBirdBoolGandalf = True
	else:
		earlyBirdBoolGandalf = False
		
	if (nightOwlLegolas > earlyBirdLegolas):
		earlyBirdBoolLegolas = True
	else:
		earlyBirdBoolLegolas = False
		
	if (nightOwlArwen > earlyBirdArwen):
		earlyBirdBoolArwen = True
	else:
		earlyBirdBoolArwen = False
		
	if (nightOwlGimli > earlyBirdGimli):
		earlyBirdBoolGimli = True
	else:
		earlyBirdBoolGimli= False
		
	if (nightOwlBilbo > earlyBirdBilbo):
		earlyBirdBoolBilbo = True
	else:
		earlyBirdBoolBilbo = False
	
	if (nightOwlEverard > earlyBirdEverard):
		earlyBirdBoolEverard = True
	else:
		earlyBirdBoolEverard = False
			
frodoSunday = frodoWeekday.count(0)
frodoMonday = frodoWeekday.count(1)
frodoTuesday = frodoWeekday.count(2)
frodoWednesday = frodoWeekday.count(3)
frodoThusday = frodoWeekday.count(4)
frodoFriday = frodoWeekday.count(5)
frodoSaturday = frodoWeekday.count(6)
frodoWeekdays = [frodoSunday, frodoMonday, frodoTuesday, frodoWednesday, frodoThusday, frodoFriday, frodoSaturday]
frodoWeekdays.sort(reverse=True)
frodoSundayIndex = frodoWeekdays.index(frodoSunday)
frodoMondayIndex = frodoWeekdays.index(frodoMonday)
frodoTuesdayIndex = frodoWeekdays.index(frodoTuesday)
frodoWednesdayIndex = frodoWeekdays.index(frodoWednesday)
frodoThursdayIndex = frodoWeekdays.index(frodoThusday) + 1 #Had to add 1 to Thursday index becuase Thursday count = Saturday count
frodoFridayIndex = frodoWeekdays.index(frodoFriday)
frodoSaturdayIndex = frodoWeekdays.index(frodoSaturday)
frodoWeekdaysSorted = [0,0,0,0,0,0,0]
frodoWeekdayIndexes = [frodoSundayIndex,frodoMondayIndex, frodoTuesdayIndex, frodoWednesdayIndex, frodoThursdayIndex, frodoFridayIndex, frodoSaturdayIndex]
for (index, replacement) in zip(frodoWeekdayIndexes, weekdaysArray):
	frodoWeekdaysSorted[index] = replacement
print("Frodo's five most popular days of the week are as follows: " + str(frodoWeekdaysSorted[0:5]))

aragornSunday = aragornWeekday.count(0)
aragornMonday = aragornWeekday.count(1)
aragornTuesday = aragornWeekday.count(2)
aragornWednesday = aragornWeekday.count(3)
aragornThusday = aragornWeekday.count(4)
aragornFriday = aragornWeekday.count(5)
aragornSaturday = aragornWeekday.count(6)
aragornWeekdays = [aragornSunday, aragornMonday, aragornTuesday, aragornWednesday, aragornThusday, aragornFriday, aragornSaturday]
aragornWeekdays.sort(reverse=True)
aragornSundayIndex = aragornWeekdays.index(aragornSunday)
aragornMondayIndex = aragornWeekdays.index(aragornMonday)
aragornTuesdayIndex = aragornWeekdays.index(aragornTuesday)
aragornWednesdayIndex = aragornWeekdays.index(aragornWednesday)
aragornThursdayIndex = aragornWeekdays.index(aragornThusday)
aragornFridayIndex = aragornWeekdays.index(aragornFriday)
aragornSaturdayIndex = aragornWeekdays.index(aragornSaturday)
aragornWeekdaysSorted = [0,0,0,0,0,0,0]
aragornWeekdayIndexes = [aragornSundayIndex,aragornMondayIndex, aragornTuesdayIndex, aragornWednesdayIndex, aragornThursdayIndex, aragornFridayIndex, aragornSaturdayIndex]
for (index, replacement) in zip(aragornWeekdayIndexes, weekdaysArray):
	aragornWeekdaysSorted[index] = replacement
print("Aragorn's five most popular days of the week are as follows: " + str(aragornWeekdaysSorted[0:5]))

gandalfSunday = gandalfWeekday.count(0)
gandalfMonday = gandalfWeekday.count(1)
gandalfTuesday = gandalfWeekday.count(2)
gandalfWednesday = gandalfWeekday.count(3)
gandalfThusday = gandalfWeekday.count(4)
gandalfFriday = gandalfWeekday.count(5)
gandalfSaturday = gandalfWeekday.count(6)
gandalfWeekdays = [gandalfSunday, gandalfMonday, gandalfTuesday, gandalfWednesday, gandalfThusday, gandalfFriday, gandalfSaturday]
gandalfWeekdays.sort(reverse=True)
gandalfSundayIndex = gandalfWeekdays.index(gandalfSunday)
gandalfMondayIndex = gandalfWeekdays.index(gandalfMonday)
gandalfTuesdayIndex = gandalfWeekdays.index(gandalfTuesday)
gandalfWednesdayIndex = gandalfWeekdays.index(gandalfWednesday)
gandalfThursdayIndex = gandalfWeekdays.index(gandalfThusday)
gandalfFridayIndex = gandalfWeekdays.index(gandalfFriday)
gandalfSaturdayIndex = gandalfWeekdays.index(gandalfSaturday)
gandalfWeekdaysSorted = [0,0,0,0,0,0,0]
gandalfWeekdayIndexes = [gandalfSundayIndex,gandalfMondayIndex, gandalfTuesdayIndex, gandalfWednesdayIndex, gandalfThursdayIndex, gandalfFridayIndex, gandalfSaturdayIndex]
for (index, replacement) in zip(gandalfWeekdayIndexes, weekdaysArray):
	gandalfWeekdaysSorted[index] = replacement
print("Gandalf's five most popular days of the week are as follows: " + str(gandalfWeekdaysSorted[0:5]))

legolasSunday = legolasWeekday.count(0)
legolasMonday = legolasWeekday.count(1)
legolasTuesday = legolasWeekday.count(2)
legolasWednesday = legolasWeekday.count(3)
legolasThusday = legolasWeekday.count(4)
legolasFriday = legolasWeekday.count(5)
legolasSaturday = legolasWeekday.count(6)
legolasWeekdays = [legolasSunday, legolasMonday, legolasTuesday, legolasWednesday, legolasThusday, legolasFriday, legolasSaturday]
legolasWeekdays.sort(reverse=True)
legolasSundayIndex = legolasWeekdays.index(legolasSunday)
legolasMondayIndex = legolasWeekdays.index(legolasMonday) + 1
legolasTuesdayIndex = legolasWeekdays.index(legolasTuesday)
legolasWednesdayIndex = legolasWeekdays.index(legolasWednesday)
legolasThursdayIndex = legolasWeekdays.index(legolasThusday)
legolasFridayIndex = legolasWeekdays.index(legolasFriday)
legolasSaturdayIndex = legolasWeekdays.index(legolasSaturday)
legolasWeekdaysSorted = [0,0,0,0,0,0,0]
legolasWeekdayIndexes = [legolasSundayIndex,legolasMondayIndex, legolasTuesdayIndex, legolasWednesdayIndex, legolasThursdayIndex, legolasFridayIndex, legolasSaturdayIndex]
for (index, replacement) in zip(legolasWeekdayIndexes, weekdaysArray):
	legolasWeekdaysSorted[index] = replacement
print("Legolas's five most popular days of the week are as follows: " + str(legolasWeekdaysSorted[0:5]))

arwenSunday = arwenWeekday.count(0)
arwenMonday = arwenWeekday.count(1)
arwenTuesday = arwenWeekday.count(2)
arwenWednesday = arwenWeekday.count(3)
arwenThusday = arwenWeekday.count(4)
arwenFriday = arwenWeekday.count(5)
arwenSaturday = arwenWeekday.count(6)
arwenWeekdays = [arwenSunday, arwenMonday, arwenTuesday, arwenWednesday, arwenThusday, arwenFriday, arwenSaturday]
arwenWeekdays.sort(reverse=True)
arwenSundayIndex = arwenWeekdays.index(arwenSunday)
arwenMondayIndex = arwenWeekdays.index(arwenMonday)
arwenTuesdayIndex = arwenWeekdays.index(arwenTuesday)
arwenWednesdayIndex = arwenWeekdays.index(arwenWednesday)
arwenThursdayIndex = arwenWeekdays.index(arwenThusday)
arwenFridayIndex = arwenWeekdays.index(arwenFriday)
arwenSaturdayIndex = arwenWeekdays.index(arwenSaturday)
arwenWeekdaysSorted = [0,0,0,0,0,0,0]
arwenWeekdayIndexes = [arwenSundayIndex,arwenMondayIndex, arwenTuesdayIndex, arwenWednesdayIndex, arwenThursdayIndex, arwenFridayIndex, arwenSaturdayIndex]
for (index, replacement) in zip(arwenWeekdayIndexes, weekdaysArray):
	arwenWeekdaysSorted[index] = replacement
print("Arwen's five most popular days of the week are as follows: " + str(arwenWeekdaysSorted[0:5]))

gimliSunday = gimliWeekday.count(0)
gimliMonday = gimliWeekday.count(1)
gimliTuesday = gimliWeekday.count(2)
gimliWednesday = gimliWeekday.count(3)
gimliThusday = gimliWeekday.count(4)
gimliFriday = gimliWeekday.count(5)
gimliSaturday = gimliWeekday.count(6)
gimliWeekdays = [gimliSunday, gimliMonday, gimliTuesday, gimliWednesday, gimliThusday, gimliFriday, gimliSaturday]
gimliWeekdays.sort(reverse=True)
gimliSundayIndex = gimliWeekdays.index(gimliSunday)
gimliMondayIndex = gimliWeekdays.index(gimliMonday)
gimliTuesdayIndex = gimliWeekdays.index(gimliTuesday)
gimliWednesdayIndex = gimliWeekdays.index(gimliWednesday)
gimliThursdayIndex = gimliWeekdays.index(gimliThusday)
gimliFridayIndex = gimliWeekdays.index(gimliFriday)
gimliSaturdayIndex = gimliWeekdays.index(gimliSaturday)
gimliWeekdaysSorted = [0,0,0,0,0,0,0]
gimliWeekdayIndexes = [gimliSundayIndex,gimliMondayIndex, gimliTuesdayIndex, gimliWednesdayIndex, gimliThursdayIndex, gimliFridayIndex, gimliSaturdayIndex]
for (index, replacement) in zip(gimliWeekdayIndexes, weekdaysArray):
	gimliWeekdaysSorted[index] = replacement
print("Gimli's five most popular days of the week are as follows: " + str(gimliWeekdaysSorted[0:5]))

bilboSunday = bilboWeekday.count(0)
bilboMonday = bilboWeekday.count(1)
bilboTuesday = bilboWeekday.count(2)
bilboWednesday = bilboWeekday.count(3)
bilboThusday = bilboWeekday.count(4)
bilboFriday = bilboWeekday.count(5)
bilboSaturday = bilboWeekday.count(6)
bilboWeekdays = [bilboSunday, bilboMonday, bilboTuesday, bilboWednesday, bilboThusday, bilboFriday, bilboSaturday]
bilboWeekdays.sort(reverse=True)
bilboSundayIndex = bilboWeekdays.index(bilboSunday)
bilboMondayIndex = bilboWeekdays.index(bilboMonday)
bilboTuesdayIndex = bilboWeekdays.index(bilboTuesday)
bilboWednesdayIndex = bilboWeekdays.index(bilboWednesday)
bilboThursdayIndex = bilboWeekdays.index(bilboThusday)
bilboFridayIndex = bilboWeekdays.index(bilboFriday)
bilboSaturdayIndex = bilboWeekdays.index(bilboSaturday)
bilboWeekdaysSorted = [0,0,0,0,0,0,0]
bilboWeekdayIndexes = [bilboSundayIndex,bilboMondayIndex, bilboTuesdayIndex, bilboWednesdayIndex, bilboThursdayIndex, bilboFridayIndex, bilboSaturdayIndex]
for (index, replacement) in zip(bilboWeekdayIndexes, weekdaysArray):
	bilboWeekdaysSorted[index] = replacement
print("Bilbo's five most popular days of the week are as follows: " + str(bilboWeekdaysSorted[0:5]))

everardSunday = everardWeekday.count(0)
everardMonday = everardWeekday.count(1)
everardTuesday = everardWeekday.count(2)
everardWednesday = everardWeekday.count(3)
everardThusday = everardWeekday.count(4)
everardFriday = everardWeekday.count(5)
everardSaturday = everardWeekday.count(6)
everardWeekdays = [everardSunday, everardMonday, everardTuesday, everardWednesday, everardThusday, everardFriday, everardSaturday]
everardWeekdays.sort(reverse=True)
everardSundayIndex = everardWeekdays.index(everardSunday)
everardMondayIndex = everardWeekdays.index(everardMonday)
everardTuesdayIndex = everardWeekdays.index(everardTuesday)
everardWednesdayIndex = everardWeekdays.index(everardWednesday)
everardThursdayIndex = everardWeekdays.index(everardThusday)
everardFridayIndex = everardWeekdays.index(everardFriday)
everardSaturdayIndex = everardWeekdays.index(everardSaturday)
everardWeekdaysSorted = [0,0,0,0,0,0,0]
everardWeekdayIndexes = [everardSundayIndex,everardMondayIndex, everardTuesdayIndex, everardWednesdayIndex, everardThursdayIndex, everardFridayIndex, everardSaturdayIndex]
for (index, replacement) in zip(everardWeekdayIndexes, weekdaysArray):
	everardWeekdaysSorted[index] = replacement
print("Everard's five most popular days of the week are as follows: " + str(everardWeekdaysSorted[0:5]))

print("\nIs Frodo a night owl?: " + str(earlyBirdBoolFrodo))
print("Is Aragorn a night owl?: " + str(earlyBirdBoolAragorn))
print("Is Gandalf a night owl?: " + str(earlyBirdBoolGandalf))
print("Is Legolas a night owl?: " + str(earlyBirdBoolLegolas))
print("Is Arwen a night owl?: " + str(earlyBirdBoolArwen))
print("Is Gimli a night owl?: " + str(earlyBirdBoolGimli))
print("Is Bilbo a night owl?: " + str(earlyBirdBoolBilbo))
print("Is Everard a night owl?: " + str(earlyBirdBoolEverard))

frodoTimeList = [int(numeric_string) for numeric_string in frodoTimeList]
frodoTimeArray = np.array(frodoTimeList)
frodoCountArray = np.array(frodoCountList)
frodoTimeArray = frodoTimeArray.flatten()
frodoCountArray = frodoCountArray.flatten()
frodoCountArray = frodoCountArray.reshape(-1, 1)
frodoPredictDay = [[frodoCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
frodoRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
frodoRBF_SVR.fit(frodoCountArray, frodoTimeArray)
print("\nOn day " + str(frodoPredictDay) + " Frodo is expected to arrive next at:", frodoRBF_SVR.predict(frodoPredictDay))

xFrodoTrain, xFrodoTest, yFrodoTrain, yFrodoTest = train_test_split(frodoCountArray, frodoTimeArray, test_size = 0.075)#1/13 (13 weeks, assume pattern is repeated weekly)
frodoRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
frodoRegressor.fit(xFrodoTrain, yFrodoTrain)
frodoTrainingPrediction = frodoRegressor.predict(xFrodoTrain)
frodoTrainingMSE = mean_squared_error(yFrodoTrain, frodoTrainingPrediction) 
frodoTrainingRMSE = sqrt(frodoTrainingMSE)/60
print("Frodo Training Mean Squared Error: " + str(frodoTrainingRMSE))
yPredictionFrodo = frodoRegressor.predict(xFrodoTest) 
frodoTestMSE = mean_squared_error(yFrodoTest, yPredictionFrodo)
frodoTestMAE = mean_absolute_error(yFrodoTest, yPredictionFrodo)
frodoTestRMSE = sqrt(frodoTestMSE)/60
frodoTestMMSE = sqrt(frodoTestMAE)/60
print(f"Frodo Test Root Mean Squared Error:  {frodoTestRMSE}")
print(f"Frodo Test Root Mean Absolute Error: {frodoTestMMSE}")
xaxisFrodo = range(len(yFrodoTest))
frodoPlot = plt.figure(1)
plt.plot(xaxisFrodo, yFrodoTest, linewidth = 1, label = "Actual")
plt.plot(xaxisFrodo, yPredictionFrodo, linewidth = 1.1, label = "Predicted")
plt.title("Frodo Test vs Frodo Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

aragornTimeList = [int(numeric_string) for numeric_string in aragornTimeList]
aragornTimeArray = np.array(aragornTimeList)
aragornCountArray = np.array(aragornCountList)
aragornTimeArray = aragornTimeArray.flatten()
aragornCountArray = aragornCountArray.flatten()
aragornCountArray = aragornCountArray.reshape(-1, 1)
aragornPredictDay = [[aragornCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
aragornRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
aragornRBF_SVR.fit(aragornCountArray, aragornTimeArray)
print("\nOn day " + str(aragornPredictDay) + " Aragorn is expected to arrive next at:", aragornRBF_SVR.predict(aragornPredictDay))
xAragornTrain, xAragornTest, yAragornTrain, yAragornTest = train_test_split(aragornCountArray, aragornTimeArray, test_size = 0.075)
aragornRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
aragornRegressor.fit(xAragornTrain, yAragornTrain)
aragornTrainingPrediction = aragornRegressor.predict(xAragornTrain)
aragornTrainingMSE = mean_squared_error(yAragornTrain, aragornTrainingPrediction) 
aragornTrainingRMSE = sqrt(aragornTrainingMSE)/60
print("Aragorn Training Mean Squared Error: " + str(aragornTrainingRMSE))
yPredictionAragorn = aragornRegressor.predict(xAragornTest) 
aragornTestMSE = mean_squared_error(yAragornTest, yPredictionAragorn)
aragornTestMAE = mean_absolute_error(yAragornTest, yPredictionAragorn)
aragornTestRMSE = sqrt(aragornTestMSE)/60
aragornTestMMSE = sqrt(aragornTestMAE)/60
print(f"Aragorn Test Root Mean Squared Error:  {aragornTestRMSE}")
print(f"Aragorn Test Root Mean Absolute Error: {aragornTestMMSE}")
xAxisAragorn = range(len(yAragornTest))
aragornPlot = plt.figure(2)
plt.plot(xAxisAragorn, yAragornTest, linewidth = 1, label = "Actual")
plt.plot(xAxisAragorn, yPredictionAragorn, linewidth = 1.1, label = "Predicted")
plt.title("Aragorn Test vs Aragorn Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

gandalfTimeList = [int(numeric_string) for numeric_string in gandalfTimeList]
gandalfTimeArray = np.array(gandalfTimeList)
gandalfCountArray = np.array(gandalfCountList)
gandalfTimeArray = gandalfTimeArray.flatten()
gandalfCountArray = gandalfCountArray.flatten()
gandalfCountArray = gandalfCountArray.reshape(-1, 1)
gandalfPredictDay = [[gandalfCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
gandalfRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
gandalfRBF_SVR.fit(gandalfCountArray, gandalfTimeArray)
print("\nOn day " + str(gandalfPredictDay) + " Gandalf is expected to arrive next at:", gandalfRBF_SVR.predict(gandalfPredictDay))
xGandalfTrain, xGandalfTest, yGandalfTrain, yGandalfTest = train_test_split(gandalfCountArray, gandalfTimeArray, test_size = 0.075)
gandalfRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
gandalfRegressor.fit(xGandalfTrain, yGandalfTrain)
gandalfTrainingPrediction = gandalfRegressor.predict(xGandalfTrain)
gandalfTrainingMSE = mean_squared_error(yGandalfTrain, gandalfTrainingPrediction) 
gandalfTrainingRMSE = sqrt(gandalfTrainingMSE)/60
print("Gandalf Training Mean Squared Error: " + str(gandalfTrainingRMSE))
yPredictionGandalf = gandalfRegressor.predict(xGandalfTest) 
gandalfTestMSE = mean_squared_error(yGandalfTest, yPredictionGandalf)
gandalfTestMAE = mean_absolute_error(yGandalfTest, yPredictionGandalf)
gandalfTestRMSE = sqrt(gandalfTestMSE)/60
gandalfTestMMSE = sqrt(gandalfTestMAE)/60
print(f"Gandalf Test Root Mean Squared Error:  {gandalfTestRMSE}")
print(f"Gandalf Test Root Mean Absolute Error: {gandalfTestMMSE}")
xAxisGandalf = range(len(yGandalfTest))
gandalfPlot = plt.figure(3)
plt.plot(xAxisGandalf, yGandalfTest, linewidth = 1, label = "Actual")
plt.plot(xAxisGandalf, yPredictionGandalf, linewidth = 1.1, label = "Predicted")
plt.title("Gandalf Test vs Gandalf Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

legolasTimeList = [int(numeric_string) for numeric_string in legolasTimeList]
legolasTimeArray = np.array(legolasTimeList)
legolasCountArray = np.array(legolasCountList)
legolasTimeArray = legolasTimeArray.flatten()
legolasCountArray = legolasCountArray.flatten()
legolasCountArray = legolasCountArray.reshape(-1, 1)
legolasPredictDay = [[legolasCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
legolasRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
legolasRBF_SVR.fit(legolasCountArray, legolasTimeArray)
print("\nOn day " + str(legolasPredictDay) + " Legolas is expected to arrive next at:", legolasRBF_SVR.predict(legolasPredictDay))
xLegolasTrain, xLegolasTest, yLegolasTrain, yLegolasTest = train_test_split(legolasCountArray, legolasTimeArray, test_size = 0.075)
legolasRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
legolasRegressor.fit(xLegolasTrain, yLegolasTrain)
legolasTrainingPrediction = legolasRegressor.predict(xLegolasTrain)
legolasTrainingMSE = mean_squared_error(yLegolasTrain, legolasTrainingPrediction) 
legolasTrainingRMSE = sqrt(legolasTrainingMSE)/60
print("Legolas Training Mean Squared Error: " + str(legolasTrainingRMSE))
yPredictionLegolas = legolasRegressor.predict(xLegolasTest) 
legolasTestMSE = mean_squared_error(yLegolasTest, yPredictionLegolas)
legolasTestMAE = mean_absolute_error(yLegolasTest, yPredictionLegolas)
legolasTestRMSE = sqrt(legolasTestMSE)/60
legolasTestMMSE = sqrt(legolasTestMAE)/60
print(f"Legolas Test Root Mean Squared Error:  {legolasTestRMSE}")
print(f"Legolas Test Root Mean Absolute Error: {legolasTestMMSE}")
xAxisLegolas = range(len(yLegolasTest))
legolasPlot = plt.figure(4)
plt.plot(xAxisLegolas, yLegolasTest, linewidth = 1, label = "Actual")
plt.plot(xAxisLegolas, yPredictionLegolas, linewidth = 1.1, label = "Predicted")
plt.title("Legolas Test vs Legolas Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

arwenTimeList = [int(numeric_string) for numeric_string in arwenTimeList]
arwenTimeArray = np.array(arwenTimeList)
arwenCountArray = np.array(arwenCountList)
arwenTimeArray = arwenTimeArray.flatten()
arwenCountArray = arwenCountArray.flatten()
arwenCountArray = arwenCountArray.reshape(-1, 1)
arwenPredictDay = [[arwenCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
arwenRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
arwenRBF_SVR.fit(arwenCountArray, arwenTimeArray)
print("\nOn day " + str(arwenPredictDay) + " Arwen is expected to arrive next at:", arwenRBF_SVR.predict(arwenPredictDay))
xArwenTrain, xArwenTest, yArwenTrain, yArwenTest = train_test_split(arwenCountArray, arwenTimeArray, test_size = 0.075)
arwenRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
arwenRegressor.fit(xArwenTrain, yArwenTrain)
arwenTrainingPrediction = arwenRegressor.predict(xArwenTrain)
arwenTrainingMSE = mean_squared_error(yArwenTrain, arwenTrainingPrediction) 
arwenTrainingRMSE = sqrt(arwenTrainingMSE)/60
print("Arwen training Mean Squared Error: " + str(arwenTrainingRMSE))
yPredictionArwen = arwenRegressor.predict(xArwenTest) 
arwenTestMSE = mean_squared_error(yArwenTest, yPredictionArwen)
arwenTestMAE = mean_absolute_error(yArwenTest, yPredictionArwen)
arwenTestRMSE = sqrt(arwenTestMSE)/60
arwenTestMMSE = sqrt(arwenTestMAE)/60
print(f"Arwen Test Root Mean Squared Error:  {arwenTestRMSE}")
print(f"Arwen Test Root Mean Absolute Error: {arwenTestMMSE}")
xAxisArwen = range(len(yArwenTest))
arwenfPlot = plt.figure(5)
plt.plot(xAxisArwen, yArwenTest, linewidth = 1, label = "Actual")
plt.plot(xAxisArwen, yPredictionArwen, linewidth = 1.1, label = "Predicted")
plt.title("Arwen Test vs Arwen Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

gimliTimeList = [int(numeric_string) for numeric_string in gimliTimeList]
gimliTimeArray = np.array(gimliTimeList)
gimliCountArray = np.array(gimliCountList)
gimliTimeArray = gimliTimeArray.flatten()
gimliCountArray = gimliCountArray.flatten()
gimliCountArray = gimliCountArray.reshape(-1, 1)
gimliPredictDay = [[gimliCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
gimliRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
gimliRBF_SVR.fit(gimliCountArray, gimliTimeArray)
print("\nOn day " + str(gimliPredictDay) + " Gimli is expected to arrive next at:", gimliRBF_SVR.predict(gimliPredictDay))
xGimliTrain, xGimliTest, yGimliTrain, yGimliTest = train_test_split(gimliCountArray, gimliTimeArray, test_size = 0.075)
gimliRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
gimliRegressor.fit(xGimliTrain, yGimliTrain)
gimliTrainingPrediction = gimliRegressor.predict(xGimliTrain)
gimliTrainingMSE = mean_squared_error(yGimliTrain, gimliTrainingPrediction) 
gimliTrainingRMSE = sqrt(gimliTrainingMSE)/60
print("Gimli training Mean Squared Error: " + str(gimliTrainingRMSE))
yPredictionGimli = gimliRegressor.predict(xGimliTest) 
gimliTestMSE = mean_squared_error(yGimliTest, yPredictionGimli)
gimliTestMAE = mean_absolute_error(yGimliTest, yPredictionGimli)
gimliTestRMSE = sqrt(gimliTestMSE)/60
gimliTestMMSE = sqrt(gimliTestMAE)/60
print(f"Gimli Test Root Mean Squared Error:  {gimliTestRMSE}")
print(f"Gimli Test Root Mean Absolute Error: {gimliTestMMSE}")
xAxisGimli = range(len(yGimliTest))
gimliPlot = plt.figure(6)
plt.plot(xAxisGimli, yGimliTest, linewidth = 1, label = "Actual")
plt.plot(xAxisGimli, yPredictionGimli, linewidth = 1.1, label = "Predicted")
plt.title("Gimli Test vs Gimli Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

bilboTimeList = [int(numeric_string) for numeric_string in bilboTimeList]
bilboTimeArray = np.array(bilboTimeList)
bilboCountArray = np.array(bilboCountList)
bilboTimeArray = bilboTimeArray.flatten()
bilboCountArray = bilboCountArray.flatten()
bilboCountArray = bilboCountArray.reshape(-1, 1)
bilboPredictDay = [[bilboCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
bilboRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
bilboRBF_SVR.fit(bilboCountArray, bilboTimeArray)
print("\nOn day " + str(bilboPredictDay) + " Bilbo is expected to arrive next at:", bilboRBF_SVR.predict(bilboPredictDay))
xBilboTrain, xBilboTest, yBilboTrain, yBilboTest = train_test_split(bilboCountArray, bilboTimeArray, test_size = 0.075)
bilboRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
bilboRegressor.fit(xBilboTrain, yBilboTrain)
bilboTrainingPrediction = bilboRegressor.predict(xBilboTrain)
bilboTrainingMSE = mean_squared_error(yBilboTrain, bilboTrainingPrediction) 
bilboTrainingRMSE = sqrt(bilboTrainingMSE)/60
print("Bilbo training Mean Squared Error: " + str(bilboTrainingRMSE))
yPredictionBilbo = bilboRegressor.predict(xBilboTest) 
bilboTestMSE = mean_squared_error(yBilboTest, yPredictionBilbo)
bilboTestMAE = mean_absolute_error(yBilboTest, yPredictionBilbo)
bilboTestRMSE = sqrt(bilboTestMSE)/60
bilboTestMMSE = sqrt(bilboTestMAE)/60
print(f"Bilbo Test Root Mean Squared Error:  {bilboTestRMSE}")
print(f"Bilbo Test Root Mean Absolute Error: {bilboTestMMSE}")
xAxisBilbo = range(len(yBilboTest))
bilboPlot = plt.figure(7)
plt.plot(xAxisBilbo, yBilboTest, linewidth = 1, label = "Actual")
plt.plot(xAxisBilbo, yPredictionBilbo, linewidth = 1.1, label = "Predicted")
plt.title("Bilbo Test vs Bilbo Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

everardTimeList = [int(numeric_string) for numeric_string in everardTimeList]
everardTimeArray = np.array(everardTimeList)
everardCountArray = np.array(everardCountList)
everardTimeArray = everardTimeArray.flatten()
everardCountArray = everardCountArray.flatten()
everardCountArray = everardCountArray.reshape(-1, 1)
everardPredictDay = [[everardCount + 1]] #adjust to check any date. Ex nameCount = most recent check in date. 
everardRBF_SVR = SVR(kernel = 'rbf', C = 1000.0, gamma = 0.1)
everardRBF_SVR.fit(everardCountArray, everardTimeArray)
print("\nOn day " + str(everardPredictDay) + " Everard is expected to arrive next at:", everardRBF_SVR.predict(everardPredictDay))
xEverardTrain, xEverardTest, yEverardTrain, yEverardTest = train_test_split(everardCountArray, everardTimeArray, test_size = 0.075)
everardRegressor = RandomForestRegressor(n_estimators = 128, random_state = 2, criterion = 'absolute_error') 
everardRegressor.fit(xEverardTrain, yEverardTrain)
everardTrainingPrediction = everardRegressor.predict(xEverardTrain)
everardTrainingMSE = mean_squared_error(yEverardTrain, everardTrainingPrediction) 
everardTrainingRMSE = sqrt(everardTrainingMSE)/60
print("Everard training Mean Squared Error: " + str(everardTrainingRMSE))
yPredictionEverard = everardRegressor.predict(xEverardTest) 
everardTestMSE = mean_squared_error(yEverardTest, yPredictionEverard)
everardTestMAE = mean_absolute_error(yEverardTest, yPredictionEverard)
everardTestRMSE = sqrt(everardTestMSE)/60
everardTestMMSE = sqrt(everardTestMAE)/60
print(f"Everard Test Root Mean Squared Error:  {everardTestRMSE}")
print(f"Everard Test Root Mean Absolute Error: {everardTestMMSE}")
xAxisEverard = range(len(yEverardTest))
everardPlot = plt.figure(8)
plt.plot(xAxisEverard, yEverardTest, linewidth = 1, label = "Actual")
plt.plot(xAxisEverard, yPredictionEverard, linewidth = 1.1, label = "Predicted")
plt.title("Everard Test vs Everard Predicted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc = 'best', fancybox=True, shadow=True)
plt.grid(True)

plt.show()