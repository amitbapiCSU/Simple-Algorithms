import random as rn

"""
This is the merger function, which merges an array of size >= 4
 and which contains first half sorted and 2nd half sorted.
"""
def merger (arr, st, en):
    diff = en - st;
    if diff >= 4 :
        i = 0;
        dist = int(diff/2)
        while i < (dist):
            if (arr[st+i] > arr[st+dist+i]) :
                arr[st+i], arr[st+dist+i] = arr[st+dist+i], arr[st+i];
            i+=1;
        return merger(arr, (st+2), (en-2));
    else :
        return arr;

"""
sorter function does the base case swap for the base case merger and 
base case swapping of even and odd lines for all mergers of size >= 4 
"""
def sorter (input_arr, strt, end):
    diff = end - strt;
    if (diff-1) == 1 :
        if (input_arr[strt] > input_arr[end-1]):
            input_arr[strt], input_arr[end-1] = input_arr[end-1], input_arr[strt];
    else :        
        merger(input_arr, strt , end);
        if (strt != end) :
            indx = strt+1;
            while indx < (end - 2) :
                if input_arr[indx] > input_arr[(indx+1)] :
                    input_arr[indx],input_arr[(indx+1)] = input_arr[(indx+1)], input_arr[indx];
                indx+=2;
    return input_arr;

"""
This is the sorting function which is called recursively 
on both halves of the input array.
"""
def odd_even_sorter(input_arr, strt, end):
    leng = end - strt;
    if leng > 1 :
        odd_even_sorter(input_arr, strt, (strt+int(leng/2)));
        odd_even_sorter(input_arr, (strt+int(leng/2)), end);
        sorter(input_arr, strt, end);
    
    return input_arr;

size = 256;
input_arr = rn.sample(range(512), size)
print('ip ', input_arr)
output_arr = odd_even_sorter(input_arr, 0, len(input_arr));
check = (output_arr == sorted(input_arr))
print('check ',check)
 
        