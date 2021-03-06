#!/bin/bash

# Seconds before asking the server for more URLs
WAIT_TIME=5
URL_CACHE_FILE="/tmp/icanhazinternet.cache"
URL_CACHE_SIZE=10000

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

    # Clear half the cache after some number of URLs are stored
    if [ `wc -l $URL_CACHE_FILE | cut -d' ' -f1` -ge $URL_CACHE_SIZE ]; then
        let tail_amount=$URL_CACHE_SIZE/2
        tail -$tail_amount $URL_CACHE_FILE > $URL_CACHE_FILE.trimmed
        mv $URL_CACHE_FILE.trimmed $URL_CACHE_FILE
    fi
}

RES=$(curl -sX POST $SERV)
while :; do
	# So we can kill the clients
	if [[ "$RES" =~ ^TERMINATE$ ]]; then
		exit
	fi

    # Only wait if there are no URL results. (prevents self-DDoS)
    [[ -z "$(echo $RES | tr -d ' \n\t')" ]] && sleep $WAIT_TIME

	NEWRES=$(echo $RES | strip_cached | \
		`dirname $0`/scrape.sh | strip_cached | \
		curl -sX POST --data-binary @- $SERV)
	RES=$NEWRES
done
