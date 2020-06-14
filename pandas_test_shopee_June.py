#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:51:59 2020

@author: jameselijah
"""

import pandas as pd
#1a)
df = pd.read_excel("/Users/jameselijah/Documents/GitHub/Shopee/Test_Pandas_.xlsx")


'''
#1b)
column = list(df.columns)

#2)Unique items for each year
total_no_unique_items = df.groupby('item_creation_date').itemid.nunique()

#3)

df.index = pd.to_datetime(df['item_creation_date'],format='%d/%m/%y %I:%M')
grouped_df = df.groupby(by=[df.index.month, df.index.year])


#4)
group_by_unique_id = df.groupby(pd.Grouper(key='itemid'), sort = False)['stock'].max()
print (group_by_unique_id.sort_values(ascending=False).head(10))
#this returns top 10 itemid with highest stocks

#5) 
sorting = df.sort_values(['cb_option', 'itemid'], ascending = False).drop([ 
        'item_creation_date', 
        'item_description', 
        'item_name', 
        'item_variation', 
        'is_preferred' ,
        'price',
        'sold_count',
        'category'], axis = 1).head(3)
#6)

group_by_shop_id = df.groupby('itemid').sum().reset_index().sort_values('is_preferred', ascending = False)

is_preffered = group_by_shop_id.is_preferred >= 1

group_by_shop_id[is_preffered]

x = list (group_by_shop_id [all_cb]['itemid'][0:3])

categoriesiter = []
CATEGORY = []
for i in range(len(x)):
    categoriesiter.append(group_by_shop_id['itemid'].eq(x[i]).idxmax())

for i in categoriesiter:
    CATEGORY.append(df['category'].iloc[i])
    
print (CATEGORY) #top 3 category

#7)

new_group_by_shop_id = df.groupby('itemid').sum().reset_index()

#8)
"Regroup shop id"
group_by_shop_id2 = df.groupby('itemid').sum().reset_index().sort_values('is_preferred', ascending = False)

sorting2 = df.sort_values(['cb_option', 'itemid'], ascending = False).drop([ 
        'item_creation_date', 
        'item_description', 
        'item_name', 
        'item_variation',
        'price',
        'sold_count',
        'category'], axis = 1)
    
is_preffered = sorting2.is_preferred >= 1 

temp = sorting2[is_preffered]

'''
    
