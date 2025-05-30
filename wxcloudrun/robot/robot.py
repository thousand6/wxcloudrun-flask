from ..werobot.robot import WeRoBot
from ..werobot.replies import ImageReply
from ..dao.mapper import get_content
from PIL import Image, ImageDraw, ImageFont
import uuid 
import requests
from io import BytesIO
from loguru import logger
import textwrap

robot = WeRoBot()

@robot.text
def get_duties(message):
    try:
        return get_content(message.content)
        # if success:
        #     image_bytes = BytesIO()
        #     text_to_image(content, image_path=image_bytes)
        #     image_bytes.seek(0)
        #     media_id = upload_image(image_bytes)
        #     return ImageReply(message, media_id=media_id)
        #     # return media_id
        # return content
    except:
        logger.exception('')
        return get_content(message.content)



def text_to_image(text, image_path, font_path='msyh.ttf', font_size=40):
    #创建字体对象
    font = ImageFont.truetype(font_path, font_size)
    
    # 将文本分行
    lines = []
    for segment in text.split('\n'):
        lines.extend(textwrap.wrap(segment, width=400 // font_size * 2))
        lines.append('')
    line_height = font.getsize('A')[1]

    # 计算图像大小
    image_height = (line_height + 10) * len(lines) + 40
    image_width = max(font.getsize(line)[0] for line in lines) + 40
    # 创建白色背景的图像
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    # 绘制文本
    y_offset = 20
    for line in lines:
        draw.text((20, y_offset), line, font=font, fill='black')
        y_offset += line_height + 5
    
    # 保存图像
    image.save(image_path, format='PNG')

def upload_image(image):
    url = 'http://api.weixin.qq.com/cgi-bin/media/upload'
    files = {'media': (str(uuid.uuid4()) + '.png', image)}
    response = requests.post(url, params={'type':'image'}, files=files)
    return response.json()['media_id']

