from datetime import datetime

import pytz

print("\n")

print("\n")

print("WElcome to the africa time app,we will tell the local time of Blantyre")

africa=pytz.timezone("Africa/Blantyre")

local_time= datetime.now(africa)

print("The local time now at Blantyre is", local_time)

print("\n")

print("\n")