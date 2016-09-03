#! /bin/bash

sort -t $'\t' -k "$2,$2" $1 >t1

sort -t $'\t' -k "$4,$4" $3 >t2

join -t $'\t' -1 $2 -2 $4 t1 t2 -a 1 |awk -v n=$2 '{
        s=$2;
        for(i=3;i<n;++i){
                s=s"\t"$i
        }
        s=s"\t"$1
        for(i=n;i<=NF;i++){
                s=s"\t"$i
        }
        print s
}'

rm -f t1 t2
