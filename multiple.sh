#!/bin/sh

#



function run {

  echo "$1 start $2 $3  "
  mkdir $1
  cd $1
  cp  -R ../shared .
  cd shared
  sh run.sh
  cd ..
  # result files
  mkdir rst
  cp  -R ../clean/rst  .


  # script and frame
  cp ../cte_step.py cte_step.py
  cp ../frame.py frame.py

  python cte_step.py 10 $2 $3

  cp rst/stash/results_summary.txt  kitten"$1"

  echo "$1 done for  operator range $2 $3 "

}



run t1 0 12 &

run t2 12 4 &

run t3 16 2 &

run t4 18 13 &