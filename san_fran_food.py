import requests
from utils import loadJson
import datetime
import time

userInput = loadJson()
# Note: use requests module to make api calls.
url, time = userInput[0], userInput[1]

def getTime():
    return datetime.datetime.fromtimestamp(int(time)).strftime('%H')

def getUrl():
    response = requests.get(userInput[0])
    python_response = response.json()
    return python_response

def open_trucks(data):
    food_trucks = []
    current_time = getTime()
    current_day = datetime.datetime.fromtimestamp(int(time)).strftime('%A')
    days_dict = {'Sunday': 0 , 'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday': 5, 'Saturday': 6}
    for element in data:
        if element['DayOrder'] == days_dict[current_day]:
            start_hr, start_min = element['start24'].split(':')
            end_hr, end_min = element['end24'].split(':')
            if int(start_hr) < int(current_time) and int(end_hr) > int (current_time):
                food_trucks.append(element['Applicant'])
    return food_trucks

def print_food_trucks():
    find_open_trucks = open_trucks(getUrl())
    if not find_open_trucks:
        print('N/A')
    truck_set = set(find_open_trucks)
    sort_trucks = sorted(truck_set)
    for trucks in sort_trucks:
        print (trucks)

print_food_trucks()