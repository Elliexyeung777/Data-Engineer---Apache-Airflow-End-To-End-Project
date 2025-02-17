import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Job Titles:")
for job in soup.find_all("h2", class_="jobTitle"):
    print(job.text.strip())