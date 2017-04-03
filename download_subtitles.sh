#!/bin/bash

cd /Users/rajesh13/Documents/health_datascience/Youtube_scrapping_tool/youtube-dl/bin
mkdir subtitles

cat urls.txt | while read line
do
youtube-dl --write-sub \
--write-auto-sub \
--skip-download \
--quiet \
--no-warnings \
--ignore-errors \
$line
echo -e "\033[1m*\033[0m" | tr '\n' ' '
done
mv *.vtt subtitles/

cd subtitles
mkdir transcript
for f in *.vtt; do cat "$f" | \
sed -e 's/[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9].*%//g' \
-e 's/<*>//g' \
-e 's/<c.colorE5E5E5//g' \
-e 's/<c.colorCCCCCC//g' \
-e 's/<\/c<[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]<c//g' \
-e 's/<[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]<c//g' -e 's/<\/c//g' | grep -ve "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]" > \
transcript/"`basename "$f" .en.vtt`.txt"
done

printf "\n\n\n"
echo -e "\033[1mDone with Analysis!"

cd transcript;

#if false
#then

while true; 
do
read -p "Would you like to see the results?" yn
case $yn in
[y]* ) break;;
[n]* ) exit;;
* ) echo "Please answer yes or no.";;
esac
done

for cat in *.txt; 
do 
echo -e "\033[1m$cat\033[0m"; 
read -n1; 
cat "$cat"; 
read -n1; 
done

#fi

cd ../../
mv subtitles /Users/rajesh13/Documents/health_datascience/Youtube_scrapping_tool/
mv urls.txt /Users/rajesh13/Documents/health_datascience/Youtube_scrapping_tool/
cd subtitles
rm *.vtt
exit;



