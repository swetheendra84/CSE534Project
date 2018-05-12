#!/bin/bash

user=root
host=vl63.cs.stonybrook.edu
folderpath=/usr/src/FCN

while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    IFS=' ' read -a array <<< "${line}"
    echo ${array[0]} ${array[1]}


    ssh -p 130 -n $user@$host "sed -i '/predicted_rtt = / s/=.*/=${array[1]};/' $folderpath/net/ipv4/tcp_input.c && cd $folderpath && make > make.txt 2> make.err < /dev/null && make modules_install install > install.txt && reboot"

    a=1
    while [[ "$a" == "1" ]]
    do
        sleep 5
        nc -zv $host 130 &> /dev/null; a=$?
    done


    ssh -p 130 -n $user@$host "hping3 -S -V -c 5 -p 80 ${array[0]} > ${array[0]}.txt 2>&1 && grep 'round-trip' ${array[0]}.txt"

    echo "-----------------------------------------------------------------------------"


done < "$1"