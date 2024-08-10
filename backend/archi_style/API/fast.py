from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.responses import JSONResponse

import numpy as np
import cv2
import io

# call the model for the recognazion
from archi_rec.archi_detection import architerctural_detection

app = FastAPI()

# # Allow all requests (optional, good for development purposes)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

@app.get("/")
def index():
    return {"status": "ok"}

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

    ### architecture detection
    architectural_style = architerctural_detection(cv2_img)

     ### Returning the detected architectural style
    return JSONResponse(content={"architectural_style": architectural_style})
