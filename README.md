# Run backend

### start working with Python

    * create virtual environment // only on first time 
        python -m venv env --prompt="thesaurus"
    * enter the virtual environament 
        .\env\Scripts\activate
    * install poetry // only on first time 
        pip install poetry
    * install all required modules // everytime we add a new module 
        poetry install
    
### Run FastAPI app using uvicorn server

    * uvicorn main:app --reload // "main" can be replaced with the name of the file u are running , dont forget to rerun this cmd with the right name 
    This command starts a local server at http://127.0.0.1:8000

    * use uvicorn to get data according to get function in main.py
    for example http://127.0.0.1:8000/adress/1

    * change/add dtos from into ***models.py***

    * add functions to get data from db , change thesaurus in db .... from into ***main.py***
