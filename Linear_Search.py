def linear_search(target, cities):
    for i, city in enumerate(cities):
        if city == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

target_city = "Tbilisi"
cities = ["London", "New York", "Paris", "Munich", "Mumbai", "Montreal", "Tbilisi", "Amsterdam"]

result = linear_search(target_city, cities)
if result != -1:
    print(f"The target city '{target_city}' is found at index {result}.")
else:
    print(f"The target city '{target_city}' is not found in the list.")
