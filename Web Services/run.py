import pathlib
import requests 

text_files = pathlib.Path("./text_files").iterdir()

def upload_feedback(url, review):
    response = requests.post(url, json = review)
    print(f"Uploaded review with a status code of {response.status_code}")


for text_file in text_files:
    with open(text_file) as file:
        keys = ["title", "name", "date", "feedback"]
        review_dict = {}
        key_index = 0
        for line in file:
            review_dict[keys[key_index]] = line.strip()
            key_index += 1
        upload_feedback("http://<IP Address>/feedback/", review_dict)
