#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:20:33 2017

@author: mh70
"""

import pandas as pd
import numpy as np
from urllib.parse import urlparse
import matplotlib.pyplot as plt

import get_raw_data

#df_visits, df_urls = get_raw_data.main()
# df_visits['trans_type'] = df_visits['transition'].apply(lambda t: t & 0xff)

def data_sites(pd_df):
    data = pd_df.copy()
    #remove all information from the URL, leaving only the domain/subdomain:
    parser = lambda u: urlparse(u).netloc
    data.url = data.url.apply(parser)   
    
        
    site_frequencies = data.groupby(['url'])['visitcount'].sum().to_frame()
    
    site_frequencies.reset_index(inplace=True) # Make the domain a column
    
    site_frequencies.columns = ['domain', 'count']
    return site_frequencies

def visualize_sf(site_frequencies):
    topN = 20
    plt.title('Top $n sites Visited'.replace('$n', str(topN)))
    pie_data = site_frequencies['count'].head(topN).tolist()
    
    pie_labels = None
    
    plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)
    plt.show()
    
def transition(df_visits):
    t1 = df_visits.groupby(['trans_type','transition'],
                          as_index=False)['transition'].agg({'count': len})
    # as_index=False is effectively “SQL-style” grouped output
    # agg If a dict is passed, the keys will be used to name the columns.
    
    
    t2 = df_visits.groupby(
            ['trans_type','transition']).transition.count().to_frame()
    t2.columns = ['count']         # rename column first
    t2.reset_index(inplace=True)   # make the index columns
    
    # t1 == t2 - should be True
    
    trans_types = ["link", "typed", "auto_bookmark", "auto_subframe",
                   "manual_subframe", "generated", "auto_toplevel",
                   "form_submit", "reload", "keyword", "keyword_generated"]
    
    t2['trans_type_txt'] = t2['trans_type'].apply(lambda i: trans_types[i])
    # https://groups.google.com/a/chromium.org/forum/#!topic/chromium-discuss/r7UQ2i98Lu4
    # https://developer.chrome.com/extensions/history
    
site_frequencies = data_sites(df_urls)
visualize_sf(site_frequencies)



"""
sites_per_week = data['datetime'].groupby(data['datetime'].dt.week).count()
"""

