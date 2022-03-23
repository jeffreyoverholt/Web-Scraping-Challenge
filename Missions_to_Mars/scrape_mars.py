
import marshal
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time



def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA Mars News
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Title
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_title

    # Paragraph Text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    news_p


    # JPL Mars Space Images
    JPL_Mars_URL = 'https://spaceimages-mars.com'
    browser.visit(JPL_Mars_URL)


    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()



    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # img_soup


    # find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    img_url_rel


    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    img_url


    # Mars Facts


    Mars_facts_URL = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(Mars_facts_URL)
    tables



    df = tables[0]
    df.columns = ['Facts', 'Mars', 'Earth']



    df = df.drop(labels=0, axis=0)



    df.set_index("Facts", inplace = True)


    Mars_facts_HTML = df.to_html().replace('\n','')


    # Mars Hemispheres


    hemisphere_URL = 'https://marshemispheres.com/'
    browser.visit(hemisphere_URL)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')



    hemisphere_page = soup.find_all('div', class_ = 'item')



    hemi_href = []
    for row in hemisphere_page:
        hemi_href.append( hemisphere_URL + (row.find('a', class_='itemLink product-item')['href']))
    hemi_href



    hemi_images_url = []
    for url in hemi_href:
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h2', class_ = 'title').text
        image_url = hemisphere_URL + soup.find('img', class_ = 'wide-image')['src']
        hemi_images_url.append({'title': title, 'img_url': image_url})
    hemi_images_url


    #Store Data in Dictionary
    mars = {
        "news_title": news_title,
        "news_p": news_p,
        "Featured Image URL": img_url,
        "Fact Table": Mars_facts_HTML,
        "Hemisphere Images": hemi_images_url
    }

    # Close Browser
    browser.quit()

    # Return results
    return mars








