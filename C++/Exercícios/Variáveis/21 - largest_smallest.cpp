//21 - Write a program that prompts the user to enter three integers and outputs the largest and smallest of the three.
#include <iostream>

int main(){
    int var1, var2, var3, largest, smallest;

    std::cout << "Type a number: ";
    std::cin >> var1;
    std::cout << "Type another number: ";
    std::cin >> var2;
    std::cout << "Type another number: ";
    std::cin >> var3;

    int array[3] = {var1, var2, var3};

    largest = 0;
    smallest = 0;

    for (int i : array){
        if (i > largest){
            largest = i;
        };
        if (i < smallest){
            smallest = i;
        };
    };

    std::cout
    << "The smallest number is " << smallest << " and the largest is " << largest << "." << std::endl;
}