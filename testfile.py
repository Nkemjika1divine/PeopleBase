from models.activity import Activity
from models import storage
from models.user import User

"""user = User(username="nkemdivine", email="cndivine@gmail.com", address="no 9 mangs", phone_number="07034243726", password="iDivi", role="admin")
storage.new(user)
storage.save()"""



"""activity = Activity(user_id='64297178-9332-487f-a784-b437bd3e970d', information_accessed="Searched for the dataset")
storage.new(activity)
storage.save()"""

print(storage.get_crime("08138816960", "02a8aba5-d8c7-4971-ae5d-acba0a3c302c"))