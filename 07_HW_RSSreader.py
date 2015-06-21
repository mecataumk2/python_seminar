__author__ = 'sdlee'

# import feedparser
#
# my_rss_url = "http://blog.rss.naver.com/darkan84.xml"
# feed = feedparser.parse(my_rss_url)
#
# f = open("feed.txt", "wb")
# f.write(feed)
# f.close()
#

import urllib
import os.path
import filecmp

# def print_feed_title(rss_filename):

# def get_linecount(filename):

def rss_reader(rss_url):
    if os.path.isfile("darkan84.xml") == False:
        urllib.urlretrieve (rss_url, "darkan84.xml")
#        print print_feed_title("darkan84.xml")
        return 0

    urllib.urlretrieve (rss_url, "tmp.xml")
    if filecmp.cmp("darkan84.xml", "tmp.xml") == False:
        before_file = open("darkan84.xml", "w+")
        after_file = open("tmp.xml", "r")
        before_file = after_file
        before_file.write()
        before_file.close()
        after_file.close()
        os.remove("tmp.xml")

    # print_feed_title("darkan84.xml")



    # before_file = open("darkan84.xml", "w+")
    # after_file = open("tmp.xml", "r")
    #
    # if len(before_file.readlines()) != len(after_file.readlines()):
    #     before_file = after_file
    #     before_file.write()
    #     before_file.close()
    #     after_file.close()
    #     os.remove("tmp.xml")
    #     print_feed_title("darkan84.xml")





rss_reader("http://blog.rss.naver.com/darkan84.xml")


# file = open("darkan84.xml", "r")
# print file.readline()
# file.close()






