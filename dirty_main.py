from application import *
from datetime import datetime

if __name__ == '__main__':
    print('Текущая дата:', datetime.now().date())
    salary.calculate_salary()
    db.people.get_employees()