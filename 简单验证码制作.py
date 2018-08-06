
# 验证码制作
from django.http import HttpResponse

def verifyCode(self):
    from PIL import Image, ImageDraw,ImageFont
    import random

    bgColor = (random.randrange(50,100),random.randrange(50,100),0)
    width = 100
    height = 25
    # 创建画布
    image = Image.new('RGB', (width,height), bgColor)
    # 构造字体对象
    font = ImageFont.truetype("simsun.ttc", 26, index=1)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 创建文本内容
    text = '01234567890ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
    # 创建存储session的列表 
    textcode = []
    # 绘制字符
    for i in range(4):
    	textcode1 = text[random.randrange(0,len(text))]
    	textcode += textcode1
        draw.text((i*25,0),
                  textcode1,
                  (255,255,255),
                  font)
    # 存储session
    request.session['code1'] = textcode
    # 保存到内存流中
    import io
    buf = io.BytesIO()
    image.save(buf,'png')
    # 将内存流中的内容输出到客户端
    response = HttpResponse(buf.getvalue(),'image/png')
    return response
        


if __name__ == '__main__':
    verifyCode()
