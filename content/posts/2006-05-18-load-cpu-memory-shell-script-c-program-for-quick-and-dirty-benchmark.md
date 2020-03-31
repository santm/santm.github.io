+++
title = "load cpu & memory shell script c program for quick and dirty benchmark"
slug = "2006-05-18-load-cpu-memory-shell-script-c-program-for-quick-and-dirty-benchmark"
published = 2006-05-18T23:38:00+05:30
author = "Santanu Misra"
tags = [ "Tech Notes",]
+++
This script is a simple empty while loop which will load or increase the
usage of your cpu.  
a good way to test your cpu check for different monitoring tool  
  

while :  
&gt; do :  
&gt; done  
  
/home/sanmisra&gt;more memory.c  

> main ()  
> {  
> while ( 1 ) {  
> malloc (10240) ;  
> }  
> }
