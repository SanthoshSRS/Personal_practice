import requests
import json

def create_new_user(name, job):
    url = "https://reqres.in/api/users"
    data = {"name" : name, "job" : job}

    response = requests.post(url, json=data, timeout=10)

    if response.status_code == 201:
        print("new user created")
    else:
        print("Error " + str(response.status_code)+". User not created")

# create_new_user("sam", "doctor")

def upload_even_numbers(data_list):
    url = "https://api.example.com/process"
    success_count = 0
    try:
        for num in data_list:
            # 1. Check if the number is even
            # 2. If even, prepare the payload: {"value": num, "category": "even"}
            # 3. Send the POST request
            # 4. Check if response.status_code == 201
            
            if num%2 == 0:
                data = {"value" : num, "category" : "even"}
                response = requests.post(url, json=data, timeout= 5)

                if response.status_code == 201:
                    success_count +=1
                else:
                    print(f"Even number was not posted: {response.status_code}")
            
        return success_count
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

# Test data
my_data = [1, 2, 3, 4, 5, 6]
print(upload_even_numbers(my_data)) # Should attempt to upload 2, 4, and 6