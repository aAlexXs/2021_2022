from PIL import Image

def bilde():

  datne = '831180b859f0ef9850f8669356fd50461b3e5f8f.jpg'
  with Image.open(datne) as im:
      print(datne, im.format,f'){im.size}x{im.mode}')
      izmers = (10000,10000)
      im.thumbnail(izmers)
      im.save('maza_bilde.jpg', im.format)
bilde()

