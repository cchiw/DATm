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
  cp  -R ../clean/fem  .
  cp  -R ../clean/fnspace_data .

  # script and frame
  cp ../fem_step.py fem_step.py
  cp ../frame.py frame.py

  python fem_step.py 10 $2 $3

  cp rst/stash/results_summary.txt  kitten"$1"

  echo "$1 done for  operator range $2 $3 "

}



run t1 0 7 &

run t2 7 2 &

run t3 9 2 &

run t4 11 29 &