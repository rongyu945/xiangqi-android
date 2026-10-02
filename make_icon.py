from PIL import Image, ImageDraw, ImageFont
import os

base = "/Volumes/TFcard/中国象棋/版本1.0.0/apk-project/app/src/main/res"
dens = {'mipmap-mdpi':48, 'mipmap-hdpi':72, 'mipmap-xhdpi':96, 'mipmap-xxhdpi':144, 'mipmap-xxxhdpi':192}

font_candidates = ["/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc", "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/PingFang.ttc", "/System/Library/Fonts/Supplemental/Songti.ttc"]
font_path = None
for fp in font_candidates:
    if os.path.exists(fp):
        font_path = fp; break
print("字体:", font_path)

def make_icon(size):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)
    r = int(size*0.20)
    d.rounded_rectangle([0,0,size-1,size-1], radius=r, fill=(179,34,28,255))
    fs = int(size*0.62)
    try:
        f = ImageFont.truetype(font_path, fs) if font_path else ImageFont.load_default()
    except Exception:
        f = ImageFont.load_default()
    bbox = d.textbbox((0,0), "帅", font=f)
    w = bbox[2]-bbox[0]; h = bbox[3]-bbox[1]
    x = (size-w)/2 - bbox[0]
    y = (size-h)/2 - bbox[1]
    d.text((x+size*0.01, y+size*0.015), "帅", font=f, fill=(120,20,16,255))
    d.text((x, y), "帅", font=f, fill=(255,250,235,255))
    return img

for dn, sz in dens.items():
    os.makedirs(f"{base}/{dn}", exist_ok=True)
    make_icon(sz).save(f"{base}/{dn}/ic_launcher.png")
    print(f"OK {dn}/{sz}")

print("图标完成")