from pathlib import Path
import json
from pprint import pprint
import pandas as pd

data_path = Path(__file__).parent / "data"
print(data_path)

with open(data_path/"orders.json", 'r') as file:
    orders = json.load(file)

# pprint(orders[0]["products"][0]["name"])

df = pd.DataFrame(orders)

# pprint(orders[0]["products"][1]["name"])

price = []
names = []
quantity = []
for order in orders:
    print(f"Input: {order}")
    for product in order["products"]:
       print(f'Product: {product["name"]:<20} Quantity: {product["quantity"]:<20} Price: {product["price"]:<20}')
       
       
        
        

    
    



    

    
    
    
    
        
    
    