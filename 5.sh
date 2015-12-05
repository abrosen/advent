#!/bin/bash


egrep "([^aeiou]*[aeiou]){3,}\w*"  input5.txt | egrep "(\w)\1" | egrep -v "(ab|cd|pq|xy)" | wc -l
egrep "(\w\w)\w*\1" input5.txt | egrep "(\w)\w\1" | wc -l
