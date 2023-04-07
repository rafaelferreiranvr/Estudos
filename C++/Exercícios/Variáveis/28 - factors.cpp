//28 - Write a program that prompts the user to enter a positive integer and outputs all of its factors.
#include <iostream>

int main(){
    int var1;
    std::cout << "Type a number: ";
    std::cin >> var1;

    std::cout << "Factors of " << var1 << ": " << std::endl;
    for (int i = 1; i <= var1/2; i++){
        if (var1 % i == 0){
            std::cout << i << std::endl;
        }
    }
    std::cout << var1 << std::endl;
}