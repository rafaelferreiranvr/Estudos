//13 - Write a program that prompts the user to enter two double values, calculates their average, and outputs the result rounded to two decimal places.
#include <iostream>

int main(){
    double var1;
    double var2;

    std::cout << "Type a number: ";
    std::cin >> var1;

    std::cout << "Type another number: ";
    std::cin >> var2;
    
    float rounded_mean = round((var1 + var2)/2 * 100)/100;
    std::cout << "Rounded Average: " << rounded_mean << std::endl;
}