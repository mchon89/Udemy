#!/bin/bash

for i in {86..99}
do
url="https://www.udemy.com/api-2.0/courses/?page_size=100&page="
url=$url$i  
echo $url
curl --user key:private key $url > 1234.json | python udemy_fixed.py
done

exit 0
