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
    result = 400
    translte_val = Translate.read_translated_img(Translate, translate_req)

    if translte_val is not None:
        result = 200

    return result
