import azure.functions as func
import datetime
import json
import logging
import os

from LegendDetector import extract_wall_codes

app = func.FunctionApp()

# @legend_router.post("/detect")
# async def detect(request: Request):
#     data = await request.json()
#     base64_img = data["base64"]
#     endpoint = os.environ["AZURE_DI_ENDPOINT"]
#     key = os.environ["AZURE_DI_KEY"]
#     wall_codes = extract_wall_codes(base64_img, endpoint, key)
#     return {"wallCodes": wall_codes}



@app.route(route="legend/detector", auth_level=func.AuthLevel.ANONYMOUS)
def Detector(req: func.HttpRequest) -> func.HttpResponse:
    try:

        data = req.get_json()

        base64_img = data["base64"]
        endpoint = os.environ["AZURE_DI_ENDPOINT"]
        key = os.environ["AZURE_DI_KEY"]

        logging.info('Python HTTP trigger function processed a request.')

        wall_codes = extract_wall_codes(base64_img, endpoint, key)

        logging.info(f"Detected wall codes: {wall_codes}")
        # ✅ Wrap the dict in HttpResponse
        return func.HttpResponse(
            body=json.dumps({"wallCodes": wall_codes}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=500
        )
