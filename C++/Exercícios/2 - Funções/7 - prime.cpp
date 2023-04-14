//7- Write a function that takes an integer as parameter and returns true if the number is prime, and false otherwise.

#include <iostream>
bool is_prime(int value){
    int factors = 0;
    for (int i = 1; i <= value; i++){
        if (value % i == 0){
            factors++;
        }
    }
    if (factors == 2){
        return true;
    } else {
        return false;
    }
}

int main(){
    int var1;
    std::cout << "Type an integer: ";
    std::cin >> var1;

    if (is_prime(var1)){
        std::cout << var1 << " is prime." << std::endl;
    } else {
        std::cout << var1 << " is not prime." << std::endl;
    }
}