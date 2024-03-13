foul = {"key1": {"bounce": 43, "Name": "Chioma"},
        "key2": {"bounce": 44, "Name": "John"}}

# Loop through the outer dictionary
for outer_key in foul:
  # Access the inner dictionary using the outer key
  inner_dict = foul[outer_key]

  # Check for "Name" key in the inner dictionary and print the value
  if "Name" in inner_dict:
    print(inner_dict["Name"])  # Print "Chioma"
    break  # Exit the loop after finding "Chioma" (optional)