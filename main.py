from fastapi import FastAPI, Body
from pydantic import BaseModel
from bot import property_loop
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
import datetime

app = FastAPI() #docs_url=None, redoc_url=None

class PipelineDetail(BaseModel):
    ChatGPT_key: str
    query: list[str]

@app.post('/api/v1/property_loop/bot',
name="CREATE:Bot"
)
def BOT_API(body: PipelineDetail = Body(...)):
    try:
        start = datetime.datetime.now()
        pipeline_config = body.dict()
        key = pipeline_config['ChatGPT_key']
        query = pipeline_config['query']

        obj = property_loop()
        obj.bot_response(key, query)
        stop = datetime.datetime.now()
        print('------------------------------------------------------------------------------------------------------------') 
        print('TOTAL RUNTIME = ', stop - start ,','," | ",',', "Time_format = h:mm:ss")
        print('------------------------------------------------------------------------------------------------------------')

        return {'Status': HTTP_200_OK}
    except Exception as e:
        print(str(e))
        return {'Status': HTTP_500_INTERNAL_SERVER_ERROR}
