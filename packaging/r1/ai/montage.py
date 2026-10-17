import sys
from PIL import Image, ImageDraw
eps=sys.argv[2:]; out=sys.argv[1]
w,h=384,256
im=Image.new('RGB',(6*w,len(eps)*(h+16)),'white'); d=ImageDraw.Draw(im)
for r,e in enumerate(eps):
    for c,v in enumerate('abcdef'):
        try: im.paste(Image.open(f'raw/{e}-{v}.png').convert('RGB').resize((w,h)),(c*w,r*(h+16)))
        except FileNotFoundError: pass
        d.text((c*w+4,r*(h+16)+h+2),f'{e}-{v}',fill='black')
im.save(out,quality=82)
