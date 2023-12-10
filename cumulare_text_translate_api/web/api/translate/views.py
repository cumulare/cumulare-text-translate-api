import json
from fastapi import APIRouter, HTTPException, logger
from fastapi.responses import JSONResponse

from cumulare_text_translate_api.model.translate import Translate
from cumulare_text_translate_api.model.translate_model import TranslateModel

router = APIRouter()


@router.post("/translations/")
def translate_image(translate_req: TranslateModel):
    """Read configuration to get image text.

    :param translate_req: transformation model.
    :type translate_req: TranslateModel
    :return: Returns status code.
    :rtype: any
    """
    status_code = 400
    translate_val = Translate.read_translated_img(Translate, translate_req)

    # add logic to return 200 if translation is successful
    if translate_val is not None:
        status_code = 200

   ## add logic to return 200 if translation is successful
    if translate_val     is not None:
        return {"status_code": status_code, "img_data": translate_val}
    else:
        raise HTTPException(status_code=status_code, detail="Translation failed")

