//24 - Declare an integer variable and prompt the user to enter a value for it. Then, use a loop to output the Fibonacci sequence up to the given value.

#include <iostream>

int main(){
    int var1, current_value, previous_value, add_value;

    std::cout << "Type a number: ";
    std::cin >> var1;

    current_value = 1;
    previous_value = 0;
    add_value = 0;

    std::cout << "Fibonacci sequence until " << var1 << ":" << std::endl; 

    while (current_value < var1)
    {
        std::cout << current_value << std::endl;
        add_value = previous_value;
        previous_value = current_value;
        current_value += add_value;    
    };    
}