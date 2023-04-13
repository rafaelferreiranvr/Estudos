//3- Write a function that takes a string as parameter and returns the length of the string.

#include <iostream>
int string_length(std::string str){
    int length = 0;
    for (int i : str){
        length++;
    }
    return length;
}

int main(){
    std::string var1;
    std::cout << "Type a string: ";
    std::cin >> var1;

    std::cout << "Length of the string: " << string_length(var1) << std::endl;
}