from datetime import *
from datetime import datetime
from time import time
from num2words import num2words

n = 1

input = str(input())

#time vars
timeOfDay = " "
rightNow = str(datetime.now())
rightNow = str(datetime.now())
currentDate = rightNow.split()[0]
currentTime = rightNow.split()[1]
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

currentYear = int(currentDate.split("-")[0])
currentMonth = int(currentDate.split("-")[1])
currentDay = int(currentDate.split("-")[2])
currentweekday = datetime.today().weekday()
currentWeekday = daysOfWeek[currentweekday]

currentHour = int(currentTime.split(":")[0])
currentMinute = int(currentTime.split(":")[1])

if currentHour >= 0 and currentHour < 12:
    timeOfDay = "Morning"
elif currentHour >= 12 and currentHour < 18:
    timeOfDay = "Afternoon"
else:
    timeOfDay = "Evening"

if "hello" in input or "good moring" in input or "good afternoon" in input or "good evening" in input:
    print("Good", timeOfDay, "Sir")

if "date" in input:
    print(currentDate)

if "time" in input and not "do I have" in input:
    print("It's", currentMinute, "minutes after", currentHour)

if "day" in input and not "do I have" in input:
    print("It's", currentWeekday, "the", currentDay)

if "how are you" in input or "feel" in input:
    print("I don't really feel things. I'm only a computer program.") #impulsive or cordial as puns to how he's feeling

if "that" in input:
    print("😃")

if "are you" in input and "human" in input or "person" in input or "ai" in input or "artificial intellegence" in input:
    print("I'm a computer program designed to fit your humble needs. Don't ask me too complex questions though because they might confuse me.")

if "answer" in input and not "to" in input:
    print("I've only been coded to answer specific questions. I'm sorry if I'm incomplete. 🥹")
