import random
import urllib.request

def download_image(url):
    file_name = str(random.randrange(1,1000)) + ".jpg"
    urllib.request.urlretrieve(url,file_name)


download_image("https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fguardian.ng%2Fwp-content%2Fuploads%2F2017%2F08%2FOlanrewaju-kayode.jpg&f=1")