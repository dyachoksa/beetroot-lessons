import datetime

# import models
from models import version

# import models.user
from models.user import name as user_name

print("Today:", datetime.datetime.today())
print("Version:", version)
print("User module:", user_name)
