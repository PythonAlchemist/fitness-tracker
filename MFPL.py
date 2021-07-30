import myfitnesspal
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

client = myfitnesspal.Client(os.getenv('mfpl_user'), password=os.getenv('mfpl_pass'))

thisweek = datetime.date(2015, 5, 11)
lastweek = datetime.date(2015, 5, 4)

day = client.get_date(2021, 7, 30)
weight = client.get_measurements('Weight')

print(day)
print(weight)