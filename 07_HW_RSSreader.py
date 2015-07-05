__author__ = 'sdlee'

import urllib
import os
import filecmp
import re
import hashlib
from xml.etree.ElementTree import parse

def string_to_md5(string):
    md5 = hashlib.md5(string)
    return md5.hexdigest()

# def print_feed_title(rss_filename):
#     re_title = re.compile('(<title>.*CDATA\[)(.*)(]]></title>)')
#     f = open(rss_filename, 'r')
#     lines = f.readlines()
#     f.close()
#     for line in lines:
#         m = re_title.search(line)
#         if m:
#             print (m.group(2))

def print_feed_title(rss_filename):
    tree = parse(rss_filename)
    note = tree.getroot()
    for children_item in note.getiterator("item"):
        print "Title : ", children_item.findtext("title")

def remove_taglines(filename, tagname):
    f = open(filename, 'r')
    filename_tmp = filename + '_tmp'
    f_tmp = open(filename_tmp, 'w')
    re_pubDate = re.compile(tagname)

    lines = f.readlines()
    for line in lines:
        re_object = re_pubDate.search(line)
        if not re_object:
            f_tmp.write(line)
    f.close()
    f_tmp.close()
    return filename_tmp

def rss_reader(rss_url, filename):

    if not os.path.exists(filename):                                 # when downloaded file is not exist
        urllib.urlretrieve (rss_url, filename)
        print "New RSS Feed is created succesfully."
        print_feed_title(filename)
        return

    urllib.urlretrieve (rss_url, "tmp.xml")

    no_pubDate_filename = remove_taglines(filename, 'pubDate')                                        # Remove line using tag "<pubDate>" for file compare.
    no_pubDate_tmp = remove_taglines("tmp.xml", 'pubDate')

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

    print_feed_title(filename)

# url = raw_input('Enter RSS Feed url : ')
# url = "http://onenable.tumblr.com/rss"
url = "http://blog.rss.naver.com/darkan84.xml"
filename = string_to_md5(url)
rss_reader(url, filename)                                       ##### rss_reader