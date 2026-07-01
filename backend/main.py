import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # কন্টেইনারের ভেতরের ইউনিক হোস্টনেম (K8s Pod Name) তুলে আনবে
    container_id = socket.gethostname()
    
    return {
        "status": "success",
        "Name": "Valo Runi 3.0.0",
        "message": "Welcome to our production Runi valoi",
        "served_by_pod": container_id
    }