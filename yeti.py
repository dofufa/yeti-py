## yeti.py

from PIL import Image, ImageDraw, ImageFont
import urllib.request
import qrcode
import yaml
import os

datapath = os.getenv('DATAPATH')
fontpath = os.getenv('FONTPATH')

qrdir = os.getenv('QRDIR')
ytdir = os.getenv('YTDIR')
ytqrdir = os.getenv('YTQRDIR')

with open(f'{datapath:s}') as f:
    vdo = yaml.safe_load(f)

watchurl = 'https://www.youtube.com/watch?v='

# colors
white = 255,255,255
black = 0,0,0

def mkqr(videoid):

    size = 75,75

    url = f'{watchurl:s}{videoid:s}'
    qr = qrcode.make(url)
    qr.thumbnail(size)
    qrpath = f'{qrdir:s}/qr@{videoid:s}.png'
    qr.save(qrpath)

    print(url)
    print(qrpath)

    pass


def mkytqr_bw(videoid, title):

    dims = 500,250
    qrsize = 75,75

    url = f'{watchurl:s}{videoid:s}'
    qr = qrcode.make(url)
    qr.thumbnail(qrsize)
    qr.copy()

    im = Image.new("RGB", dims, white)
    draw = ImageDraw.Draw(im)
    w, h = im.size

    ufnt = ImageFont.truetype(fontpath, 16)
    tfnt = ImageFont.truetype(fontpath, 20)

    if(len(title) > 20):
        title = title + '...'

    ## draw rectangle filled white, borderd black
    xy = (0,0)+(w-1,h-1)
    draw.rectangle(xy,fill=white,outline=black,width=4)

    boxsize = [ ( x - qrsize[0] ) // 2 for x in dims ]
    im.paste(qr,box=boxsize)

    ## annotate ytqr image
    draw.text((20, h-60), title, font=tfnt, fill=black)
    draw.text((20, h-30), url, font=ufnt, fill=black)

    ytqrpath = f'{ytqrdir:s}/ytqr@{videoid:s}.png'
    im.save(ytqrpath)

    print(url)
    print(ytqrpath)
    pass

def mkyt(videoid):
    url = f'https://i1.ytimg.com/vi/{videoid:s}/mqdefault.jpg'
    ytpath = f'{ytdir:s}/yt@{videoid:s}.jpg'
    th = urllib.request.urlopen(url)
    with open(ytpath,'wb') as output:
      output.write(th.read())

