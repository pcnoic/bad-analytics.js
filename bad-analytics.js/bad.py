#!/usr/bin/env python3

###############################
# Copyright Christos Alexiou - 2021 
# Email: pcnoic@gmail.com
# WordPress installation malware scanner for infected jQuery Migrate 
################################

import os
import sys
import fire
import constant
import wget
import helpers
from pyfiglet import Figlet
import validators

def get_file(url):
    """
    Reaches a URL with a WordPress installation
    and downloads the jquery-migrate.js
    :param url: URL to scan 
    """
    helpers.make_workdir() # create temp working directory
    file_url = url + constant.MALICIOUS_LOCATION
    print(file_url)
    filename = wget.download(file_url, out=constant.WORKDIR)
    return filename

def scan_file(filename):
    """
    Reads a file and estimates the probability of  it
    being an infected jquery-migrate.js
    :param filename: filename of file to scan
    """
    bad_lingo = helpers.multiline_to_words()
    lingo_count = len(bad_lingo)
    scanfile = filename
    bad = 0
    with open(scanfile, 'r') as datafile:
        for line in datafile:
            for bad_word in bad_lingo:
                if bad_word in line:
                    bad += 1
    bad_file_estimate = bad / len(bad_lingo) * 100
    helpers.clean_workdir()
    return bad_file_estimate 

def main():
    banner = Figlet(font='5lineoblique')
    print (banner.renderText('BadAnalytics.js'))

    url = input('Enter WordPress installation URL: ')
    valid = validators.url(url)
    if valid == True:
        print("URL is good! Scanning...")
    else:
        print("URL invalid...")
        exit()

    possible_js = get_file(url)
    print('\nProbability of installation being infected: ' + str(scan_file(possible_js)) + "%")

if __name__ == '__main__':
    main()
  
    
    
