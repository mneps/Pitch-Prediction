#!/bin/bash

while IFS='' read -r name || [[ -n "$name" ]]; do
	echo $name
 	eval python3 pull_data.py $name
done < "$1"

files=( *.csv ) # collect input filenames in an array
{
  head -n 2 "${files[0]}" # output the header lines (using the 1st file)
  tail -q -n +3 "${files[@]}" # append the data lines from all files, in sequence
}  > out.csv
