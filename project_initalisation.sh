pip install poetry
poetry new sample
cd sample
mv sample app
cd app
poetry add fastapi
poetry add 'uvicorn[standard]'