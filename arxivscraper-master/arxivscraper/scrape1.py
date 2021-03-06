#! /usr/bin/env python
'''
A python program to retrieve records from ArXiv.org for
Social Media Mining course at Arizona State University.

Author: Jie Zhang.
'''

# To use arxivcraper directly in our script,
# we need to import it first.
import arxivscraper

# Create a scraper to fetch all eprints in category='math'
# Filtered by subcategory='math.DG' --- DG='Differential Geometry'
# Time span: 1 year starting with most recent
scraper = arxivscraper.Scraper(category='math',date_from='2016-09-01',date_until='2017-09-01',t=30,filters={'categories':['math.DG']})
#scraper = arxivscraper.Scraper(category='math',date_from='2016-09-01',date_until='2017-09-01',t=30)

# Use the previously created instance of scraper to scrape the website
output = scraper.scrape()

# Save the output to required/desired format
import pandas as pd
#cols = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors')
cols = ('id', 'title', 'categories', 'authors')
df = pd.DataFrame(output,columns=cols)

df.to_csv('scrape1.txt', header=None, index=None, sep='$', mode='a')
