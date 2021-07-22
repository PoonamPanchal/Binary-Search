# Binary-Search
##### What is Binary Search ?
Binary Search is a searching Algorithm which is used to search an element in a sorted array.It is a recursive algorithm where we search the element by dividing the array recursively in two parts.
* Steps
   * Firstly we have to sort the array
   * After sorting calculate the mid of the array using formula (low + high) // 2 where low is the 1st index 
     and high is the last index of array and compare element with the mid elementif it returns true ,that
     means we have searched the element ,return the mid element index
   * if element is greater than the mid element then search the element in right half using the same approach,
     now the low will be mid + 1 and high will be the same ,and return the index
   * if element is less than the mid element then search the element in left half using the same approach,
     now the low will be the same and high will be mid-1 ,and return the index
    
     

