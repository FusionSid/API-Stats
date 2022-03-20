from fastapi import FastAPI
from fastapistats import Stats

app = FastAPI()

# Add this line if you want a custom location for you json file
Stats.file_name = "json_files/stats.json"

# you can also make a variable with the class and use that instead of @Stats.update_stats
update = Stats.update_stats

@app.get("/name")
@update(name="name") # if the name kwarg is not passed it will default to the function name
def show_name(name : str): # This is just an example endpoint
    return {"your_name" : name}