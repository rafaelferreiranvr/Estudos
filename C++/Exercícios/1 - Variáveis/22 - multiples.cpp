//22 - Declare an integer variable and prompt the user to enter a value for it. Then, use a loop to output the first 10 multiples of the value.

#include <iostream>

int main(){
    int var1;

    std::cout << "Type a number: ";
    std::cin >> var1;

    std::cout << "First 10 multiples of " << var1 << " are:" << std::endl;

    for (int i = 1; i <= 10; i++){
        std::cout << i * var1 << std::endl;
    }
}