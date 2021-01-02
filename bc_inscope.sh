#!/bin/bash

python3 bugC.py > output2.txt

cat output2.txt | grep "<code>"|sed -i 's/<code>//g' output2.txt

cat output2.txt | grep "</code>"|sed -i 's/<\/code>//g' output2.txt

cat output2.txt | sed -i 's/<a href="//g' output2.txt

cat output2.txt | sed -i 's/rel="external">//g' output2.txt | sed -i 's/<\/a>//g' output2.txt

./sc.sh > output.txt

cat output.txt | sed -i 's/,//g' output.txt | sed -i 's/"//g' output.txt

cat output.txt | grep "\[" | sed -i 's/\[//g' output.txt

cat output.txt | sed -i 's/]//g' output.txt 

cat output.txt | sed -i "s/'//g" output.txt 

cat output.txt | sed -i "s/(//g" output.txt

cat output.txt | sed -i "s/)//g" output.txt



cat output.txt | sort -u > output3.txt

echo "Check the output will be in target.txt";

cat output3.txt | grep "\." > target.txt





