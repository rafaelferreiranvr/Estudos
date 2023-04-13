//12 - Declare an integer variable and prompt the user to enter a value for it. Then, output whether the value is even or odd.
#include <iostream>

int main(){
    int var1;
    
    std::cout << "Type a number: ";
    std::cin >> var1;
    
    int remainder = var1 % 2;

    if (remainder){
        std::cout << var1 << " is odd." << std::endl;
    } 
    else {
        std::cout << var1 << " is even." << std::endl;
    }   
}
