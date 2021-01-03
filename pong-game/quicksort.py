#Copyright 2020 Tooryanand Seetohul

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

#  Lab assignment 2
#  Based on Professor Cormen's examples and instructions
#  Author Tooryanand Seetohul

#  function to partition the list
def partition(the_list, p, r):
    pivot = the_list[r]
    i = p - 1
    j = p

    #  looping through all items in the list
    while j < r:
        if the_list[j] > pivot:
            j += 1
        else:
            i += 1
            the_list[j], the_list[i] = the_list[i], the_list[j]
            j += 1

    #  put pivot in the right place
    the_list[r], the_list[i+1] = the_list[i+1], the_list[r]

    #  return the index of the pivot
    return i + 1

#  function to quicksort a list/sublist
def quicksort(the_list, p = 0, r = None):
    if r == None:
        r = len(the_list) - 1

    #  base case
    if p >= r:
        return
    else:
        #  recursive case
        q = partition(the_list, p, r)
        quicksort(the_list, p, q - 1)  #  sorting before pivot
        quicksort(the_list, q + 1, r)  #  sorting after pivot
