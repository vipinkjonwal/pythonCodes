import sys
class MyDate:
    
    '''
    MyDate: A simple implementation of date as a class.
    '''
    def __init__(self, day = 1, month = 1, year = 2000):
        '''
        Objective: To initialize data members of object MyDate
        Input Parameters:
            self (implicit parameter) - object of type MyDate
            day, month, and year - int
        Return Value: None
        '''
        if not(type(day)==int and type(month)==int and
        type(year)==int):
            print('Invalid data provided for date')
            sys.exit()
        if month > 0 and month <= 12:
            self.month = month
        else:
            print('Invalid value for month')
            sys.exit()
        if year > 1900:
            self.year = year
        else:
            print('Invalid value for year. Year should be greater\
            than 1900.')
            sys.exit()
        self.day = self.checkDay(day) # validate day

    def checkDay(self, day):
        '''
        Objective: To validate day component
        Input Parameters:
            self (implicit parameter) - object of type MyDate
            day - numeric
        Return Value: day if it is correct else message 'Invalid
            value for the day' is printed and the program is terminated
        '''
        # currentYear: list of no of days in months of current year

        if self.year%400==0 or (self.year%100!=0 and self.year%4==0): #if leap year
            currentYear = [31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            currentYear = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (day > 0 and day <= currentYear[self.month - 1]):
            return day
        else:
            print('Invalid value for day')
            sys.exit()

    def __str__(self):
        '''
        Objective: To return string representation of object
        Input Parameter:
            self (implicit parameter) - object of type MyDate
        Return Value: string
        '''
        # Approach: use dd-mm-yyyy format
        if self.day <= 9:
            day = '0' + str(self.day)
        else:
            day = str(self.day)
        if self.month <= 9:
            month = '0' + str(self.month)
        else:
            month = str(self.month)
        return day+'-'+month+'-'+str(self.year)

def main():
    '''
    Objective: To create objects of class Date and to perform operations on it
    Input Parameter: None
    Return Value: None
    '''
    today = MyDate(3,9,2014)
    print(today)
    defaultDate = MyDate()
    print(defaultDate)
        
if __name__=='__main__':
    main()
