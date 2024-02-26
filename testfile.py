import os
from models import person, storage
from dotenv import load_dotenv

# Test person creation
try:
    person1 = person.Person(first_name="Divine", middle_name="Nkemjika", last_name="Anizoba", date_of_birth="1980-01-01", phone_number="0703243726")
    storage.new(person1)
    storage.save()
    print("Person created successfully:", person1)
except Exception as e:
    print("Error creating person:", e)

# Test person retrieval
try:
    retrieved_person = storage.get("Person", person1.id)
    if retrieved_person:
        print("Person retrieved successfully:", retrieved_person)
    else:
        print("Person not found.")
except Exception as e:
    print("Error retrieving person:", e)

# Test person update
try:
    retrieved_person.first_name = "Jane"
    retrieved_person.save()
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

print("Basic testing completed.")
