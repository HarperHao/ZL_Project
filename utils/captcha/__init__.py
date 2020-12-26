"""
Author   : HarperHao
TIME    ： 2020/12/26
FUNCTION:  图片验证码
"""
from PIL import Image, ImageDraw, ImageFont
import random
import string


class Captcha:
    # 生成几位数的验证码
    number = 4
    # 验证码图片的宽度和高度
    size = (100, 30)
    # 字体大小
    fontsize = 25
    # 干扰线条数量
    line_number = 3
    # 噪点的数目
    point_number = 300
    # 构建验证码源文本
    SOURCE = string.ascii_letters + string.digits

    # 生成验证码
    @classmethod
    def gene_graph_capthca(cls):
        width, height = cls.size
        # 画布
        image = Image.new('RGBA', (width, height), cls.__gene_random_color(0, 100))
        # 字体
        font = ImageFont.truetype(cls.__gene_random_font(), cls.fontsize)
        # 画笔
        draw = ImageDraw.Draw(image)
        # 验证码文本
        text = cls.gene_text(cls.number)
        # 验证码字体的大小
        font_width, font_height = font.getsize(text)
        # 绘制验证码
        draw.text(((width - font_width) / 2, (height - font_height) / 2-2), text, font=font,
                  fill=cls.__gene_random_color(start=150, end=255))
        # 绘制干扰线
        for x in range(0, cls.line_number):
            cls.__gene_line(draw, width, height)
        # 绘制噪点
        cls.__gene_points(draw, width=width, height=height, number=cls.point_number)
        return (text, image)

    # 生成噪点
    @classmethod
    def __gene_points(cls, draw, width, height, number):
        random.seed()
        for i in range(number):
            w = random.randint(0, width)
            h = random.randint(0, height)
            draw.point((w, h), fill=cls.__gene_random_color())

    # 生成干扰线
    @classmethod
    def __gene_line(cls, draw, width, height):
        begin_point = (random.randint(0, width), random.randint(0, height))
        end_point = (random.randint(0, width), random.randint(0, height))
        draw.line([begin_point, end_point], fill=cls.__gene_random_color(), width=2)

    # 生成验证码文本
    @classmethod
    def gene_text(cls, number):
        # temp是一个列表
        temp = random.sample(cls.SOURCE, number)
        captcha_text = ''.join(temp)
        return captcha_text

    # 随机产生验证码的字体
    @classmethod
    def __gene_random_font(cls):
        fonts = [
            'Courgette-Regular.ttf',
            'LHANDW.TTF',
            'Lobster-Regular.ttf',
            'verdana.ttf'
        ]
        font = random.choice(fonts)
        #print('选取的字体为{}'.format(font))
        return 'utils/captcha/' + font

    # 随机生成颜色RGB值(R,G,B)
    @classmethod
    def __gene_random_color(cls, start=0, end=255):
        random.seed()
        return (
            random.randint(start, end),
            random.randint(start, end),
            random.randint(start, end)
        )
