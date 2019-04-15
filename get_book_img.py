from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup

def img_from_goodreads(goodreads_book_id):
    """Parse Goodreads book display page to get image URL"""
    url_base = 'https://www.goodreads.com/book/show/'
    book_url = url_base+str(goodreads_book_id)
    url_response = requests.get(book_url)
    soup = BeautifulSoup(url_response.text, 'html.parser')
    img_url = soup.find(id="coverImage")['src']
    return img_url


def get_book_img(goodreads_book_id,img_url,resize=False):
    """Get book image from assets URL or by parsing Goodreads html"""
    if img_url:
        if "nophoto" in set(img_url.split("/")):
            img_url = img_from_goodreads(goodreads_book_id)
        else:
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
    else:
        img_url = img_from_goodreads(goodreads_book_id)
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    if resize:
        if img.size != (98, 146)
        img = img.resize((98, 146))
    return(img)
