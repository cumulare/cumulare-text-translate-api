from pydantic import BaseModel


class TranslateModel(BaseModel):
    """Translate model to be used for the api.

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    lang: str
    img_path: str
