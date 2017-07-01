#!/bin/bash

# Seconds before asking the server for more URLs
WAIT_TIME=5
URL_CACHE_FILE="/tmp/icanhazinternet.cache"

if [ $# -ne 1 ]; then
    echo "Usage: $0 <scraper url>"
    exit 1
fi

SERV=$1

:>$URL_CACHE_FILE

# Removes cached URLs, which we don't care about
strip_cached() {
    while read URL; do
        if ! grep -Eq "^$URL$" $URL_CACHE_FILE; then
            echo $URL
        fi
    done | tee -a $URL_CACHE_FILE
}

RES=$(curl -s $SERV)
while :; do
	# So we can kill the clients
	if [[ "$RES" =~ ^TERMINATE$ ]]; then
		exit
	fi
	NEWRES=$(echo $RES | strip_cached | \
		`dirname $0`/scrape.sh | strip_cached | \
		curl -sX POST --data-binary @- $SERV)
	RES=$NEWRES
	sleep $WAIT_TIME
done
