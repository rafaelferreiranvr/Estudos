//6- Write a function that takes two integer arrays and their sizes as parameters, and returns a new array that is the concatenation of the two arrays.

#include <iostream>

int* array_sum(int *array1, int *array2, int array_size){
    int* result_array = new int[array_size];

    for (int i = 0; i < array_size; i++){
        result_array[i] = array1[i] + array2[i];
    };

    return result_array;
}

int main(){
    int array1[] = {1, 2, 3, 4, 5};
    int array2[] = {2, 3, 4, 5, 6};

    int* result_array = array_sum(array1, array2, 5);

    std::cout << "Array 1: ";
    for (int i = 0; i < 5; i++){
        std::cout << array1[i];
        if (i != 4) {
            std::cout << ", ";
        }
    };
    std::cout << std::endl;
    
    std::cout << "Array 2: ";
    for (int i = 0; i < 5; i++){
        std::cout << array2[i];
        if (i != 4) {
            std::cout << ", ";
        }
    };
    std::cout << std::endl;

    std::cout << "Sum Result Array: ";
    for (int i = 0; i < 5; i++){
        std::cout << result_array[i];
        if (i != 4) {
            std::cout << ", ";
        }
    };
    std::cout << std::endl;
}