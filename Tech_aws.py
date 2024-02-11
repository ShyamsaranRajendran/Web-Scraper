import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_page(link):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            print("Image Tag:")
            print(img_tag)
            print("Image Source (src):", img_tag.get('src'))
            print("Alt Text:", img_tag.get('alt'))
            print("\n" + "=" * 50 + "\n")  
    else:
        print(f"Failed to fetch the webpage at {link}. Status code:", response.status_code)

main_page_url = 'http://web-scrapper-api.s3-website.ap-south-1.amazonaws.com/'  
main_page_response = requests.get(main_page_url)

if main_page_response.status_code == 200:
    main_page_soup = BeautifulSoup(main_page_response.content, 'html.parser')

    all_links = main_page_soup.find_all('a', href=True)

    absolute_links = [urljoin(main_page_url, link['href']) for link in all_links]

    for link in absolute_links:
        try:
            scrape_page(link)
        except requests.RequestException as e:
            print(f"Error processing {link}: {e}")
else:
    print("Failed to fetch the main page. Status code:", main_page_response.status_code)
