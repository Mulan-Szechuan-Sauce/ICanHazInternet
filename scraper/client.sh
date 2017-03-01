#!/bin/sh

SERV=$1

while :
do
	RES=$(curl $SERV)
	# So we can kill the clients
	if [ "$RES" =~ ^TERMINATE$ ]
	then
		exit
	fi
	NEWRES=$(echo $RES | \
		`dirname $0`/scrape.sh | \
		curl -X POST --data-binary @- $SERV)
	RES=$NEWRES
	sleep 5
done

