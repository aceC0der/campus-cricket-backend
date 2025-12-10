from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
async def root():
    """
    Return a greeting message for the application's root HTTP endpoint.
    
    Returns:
        dict: A dictionary with the key "message" set to "Hello world".
    """
    return {"message": "Hello world"}