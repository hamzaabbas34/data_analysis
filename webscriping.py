import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup 
# ping www.similarweb.com
headers = {'user_agent': 'Mozilla/5.0(Windows NT 6.3 Win64; x64)AppleWebkit/537.36(KHTML , like Gecko Chrome/80.0.3987.162 Safari/537.36)'}
response= requests.get('https://www.similarweb.com/website/ambitionbox.com/competitors/' , headers=headers).text
print(response)