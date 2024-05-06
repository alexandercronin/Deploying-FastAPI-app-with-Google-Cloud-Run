from fastapi import FastAPI

from fastapi.responses import StreamingResponse
import httpx

app = FastAPI()


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}

@app.get("/mars_rover", tags=["root"])
async def mars_rover(api_key: str):
    # Create a client instance
    with httpx.Client() as client:
        # Send a GET request
        response = client.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key={api_key}", follow_redirects=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Print the response contents
            print(response.text)
        else:
            print(f'Request failed: {response.status_code}')
        # return response.json()
        file_url = response.json()['photos'][0]['img_src']
        print(file_url)
    with httpx.Client() as client:
        # Send a GET request
        response = client.get(file_url, follow_redirects=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Print the response contents
            print(response.text)
        else:
            print(f'Request failed: {response.status_code}')     
        # Create and return a StreamingResponse
    return StreamingResponse(response.aiter_bytes(), media_type=response.headers["Content-Type"])