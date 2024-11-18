# -*- coding: utf-8 -*-
"""Untitled40.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/142QBdPjOY8LjednY3FdTZvo4U9vc5dFr
"""

import math
# step 1
max_m = 999
max_sm = int(math.sqrt(max_m))
p = [True for i  in range(max_sm+1)]
p[0] = p[1] = False
for i in range(2,int(math.sqrt(max_sm+1))+1):
  if p[i]:
    for j in range(i*i,len(p),i):
      p[j] = False
prs = []
for k in range(2,len(p)):
  if p[k]:
    prs.append(k)
print(prs)

# step 2

def seg_sieve():
  n,m = map(int,input().split())
  seg_prime = []
  print(f'n : {n} and m : {m}')
  aug_arr = [True for i in range(0,m-n+1)]
  # print(aug_arr)
  if n == 1:
    aug_arr[0] = False
  for i in prs:
    # print(f'i : {i}')
    x = (n//i)*i
    if x<n:
      x += i
    if x<(i*i):
      x = i*i
    # print(f'x : {x}')
    for j in range(x,m+1,i):
      aug_arr[j-n] = False
      # print(aug_arr)
  # print(aug_arr)
  for k in range(m-n+1):
    if aug_arr[k]:
      seg_prime.append(n+k)
  print(seg_prime)

seg_sieve()