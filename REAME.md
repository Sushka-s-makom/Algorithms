# Algorithms (Python)

This repository contains my implementations of basic algorithms and data structures in Python.
The code was written while studying a full algorithms course based on video lectures
from MIPT (Moscow Institute of Physics and Technology).

The goal of this repository is educational: to practice core algorithmic ideas,
write clean and readable code, and understand time and space complexity.

## Course source

* Algorithms and Data Structures — MIPT video lectures
  https://youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&si=gvbNM_Sbbk46aomF

## Topics covered

* Sorting algorithms:

  * MergeSort
  * QuickSort (three-way partition)
  * Quadratic-time sorts (Insertion, Selection, Bubble)
* Array algorithms and patterns:

  * merging sorted arrays
* String algorithms:

  * string equality check
  * naive substring search

## Repository structure

* `arrays/` — sorting and array-based algorithms
* `strings/` — basic string-processing algorithms

Each algorithm file includes:

* a short explanation of the idea
* time and space complexity analysis
* a simple runnable example or test

## Notes

* The implementations are intentionally straightforward and avoid heavy optimizations.
* The repository is not intended for competitive programming.
* The focus is on understanding, correctness, and clear presentation of algorithms.

## Technologies

* Python 3.x

## How to run

Most files can be run directly:

```bash
python arrays/merge_sort.py
python arrays/quicksort_three_lists.py
python strings/substring_search.py
```
