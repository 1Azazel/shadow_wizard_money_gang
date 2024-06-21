from PIL import Image, ImageDraw, ImageColor


class ColorPalette:
    def __init__(self, color_list):
        self.colors = color_list

    def get_colors_in_palette(self):
        color_list = []
        for color in self.colors:
            color_list.append(color)
        return color_list


test_palette = ColorPalette(["#FFEBD2", "#273248", "#AF4F41", "#FFA364", "#FC7643"])

