//9- Write a function that takes a double as parameter and returns its rounded value.

#include <iostream>
int round(double value, int precision){
    int int_value = value * precision;
    float rounded_value = int_value/precision;
    return rounded_value;
}

int main(){
    double var1;
    std::cout << "Type a double: ";
    std::cin >> var1;
    std::cout << "Rounded value: " << round(var1) << std::endl;
}