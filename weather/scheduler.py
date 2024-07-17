import os
import threading
import time

import schedule

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANAGE_PY_PATH = os.path.join(BASE_DIR, 'manage.py')


def fetch_weather_data():
    os.system(f'python {MANAGE_PY_PATH} fetch_weather_data')


def run_scheduler():
    schedule.every(5).minutes.do(fetch_weather_data)
    while True:
        schedule.run_pending()
        time.sleep(1)


# Start the scheduler in a separate thread
if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
