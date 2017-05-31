#!/bin/bash

for i in {1..5}
do
url="https://www.udemy.com/api-2.0/courses/?page_size=100&category=Test+Prep&page="
url=$url$i  
echo $url
echo " "
echo " "
sleep 5s
curl --user SrBh8o75qcbH6mpOiMiWj4Mno1bGnkP4cqq4kKO9:SSqv8QBG2FcLAn34X1eMZH7xT5tdLS8gan7HmQ1Y1brHkegAJrzz9r9d5CrYLE2mB077H111HbHLVamyCCjXNxDXM8gW23Wbm4xfcvsceaOo5D34x6hQdvR2bZ35XWQl $url > 1234.json
python udemy_fixed.py
echo " "
echo " "
done

exit 0