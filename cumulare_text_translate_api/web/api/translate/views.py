from fastapi import APIRouter

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
    return Translate.read_translated_img(translate_req)
