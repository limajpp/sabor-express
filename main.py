from models.data import Data
from models.utils import Utils
from fastapi import FastAPI, Query
import requests

# Already executed;
# Data.generate_restaurants_json()

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello': 'World'}   

@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    RESPONSE = requests.get(Utils.URL)
    json_data = RESPONSE.json()

    if restaurant is None:
        return {"Data": json_data}
    
    return {'Restaurant': restaurant, 'Menu': Data.process_data()[restaurant]}

if __name__ == '__main__':
    app.run()
