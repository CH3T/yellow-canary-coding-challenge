import os
import pandas as pd
from datetime import datetime

def datetimeconv(date_str):

    # Example with the standard date and time format
    date_format = '%Y-%m-%dT%H:%M:%S'

    date_obj = datetime.strptime(date_str, date_format).month
    print("date_obj",date_obj)

    # Example with a different format
    return date_obj

def main():
    print("test")
    dtobj = datetimeconv("2017-11-01T00:00:00")
    s = pd.to_datetime(dtobj).month()

if __name__ == "__main__":
    main()

