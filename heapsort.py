class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        current = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < n and arr[left] > arr[current]:
            current = left
        if right < n and arr[right] > arr[current]:
            current = right
        
        if i != current:
            arr[i], arr[current] = arr[current],arr[i]
            self.heapify(arr,n,current)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)

        # print(self.arr[:]
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            self.heapify(arr,i+1,0)
            arr[i],arr[0] = arr[0],arr[i]
            
            