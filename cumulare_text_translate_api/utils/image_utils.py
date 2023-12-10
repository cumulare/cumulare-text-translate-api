# import libraries ImageDraw, ImageFont, Image
from PIL import ImageDraw, ImageFont, Image

# create function to draw results and text from easyocr  and save to new image to disk 

def draw_boxes(image, bounds, color='yellow', width=2):
    """Draws bounding boxes around text.

    :param image: image to draw bounding boxes on.
    :type image: any
    :param bounds: bounds to draw on image.
    :type bounds: any
    :param color: color of bounding box, defaults to 'yellow'.
    :type color: str, optional
    :param width: width of bounding box, defaults to 2.
    :type width: int, optional
    :return: returns image with bounding boxes.
    :rtype: any
    """
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image