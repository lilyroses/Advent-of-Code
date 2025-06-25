#!/bin
for year in {2015..2024};
do
  for day in {1..25};
  do
    day_num=$(printf "%02d" "$day")
    ls ./$year/day_$day_num
  done
done
