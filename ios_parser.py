# pretty much same as android parser except a changes
# (read android parser comments)
# key changes -> iOS has seconds in timestamp
# timestamp isn't between '[ ]'
# android has '-' after timestamp, iOS has nothing
# modded the regex accordingly

import re
import numpy as np
import pandas as pd
from datetime import datetime
import calendar
from dateutil import parser

regexDate = r"\[(\d*\/\d+\/\d+)\, (\d+\:\d+:\d+)\]"
regexUserName = r"\]\s([a-zA-z0-9 ]*)"
regexUserNumber = r"\+[\s+\d\s]*"
# number2 = r"\+[+\s\w:]+"


def get_date_time_day(line):
    matchesDate = re.search(regexDate, line, re.MULTILINE)

    if matchesDate is None:
        Date, Day, Time = np.NaN, np.NaN, np.NaN

    else:
        Date = matchesDate.groups()[0]
        Time = matchesDate.groups()[1]
        my_date_str = str(Date) + ' ' + str(Time)
        try:
            datetime_obj = parser.parse(my_date_str, dayfirst=True)
            Date = datetime_obj.date().isoformat()
            Time = datetime_obj.strftime("%H:%M:%S")
            Day = calendar.day_name[datetime_obj.weekday()]
        except:
            Date, Time, Day = np.NaN, np.NaN, np.NaN

    return Date, Day, Time


def get_user(line):
    matchesName = re.search(regexUserName, line, re.MULTILINE)

    matchesNumber = re.search(regexUserNumber, line, re.MULTILINE)

    if matchesName is not None:
        Name = matchesName.groups()[0]
    if matchesNumber is not None:
        Number = matchesNumber.group()

    if Name:
        if "changed" in str(Name) or "secured" in str(Name):
            return np.NaN
        else:
            return str(Name)
    else:
        return str(Number)


def get_message(line):
    # like literally everything after the third colon is the message
    # so why use regex when can get number of colons ha
    message = ''
    colon = ':'
    counter = 0
    for i in range(len(line)):
        if line[i] == colon:
            counter = counter + 1

        if counter == 3:
            message = line[i + 2:]
            break
    counter = 0
    return message


def get_data(fileName):

    totalTable = []
    with open(fileName, 'r', encoding='UTF-8') as chat:
        for line in chat:
            # weird typesetting thing I have to remove
            line = line.replace('\u200e', '')
            # if line doesn't start with a timestamp, its a continuation
            # of previous message, so just append the content while removing the
            # newline character, else get data from it
            if line[0] != '[':
                totalTable.append([np.NaN, np.NaN, np.NaN, np.NaN, line.replace('\n', '')])
            else:
                date, day, time = get_date_time_day(line)
                user = get_user(line)
                message = get_message(line)
                totalTable.append([date, day, time, user, message.replace('\n', '')])

    return totalTable

# the main function that's exported


def ios_data(fileName):
    data = get_data(fileName)

    df = pd.DataFrame(columns=['Date', 'Day', 'Time', 'User', 'Message'])

    for num, info in enumerate(data):
        df.loc[num] = info

    df.to_csv(r'userdata/chat.csv')