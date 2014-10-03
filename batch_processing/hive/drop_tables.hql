--Drop Tables.hql
USE wiki;

drop table IF EXISTS wikiedits;
drop table IF EXISTS wikieditslatest;
drop table IF EXISTS wiki_small;
drop table IF EXISTS wiki_smalllatest;

DROP DATABASE IF EXISTS wiki;