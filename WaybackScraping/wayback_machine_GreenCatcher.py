# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 19:05:38 2024

@author: Michele Scalzotto

In this version,
1. I modify the list_closest_snapshot so that it can identify and return also green snapshots 
    namely, those which were redirections or overwritten - they have a message of kind 3##.
    Before it could identify only blue ones. In practice I create list_snapshots and remove list_closest_snapshot
2. In these snapshots, I only keep the blue and green ones, and I only keep those pointing to an html file. 
3. I scrape the natural language text in every html box of the homepage. I save each as a separate document in the corpus.  
    I do this because right now, the text downloaded is a long string, while word2vec requires sentences, or documents as inputs. 
"""

import codecs
import re
import requests
import datetime
import os
from bs4 import BeautifulSoup
import sys
from urllib.parse import quote
import pandas as pd
import numpy as np

class wayback_machine_GreenCatcher:

    def __init__(self, website, output_folder="../../out", year_folder=False):
        print("Looking at new website {0}...".format(website))
        # this is the website url as found on the web. 
        self.website = website
        self.output_folder = output_folder
        self.year_folder = year_folder

   # extract domain and address from wayback_url     
    def split_wayback_url(self, wayback_url):
        original_url = re.sub(r'http://web.archive.org/web/\d+/',"",wayback_url)
        website_piece = re.sub(r"http(s?)\://","", original_url)

        try:
            (domain, address) = website_piece.split("/", 1)            
        except ValueError:
            domain  = website_piece
            address = ""

        
        domain = self.clean_domain_url(domain)
        
        return (domain, address)
    
    def clean_domain_url(self, domain):
        s =  re.sub("www\.","",domain)
        s =  re.sub("home\.","",s)
        s  = re.sub(r"\:.*","",s)
        s = re.sub(r"http(s?)://(\w+)\.(\w+)\.(\w+)",r"\3.\4",s)
        return s

    # to make this run you need to provide the url of the website as found on the wayback machine
    def crawl(self, wayback_url, levels=1, done_urls={}, counter_threshold=9, homepage_language=None):
        #Recursive algorithm
        print ("\t .Crawl [L={0}].. {1}".format(levels, wayback_url))
        
        clean_url = re.sub("\?.*","",wayback_url)
        clean_url = re.sub(r"\#.*","",clean_url)

        try:
            response  = requests.get(clean_url, timeout=10000)
            html = response.text
            
            self.store_page(clean_url, html)
            
            soup = BeautifulSoup(html, 'html.parser')

            corpus = []
            for box_type in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'li', 'span', 'strong', 'em', 'blockquote', 'pre']:
                page_boxes = soup.find_all(box_type)
                for single_box in page_boxes:
                    document = single_box.get_text(separator=' ', strip=True)
                    corpus.append(document)

            if homepage_language==None:
                homepage_soup = BeautifulSoup(response.content, 'html.parser')
                homepage_language = homepage_soup.html.get('lang')
            
        except Exception as e:
            print ("Connection Error: Error is {0}".format(e))
            return homepage_language, corpus, done_urls
            
            
        done_urls = self.add_done_url(clean_url, done_urls)
        
        counter = 0

        if levels > 0:

            (domain, address) = self.split_wayback_url(clean_url)
            
            soup = BeautifulSoup(html, features="html.parser")
            for link in soup.findAll('a', attrs={'href': re.compile(domain)}):            
                url = link['href']
                print("\t" + url)
                
                ## Skipping Conditions: Begin

                if not self.is_valid_url(url):
                    print("\t .Skipped (not a valid url)")
                    continue

                if not url.startswith("http"):
                    url = "http://web.archive.org" + url

                # if url not done.. Scrape it.
                if self.url_done(url, done_urls):
                    print("\t .Skipped (already done)")
                    continue
                
                if isinstance(counter_threshold, int):
                    counter += 1                
                    if counter > counter_threshold:
                        print("\t .{0} links donwloaded for website. Done.".format(counter))
                        break
                ## Skipping Conditions: End
                
                corpus.extend(self.crawl(url, levels-1, done_urls, counter_threshold=9, homepage_language=homepage_language)[1])
                
        return homepage_language, corpus, done_urls

    # use domain and address of wayback_url to define a directory, and writes html there. 
    def store_page(self, wayback_url, html):
        (domain, address) = self.split_wayback_url(wayback_url)

        if self.year_folder:
            base_directory = "{0}/{1}/{2}".format(self.output_folder, domain, self.crawled_year)
        else:
            base_directory = self.output_folder + "/" + domain

            
        if not os.path.exists(base_directory):
                os.makedirs(base_directory)

        if address == "":
            address = "homepage.html"

        file_path = base_directory +  "/" + address.replace("/","_")
        outfile = codecs.open(file_path, "w",'utf-8')
        outfile.write(html)
        outfile.close()
        print ("\t .Stored in: {0}".format(file_path))


    # Notes: If no year.. then stored under key value 0
    def add_done_url(self, wayback_url, done_urls):
        
        if self.year_folder is True and self.crawled_year not in done_urls:
            done_urls[self.crawled_year] = []

        elif self.year_folder is False and done_urls  == {}:
            done_urls[0] = []

        ix = self.crawled_year if self.year_folder is True else 0
        
        done_urls[ix].append(wayback_url)

        return done_urls


    def url_done(self,url,done_urls):
        ix = self.crawled_year if self.year_folder is True else 0

        if url in done_urls[ix]:            
            return True

        if url.replace("www.","") in done_urls[ix]:
            return True

        return False

    # fill self.crawled_year, 
    # to make this one run you need to provide the website url as it is found on the web
    def crawl_from_date(self, year, month, day, levels=0, counter_threshold=9):
        wayback_url = self.closest_snapshot_url(year, month, day)
        self.crawled_year = year
        
        if wayback_url is not None:
            return self.crawl(wayback_url, levels=levels, counter_threshold=counter_threshold)
        else:
            print("\t .Failed to generate closest wayback_url")
            return None


    def is_valid_url(self, url):
        
        if url.endswith('.pdf'):
            return False

        if len(url) > 200:
            return False
        
        if url == "." or url == "..":
            return False
        
        return True
    
    def closest_snapshot_url(self, year, month, day):
        sought_date = int(datetime.date(year = year, month = month, day = day).strftime("%Y%m%d") + '000000')
        snapshots = self.list_snapshots(2000, 1, 1, 2024, 12, 31)
        
        # improve by finding the day of the closest snapshot. 
        # then, among the snapshots in that day, find the closest blue (statuscode beginning in 2)
        # if no blue is present on that day, select the closest green (statuscode beginning in 3)
        if snapshots is not None:
            # get url of closest snapshot
            snapshots['closeness']=np.abs(snapshots['timestamp']-sought_date)
            min_index = snapshots['closeness'].idxmin()
            closest_url = snapshots.loc[min_index, 'original']
            closest_timestamp = snapshots.loc[min_index, 'timestamp']
            closest_status = snapshots.loc[min_index, 'statuscode']
            print("\t .Closest timestamp is {0}, with status {1}".format(closest_timestamp, closest_status))
            
            #build wayback url on which to crawl
            wayback_url = 'http://web.archive.org/web/{0}/{1}'.format(closest_timestamp, closest_url)
            return wayback_url
        else:
            print("\t .Failed to fetch list of snapshots for this web url")
            return None
    
    def list_snapshots(self, strt_year, start_month, start_day, end_year, end_month, end_day):
        """
        # I want to filter out any snapshot with statuscode starting with 4## or 5## as they respectively mean that upon being performed, the snapshot received "bad response error" and "bad gateway error". 
        # As of status code "-", it often couples with a mimetype of the archived document which we are not interested in for the current analysis, 
            i.e. warc/revisit, which to the best of my knowledgeonly captures the updates to the previous snapshot. 
        # I want to retain only the snapshots with mimetype text\html. In fact, this field could indicate PNG, JPEG, JSON, PDF, MP4, JavaScript, and many other format files - including warc/revisit. 
            We only want html file types
        """
        start_timestamp = datetime.date(strt_year, start_month, start_day).strftime("%Y%m%d")
        end_timestamp = datetime.date(end_year, end_month, end_day).strftime("%Y%m%d")
        cdx_url = "http://web.archive.org/cdx/search/cdx?url={0}&from={1}&to={2}&output=json".format(quote(self.website), start_timestamp, end_timestamp)
        
        response = requests.get(cdx_url)
        if response.status_code == 200:
            print("\t .Listing snapshots between {0} and {1}, response status is {2}".format(start_timestamp, end_timestamp, response.status_code))
            snapshots = response.json()
            snapshots = pd.DataFrame(snapshots)
            snapshots.columns = snapshots.iloc[0]
            snapshots = snapshots[1:]
            snapshots.reset_index(drop=True, inplace=True)
            snapshots['timestamp'] = snapshots['timestamp'].astype(np.int64)
            snapshots = snapshots.loc[(snapshots['mimetype'] == 'text/html') & (snapshots['statuscode'].str.startswith(('2', '3'))), :]
            return snapshots
        else:
            return None
    
    