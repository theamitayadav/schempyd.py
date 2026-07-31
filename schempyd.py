#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class User(BaseModel):
   # name: str
   # age:int
   # email:str

#@app.post("/create_user")
#def create_user(user:User):
    #return{
        #"message":"User Created",
        #"data":user
    #}

# nested model
class Address(BaseModel):
    street:str
    city:str
    state:str
    zip_code:str
@app.post("/create_user_with_address")
def create_user_with_address(user:User,address:Address):
    return{
        "message":"User Created",
        "data":{
            "user":user,
            "address":address
        }
    }


    
    
