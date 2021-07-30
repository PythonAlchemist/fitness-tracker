import myfitnesspal
import os
from dotenv import load_dotenv

load_dotenv()

client = myfitnesspal.Client(os.getenv('mfpl_user'), password=os.getenv('mfpl_pass'))

day = client.get_date(2021, 7, 30)

print(day)