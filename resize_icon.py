from PIL import Image
import os

SRC = "/Users/rongyu/Downloads/undefined_57313393791011330_undefined_tos-cn-i-a9rns2rl98_rc_gen_image_57d850259f3746deb45d7c1339be22ed.jpeg.png"
BASE = "/Users/rongyu/ChinaChess-xiangqi-build/app/src/main/res"
dens = {'mipmap-mdpi':48, 'mipmap-hdpi':72, 'mipmap-xhdpi':96, 'mipmap-xxhdpi':144, 'mipmap-xxxhdpi':192}

img = Image.open(SRC)
print("源图:", img.size, img.mode)
if img.mode != 'RGBA':
    img = img.convert('RGBA')

for dn, sz in dens.items():
    d = os.path.join(BASE, dn)
    os.makedirs(d, exist_ok=True)
    img.resize((sz, sz), Image.LANCZOS).save(os.path.join(d, "ic_launcher.png"))
    print(f"OK {dn}/{sz}", os.path.join(d, "ic_launcher.png"))

print("图标替换完成")