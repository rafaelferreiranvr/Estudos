//2- Write a function that takes an integer as parameter and returns its absolute value.

#include <iostream>

int absolute_value(int value){
    if (value < 0) {
        value *= -1;
    }
    return value;
}

int main(){
    int var1;
    std::cout << "Type an integer: ";
    std::cin >> var1;

    std::cout << "Absolute value: " << absolute_value(var1) << std::endl;
}