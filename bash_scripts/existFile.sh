#!/bin/bash

rmfile=~/rmfile.txt

echo "Please write a name of file: "
read name


while [ -f ~/$name ]
do 
  echo "The file is exists."
  sleep 1
done 


echo "==================================="

echo "The file no longer exists. Exiting."

echo "==================================="

echo $name.txt_$(date +%F)_$(date +%r) >> $rmfile
