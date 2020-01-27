import requests
from bs4 import BeautifulSoup
import urllib


def run():
    image_name_url = str(input('Pega el URL de la imagen: '))
    for i in range(0,1):
        response = requests.get(image_name_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        #image_container = soup.find(class='KL4Bh')

        image_container = soup.findAll('div')
        print(image_container)
        
        
        
        image_url = image_container.find('img')['src']
#        image_name = image_container.find('img')['alt']
#        image_name = image_url.split('/')[-1]
#        print('{}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url))




if __name__ == "__main__":
    run()