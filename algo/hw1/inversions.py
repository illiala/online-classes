'''
Your task is to find the number of inversions in the file given (every row has a single integer between 1 and 100,000).
Assume your array is from 1 to 100,000 and ith row of the file gives you the ith entry of the array.
Write a program and run over the file given.
'''
import random

def main():
  arr = range(10)
  random.shuffle(arr)

  print "Before: %s \n\n" % str(arr)

  # Merge sort
  arr = sort(arr)
  
  print "After: %s \n\n" % str(arr)

def sort(arr):
  len_arr = len(arr)
  if len_arr < 2:
    return arr
  
  left = sort(arr[:len_arr/2])
  right = sort(arr[len_arr/2:])
  return merge(left, right)

def merge(left, right):
  i_a = 0
  i_b = 0
  res = []
  while (i_a < len(left) and i_b < len(right)):    
    if left[i_a] <= right[i_b]:
      res.append(left[i_a])
      i_a = i_a + 1
    else:
      res.append(right[i_b])
      i_b = i_b + 1
  
  res += left[i_a:]
  res += right[i_b:]
  return res

if __name__ == '__main__':
  main()