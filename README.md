Wikihub
=======


### Building a portal to provide Github-like stats for Wikipedia Pages.

*N.B.: Wikihub is still in alpha*

Wikipedia is an amazing tool, but it is sometimes difficult to assess how active a page is or to find statistics on edits. [Wikihub](http://wikihub.info/) aims at providing painless access to summary statistics and edits timeseries.

## Data Pipeline
![The Wikihub Pipeline](images/pipeline2.png "Jaunt Pipeline")

The latest [Wikipedia XML dumps](http://dumps.wikimedia.org/enwiki/latest/) are downloaded from the Wikipedia Servers via a [shell script](data_scripts/download_wiki_dumps.sh). Preprocessing is done in [Python](data_scripts/xml2tsvgzip.py) with minimal memory footprint (SAX parser) for conversion to TSV.

The files are then put into HDFS for aggregation in Hive. Data is then inserted into Hbase through bulk loading.

A Flask API serves API requests offering statistics on a per page basis.


### Additional setup requirements

```Shell
sudo apt-get install python-pip
``` 