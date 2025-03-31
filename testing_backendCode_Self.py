import requests
from bs4 import BeautifulSoup

# Amazon Product URL (Replace with actual URL)
url = "https://www.amazon.in/Redmi-Note-14-5G-Dimensity/dp/B0DPFV3T4V?th=1"

# Add headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Use `select_one` to get the product title
    title_tag = soup.select_one("#productTitle")
    
    if title_tag:
        amazon_title = title_tag.get_text(strip=True)
        print("Product Title:", amazon_title)
    else:
        print("Product title not found! The structure might have changed.")
else:
    print(f"Request failed with status code: {response.status_code}")
