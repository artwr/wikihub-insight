--
set hive.map.aggr=true;
-- Test queries

USE wiki;

drop table IF EXISTS stats_small;
drop table IF EXISTS rev_small;
drop table IF EXISTS editcount_small;

-- drop table IF EXISTS stats_all;
-- drop table IF EXISTS rev_all;
-- drop table IF EXISTS editcount_all;

create table stats_small
as select title, pid, ns, count(distinct contributor_username), count(distinct contributor_ip), count(distinct contributor_ip), count(rid)
from wiki_small
where ns = 0
group by title, pid, ns;

create table rev_small
as select title, pid, ns, SUBSTR(ts,0,4) as year, SUBSTR(ts,6,2) as month, SUBSTR(ts,9,2) as day, rid
from wiki_small
where ns = 0;

-- create table rev_all
-- as select title, pid, ns, SUBSTR(ts,0,4) as year, SUBSTR(ts,6,2) as month, SUBSTR(ts,9,2) as day, rid
-- from wikiedits
-- where ns =0


create table editcount_small
as select * 
from
(select title, pid, 'D' as granularity, year, month, day, count(rid) as editcount 
 from rev_small
 group by title, pid, year, month, day
 UNION
 select title, pid, 'M' as granularity, year, month, null, count(rid) as editcount 
 from rev_small
 group by title, pid, year, month
 UNION
 select title, pid, 'Y' as granularity, year, null, null, count(rid) as editcount 
 from rev_small
 group by title, pid, year ) t;


-- CREATE EXTERNAL TABLE editcountsmall
-- row format delimited
-- fields terminated by '\t'
-- stored as textfile
-- location '/user/ubuntu/for_Hbase/editcountsmall'
-- AS
-- select CONCAT_WS('_',title,year,month,day), editcount from ag_small;

-- CREATE EXTERNAL TABLE editcount 
-- row format delimited
-- fields terminated by '\t'
-- stored as textfile
-- location '/user/ubuntu/for_Hbase/editcount'
-- AS
-- select CONCAT_WS('_',title,year,month,day), editcount from ag_all;

--