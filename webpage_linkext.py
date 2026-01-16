print("=========================================")
print("Welcome to Webpage Link Extractor\n")

from bs4 import BeautifulSoup
import requests

page = input("Enter the URL (http/https): ")
resp = requests.get(page)
soup = BeautifulSoup(resp.text, "html.parser")

for a in soup.find_all("a"):
    print(a.get("href"))

print("\n=========================================")
print("Extraction Completed")
print("Developed by sudo_0xksh")