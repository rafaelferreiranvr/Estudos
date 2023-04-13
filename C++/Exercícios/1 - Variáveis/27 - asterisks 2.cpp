//27 - Write a program that prompts the user to enter two integer values representing the length and width of a rectangle. Then, use recursion to output a pattern of asterisks that represents the rectangle.

#include <iostream>
std::string rectangle_length(int length, std::string str){
    if (str.length() < length){
        str.append("*");
        return rectangle_length(length, str);
    } else {
        return str;
    }
}

void rectangle_width(std::string line, int width, int printed_lines){
    if (printed_lines < width){
        std::cout << line << std::endl;
        printed_lines++;
        rectangle_width(line, width, printed_lines);
    }
}

void asterisk_rectangle(int width, int length){
    std::string line = "";
    line = rectangle_length(length, line);
    rectangle_width(line, width, 0);
}

int main(){
    float width, length;

    std::cout << "Type the width of the retangle: ";
    std::cin >> width;

    std::cout << "Type the length of the retangle: ";
    std::cin >> length;

    std::cout << "Asterisk Rectangle: " << std::endl;
    asterisk_rectangle(width, length);
}
