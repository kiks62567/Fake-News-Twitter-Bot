import tweepy
from textblob import TextBlob
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import time


start_time = time.time()


def main():
    # Uses tweepy to access twitter to allow the ability to tweet
    consumer_key = #consumer key
    consumer_secret = #consumer secret

    access_token = #enter access token
    access_token_secret = #enter access password

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Stores URL
    my_url = 'https://www.snopes.com/category/facts/'

    # Opening connection, grab the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # parse
    page_soup = soup(page_html, "html.parser")

    # get specific part of html
    containers = page_soup.findAll("a", {"class": "article-link"})

    title = [15]
    url = [15]
    validity = [15]

    # Grabs title from Snopes web page
    for container in containers[:10]:
        try:
            # Grabs the title of article
            x = 0
            title.insert(x, str(container.h2.text))
        except(NameError, IndexError, AttributeError):
            print("Error")
        # print(title[x])
        x += 1

    # Grabs validity from Snopes web page
    for container in containers[:10]:
        try:
            validity_container = container.findAll("span", {"itemprop": "reviewRating"})
            x = 0
            for valid in validity_container:
                validity.insert(x, valid.span.text)
        except(NameError, IndexError, AttributeError):
            print("Error")
        x += 1

    # Creates link list that stores all url on web page
    links = []
    # URL's we are actually interested in start here
    ind = 94

    # # Grabs url from Snopes web page
    for container in containers[:10]:
        try:
            # Grabs all url tags on web page
            y = 0
            for link in page_soup.findAll('a', attrs={'href': re.compile("^https://www.snopes.com")}):
                links.append(link.get('href'))
            # Iterates to corresponding url
            url.insert(y, links[ind])
            ind += 1
        except(NameError, IndexError, AttributeError):
            print("Error")
    # Test print to make sure three
    # for x in range(10):
    #    print(title[x] + " " + validity[x] + " " + url[x])
    # Creates tweet with articles found false by Snopes
    for x in range(10):
        if validity[x] in ('FALSE', 'MOSTLY FALSE'):
            api.update_status("FAKE NEWS ALERT!! \n" +
                              title[x] + " " + url[x]
                              + " #FAKENEWS #RESISTTRUMP #RESIST"
                                " #STOPHATE #REALNEWS #TRUMP "
                                "#POLITICS #RESIST #NEWS"
                                " #RUSSIA" "ANTIRUSSIA" 
                                " #INVESTIGATE"
                              )
        else:
            continue
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
