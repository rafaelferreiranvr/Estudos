//9- Write a function that takes a double as parameter and returns its rounded value.

#include <iostream>
#include <math.h>

float round(double value, int precision){
    value *= pow(10, precision);
    int int_value = value;
    float rounded_value = int_value/pow(10, precision);
    return rounded_value;
}

int main(){
    double var1;
    std::cout << "Type a double: ";
    std::cin >> var1;
    std::cout << "Rounded value: " << round(var1, 2) << std::endl;
}