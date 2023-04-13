//4- Write a function that takes a double as parameter and returns its square root.

#include <iostream>
#include <math.h>

double square_root(double value){
    return sqrt(value);
}

int main(){
    double var1;
    std::cout << "Type a double: ";
    std::cin >> var1;
    std::cout << "Square root: " << square_root(var1) << std::endl;
}