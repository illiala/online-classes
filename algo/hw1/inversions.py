'''
Your task is to find the number of inversions in the file given (every row has a single integer between 1 and 100,000).
Assume your array is from 1 to 100,000 and ith row of the file gives you the ith entry of the array.
Write a program and run over the file given.
'''
import random

def main():
  #arr = range(10)
  #random.shuffle(arr)
  #arr = [1, 3, 5, 2, 4, 6]
  arr = read_arr()

  print "Before: %s \n\n" % str(arr)

  # Merge sort
  (inv, arr) = sort(arr)
  
  print "After: %s, inversions: %s \n\n" % (str(arr), str(inv))
  
def read_arr():
  arr = []
  f = open('IntegerArray.txt', 'r')
  for line in f:
    if line != '':
      n = int(line)
      arr.append(n)
  f.close();
  return arr

def sort(arr):
  len_arr = len(arr)
  if len_arr < 2:
    return 0, arr
  
  (inv_left, left) = sort(arr[:len_arr/2])
  (inv_right, right) = sort(arr[len_arr/2:])
  (inv, res) = merge(left, right)
  return inv + inv_left + inv_right, res

def merge(left, right):
  i_a = 0
  i_b = 0
  res = []
  inv = 0;  
  while (i_a < len(left) and i_b < len(right)):    
    if left[i_a] <= right[i_b]:
      res.append(left[i_a])
      i_a += 1
    else:
      res.append(right[i_b])
      i_b += 1
      inv += (len(left) - i_a)
  #print left, right, inv
  
  res += left[i_a:]
  res += right[i_b:]
  return (inv, res)

if __name__ == '__main__':
  main()