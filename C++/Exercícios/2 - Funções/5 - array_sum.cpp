//5- Write a function that takes an integer array and its size as parameters, and returns the sum of all elements in the array.

#include <iostream>

int array_sum(int *array, int array_size){
    int sum = 0;

    for (int i = 0; i < array_size; i++){
        sum += array[i];
    };

    return sum;
}

int main(){
    int array[] = {1, 2, 3, 4, 5};
    std::cout << "Sum of the array: " << array_sum(array, 5) << std::endl;
}