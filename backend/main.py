import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # কন্টেইনারের ভেতরের ইউনিক হোস্টনেম (K8s Pod Name) তুলে আনবে
    container_id = socket.gethostname()
    
    return {
        "status": "success",
        "version": "1.0.0 Latest",
        "message": "Welcome to our production cluster! Version 2.0 Auto Deploy Successful!",
        "served_by_pod": container_id
    }