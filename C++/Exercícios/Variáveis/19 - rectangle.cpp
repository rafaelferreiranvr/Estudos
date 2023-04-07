//19 - Write a program that prompts the user to enter the length and width of a rectangle, calculates its area and perimeter, and outputs the results.

#include <iostream>

int main(){
    float length, width, area;

    std::cout << "Type the length of the rectangle: ";
    std::cin >> length;

    std::cout << "Type the width of the rectangle: ";
    std::cin >> width;

    area = length * width;
    
    std::cout << "The area of the rectangle is " << area << std::endl;
}
