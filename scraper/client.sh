#!/bin/sh

SERV=$1

RES=$(curl $SERV)
while :
do
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

