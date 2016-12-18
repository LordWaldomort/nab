#!/bin/bash
FILE=activation_links.txt

while read email link; do
	echo Trying $email
	curl -I -s -L "$link"
done < $FILE
