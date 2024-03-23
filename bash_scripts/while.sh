#!/bin/bash
echo "please write a number..."
myvar=1

read int

while [ $myvar  -le $int ]
do 
  echo $myvar
  myvar=$(( $myvar +1))
  sleep 0.5
done
