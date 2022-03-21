"""

This is a script to analyze how aware employees are about taking and giving help


There are two behaviors:

a) taking help

b) giving help


Intuition:

If your awareness score for a behavior is

a) more than 100, you think you are doing more of that than other people report

b) less than 100, you are doing more of that behavior than other people report


In general:

a) you want to be in the Goldilocks range of 75-125 for both taking and giving awareness

b) scores below 75 are more harmful than scores above 125 

"""
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta, FR
import requests
import json
import pandas as pd
import conf
from urllib.parse import urljoin

class Employee:
    "Model an employee"

    def __init__(self,firstname,lastname=None):
        "Initializer"
        self.name = firstname + ' ' + lastname if lastname is not None else ''

    def set_giving_awareness(self,own,others):
        "Setup a giving awareness score"
        if others != 0:
            self.giving_awareness = int(own*100/others) 
        else:
            self.giving_awareness = 'N/A'

        #Intuition
        # > 1 --> think they are helping more 

        # < 1 --> not aware enough of how much they help

    def set_taking_awareness(self,own,others):
        "Setup a giving awareness score"
        if others != 0:
            self.taking_awareness = int(own*100/others) 
        else:
            self.taking_awareness = 'N/A'

        #Intuition
        # > 1 --> think they are taking more help than actual

        # < 1 --> not aware enough of how much help they get

    def print_me(self):
        "Print out the details of the user"
        print(self.name[:14], "\t\t", self.giving_awareness, "\t\t", self.taking_awareness)

def get_users():
    "Fetch the users from survey database and convert to dataframe"
    get_user_url = urljoin(conf.URL, 'survey/admin/QElo_users')
    users = requests.get(get_user_url, headers={"User":conf.API_KEY}).json()
    users_data_frame = pd.DataFrame(users)
    return users_data_frame

def fetch_response(date=None):
    "Fetch user response between given dates and convert to dataframe"
    fetch_response_url = urljoin(conf.URL, 'survey/admin/QElo_filter_response') 
    friday_of_current_week = (datetime.now() + relativedelta(weekday=FR(0))).strftime("%Y-%m-%d")
    previous_year = (datetime.now() - relativedelta(months=12)).strftime("%Y-%m-%d") 
    start_date = previous_year
    if date is not None:
        start_date = date

    dates = {"start_date": start_date, "end_date": friday_of_current_week}
    json_dates = json.dumps(dates)
    response= requests.post(fetch_response_url, data=json_dates, headers={"User":conf.API_KEY}).json()
    response_data_frame=pd.DataFrame(response)
    return response_data_frame

def run_awareness_analysis(date=None):
    "Figure out giving and taking help awareness"
    employees= get_users()    
    if date is not None:
        responses = fetch_response(date)    
    else:
        responses = fetch_response()
    print('name \t\t giving_awareness \t taking_awareness')

    for index,row in employees.iterrows():
        if row['active_flag'] != 'Y' or row['first_name'] in ['External','Edward','Shrihari','Kavitha']:
            continue
        emp_obj = Employee(row['first_name'],row['last_name'])

        #1. Giving help

        #a. Self
        whom_you_helped_responses = responses[(responses.question_no ==2) & (responses.respondent_id==row['id'])][['respondent_id', 'answer']].groupby(['respondent_id','answer']).size().reset_index(name='counts').values.tolist()
        whom_you_helped_responses = list(filter(lambda emp: emp[1].strip() != 'External',whom_you_helped_responses))
        giving_own = len(whom_you_helped_responses)

        #b. Others
        who_helped_you_responses=responses[(responses.question_no ==1) & (responses.answer==emp_obj.name)][['respondent_id', 'answer']].groupby(['respondent_id','answer']).size().reset_index(name='counts').values.tolist()
        giving_others = len(who_helped_you_responses)

        #2. Taking help

        #a. Self
        who_helped_you_responses=responses[(responses.question_no ==1) & (responses.respondent_id==row['id'])][['respondent_id', 'answer']].groupby(['respondent_id','answer']).size().reset_index(name='counts').values.tolist()
        who_helped_you_responses = list(filter(lambda emp: emp[1].strip() != 'External', who_helped_you_responses))
        taking_own = len(who_helped_you_responses)

        #b. Others
        whom_you_helped_responses = responses[(responses.question_no ==2) & (responses.answer==emp_obj.name)][['respondent_id', 'answer']].groupby(['respondent_id','answer']).size().reset_index(name='counts').values.tolist()
        taking_others = len(whom_you_helped_responses)        
        emp_obj.set_giving_awareness(giving_own,giving_others)
        emp_obj.set_taking_awareness(taking_own,taking_others)
        emp_obj.print_me()

#----START OF SCRIPT
if __name__ == '__main__':
    
    if len(sys.argv)<2:
        date = None
        print('Usage: python {} <YYYY-mm-dd>\nExample usage: {} 2022-01-30'.format(__file__,__file__))
    else:
        date = sys.argv[1].strip()

    run_awareness_analysis(date)

    
