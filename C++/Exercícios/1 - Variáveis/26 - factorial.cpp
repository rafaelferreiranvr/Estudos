//26 - Declare an integer variable and prompt the user to enter a value for it. Then, use recursion to output the factorial of the value.

#include <iostream>
int rec_fact(int multiplicand, int multiplier){
    if (multiplier > 1){
        multiplier--;
        multiplicand *= multiplier;
        return rec_fact(multiplicand, multiplier);
    } else {
        return multiplicand;
    };
}

int factorial(int number){
    return rec_fact(number, number);
}

int main(){
    int var1;

    std::cout << "Type a number: ";
    std::cin >> var1;

    std::cout << "Factorial of " << var1 << ": " << factorial(var1) << std::endl;
}