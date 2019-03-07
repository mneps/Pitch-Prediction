#!/bin/bash

while IFS='' read -r name || [[ -n "$name" ]]; do
	echo $name
 	eval python3 pull_data.py $name
done < "$1"