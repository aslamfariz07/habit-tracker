"""Copies the app icon into the generated Android project (run after `npx cap add android`)."""
import os
from PIL import Image

RES = 'android/app/src/main/res'
LEGACY = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
FOREGROUND = {'mdpi': 108, 'hdpi': 162, 'xhdpi': 216, 'xxhdpi': 324, 'xxxhdpi': 432}

icon = Image.open('www/icons/icon-512.png').convert('RGBA')
mask = Image.open('www/icons/maskable-512.png').convert('RGBA')

for density, px in LEGACY.items():
    folder = f'{RES}/mipmap-{density}'
    if not os.path.isdir(folder):
        continue
    for name in ('ic_launcher.png', 'ic_launcher_round.png'):
        icon.resize((px, px), Image.LANCZOS).save(f'{folder}/{name}')
    fpx = FOREGROUND[density]
    mask.resize((fpx, fpx), Image.LANCZOS).save(f'{folder}/ic_launcher_foreground.png')

print('App icons updated')
