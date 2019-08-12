# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:56:37 2019

@author: ayush
"""

def un_sequential(arr,ele):
    pos=0
    found=False
    while pos<len(arr) and not found :
        if arr[pos]==ele:
            found=True
        else:
            pos+=1
    return found
def o_sequential(arr,ele):
    pos=0
    found=False
    end=False
    while pos<len(arr) and not found:
        if arr[pos]==ele:
            found=True
        else:
            if arr[pos]>ele:
                end=True
            else:
                pos+=1
    return found


def binary(arr,ele):
    first=0
    last=len(arr)-1
    found=False
    while first <= last and not found:
        mid=(first+last)//2
        if arr[mid]==ele:
            found=True
            #for left half part
        else:
            if arr[mid]<ele:
                last=mid-1
        #forright half part 
            else:
                first=mid+1
    return found
#recursive binary search
def rec_binary(arr,ele):
    #in recursion wee start from the base
    if len(arr)==0:
        return False
    #for comparing exact middle value
    else:
        mid=len(arr)//2
        if arr[mid]==ele:
            return True
        else:
            #left half from 0 to mid
            if arr[mid]<ele:
                return rec_binary(arr[:mid],ele)
            else:
                #right half from mid+1 to end
                return rec_binary(arr[mid+1:],ele)
        
            
arr=[1,3,4,5,6,9,12,13]
print(rec_binary(arr,10))



