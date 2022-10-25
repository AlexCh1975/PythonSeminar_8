from datetime import datetime as dt
from time import strftime

def all_logger(result, comment):

    time = dt.now()
    with open('log_c_service.csv', 'a', encoding='utf-8') as file:
        file.write('{};{};{}\n'.format(time, result,comment))