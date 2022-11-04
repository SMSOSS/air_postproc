import holidays
from datetime import date

def check_date (year , month , day):
    # check if that date is holiday or weekend 
    HK_holidays =  holidays.HK(years=[year])
    get_date = date(year , month , day)

    return [get_date in HK_holidays , get_date.weekday() >= 5]

# y = int(input("Year :"))
# m = int(input("Month :"))
# d = int(input("Day :"))

# print ("Holiday : "+str(check_date(y , m ,d)[0]) + " Weekend : "+str(check_date(y , m ,d)[1]))