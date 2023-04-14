//8- Write a function that takes a string as parameter and returns true if the string is a palindrome, and false otherwise.

#include <iostream>

bool is_palindrome(std::string str){
    int size = str.size();
    int middle = size/2;

    for (int i = 0; i < middle; i++){
        if (str[i] != str[size - 1 - i]){
            return false;
        }
    }

    return true;
}

int main(){
    std::string var1;
    std::cout << "Type a string: ";
    std::cin >> var1;

    if (is_palindrome(var1)){
        std::cout << var1 << " is a palindrome." << std::endl;
    } else {
        std::cout << var1 << " is not a palindrome." << std::endl;
    }
}