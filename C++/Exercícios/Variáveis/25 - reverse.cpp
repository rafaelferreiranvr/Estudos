//25 - Write a program that prompts the user to enter a string and outputs the string in reverse order.

#include <iostream>

int main(){
    std::string str;
    std::cout << "Type a string: " << std::endl;
    std::cin >> str;
    
    const int character_count = str.length();
    std::string reversed_string = str;

    for (int i = 0; i < character_count; i++){
        reversed_string[character_count - i - 1] = str[i];
    }

    std::cout << "Reversed string: " << std::endl << reversed_string << std::endl;
}
