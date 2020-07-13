#!/bin/bash
a=`grep time OUTCAR | tail -1|awk '{print int($4)}'`
echo -n "Elapsed time : ($a seconds)"
a=$[a/3600+1]
echo -n " ($a hours)"
b=`grep time OUTCAR | tail -1|awk '{print int($4)}'`
b=$[b/86400+1]
if (($a > 24));then
  echo " ($b days)"
else
  echo " "
fi
