from io import BytesIO
from PIL import Image, ImageDraw


class MemeGenerator:

    SIZES = (128, 128)

    def __init__(self, image: bytes, text: str):
        self.image = image
        self.text = text

    def create_meme(self):
        image = self._combine_image_with_text()
        image.save()

    def _retrieve_uploaded_image(self) -> Image:
        im = Image.open(BytesIO(self.image))
        return im

    def _resize_image(self) -> Image:
        image = self._retrieve_uploaded_image()
        image.resize(self.SIZES)
        return image

    def _add_text(self) -> Image:
        text_box = Image.new('RGBA', (128, 50), "black")
        draw = ImageDraw.Draw(text_box)
        draw.text((25, 74), self.text)
        return text_box

    def _combine_image_with_text(self) -> Image:
        image = self._resize_image()
        text = self._add_text()
        image.paste(text, (0, 0))
        return image
