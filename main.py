from fastapi import FastAPI
from route.route import router

app = FastAPI()

app.include_router(router)


# @app.get("/")
# async def root():
#     return {"message": "hello world"}


# uri = "mongodb+srv://sshail:shail123@cluster0.mqgtmsq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi("1"))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command("ping")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
