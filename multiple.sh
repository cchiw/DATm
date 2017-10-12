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
  cp  -R ../fem  .
  cp  -R ../fnspace_data .

  # script and frame
  cp ../fem_step.py fem_step.py
  cp ../frame.py frame.py

  python fem_step.py 10 $2 $3

  cp rst/stash/results_summary.txt  kitten"$1"

  echo "$1 done for  operator range $2 $3 "

}



run t1 0 9 &

run t2 9 3 &

run t3 12  5  &

run t4 17 24 &