from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from chromedriver_py import binary_path  # Import binary_path from chromedriver_py

# Set up WebDriver using chromedriver-py
service = Service(binary_path)
driver = webdriver.Chrome(service=service)

def scrape_imdb_reviews(url):
    driver.get(url)
    reviews = []
    
    while True:
        # Wait for reviews to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.text.show-more__control'))
        )
        
        # Scrape reviews
        review_elements = driver.find_elements(By.CSS_SELECTOR, 'div.text.show-more__control')
        summary_elements = driver.find_elements(By.CSS_SELECTOR, 'a.title')
        rating_elements = driver.find_elements(By.CSS_SELECTOR, 'span.rating-other-user-rating')
        
        for summary, rating in zip(summary_elements, rating_elements):
            summary_text = summary.text.strip()
            rating_text = rating.find_element(By.CSS_SELECTOR, 'span').text.strip()
            rating_text = f"{rating_text}/10"  # Format the rating as 'X/10'
            reviews.append({'summary': summary_text, 'rating': rating_text})
        
        # Check for the "Load More" button
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.ipl-load-more__button'))
            )
            load_more_button.click()
            
            # Optionally wait for the loader to disappear
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, 'svg.ipl-dot-loader'))
            )
            
            # Optional: Add a delay to allow new reviews to load
            time.sleep(3)
        except Exception as e:
            print(f'No more reviews to load or an error occurred: {e}')
            break

    driver.quit()
    return reviews

# Example usage
imdb_url = 'https://www.imdb.com/title/tt6263850/reviews?ref_=tt_ql_3'
reviews = scrape_imdb_reviews(imdb_url)

# Save to DataFrame
df = pd.DataFrame(reviews, columns=['summary', 'rating'])
df.to_csv('imdb_reviews_summary_and_ratings.csv', index=False)
