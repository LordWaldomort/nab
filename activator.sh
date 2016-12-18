#!/bin/bash
FILE=activation_links.txt
> auth_list.txt
while read email link; do
	echo Trying $email
	curl -I -s -L "$link" > /dev/null
	echo $email >> auth_list.txt
done < $FILE

