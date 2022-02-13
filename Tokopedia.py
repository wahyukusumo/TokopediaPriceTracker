from bs4 import BeautifulSoup
import requests
import re


class Tokopedia:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

    def get_data(self):
        req_page = requests.get(self.url, headers=self.headers).text
        soup = BeautifulSoup(req_page, 'html.parser')

        return soup

    # def is_empty(self, soup):
    #     return len(soup.findAll('h4'))

    def get_product_image_url(self, soup):
        img = soup.find('div', {'class': 'magnifier'})
        return re.findall('\((.*?)\)', str(img))[0].replace('100-square', '700')

    def get_product_name(self, soup):
        return soup.find('h1').get_text()

    def get_product_price(self, soup):
        return soup.find('div', {'class': 'price'}).get_text()

# Example
def main():

    urls = [
        'https://www.tokopedia.com/evernextofficial/tas-ransel-laptop-pria-backpack-pria-dixon-tas-punggung-pria-distro-grey-black',
        'https://www.tokopedia.com/komikstore/horimiya-14',
        'https://www.tokopedia.com/jbc42harco/xp-pen-deco-01-v2-versi-2-support-android-murah-garansi-2-tahun'
    ]
    for url in urls:
        tokopedia = Tokopedia(url)
        soup = tokopedia.get_data()

        product_name = tokopedia.get_product_name(soup)
        product_price = tokopedia.get_product_price(soup)
        product_image_url = tokopedia.get_product_image_url(soup)


if __name__ == '__main__':
    main()

