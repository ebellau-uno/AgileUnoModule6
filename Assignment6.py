'''
Eugene Bellau
11/1/2020
Module 6
ebellau@uno.edu
'''

import sys # This command will import the sys module which provides information about constants, functions, and methods of the Python interpreter
'''
This command will import the json module which will cause serialization and deserialization.
Serialization is the process of encoding data into JSON format
Deserialization is the process of decoding JSON data back into native objects
'''
import json 

with open ("input.json", "r") as input: # This command will open the JSON file in the context manager with read permissions
    customers = json.load(input) # This command will assign the data in the JSON file to the customers variable 

# are all customer numbers unique?
temp = [] # This is an empty list to store the cusomters IDs
for value in customers["clients"]: # This is a For loop to go through each client
    temp.append(value["id"]) # This command will add the customers ID number to the list

# Add values to set and delete any duplicate entries
unique = set(temp)
# Add values to tuple
original = (temp)

# This is an if/else statement to verify that all customer IDs are unique
if len(unique) != len(original):
    print("There are duplicate ID numbers in the data, exiting!!!")
    sys.exit()
else: 
    print("All customer IDs are unique!!!")

'''
1. Create a set of each customer email and test for uniqueness
'''
temp = [] # This is an empty list to store the cusomters email addresses
for value in customers["clients"]: # This is a For loop to go through each client
    temp.append(value["email"]) # This command will add the customers email address to the list

# Add values to set and delete any duplicate entries
unique = set(temp)
# Add values to tuple
original = (temp)

# This is an if/else statement to verify that all customer emails are unique
if len(unique) != len(original):
    print("There are duplicate email accounts in the data, exiting!!!")
    sys.exit()
else: 
    print("All customer emails are unique!!!")


'''
2. Create a dictonary of each customer, each one should contain the name and email of each employee 
   Write this as JSON to a new file called email_list.json
'''

with open ("input.json") as input: # This command will open the JSON file in the context manager
    source = input.read() # This command will read the data om the JSON file

customer = json.loads(source) # This command will assign the data in the JSON file to the customers variable as a string
email_list = {} # This is an empty dictonary to store the Name and Email address of each customer
for value in customers["clients"]: # This is a For loop to go through each client
    name = value['name'] # This will take the value of each customer's name and store it in the name variable
    email = value['email'] # This will take the value of each customer's email address and store it in the email variable
    email_list[name] = email # This command will take the values of the variables and store it in the dictonary


with open('email_list.json', 'w') as f: # This command will create a new JSON file with write permissions
    f.write(json.dumps(email_list)) # This command will write the values that are stored in the dictonary as a string

'''
3. Open the original file again, this time set each male customers isActive status to false
   Write this new data to a file called current_customers.json 
'''

for client in customer["clients"]: # This is a For loop to go through each client
    if client["gender"] == "male": # This is an IF statement to find if the gender value is equal to male
        client["isActive"] = "false" # This command will change the isActive value to false if the IF statement is true

with open("current_customers.json", "w") as outfile:   # This command will create a new JSON file with write permissions
    outfile.write(json.dumps(customer)) # This will write the changed data and write it to the JSON file as a string


