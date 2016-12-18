#!/bin/bash
FILE=activation_links.txt
> auth_list.txt

function activate() {
	args=($1)
	email=${args[0]}
	link=${args[1]}
	echo Trying $email
	curl -I -s -L "$link" > /dev/null
	echo $email >> auth_list.txt
}

export -f activate

cat $FILE | parallel -j 16 "activate {}"
