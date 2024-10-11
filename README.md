This project processes order data from a JSON file and generates two JSON files: `customers.json` and `items.json`.

The script reads the given JSON file and stores it in a python object. We iterate over the items in the object and separate phone numbers, customer names and items ordered.
Then we store phone numbers as keys and names as values in customer dictionary. We will also process items ordered as a seperate dictionary named items which hold item name as key and value as another dictionary with keys price and orders and respective values as price of item and no of times order is placed for the item.
These dictionaries are then saved as JSON files named as customers.json and items.json respectively.

To run:
1. Redirect to the folder where code is present in the terminal 
2. python project.py <JSON_FILENAME> where instead of <JSON_FILENAME> provide the actual filename.