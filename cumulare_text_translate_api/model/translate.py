import easyocr

from cumulare_text_translate_api.model.translate_model import TranslateModel


class Translate:
    """Used for translating images."""

    def read_translated_img(self, translate_model: TranslateModel) -> any:
        """Read img to use ocr to get text.

        :param translate_model: translation model for configuration.
        :type translate_model: TranslateModel
        :return: returns result from ocr.
        :rtype: any
        """
        # init easy ocr to read images
        reader = easyocr.Reader([translate_model.lang])

        return reader.readtext(translate_model.img_path)
