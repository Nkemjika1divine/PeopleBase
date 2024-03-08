import os
from models.dataset import Dataset
from models.user import User
from models import storage

# Test person creation
try:
    data1 = Dataset(first_name="Divine", middle_name="Nkemjika", last_name="Anizoba", photo="image.jpg", photo_type="jpg", date_of_birth="1980-01-01", gender="M", address="16 jump street", city="Aba", state="Abuja", country="Nigeria", phone_number="08172617430", email="Nkem@yahoo.com", nationality="Nigerian", occupation="Trader", education_level="University", marital_status="Single")
    storage.new(data1)
    storage.save()
    print("Dataset created successfully:", data1)
except Exception as e:
    print("Error creating dataset:", e)


try:
    user1 = User(full_name="Divine", email="cndivine@gmail.com", address="No 8", phone_number="77899", password="money", role="Admin")
    storage.new(user1)
    storage.save()
    print("User created successfully:", user1)
except Exception as e:
    print("Error creating User:", e)


"""try:
    person2 = Dataset(first_name="Divine", middle_name="Nkemjika", last_name="Anizoba", photo="image.jpg", photo_type="jpg", date_of_birth="1980-01-01", gender="M", address="16 jump street", city="Aba", state="Abuja", country="Nigeria", phone_number="08172617430", email="Nkem@yahoo.com", nationality="Nigerian", occupation="Trader", education_level="University", marital_status="Single")
    storage.new(person1)
    storage.save()
    print("Person created successfully:", person1)
except Exception as e:
    print("Error creating person:", e)"""


# Test person retrieval
try:
    retrieved_person = storage.all()
    if retrieved_person:
        for person in retrieved_person:
            print(person)
except Exception as e:
    print("Error retrieving person:", e)

"""# Test person update
try:
    retrieved_person["User.e4428230-58f6-42fa-82e1-8afcd70f3fe0"]["full_name"] = "Jane"
    retrieved_person.save()
    print("updated person saved")
    updated_person = storage.get("Person", person1.id)
    if updated_person and updated_person.first_name == "Jane":
        print("Person updated successfully!")
    else:
        print("Person update failed.")
except Exception as e:
    print("Error updating person:", e)

# Test person deletion (optional)
if input("Do you want to delete the created person? (y/n): ").lower() == "y":
    try:
        storage.delete(retrieved_person)
        print("Person deleted successfully.")
    except Exception as e:
        print("Error deleting person:", e)

# Test other functionalities as needed, following similar patterns

print("Basic testing completed")"""