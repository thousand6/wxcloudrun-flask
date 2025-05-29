from ..werobot.robot import WeRoBot
from ..werobot.replies import ImageReply
from ..dao.mapper import get_content
from PIL import Image, ImageDraw, ImageFont
import uuid 
import requests
from io import BytesIO

robot = WeRoBot()

@robot.text
def get_duties(message):
    content = get_content(message.content)
    image_bytes = BytesIO()
    text_to_image(content, image_path=image_bytes)
    media_id = upload_image(image_bytes)
    return ImageReply(message, media_id=media_id)

@robot.text
def default_repley(message):
    return '出错了，请稍后再试'



def text_to_image(text, font_path='Kaiti.ttf', font_size=20, image_path='output.png'):
    #创建字体对象
    font = ImageFont.truetype(font_path, font_size)
    
    # 计算文字的宽高
    text_width, text_height = font.getsize(text)
    
    # 创建白色背景的图像
    image = Image.new('RGB', (text_width, text_height), 'white')
    draw = ImageDraw.Draw(image)
    
    # 绘制黑色文字
    draw.text((0, 0), text, font=font, fill='black')
    
    # 保存图像
    image.save(image_path, format='PNG')

def upload_image(image):
    url = 'http://api.weixin.qq.com/cgi-bin/media/upload'
    files = {'media': (str(uuid.uuid4()) + '.png', image, 'image/png')}
    response = requests.post(url, params={'type':'image'}, files=files)
    return response.json().get('media_id')

