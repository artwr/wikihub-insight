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
    startym = ymrange[0].split("-")
    endym = ymrange[1].split("-")
    starty = startym[0]
    startm = startym[1]
    endy = endym[0]
    endm = endym[1]
    data_dict = {}
    for m in range(startm,13):
        month = format(m, '02')
        rowval=wes.row(title+'_'+str(starty)+'_'+month)
        if rowval is not None:
            if rowval != {}:
                val = rowval["count:editcount"]
                if val is not None:
                    data_dict[str(starty)+_+str(m)] = val
    for y in range(startm+1,endy):
        year=str(y)
        for m in range(startm,13):
        
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