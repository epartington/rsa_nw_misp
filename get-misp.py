#!/usr/bin/env python
# -*- coding: utf-8 -*-

# version 1.2
# updated 2019/03/19
# added check for last 30 days of data as per Deloitte response

import json
import datetime

# The URL of the MISP instance to connect to

misp_url = 'http://192.168.254.28:80'

# Can be found in the MISP web interface under
# http://+MISP_URL+/users/view/me -> Authkey
misp_key = 'amHOHq5J3rMzeo4NyDELCv4GwEkX1G0yi0lZuuxh'

# Should PyMISP verify the MISP certificate
misp_verifycert = False

from pymisp import PyMISP

misp = PyMISP(misp_url, misp_key, debug=False)

#get the last 30 days window to only get indicators for that period
relevant_date = (datetime.datetime.now() - datetime.timedelta(days=60)).strftime('%Y-%m-%d')


# In[2]:


# print out various debug options while building code

#r = misp.search_index(published=False)
#print(r)


# In[4]:


# original query without date limiter
#r = misp.search(controller='attributes', type_attribute= ['domain'], deleted='False', to_ids=True)

# limiter to grab the last 30 days of indicators
r = misp.search(controller='attributes', type_attribute=['domain'], deleted='False', to_ids=True, enforceWarninglist=True, date_from=relevant_date)


# In[5]:


#r = misp.search(controller='attributes', type_attribute= ['ip-dst'], deleted='False', to_ids=True)

# limiter to grab the last 30 days of indicators
r = misp.search(controller='attributes', type_attribute=['ip-dst'], deleted='False', to_ids=True, enforceWarninglist=True, date_from=relevant_date)


# In[6]:


#r


# In[8]:


#for ev in r['response']['Attribute']:
    #print(ev)


# In[6]:


for ev in r['response']['Attribute']:
    print(ev['event_id']+','+ev['comment']+','+ev['value']+',misp,'+ev['type'])
