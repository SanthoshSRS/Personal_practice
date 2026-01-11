import requests

def get_title_byID(userID):
    base_url = "https://jsonplaceholder.typicode.com/posts"
    try:

        response = requests.get(base_url,timeout=5)
        response.raise_for_status()
        Data = response.json()
        ans = []
        for i in Data:
            if i["userId"] == userID:
                ans.append(i["title"])
        print(ans)
        print(len(ans))

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}") 

# get_title_byID(8)

def get_completion_rate(user_id):
    url = "https://jsonplaceholder.typicode.com/todos"
    
    try:
        # Your code here:
        # 1. Make the request
        # 2. Check for errors
        # 3. Filter for user_id
        # 4. Calculate percentage: (completed_count / total_user_tasks) * 100
        response = requests.get(url, timeout=10, params={"userId":user_id})
        response.raise_for_status()
        data = response.json()
        total_user_task = len(data)
        ans =   0.0
        if total_user_task >0:
            completed_task = 0
            for i in data:
                if i["completed"]:
                    completed_task+=1

            ans = (completed_task/total_user_task)*100
            ans = round(ans,2)

        return ans
        
        
        
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0.0

# Test your function:
# print(get_completion_rate(1))

def calculate_total_inventory_value():
    url = "https://mock-api.com/inventory"
    total_value = 0
    current_page = 1
    total_pages = 1 # We start with 1 and update it after the first request
    
    try:
        while current_page <= total_pages:
            # 1. Make the request for the current_page
            # 2. Update total_pages from the response
            # 3. Loop through 'data' and add (price * quantity) to total_value
            # 4. Increment current_page
            
            response = requests.get(url, timeout=10, params={"page":current_page})
            response.raise_for_status()

            data = response.json()
            total_pages = data["total_pages"]
            inv = data["data"]
            for i in inv:
                total_value += (i["price"]*i["quantity"])
            current_page += 1
            
        return total_value
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    


def get_top_student(subject_name):
    url = "https://api.example.com/students"
    
    try:
        # 1. Fetch all students
        # 2. Filter the list to only include the target subject
        # 3. Track the 'max_score' and 'top_student_name'
        # 4. Return the name
        
        response = requests.get(url, timeout=10, params={"subject" : subject_name})
        response.raise_for_status()
        data = response.json()
        max = -float("inf")
        name = None
        for i in data:
            if i.get("score",-float("inf")) >= max:
                max = i.get("score",-float("inf"))
                name = i.get("name", "Noname")

        return name


        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    

def get_valid_emails():
    url = "https://api.example.com/users"
    valid_emails = []
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        users = response.json()
        
        # Your task:
        # 1. Loop through users
        # 2. Safely check if 'email' exists and is not None
        # 3. Add to valid_emails list
        for user in users:
            if user.get("email", None) !=None:
                valid_emails.append(user["email"])
        
        pass 
        
    except Exception as e:
        return []
    
def get_average_weight(type_name, limit=5):
    type_url = f"https://pokeapi.co/api/v2/type/{type_name}"
    weights = []
    
    try:
        # 1. Fetch the type data
        response = requests.get(type_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # 2. Get the list of pokemon (it's under 'pokemon' key)
        pokemon_list = data.get("pokemon", [])[:limit]
        
        for entry in pokemon_list:
            # 3. Get the URL for this specific pokemon
            poke_url = entry["pokemon"]["url"]
            
            # 4. Make a request to that URL
            supres = requests.get(poke_url, timeout=5,)
            supres.raise_for_status()
            temp = supres.json()
            
            # 5. Extract the 'weight' and add to weights list
            kg = temp["weight"]
            weights.append(kg/10)
             # Your logic here
            
        # 6. Calculate average
        print(weights)
        if not weights:
            return 0
        return sum(weights) / len(weights)
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

# Test it:
print(f"Average weight of fire pokemon: {get_average_weight('fire')}kg")