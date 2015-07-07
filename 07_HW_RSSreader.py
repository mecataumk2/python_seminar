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
    print site_title


def print_feed_title(rss_filename):
    tree = ET.parse(rss_filename)
    root = tree.getroot()
    for iterator_item in root.iter("item"):
        print iterator_item.findtext("title")

def remove_pubDate(filename):
    filename_tmp = filename + '_tmp'
    tree = ET.parse(filename)
    root = tree.getroot()
    channels = root.findall("channel")
    for parents in channels:
        for children in parents.findall("pubDate"):
            parents.remove(children)
    tree.write(filename_tmp)
    return filename_tmp

def print_rss(result_file):
    print "==================== Site name ===================="
    print_site_title(result_file)
    print "==================== Title of Items ===================="
    print_feed_title(result_file)


def rss_reader(rss_url, result_file):

    if not os.path.exists(result_file):                                 # when downloaded file is not exist
        urllib.urlretrieve (rss_url, result_file)
        print "New RSS Feed is created succesfully.\n"
        print_rss(result_file)
        return

    urllib.urlretrieve (rss_url, "tmp.xml")

    no_pubDate_result_file = remove_pubDate(result_file)
    no_pubDate_tmp = remove_pubDate("tmp.xml")

    if not filecmp.cmp(no_pubDate_result_file, no_pubDate_tmp):
        print "Update!\n"                                             # move tmp.xml to filename.   ##### Move function is exist in library(os)?
        os.remove(result_file)
        os.rename("tmp.xml", result_file)
    else:
        print "Update is not available.\n"
        os.remove("tmp.xml")

    os.remove(no_pubDate_result_file)
    os.remove(no_pubDate_tmp)

    print_rss(result_file)

url = raw_input('Enter RSS Feed url : ')
# url = "http://onenable.tumblr.com/rss"
# url = "http://blog.rss.naver.com/darkan84.xml"
# url = "https://wikidocs.net/book/2/rss"
result_file = string_to_md5(url)
rss_reader(url, result_file)                                       ##### rss_reader