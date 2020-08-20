import os
import requests


def upload_fruit(url, fruit):
        response = requests.post(url, json = fruit)
        print("Uploaded fruit with a status code of {}".format(response.status_code))


def catalog_data(description_dir):
        for text_file in os.listdir(description_dir):
                full_text_path = os.path.join(description_dir, text_file)
                file_name = os.path.splitext(text_file)[0]
                with open(full_text_path) as file:
                        fruit_dict = {}
                        keys = ['name', 'weight', 'description']
                        key_index = 0
                        image_name = "{}.jpeg".format(file_name)
                        fruit_dict['image_name'] = image_name
                        for line in file:
                                if 'lbs' in line:
                                        line = int(line.strip().replace('lbs', ''))
                                else:
                                        line = line.strip()
                                if line is not "":
                                        fruit_dict[keys[key_index]] = line
                                        key_index += 1
                        upload_fruit('http://<server IP>/fruits/', fruit_dict)


if __name__ == "__main__":
        USER = os.getenv('USER')
        description_dir = "/home/{}/supplier-data/descriptions/".format(USER)
        catalog_data(description_dir)
