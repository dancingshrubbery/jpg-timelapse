#!/usr/bin/python

import sys
import os
import fileinput
from PIL import ImageFont, ImageDraw, Image
from datetime import datetime

script_dir = os.path.dirname(os.path.realpath(__file__))
font_path = script_dir + "/arial.ttf"
font_size = 28
offset_x  = 20
offset_y  = 25
spacing   = 5
text_color = "#ffffff"
shadow_color = "#000000"
veg_color   = '#a2da7a'
flower_color = '#ff8855'
cube_size = 15

def write_week_cubes(img, weeks, veg_weeks):
    draw = ImageDraw.Draw(img)
    for i in range(1, weeks + 1):
        color = veg_color if i <= veg_weeks else flower_color
        draw.rectangle([(offset_x * i) + (spacing * i),
                        offset_y + spacing, 
                        (offset_x * i) + cube_size + (spacing * i),
                        offset_y + spacing + cube_size], 
                        fill=color)

def write_text(draw, offset_tuple, text, font):
    x = offset_tuple[0]
    y = offset_tuple[1]
    # Border
    draw.text((x-1, y-1), text, font=font, fill=shadow_color)
    draw.text((x+1, y-1), text, font=font, fill=shadow_color)
    draw.text((x-1, y+1), text, font=font, fill=shadow_color)
    draw.text((x+1, y+1), text, font=font, fill=shadow_color)
    # Text 
    draw.text((x, y), text, font=font, fill=text_color)

def write_week(img, weeks, veg_weeks):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    write_text(draw, (offset_x,offset_y * 2 + spacing * 1), 'Week {}'.format(weeks), font=font)

def write_weekday(img, date):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    weekday = date.strftime('%A')
    write_text(draw, (offset_x,offset_y * 3 + spacing * 2), weekday, font=font)

def write_day(img, days):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    write_text(draw, (offset_x,offset_y * 4 + spacing * 3), 'Day {}'.format(days), font=font)

def get_date_from_string(string):
    year  = string[:4]
    month = string[4:6]
    day   = string[6:8]
    hour  = string[9:11]
    min   = string[11:13]
    dt = datetime(int(year), int(month), int(day), int(hour), int(min))
    return dt

def get_time_delta(startdate, image_date):
    return image_date - startdate

def process_image(filename,startdate,veg_weeks):
    print("[+] Processing " + filename + "...")
    image = Image.open(filename)
    date = get_date_from_string(filename[8:21])
    tdelta = get_time_delta(startdate,date)
    weeks = tdelta.days / 7 + 1
    write_week_cubes(image, weeks, veg_weeks)
    write_week(image, weeks, veg_weeks)
    write_weekday(image, date)
    write_day(image, tdelta.days)
    image.save(filename)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: {} {} {} {}'.format(sys.argv[0], 
            '[imagefile_to_be_processed.jpg]', 
            '[startdate (eg. 20180917)]', 
            '[number of vegitation weeks]'))
    else:
        filename_arg = sys.argv[1]
        startdate_arg = sys.argv[2]
        veg_weeks_arg = sys.argv[3]
        startdate = get_date_from_string(startdate_arg)
        process_image(filename_arg, startdate, int(veg_weeks_arg))
