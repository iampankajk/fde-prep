from fastapi import FastAPI, Path, HTTPException, Query
import json

app  = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message":"hello"}


@app.get("/view")
def get_all_patients(sort_by:str = Query(..., description = "Sort by height, weight, and bmi"),
                     order:str = Query('asc')):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail="Invalid sort selection")

    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = "Invalid sort order")

    data = load_data()
    order_by = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x : x.get(sort_by,0), reverse=order_by )
    
    return sorted_data

@app.get("/patient/{patient_id}")
def get_patient_byId(patient_id: str = Path(...,
                                            description = "id of the patient",
                                            example="P001")):
    data = load_data()

    if not patient_id in data:
        raise HTTPException(status_code=404, detail = 'patient not found!')
    return data[patient_id]

