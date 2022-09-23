# Defining dictionaries
# keys: values
# Name: Sanjay
# email: sanjay@gmail.com
# phone: 12345

# Define Dictionaries in python
from tokenize import Name


customer = {
    "Name": "Sanjay",
    "email": "sanjay@gmail.com",
    "Degree": "Masters"
}
print(customer["Name"])
print(customer.get("Name"))
print(customer.get("Birthday"))
# Add new key value 
customer["Birthdate"] = "Jan 1 1990"
print(customer)


