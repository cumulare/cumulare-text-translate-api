import base64
import io
import easyocr
import matplotlib.pyplot as plt

from PIL import Image


# add logging to the application
import logging

from cumulare_text_translate_api.utils.image_utils import draw_boxes
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        
        # set readtext result in variable result 
        result = reader.readtext(translate_model.img_path)

        # log result
        logger.info(result)
        # convert result to bytes
        
        # call  draw_boxes function from image_utils.py to draw bounding boxes around text and save image to variable img_result
        img_result = draw_boxes(Image.open(translate_model.img_path), result)
        logger.info("Saving image to disk")
        img_result.save('./result.png')
        logger.info("Image saved to disk")

        #get the img_result a bufferstream and return it
        img_byte_arr = io.BytesIO()
        img_result.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        
         # Convert bytes to base64 string
        img_base64 = base64.b64encode(img_byte_arr).decode()

        # Return both the image and the OCR results
        return {    
            'image': img_base64
        }
    

    
    