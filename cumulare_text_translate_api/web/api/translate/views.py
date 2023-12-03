from fastapi import APIRouter, Body
from cumulare_text_translate_api.model.translate import Translate
from cumulare_text_translate_api.model.translate_model import TranslateModel

router = APIRouter()


@router.post("/translations/")
def translate_image(translate_req: TranslateModel):
    """_summary_

    Parameters
    ----------
    img : _type_
        _description_

    Returns
    -------
    any
        _description_
    """
    print("Image path: " + translate_req.img_path )
    result = Translate.read_translated_img(translate_req)
    return 200
