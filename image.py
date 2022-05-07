from PIL import Image
import requests


def download(link):
    picture = requests.get(link)
    file_name = f'{link[7:-4]}.jpg'.replace('/', '_')
    file = open(f'{file_name}', 'wb')
    file.write(picture.content)
    file.close()

    return file_name


billet = Image.open(download('http://alitair.1gb.ru/test_prog_plashki/benefit.png'))
image = Image.open(download('http://alitair.1gb.ru/test_prog_plashki/106044_benefit.jpg'))


billet.paste(image, (5, 200))
billet.save('image_paste.png', quality=95)

billet.close()
image.close()
