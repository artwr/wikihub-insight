#!/usr/bin/env python
import happybase

conn = happybase.Connection('localhost')
conn.open()
wes = conn.table('wikieditssmall')
we = conn.table('wikiedits')

title = 'Afghanistan'

years = range(2001,2012)
data_dict = {}
for y in years:
    rowval=wes.row(title+'_Y_'+str(y))
    if rowval is not None:
        print rowval
        val = rowval["count:edits"]
        if val is not None:
            print val

data_dict2 = {}
for key, data in wes.scan(row_prefix=title+'_Y_'):
    print key, data

conn.close()