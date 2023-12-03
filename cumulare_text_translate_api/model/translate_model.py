from pydantic import BaseModel

class TranslateModel(BaseModel):
    """_summary_

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """
    lang: str
    img_path: str

