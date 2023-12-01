from datetime import datetime

class Token():


    """
        Devuelve token.
    """
    def getToken(self):
        print("token")
        now = datetime.now()
        day = now.day
        month = now.month
        year = now.year
        hour = now.hour
        minute = now.minute
        second = now.second

        s_year = str(year)
        s_day = str(day)
        s_month = str(month)
        s_hour = str(hour)
        s_minute = str(minute)
        s_second = '0' + str(second)


        if(int(day) < 10):
            s_day = '0' + str(day)
        if(int(month) < 10):
            s_month = '0' + str(month)
        if(int(hour) < 10):
            s_hour = '0' + str(hour)
        if(int(minute) < 10):
            s_minute = '0' + str(minute)
        if(int(second) < 10):
            s_second = '0' + str(second)
        
        token = s_day + s_month + s_year + s_hour + s_minute + s_second

        return token


        



