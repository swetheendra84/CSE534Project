#!/bin/bash


for i in {1..5}
do
	rm -rf retransmissions.txt
        rm -rf data.pcap
        rm -rf vm_cpu_readings*

	siteip=52.239.154.132
	interface=ens32

	tcpdump -i $interface ip host $siteip -w data.pcap &

        wget http://azurepublicdataset.blob.core.windows.net/azurepublicdataset/trace_data/vm_cpu_readings/vm_cpu_readings-file-1-of-125.csv.gz
	
	#now interrupt the process.  get its PID:  
	pid=$(ps -e | pgrep tcpdump)  
	echo $pid  
	#interrupt it:  
	kill -2 $pid
	
	tshark -Y "tcp.analysis.retransmission" -r data.pcap > retransmissions.txt

	cat retransmissions.txt | wc -l
	cat retransmissions.txt | grep Fast | wc -l
	
	rm -rf retransmissions.txt
	rm -rf data.pcap
	rm -rf vm_cpu_readings*
done
