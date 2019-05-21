#!/usr/bin/env python
# coding: utf-8

# scrape the specified sites for information
# assign the text to variables that you can reference later

# import dependencies
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import requests
from splinter import Browser
import os
import time
import datetime


# define path for chromedriver.exe
def init_browser():
    
    executable_path = {'executable_path':'C:/Program Files/Chromedriver/chromedriver.exe'}

    return Browser('chrome', **executable_path, headless=False)

def mars_scrape():
    
    # create empty dictionary to store Mars information
    mars_dict = dict()

# ## News - NASA Mars
#----------------------------------------------------
    # collect latest news title and paragraph text
    # nasa url scrape - retrieve page
    nasa_url = 'https://mars.nasa.gov/news/'
    # response = requests.get(nasa_url)
    browser = init_browser()
    browser.visit(nasa_url)

    nasa_html = browser.html

    # create bs object, parse
    nasa_soup = BeautifulSoup(nasa_html, 'html.parser')
    # print(soup.prettify())

    try:
        news_title = nasa_soup.find('ul', class_='item_list').find('li',class_='slide').find('div', class_="content_title").text
        
        news_body = nasa_soup.find('ul', class_='item_list').find('li', class_='slide').find('div', class_="article_teaser_body").text

        print("The news title is " + news_title)
        print("The news body is " + news_body)

    except AttributeError as Atterror:
        print (Atterror)
    
    mars_dict["Mars_news_title"] = news_title
    mars_dict["Mars_news_body"] = news_body
    print(mars_dict)


   

# ## JPL Mars
#-----------------------------------------------------------
    # click on the link for 'more info'
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    time.sleep(2)
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    time.sleep(5)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    full_img_html = browser.html
    soup_image = BeautifulSoup(full_img_html, 'html.parser')
    full_img_href = soup_image.find('figure', class_='lede').a['href']

    featured_image_url = 'https://www.jpl.nasa.gov' + full_img_href
    print(featured_image_url)

    # add url to mars_dict
    mars_dict["Mars_featured_image_url"] = featured_image_url
    print(mars_dict)


# ## Mars Weather Tweet
#--------------------------------------------------------------


    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter_url)
    mars_html = browser.html

    mars_weather_soup = BeautifulSoup(mars_html, 'html.parser')

    mars_weather_tweet = mars_weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
    mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
    mars_weather



    # add weather tweet to dictionary
    mars_dict["Mars_Weather_tweet"] = mars_weather
    print(mars_dict)


# ## Mars Facts
#---------------------------------------------------------------

    facts_url = 'http://space-facts.com/mars/'

    mars_facts_df = pd.read_html(facts_url)[0]
    mars_facts_df.columns=['description', 'value']
    mars_facts_df.set_index('description', inplace=True)
    mars_facts_df

    mars_facts_df.to_html("mars_facts.html", index=False)

    # create table for mars facts and add to mars_dict
    mars_facts_html = mars_facts_df.to_html(classes='description table table-striped')
    mars_dict["Mars_facts_table"] = mars_facts_html
    print(mars_dict)


# ## Mars hemispheres
#----------------------------------------------------------------


    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)
    time.sleep(10)
    usgs_html = browser.html
    usgs_soup = BeautifulSoup(usgs_html, 'html.parser')


    class_collap_results = usgs_soup.find('div', class_='collapsible results')
    hemisphere_items = class_collap_results.find_all('div', class_='item')
    print(hemisphere_items)

    # loop through to find images
    # hemisphere_image_urls = []

    # First, get a list of all of the hemispheres
    # links = browser.find_by_css("a.product-item h3")

    # Next, loop through to find title and image urls
    hemis_img_urls_list = list()
    img_urls_list = list()
    title_list = list()

    for h in hemisphere_items:
        h_title = h.h3.text
        title_list.append(h_title)

        h_href = 'https://astrogeology.usgs.gov' + h.find(
            'a', class_='itemLink product-item')['href']
        print(h_title, h_href)

        browser.visit(h_href)
        time.sleep(5)

        html5 = browser.html
        soup_img = BeautifulSoup(html5, 'html.parser')
        h_img_url = soup_img.find('div', class_='downloads').find(
            'li').a['href']
        print('h_img_url' + h_img_url)
        img_urls_list.append(h_img_url)

        hemisphere_dict = dict()
        hemisphere_dict['title'] = h_title
        hemisphere_dict['image_url'] = h_img_url
        hemis_img_urls_list.append(hemisphere_dict)

    print(hemis_img_urls_list)
    # print(title_list)
    # print(img_urls_list)

    # add image urls to mars_dict
    mars_dict['Hemisphere_image_urls'] = hemis_img_urls_list
    print(mars_dict)


    # generate date time and store in dict
    current_datetime = datetime.datetime.utcnow()
    mars_dict["Date_time"] = current_datetime
    print(mars_dict)


    mars_final_dict = {
        "News_Title": mars_dict["Mars_news_title"],
        "News_Summary" :mars_dict["Mars_news_body"],
        "Featured_Image" : mars_dict["Mars_featured_image_url"],
        "Weather_Tweet" : mars_dict["Mars_Weather_tweet"],
        "Facts" : mars_facts_html,
        "Hemisphere_Image_urls": hemis_img_urls_list,
        "Date" : mars_dict["Date_time"],
    }
    return mars_final_dict

# mars_data_result = mars_scrape()
# print(mars_data_result)



