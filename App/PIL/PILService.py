from PIL import Image, ImageDraw, ImageFont

class PILService:
    @staticmethod
    def get_photo(level, name, fonts, bg):
        with Image.open(bg) as img:
            draw = ImageDraw.Draw(img)
            font1 = ImageFont.truetype(fonts[0]['font'], size=fonts[0]['size'])
            font2 = ImageFont.truetype(fonts[1]['font'], size=fonts[1]['size'])

            text_width, text_height = draw.textsize(str(level), font=font1)
            text2_width, text2_height = draw.textsize(name, font=font2)

            text_position_x = 732 - text_width / 2 
            text_position_y = 90 - text_height / 2 

            text2_position_x = 720 - text2_width / 2 
            text2_position_y = 90 + 70 + 48 - text2_height / 2

            draw.text((text_position_x, text_position_y), str(level), fill="white", font=font1)
            draw.text((text2_position_x, text2_position_y), name, fill="white", font=font2)

            temp_image_path = "temp_image.png"
            img.save(temp_image_path)