#! /bin/bash

cat $1 | while read LINE; do
  cd /home/rodrigo/Projects/TCC/dataset
  wget --no-dns-cache -4 --no-check-certificate $LINE
done
