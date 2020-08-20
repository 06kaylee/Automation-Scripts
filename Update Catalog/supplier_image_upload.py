import requests
import os

USER = os.getenv('USER')
images_path = '/home/{}/supplier-data/images/'.format(USER)
url = "http://<server IP>/upload/"

# post each image in the directory to the server website
for path in os.listdir(images_path):
        if path.endswith('.jpeg'):
                full_path = os.path.join(images_path, path)
                with open(full_path, mode = 'rb') as img:
                        response = requests.post(url, files={'file':img})
                        print(response.status_code)
