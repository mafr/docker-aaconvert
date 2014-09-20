#! /usr/bin/env python3
import io
import sys
import argparse
import urllib.request
from PIL import Image
import aalib


ap = argparse.ArgumentParser(description='Convert image to ASCII art')
ap.add_argument('-c', '--columns', default=80, type=int,
    help='Display width in characters')
ap.add_argument('-r', '--rows', default=40, type=int,
    help='Display height in characters')
ap.add_argument('url', metavar='URL', nargs=1,
    help='the URL to read the image from')
args = ap.parse_args()

screen = aalib.AsciiScreen(width=args.columns, height=args.rows)

res = urllib.request.urlopen(args.url[0])
raw = io.BytesIO(res.read())

image = Image.open(raw).convert('L').resize(screen.virtual_size)

screen.put_image((0, 0), image)

print(screen.render())
