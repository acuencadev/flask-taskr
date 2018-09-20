from views import db
from models import Task
from datetime import date


# create the database and the db table
db.create_all()

# insert data
db.session.add(Task("Finish this tutorial", date(2018, 10, 1), 10, 1))
db.session.add(Task("Buy some food", date(2018, 9, 21), 7, 1))

# commit the changes
db.session.commit()
