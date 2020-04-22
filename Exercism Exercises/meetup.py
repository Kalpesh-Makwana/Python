import datetime
def meetup(year, month, week, day_of_week):
    weekday_dic = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
                "Friday": 4, "Saturday": 5, "Sunday": 6}
    week_of_the_month = {"1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "last": 5, "5th": 5}
    
    if year % 4 == 0 and year % 100 != 0:
        offset = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else: 
        offset = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    result = []

    if week == "teenth":
       for day in range(13, 20):
           if weekday_dic[day_of_week] == datetime.date(year, month, day).weekday():
               return datetime.date(year, month, day)
    else:
        for day in range(1, offset[month - 1] + 1):
            if weekday_dic[day_of_week] == datetime.date(year, month, day).weekday():
                result.append(day)
        
        if week != "last" and len(result) > week_of_the_month[week] - 1:
            return datetime.date(year, month, result[week_of_the_month[week] - 1])
        if week == "last":
            return datetime.date(year, month, result[-1])
        else:
            raise MeetupDayException("the day does not exist")     
            
class MeetupDayException(Exception):
    pass #ValueError ("the day does not exist")