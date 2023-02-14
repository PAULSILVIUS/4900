from bs4 import BeautifulSoup
import requests

url = "https://www.psychologytoday.com/us/therapists"
result = requests.get(url)
print(result.text)