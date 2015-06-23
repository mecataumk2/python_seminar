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
import re

def print_feed_title(rss_filename):
    re_title = re.compile('(<title>.*CDATA\[)(.*)(]]></title>)')
    f = open(rss_filename, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        m = re_title.search(line)
        if m:
            print(m.group(2))

def rss_reader(rss_url):
    if os.path.isfile("darkan84.xml") == False:
        urllib.urlretrieve (rss_url, "darkan84.xml")
        print_feed_title("darkan84.xml")
        print "RSS Feed is added."
        return

    if os.path.isfile("tmp.xml"):
        os.remove("tmp.xml")

    urllib.urlretrieve (rss_url, "tmp.xml")

    before_file = open("darkan84.xml", 'r')
    before_file_tmp = open("darkan84_tmp.xml", 'w')
    line_before = before_file.readlines()
    re_pubDate = re.compile('pubDate')
    for line in line_before:
        m = re_pubDate.search(line)
        if m == None:
            before_file_tmp.write(line)
    before_file.close()
    before_file_tmp.close()

    after_file = open("tmp.xml", 'r')
    after_file_tmp = open("tmp_tmp.xml", 'w')
    line_after = after_file.readlines()
    re_pubDate = re.compile('pubDate')
    for line in line_after:
        m = re_pubDate.search(line)
        if m == None:
            after_file_tmp.write(line)
    after_file.close()
    after_file_tmp.close()

    if filecmp.cmp("darkan84_tmp.xml", "tmp_tmp.xml") == False:
        print "Update!"
        before_file = open("darkan84.xml", 'w')
        after_file = open("tmp.xml", 'r')
        lines = after_file.readlines()
        for line in lines:
            before_file.write(line)

        before_file.close()
        after_file.close()
    else:
        print "Update is not available"

    os.remove("tmp.xml")
    os.remove("tmp_tmp.xml")
    os.remove("darkan84_tmp.xml")

    print_feed_title("darkan84.xml")


rss_reader("http://blog.rss.naver.com/darkan84.xml")