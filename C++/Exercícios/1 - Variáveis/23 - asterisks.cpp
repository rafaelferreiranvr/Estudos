//23 - Write a program that prompts the user to enter two integer values representing the length and width of a rectangle. Then, use a loop to output a pattern of asterisks that represents the rectangle.

#include <iostream>

int main(){
    float length, width;

    std::cout << "Type the width of the retangle: ";
    std::cin >> width;

    std::cout << "Type the length of the retangle: ";
    std::cin >> length;

    std::string asterisk_row = "";
    for (int i = 0; i < width; i++){
        asterisk_row.append("*");
    };
    
    std::cout << "Asterisk Rectangle: " << std::endl;
    for (int i = 0; i < length; i++){
        std::cout << asterisk_row << std::endl;
    };
}
