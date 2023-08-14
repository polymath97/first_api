from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

dataframe = pd.read_csv('iris.csv')

@app.get("/")
def root():
    return {"message":"Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu":{1:"See shopping cart (/data)",
                    2:"Add item (/add) - You may need request",
                    3:"Edit shopping cart (/edit/id)"}}

@app.get("/display")
def show():
    return dataframe.to_json()

@app.put("/edit/{id}")
def update_cart(id:int,updated_cart:dict):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        data["items"][id].update(updated_cart)
        return {"message": f"Item with ID {id} has been updated successfully."}
    
# uvicorn main:app --reload