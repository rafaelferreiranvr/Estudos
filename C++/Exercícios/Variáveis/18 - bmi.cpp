/*18 - Write a program that prompts the user to enter their weight in kilograms
and their height in meters. Then, calculate and output their body mass index (BMI)
using the formula BMI = weight / (height * height).
*/

#include <iostream>

int main(){
    float weight, height, bmi;

    std::cout << "Type your weight: ";
    std::cin >> weight;

    std::cout << "Type your height: ";
    std::cin >> height;

    bmi = weight / (height * height);

    std::cout << "Your BMI is " << bmi << std::endl;
}
