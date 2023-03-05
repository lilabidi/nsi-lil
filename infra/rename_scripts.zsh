#!/bin/zsh
cd docs/scripts/
for rep in `ls -d */`
do
  cd $rep
  echo $rep
  for i in `ls -1 corr_*`
  do
    echo $i ${i:-2}
    echo ${i:5:-3}_corr.py
    mv $i ${i:5:-3}_corr.py; 
  done
  for i in `ls -1 test_*`
  do
    echo $i ${i:-2}
    echo ${i:5:-3}_test.py
    mv $i ${i:5:-3}_test.py; 
  done
  cd ..
done
cd ..
