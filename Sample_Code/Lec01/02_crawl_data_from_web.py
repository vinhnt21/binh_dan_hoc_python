import requests
from bs4 import BeautifulSoup
import os
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def reformat_text(text):
    # Split the text into lines if it's a string
    if isinstance(text, str):
        lines = text.splitlines()
    else:
        lines = text
    
    # Remove blank lines and tab characters
    reformatted_lines = [line.strip().replace('\t', '') for line in lines if line.strip()]
    
    # Join the lines back together
    reformatted_text = '\n'.join(reformatted_lines)
    
    return reformatted_text

def crawl_and_save(url, output_file):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    time.sleep(2)
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        logger.info(f"============================\nCrawling URL: {url}")
        
        content_parts = []
        elements = {
            'title': soup.find('h1', class_='title-head'),
            'author': soup.find('span', class_='author'),
            'price_box': soup.find('div', class_='price-box'),
            'book_info': soup.find('aside', class_='book-info'),
            'product_getcontent': soup.find('div', class_='product_getcontent')
        }
        
        for name, element in elements.items():
            if element:
                content_parts.append(f"{name.upper()}:\n{element.get_text(strip=True)}")
            else:
                logger.warning(f"{name.capitalize()} element not found on the page")
        
        if not content_parts:
            logger.warning("No content found on the page")
            return
        
        content = '\n\n'.join(content_parts)
        content = reformat_text(content)
        content = f"{'='*50}\nURL: {url}\n{'='*50}\n\n{content}\n\n"
        
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(content)
        
    except requests.RequestException as e:
        logger.error(f"Failed to retrieve the web page: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)


output_file = "02_crawl_data_from_web_output.txt"

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the output file path to be in the same directory as the script
output_file_path = os.path.join(script_dir, output_file)

urls_file = "02_crawl_data_from_web_urls.txt"
urls_file_path = os.path.join(script_dir, urls_file)

try:
    with open(urls_file_path, "r", encoding="utf-8") as file:
        urls = file.read().splitlines()
except FileNotFoundError:
    logger.warning(f"File '{urls_file}' not found. Please enter a URL manually.")
    url = input("Enter a URL to crawl: ").strip()
    urls = [url] if url else []

if urls:
    for url in urls:
        crawl_and_save(url.strip(), output_file_path)
        logger.info(f"Data saved to '{output_file}'")
else:
    logger.error("No URLs provided. Exiting the script.")
