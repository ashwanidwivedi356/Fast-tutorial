from  fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()
class Num(BaseModel):
    id:int
    name:str
    origin:str

nums:List[Num]=[]
@app.get("/")
def read_root():
    return {"message": "welcome to my code"}

@app.get("nums")
def get_nums():
    return nums

@app.post("/nums")
def add_tea(num:Num):
    nums.append(num)
    return num

@app.put("/nums/{num_id}")
def update_num(num_id: int,Update_num:Num):
    for index, num in enumerate(nums):
        if num.id == num.id:
            nums[index]=update_num
            return update_num
    return{"error", "Num not found"}

@app.delete("/nums/{num_id}")
def delete_num(num_id:int):
    for index,num in enumerate(nums):
        if num.id == num_id:
            deleted = nums.pop(index)
            return deleted
    return("error", "Num not found")
