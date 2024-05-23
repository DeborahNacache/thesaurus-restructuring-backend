# Run backend

### start working with Python

    * create virtual environment 
        python -m venv env --prompt="thesaurus"
    * enter the virtual environament 
        .\env\Scripts\activate
    * install poetry
        pip install poetry
    * install all required modules 
        poetry install
    
### Run FastAPI app using uvicorn server

    * uvicorn main:app --reload
    This command starts a local server at http://127.0.0.1:8000

    * use uvicorn to get data according to get function in main.py
    for example http://127.0.0.1:8000/adress/1

    * change/add dtos from into ***models.py***

    * add functions to get data from db , change thesaurus in db .... from into ***main.py***
