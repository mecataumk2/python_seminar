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
import os
import filecmp
import re
import hashlib

def string_to_md5(string):
    md5 = hashlib.md5(string)
    return md5.hexdigest()

def print_feed_title(rss_filename):
    re_title = re.compile('(<title>.*CDATA\[)(.*)(]]></title>)')
    f = open(rss_filename, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        m = re_title.search(line)
        if m:
            print"Title: ", (m.group(2))

def remove_taglines(filename, tagname):
    file = open(filename, 'r')
    filename_tmp = filename + '_tmp'
    file_tmp = open(filename_tmp, 'w')
    lines_file = file.readlines()

    re_pubDate = re.compile(tagname)

    for line in lines_file:
        m = re_pubDate.search(line)
        if m == None:
        # if not m:
            file_tmp.write(line)
    file.close()
    file_tmp.close()
    return filename_tmp

def rss_reader(rss_url, filename):
    # print filename_tmp                                  #testcode,testcode
    # if os.path.isfile("darkan84.xml") == False:



    if not os.path.isfile(filename):                                 # when downloaded file is not exist
        urllib.urlretrieve (rss_url, filename)
        print "New RSS Feed is created succesfully."
        print_feed_title(filename)
        return

    if os.path.isfile("tmp.xml"):                                   # when tempolory file is exist (pre check. Is this not mandatory?.I need some test.)
        os.remove("tmp.xml")

    urllib.urlretrieve (rss_url, "tmp.xml")

    no_pubDate_filename = remove_taglines(filename, 'pubDate')                                        # Remove line using tag "<pubDate>" for file compare.
    no_pubDate_tmp = remove_taglines("tmp.xml", 'pubDate')

    # downloaded_file = open(filename, 'r')                               # Remove line using tag "<pubDate>" for file compare.
    # downloaded_file_tmp = open("downloaded_file_tmp.xml", 'w')
    # lines_downloaded_file = downloaded_file.readlines()
    # re_pubDate = re.compile('pubDate')
    # for line in lines_downloaded_file:
    #     m = re_pubDate.search(line)
    #     # if m == None:
    #     if not m:
    #         downloaded_file_tmp.write(line)
    # downloaded_file.close()
    # downloaded_file_tmp.close()

    # after_file = open("tmp.xml", 'r')
    # after_file_tmp = open("tmp_tmp.xml", 'w')
    # line_after = after_file.readlines()
    # re_pubDate = re.compile('pubDate')
    # for line in line_after:
    #     m = re_pubDate.search(line)
    #     if m == None:
    #         after_file_tmp.write(line)
    # after_file.close()
    # after_file_tmp.close()

    if not filecmp.cmp(no_pubDate_filename, no_pubDate_tmp):
        print "Update!"                                             # move tmp.xml to filename
        downloaded_file = open(filename, 'w')
        new_file = open("tmp.xml", 'r')
        lines = new_file.readlines()
        for line in lines:
            downloaded_file.write(line)

        downloaded_file.close()
        new_file.close()
    else:
        print "Update is not available"

    os.remove("tmp.xml")
    os.remove(no_pubDate_filename)
    os.remove(no_pubDate_tmp)

    print_feed_title(filename)

# rss_reader("http://onenable.tumblr.com/rss")
# rss_reader("http://blog.rss.naver.com/darkan84.xml")
# url = raw_input('Enter RSS Feed url : ')
url = "http://blog.rss.naver.com/darkan84.xml"
filename = string_to_md5(url)
rss_reader(url, filename)