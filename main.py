from fastapi import FastAPI

app = FastAPI()

product = [
    {"id":1,
        "name":"mukesh",
        "city":"banglore",
        "age":30
        }
        ,

        {"id":12,
        "name":"mukeshe",
        "city":"bangloere",
        "age":30
        },

        {"id":13,
        "name":"mukesht",
        "city":"banglores",
        "age":30
        }
    ]


@app.get("/product") # fetching all data 
async def all_data():
    return product


@app.get("/product_id/{id}") # fetching data by id
async def single_data(id:int):
    for i in product:
        if i["id"] == id:
            return i 
        

@app.post("/create_new_product") # creating new data
async def create_product(data:dict):
    product.append(data)
    return{"message":"one data created successfully"}


@app.put("/updated_record/{id}") # update record
async def update_data(id:int,data:dict):
    for i in product:
        if i["id"] == id:
            i.update(data)
            return i

@app.patch("/partial_update/{id}") # partial update 
async def partial_update(id:int,data:dict):
    for i in product:
        if i["id"] == id:
            i.update(data)
            return i
        
@app.delete("/delete_record/{id}") # delete record
async def delete_data(id:int):
    for i in product:
        if i["id"] == id:
            product.remove(i)
            return{"message":"one data deleted successfully"} 