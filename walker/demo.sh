#! /bin/sh

echo "Hello, Web-Walker!"

echo "Removing existing walker_seeds.txt file... "
rm walker/spiders/walker_seeds.txt
echo "Complete."

echo "Executing Google Search Query: $1"
python3 ../google_search/search.py "$1" > walker/spiders/walker_seeds.txt
echo "Complete."

echo "Running Web-Walker....."
sudo scrapy crawl web_walker -a query="$1"
