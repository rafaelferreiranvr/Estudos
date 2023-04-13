//14 - Declare an integer variable and prompt the user to enter a value for it. Then, output whether the value is positive, negative, or zero.
#include <iostream>

int main(){
    int var1;
    
    std::cout << "Type a number: ";
    std::cin >> var1;

    if (var1 < 0){
        std::cout << var1 << " is negative." << std::endl;
    }
    else if (var1 > 0){
        std::cout << var1 << " is positive." << std::endl;
    } 
    else if (var1 == 0){
        std::cout << var1 << " is zero." << std::endl;
    }


}