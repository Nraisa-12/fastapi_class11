from fastapi import FastAPI

app = FastAPI()


icd_codes = [
    {"code": "A00", "description": "Cholera"},
    {"code": "A01", "description": "Typhoid fever"},
    {"code": "A02", "description": "Salmonella enteritis"}
]

cpt_codes = [
    {"code": "10030", "description": "Guidance for needle placement"},
    {"code": "99213", "description": "Office or other outpatient visit"},
    {"code": "92012", "description": "Eye exam and evaluation"}
]


@app.get("/codes")
def get_codes():
    return {"icd_codes": icd_codes, "cpt_codes": cpt_codes}
