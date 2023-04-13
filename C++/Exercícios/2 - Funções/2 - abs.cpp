//2- Write a function that takes an integer as parameter and returns its absolute value.

#include <iostream>
int abs(int value){
    unsigned int absolute_value = value;
    return absolute_value;
}

int main(){
    int var1;
    std::cout << "Type an integer: ";
    std::cin >> var1;

    std::cout << "Absolute value: " << abs(var1) << std::endl;
}