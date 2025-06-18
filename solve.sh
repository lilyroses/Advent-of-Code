#!/bin/bash

solve() {
  year=$1
  day=$(printf "%02d" "$2")
  part=$3
  nano ~/code/Advent-of-Code/$year/day_$day/solution_$part.py
}
