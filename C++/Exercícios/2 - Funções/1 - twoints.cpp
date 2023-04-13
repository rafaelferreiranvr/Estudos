//1- Write a function that takes two integers as parameters and returns their sum.

#include <iostream>
int sum(int a, int b){
    return a + b;
}

int main(){
    int var1, var2;
    std::cout << "Type an integer: ";
    std::cin >> var1;

    std::cout << "Type another integer: ";
    std::cin >> var2;

    std::cout << "Sum: " << sum(var1, var2) << std::endl;
}