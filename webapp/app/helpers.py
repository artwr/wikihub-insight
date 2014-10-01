#!/usr/bin/env python
import happybase

def getYearlyData(title, yrange = ("2001","2012")):
    conn = happybase.Connection('localhost')
    conn.open()
    wes = conn.table('wikieditssmall')
    we = conn.table('wikiedits')
    titlestr = title.encode('ascii','ignore')
    years = range(2001,2012)
    data_dict = {}
    for y in years:
        year=str(y)
        rowval=wes.row(title+'_'+year)
        if rowval is not None:
            if rowval != {}:
                val = rowval["count:editcount"]
                if val is not None:
                    data_dict[y] = val
    conn.close()
    return data_dict

def getMonthlyData(title, ymrange = ("2001-01","2012-11")):
    conn = happybase.Connection('localhost')
    conn.open()
    wes = conn.table('wikieditssmall')
    we = conn.table('wikiedits')
    titlestr = title.encode('ascii','ignore')
    years = range(2001,2012)
    data_dict = {}
    for y in years:
        year=str(y)
        rowval=wes.row(title+'_'+year)
        if rowval is not None:
            if rowval != {}:
                val = rowval["count:editcount"]
                if val is not None:
                    data_dict[y] = val
    conn.close()
    return data_dict

def getDailyData(title, ymdrange = ("2001-01-15","2012-10-31")):
    conn = happybase.Connection('localhost')
    conn.open()
    wes = conn.table('wikieditssmall')
    we = conn.table('wikiedits')
    titlestr = title.encode('ascii','ignore')
    years = range(2001,2012)
    data_dict = {}
    for y in years:
        year=str(y)
        rowval=wes.row(title+'_'+year)
        if rowval is not None:
            if rowval != {}:
                val = rowval["count:editcount"]
                if val is not None:
                    data_dict[y] = val
    conn.close()
    return data_dict