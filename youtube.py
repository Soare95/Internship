from selenium import webdriver
import random


links = []

class YoutubeScrape:

    def youtube_scrape(self):
        driver = webdriver.Chrome("chromedriver.exe")
        driver.implicitly_wait(5)
        driver.get("https://www.youtube.com")
        driver.maximize_window()

        # Click on 'I agree' button
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]')\
            .click()
        youtube_video = driver.find_elements_by_xpath('//*[@id="video-title-link"]')

        for i in youtube_video:
            links.append(i.get_attribute("href"))

        # Play random youtube video
        random_link = random.choice(links)
        driver.get(random_link)

        scraping_on = True
        #Skip adds
        while scraping_on:
            try:
                skip_ads = driver.find_element_by_class_name("ytp-ad-skip-button-container")
                skip_ads.click()
                scraping_on = False
            except:
                pass