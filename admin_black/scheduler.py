import schedule
import time
import os

def job():
    os.system('extraction.py')
    os.system('importing.py')


# Schedule the job every 4 days
schedule.every(4).days.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)