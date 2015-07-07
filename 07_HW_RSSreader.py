__author__ = 'sdlee'

import urllib
import os
import filecmp
import re
import hashlib
import xml.etree.ElementTree as ET


def string_to_md5(string):
    md5 = hashlib.md5(string)
    return md5.hexdigest()

def print_site_title(rss_filename):
    tree = ET.parse(rss_filename)
    root = tree.getroot()
    channel = root.find("channel")
    site_title = channel.findtext("title")
    print "Site title : ", site_title

def print_feed_title(rss_filename):
    tree = ET.parse(rss_filename)
    root = tree.getroot()
    for iterator_item in root.iter("item"):
        print "Item title : ", iterator_item.findtext("title")



def remove_element(filename, element):
    filename_tmp = filename + '_tmp'
    tree = ET.parse(filename)
    root = tree.getroot()
    channels = root.findall("channel")
    for parents in channels:
        for children in parents.findall("pubDate"):
            parents.remove(children)
    tree.write(filename_tmp)
    return filename_tmp

def rss_reader(rss_url, filename):

    if not os.path.exists(filename):                                 # when downloaded file is not exist
        urllib.urlretrieve (rss_url, filename)
        print "New RSS Feed is created succesfully."
        print_site_title(filename)
        print_feed_title(filename)
        return

    urllib.urlretrieve (rss_url, "tmp.xml")

    no_pubDate_filename = remove_element(filename, "pubDate")
    no_pubDate_tmp = remove_element("tmp.xml", "pubDate")

    # no_pubDate_filename = remove_element(filename, 'pubDate')                                        # Remove element "<pubDate>" for file compare.
    # no_pubDate_tmp = remove_element("tmp.xml", 'pubDate')

    if not filecmp.cmp(no_pubDate_filename, no_pubDate_tmp):
        print "Update!\n"                                             # move tmp.xml to filename.   ##### Move function is exist in library(os)?
        downloaded_file = open(filename, 'w')
        new_file = open("tmp.xml", 'r')
        lines = new_file.readlines()
        for line in lines:
            downloaded_file.write(line)

        downloaded_file.close()
        new_file.close()
    else:
        print "Update is not available.\n"

    os.remove("tmp.xml")
    os.remove(no_pubDate_filename)
    os.remove(no_pubDate_tmp)

    print_site_title(filename)
    print_feed_title(filename)

url = raw_input('Enter RSS Feed url : ')
# url = "http://onenable.tumblr.com/rss"
# url = "http://blog.rss.naver.com/darkan84.xml"
# url = "https://wikidocs.net/book/2/rss"
filename = string_to_md5(url)
rss_reader(url, filename)                                       ##### rss_reader