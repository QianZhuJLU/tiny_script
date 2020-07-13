#!/bin/bash
#Summarize the elapsed time of a series of VASP jobs into file <time_used>
directory=`ls -d */`
for i in $directory ;do
    touch time_used
    cd $i
    echo "-----------------" >> ../time_used
    pwd|awk 'BEGIN{FS="/"}{print $5}' >> ../time_used
    if [ -f "OUTCAR" ];then
        used=`grep time OUTCAR |tail -1|awk '{print $1}'`
        if  [ "$used" == "Elapsed" ];then
          ~/vtime.sh >> ../time_used
        else
          echo "oh NO,did not get COVERAGED" >> ../time_used
        fi
    else 
      echo "NO OUTCAR !" >> ../time_used
    fi
    cd ..
done 
