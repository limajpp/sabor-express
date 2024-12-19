import requests
import json
from models.utils import Utils

class Data:
    @classmethod
    def __get(cls):
        print('Getting data from API...')
        
        RESPONSE = requests.get(Utils.URL)
        if RESPONSE.status_code == 200:
            print('Result: Data retrieved successfully! ->', RESPONSE, sep=' ')
            JSON_DATA = RESPONSE.json()
        else:
            print(f'Result: Could not get any data... -> {RESPONSE}')

        return JSON_DATA

    @classmethod
    def __process_data(cls):
        JSON_DATA = cls.__get()
        PARSED_DATA = {}

        for product in JSON_DATA:
            company = product['Company']

            if company not in PARSED_DATA:
                PARSED_DATA[company] = []
            
            PARSED_DATA[company].append({
                'Item': product['Item'],
                'Price': product['price'],
                'Description': product['description'] 
            })

        return PARSED_DATA
    
    @classmethod
    def generate_restaurants_json(cls):
        PARSED_DATA = cls.__process_data()

        for restaurant_name, data in PARSED_DATA.items():
            file_name = f'{restaurant_name}.json'

            with open(file_name, 'w') as restaurant_file:
                json.dump(data, restaurant_file, indent=4)
