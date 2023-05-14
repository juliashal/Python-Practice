from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://stitchpalettes.com/the-embroidery-thread-palette-generator/"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

color_codes = []
color_hex = []

for color in soup.find_all(class_='thread-image'):
    color_codes.append(color.text.strip())
    color_hex.append(color['style'].replace(
        "background-color:", "").replace(";", ""))

color_dict = {'Color': color_codes, 'HEX': color_hex}

df = pd.DataFrame(color_dict)

df.to_csv("colors_dictionary", index=False)
