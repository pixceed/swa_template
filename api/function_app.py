import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="swa_temp_func", auth_level=func.AuthLevel.ANONYMOUS)
def swa_temp_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


@app.route(route="echo", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def echo(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        response_body = json.dumps({"input": data.get("input")})
        return func.HttpResponse(response_body, mimetype="application/json", status_code=200)
    except ValueError:
        return func.HttpResponse(json.dumps({"error": "Invalid JSON"}), mimetype="application/json", status_code=400)