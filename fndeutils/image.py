from PIL import Image, ImageDraw


def channel(i, c, size, start_fill, stop_fill):
    """calculate the value of a single color channel for a single pixel"""
    return start_fill[c] + int((i * 1.0 / size) * (stop_fill[c] - start_fill[c]))


def color(i, size, start_fill, stop_fill):
    """calculate the RGB value of a single pixel"""
    return tuple([channel(i, c, size, start_fill, stop_fill) for c in range(3)])


def create_rounded_rectangle_mask(size, radius, alpha=255):
    factor = 5
    radius = radius * factor
    image = Image.new('RGBA', (size[0] * factor, size[1] * factor), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, size[0] * factor, size[1] * factor), radius=radius, fill=(255, 255, 255, alpha))
    image = image.resize(size, Image.LANCZOS)

    return image
