from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

from src.pipeline.predict_pipeline import CustomData, PredictPipeline




app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict_datapoint")
async def predict_datapoint(request: Request):
    form_data = await request.form()

    custom_data = CustomData(
        form_data['gender'],
        form_data['ethnicity'],
        form_data['parental_level_of_education'],
        form_data['lunch'],
        form_data['test_preparation_course'],
        form_data['writing_score'],
        form_data['reading_score'])

    data = custom_data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(data)[0]

    return templates.TemplateResponse("index.html", {"request": request, "result": result})

