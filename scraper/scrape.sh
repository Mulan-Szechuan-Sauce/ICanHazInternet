#!/bin/sh

# Scrapes the URLs given in STDIN

scrapePage() {
	curl -s -m 5 -L $1 | \
		grep -o '<a \+href *= *['"'"'"][^"'"'"']*['"'"'"]' | \
		sed -e 's/^<a \+href *= *["'"'"']//' -e 's/["'"'"']$//' | \
		sed '/^#/ d' | \
		grep -v "^[[:space:]]*$"
}

# Read a list of URLs
while read URL; do
	scrapePage "$URL" | while read line; do
        retrieved_url=$line
		# If a returned line doesn't have the domain prepended
		if ! echo $retrieved_url | grep -Eq "^https?:\/\/"; then
            retrieved_url="$URL/$retrieved_url"
		fi
        # To make URLs uniformly have the http prefix
		if ! echo $retrieved_url | grep -Eq "^https?"; then
            retrieved_url="http://$retrieved_url"
        fi
        echo $retrieved_url
	done
done | sort | uniq

