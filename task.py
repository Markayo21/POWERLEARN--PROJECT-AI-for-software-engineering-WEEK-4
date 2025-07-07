# Function to sort a list of dictionaries by a specific key
def sort_dicts_by_key(dicts, key): 
    """
    Sorts a list of dictionaries by a specific key.

    Args:
        dicts (list): List of dictionaries to be sorted.
        key (str): The key by which to sort the dictionaries.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dicts, key=lambda x: x[key])


#Write your own (beginner-friendly) version below the AI one:
def manual_sort_dict_list_by_key(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

#Add a test block to run both versions and see the results:
students = [
    {"name": "Alice", "score": 91},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 78}
]

# AI version
print("AI-suggested:", sort_dicts_by_key(students.copy(), "score"))

# Manual version
print("Manual:", manual_sort_dict_list_by_key(students.copy(), "score"))




