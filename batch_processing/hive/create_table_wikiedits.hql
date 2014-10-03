-- TODO : replace <user_name> with your username
-- TODO : replace <login_name> with actual login name
CREATE DATABASE IF NOT EXISTS wiki;
USE wiki;

drop table IF EXISTS wikiedits;
drop table IF EXISTS wiki_small;

create external table if not exists wiki_small (
title  STRING,
pid    BIGINT,
ns   SMALLINT,
redirect_title STRING,
rid BIGINT,
parent_id STRING,
ts STRING,
unix_ts STRING,
contributor_username STRING,
contributor_id STRING,
contributor_ip STRING,
comment STRING,
comment_deleted STRING,
text_id BIGINT,
text_bytes INT,
text_deleted STRING,
sha1 STRING)
row format delimited
fields terminated by '\t'
stored as textfile
location '/data/sample/';

create external table if not exists wikiedits (
title  STRING,
pid    BIGINT,
ns   SMALLINT,
redirect_title STRING,
rid BIGINT,
parent_id STRING,
ts STRING,
unix_ts STRING,
contributor_username STRING,
contributor_id STRING,
contributor_ip STRING,
comment STRING,
comment_deleted STRING,
text_id BIGINT,
text_bytes INT,
text_deleted STRING,
sha1 STRING)
row format delimited
fields terminated by '\t'
stored as textfile
location '/data/wiki/';

