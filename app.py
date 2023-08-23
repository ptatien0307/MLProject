from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/predict_datapoint")
async def predict_datapoint(request: Request,
                              gender: str = Form(...),
                              ethnicity: str = Form(...),
                              parental_level_of_education : str = Form(...),
                              lunch: str = Form(...),
                              test_preparation_course: str = Form(...),
                              writing_score: int = Form(...),
                              reading_score: int = Form(...)):
    custom_data = CustomData(
        gender,
        ethnicity,
        parental_level_of_education,
        lunch,
        test_preparation_course,
        writing_score,
        reading_score)

    data = custom_data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(data)[0]

    return templates.TemplateResponse("index.html", {"request": request, "result": result})