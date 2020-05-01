from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    return Browser('chrome', **executable_path, headless=False, options = options)


def scrape():
    browser = init_browser()

    # Visit webpage and get NASA Mars News
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    #Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
    news_title = browser.find_by_css('div[class="content_title"] a', wait_time=2).text
    news_p = browser.find_by_css('div[class="article_teaser_body"]').text

    # Visit JPL Space Images
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Click image to maximize
    browser.find_by_id('full_image').click()

    # Get featured image url
    featured_image_url = browser.find_by_id('fancybox-lock').first.find_by_tag('img')['src']

    #Visit Twitter for Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    # Get Mars Weather Data
    mars_weather = browser.find_by_tag('article').find_by_css('span[class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]')[4].text

    # Visit Space Facts and read table facts to html table
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description', 'Value']
    df.set_index('Description', inplace=True)
    html_table_df = df.to_html()
    html_table = html_table_df.replace('\n', '') 

    # Vist webpage to get images for Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find Hemisphere title containing the hemisphere name.
    title1 = browser.find_by_css('div[class="item"]')[0].find_by_tag('h3').text
    title2 = browser.find_by_css('div[class="item"]')[1].find_by_tag('h3').text
    title3 = browser.find_by_css('div[class="item"]')[2].find_by_tag('h3').text
    title4 = browser.find_by_css('div[class="item"]')[3].find_by_tag('h3').text

    # Browse through webpage to get image urls
    link1 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[1]/div/a/h3').click()
    open1 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/a').click()
    img1 = browser.find_by_css('div[class="downloads"]').find_by_tag('a')['href']

    back1 = browser.back()

    link2 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[2]/div/a/h3').click()
    open2 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/a').click()
    img2 = browser.find_by_css('div[class="downloads"]').find_by_tag('a')['href']

    back2 = browser.back()

    link3 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[3]/div/a/h3').click()
    open3 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/a').click()
    img3 = browser.find_by_css('div[class="downloads"]').find_by_tag('a')['href']

    back3 = browser.back()

    link4 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[4]/div/a/h3').click()
    open4 = browser.find_by_xpath('/html/body/div[1]/div[1]/div[2]/a').click()
    img4 = browser.find_by_css('div[class="downloads"]').find_by_tag('a')['href']

    # Set titles and images to a list of dictionaries

    hemisphere_image_urls = [
    {"title1": title1, "img_url1": img1},
    {"title2": title2, "img_url2": img2},
    {"title3": title3, "img_url3": img3},
    {"title4": title4, "img_url4": img4}
     ]

    mars_data = {
        "news_title": news_title,
        "news_text": news_p,
        "featured_img": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts" : html_table,
        "hemisphere_images": hemisphere_image_urls
    }

    browser.quit()

    return mars_data