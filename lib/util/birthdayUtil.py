import datetime

import dateutil.parser

import fileWriter

fileName = "birthdays"


def parseDate(dateInput: str) -> datetime.datetime:
    return dateutil.parser.parse(dateInput)


def addDay(data: dict, name: str, date: int) -> dict:
    data[name] = date
    return data


def removeDay(data: dict, name: str) -> dict:
    data.pop(name)
    return data


def readDay(data: dict, name: str) -> str:
    return str(datetime.date.fromtimestamp(data[name]).strftime("%A %d. %B %Y"))



print(readDay(fileWriter.read("birthdays"), "usernameB"))

print(parseDate("Dec 11 2004"))