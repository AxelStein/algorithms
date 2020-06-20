import concurrent.futures
import requests
import os


def download(url):
    content = requests.get(url).content
    name = url.split('/')[-1]
    with open(os.path.join(r"C:\Users\alex\Desktop", name), 'wb') as file:
        file.write(content)
        print(f'{name} was downloaded')


urls = []

with open('urls.txt') as f:
    for l in f:
        urls.append(l.rstrip())

print(urls)
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, urls)
