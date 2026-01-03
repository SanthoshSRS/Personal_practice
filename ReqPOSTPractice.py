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


def bulk_upload_inventory(item_list):
    url = "https://api.example.com/inventory/add"
    results = {"success": 0, "fail": 0}
    
    # Define your headers here
    headers = {
        "X-API-KEY": "scret_token_123",
        "Content-Type": "application/json" # Optional with requests.post(json=...) but good practice
    }
    
    for item in item_list:
        try:
            # 1. Send POST request with 'json' and 'headers'
            # 2. Check if status_code is in the 200 range (Success)
            # 3. Update results dictionary
            
            response = requests.post(url, headers= headers,json=item, timeout=5)

            if response.status_code >= 200 and response.status_code < 300:
                results["success"] += 1
            else:
                results["fail"] += 1
            
        except requests.exceptions.RequestException:
            # If the network fails entirely for one item
            results["fail"] += 1
            
    return results

def test_my_server():
    url = "http://127.0.0.1:8000/calculate-protein"
    
    # 1. Map the raw data to match your Pydantic model
    raw_data = [
        {"name": "Chicken", "protein_per_100g": 31, "weight_consumed": 200},
        {"name": "Eggs", "protein_per_100g": 13, "weight_consumed": 100}
    ]
    
    
    
    try:
        # Make the call
        response = requests.post(url, json=raw_data)
        
        if response.ok:
            print("Test Passed!")
            print(f"Total Protein: {response.json()['total_protein_grams']}g")
        else:
            print(f"Test Failed with status: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Is your FastAPI server running?")


def test_new_server():
    url = "http://127.0.0.1:8000/find_smallest_index"
    
    # 1. Map the raw data to match your Pydantic model
    raw_data = {"haystack": "leetcode", "needle": "leeto"}
    
    
    
    try:
        # Make the call
        response = requests.post(url, json=raw_data)
        
        if response.ok:
            print("Test Passed!")
            print(f"Inital Index: {response.json()['Answer']}")
        else:
            print(f"Test Failed with status: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Is your FastAPI server running?")

if __name__ == "__main__":
    test_new_server()