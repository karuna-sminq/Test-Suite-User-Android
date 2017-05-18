#!/usr/bin/bash

echo '''
Copyright (C) 2016 Sminq India Solutions Pvt Ltd.
Created on 2016-11-23
Updated on 2017-05-18

 ____    __  __   ___   _   _    ___
/ ___|  |  \/  | |_ _| | \ | |  / _ \
\___ \  | |\/| |  | |  |  \| | | | | |
___) |  | |  | |  | |  | |\  | | |_| |
|____/  |_|  |_| |___| |_| \_|  \__\_\


@author: Karuna Lingham
'''

echo "================================="
echo "Sminq User App v2.2.2 ..."
echo "Running Test Suite v1.2 ..."
echo "================================="

d="$(date +'%d-%m-%Y')"
t="$(date +%H:%M)"
now=$d-$t

start=`date +%s`

#Run scripts
for folder in ./*
do

  #  #Begin recording tests for every folder
  #  adb shell screenrecord /sdcard/$folder.mp4 &
   echo "------------------"
   echo "$folder"
   echo "------------------"

  #Begin iterating through every file in specified folder
  for fname in $folder/*.py
  do

    #Execute file
    python $fname
    total_count=$((total_count + 1))

  done
done

#Test count and timer
end=`date +%s`
total_time=$((end-start))

echo "================================="
echo "Time taken for $total_count tests: $total_time sec."
echo "================================="
