import sys
import datetime as dt

# sys.path.insert(0, "/tmp")

# import application
# import application.say_welcome

from application import Application
from application.say_welcome import hello


if __name__ == "__main__":
    from pprint import pprint
    pprint(sys.path)

    print(dt.datetime.utcnow())

    hello()

    app = Application()
    res = app.run()

    if res == 0:
        print("Ended successfully")
