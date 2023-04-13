//16 - Declare two integer variables and prompt the user to enter values for them. Then, output their sum, difference, product, and quotient.

#include <iostream>

int main(){
    int var1, var2, sum, difference, product, quotient;

    std::cout << "Type a number: ";
    std::cin >> var1;
    std::cout << "Type another number: ";
    std::cin >> var2;

    sum = var1 + var2;
    difference = var1 - var2;
    product = var1 * var2;
    quotient = var1 / var2;
    
    std::cout << "The sum between " << var1 << " and " << var2 << " is " << sum << std::endl;
    std::cout << "The difference between " << var1 << " and " << var2 << " is " << difference << std::endl;
    std::cout << "The product between " << var1 << " and " << var2 << " is " << product << std::endl;
    std::cout << "The quotient between " << var1 << " and " << var2 << " is " << quotient << std::endl;
}   