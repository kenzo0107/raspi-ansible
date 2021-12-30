#!/usr/bin/env python3

import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import mh_z19
import time

font1 = ImageFont.truetype(
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 15)
font2 = ImageFont.truetype(
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 10)
font3 = ImageFont.truetype(
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 27)


class CO2():
    def __init__(self):
        i2c = board.I2C()
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

    def initializeDisplay(self):
        self.display.fill(0)
        self.display.show()

    def show(self):
        latest_co2 = None
        while True:
            # get co2 concentration
            co2 = self.co2Concentration()
            if co2 != latest_co2:
                latest_co2 = co2
                # show co2 in lcd
                self.showCO2InLCD(co2)
            # sleep for 5 seconds each time
            time.sleep(5)

    def co2Concentration(self):
        r = mh_z19.read()
        if r is not None and 'co2' in r.keys():
            return str(r['co2'])
        return None

    def showCO2InLCD(self, co2: str):
        image = Image.new("1", (self.display.width, self.display.height))
        self.draw = ImageDraw.Draw(image)

        if co2 is None:
            self.draw.text((0, 0), "ERROR", font=font1, fill=255)
        else:
            self.draw.text((0, 0), "CO2", font=font1, fill=255)
            self.draw.text((10, 15), "ppm", font=font2, fill=255)
            self.draw.text((40, 0), co2, font=font3, fill=255)

        self.display.image(image)
        self.display.show()


if __name__ == '__main__':
    co2 = CO2()
    while True:
        try:
            co2.show()
        except Exception:
            pass
        finally:
            # initialize display when failed
            co2.initializeDisplay()
