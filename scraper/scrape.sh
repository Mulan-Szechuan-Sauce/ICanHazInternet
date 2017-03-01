#!/bin/sh

# Scrapes the URLs given in STDIN

stripUrl() {
	curl -s -m 5 -L $1 | \
		grep -o '<a href=['"'"'"][^"'"'"']*['"'"'"]' | \
		sed -e 's/^<a href=["'"'"']//' -e 's/["'"'"']$//' | \
		sed '/^#/ d' | \
		grep -v "^[[:space:]]*$"
}

# Read a list of URLs
while read URL
do
	stripUrl "$URL" | while read line
	do
		# If a returned line doesn't have the domain prepended
		if echo $line | grep -Eq "^\/"
		then
			echo -n $URL
		fi
		echo $line
	done
done | sort | uniq

