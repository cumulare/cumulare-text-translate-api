import easyocr
from cumulare_text_translate_api.model.translate_model import TranslateModel

class Translate:
    """Used for translating images."""

    def dict(self) -> int:
        """_summary_.

        :return: test.
        """
        return 10
    
    def read_translated_img(translate_model: TranslateModel) -> any:
        """_summary_

        Parameters
        ----------
        translate_model : TranslateModel
            _description_

        Returns
        -------
        any
            _description_
        """

        # init easy ocr to read images
        reader = easyocr.Reader([translate_model.lang])
        result = reader.readtext(translate_model.img_path)
        print(result)
        return result

    

