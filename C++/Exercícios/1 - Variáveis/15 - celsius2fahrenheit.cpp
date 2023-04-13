//15 - Write a program that prompts the user to enter a temperature in Celsius and outputs the temperature in Fahrenheit.

#include <iostream>

int main(){
    float temperature_in_celsius;

    std::cout << "Type the temperature in Celsius: ";
    std::cin >> temperature_in_celsius;

    float temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32;

    std::cout << temperature_in_celsius << "C equals "  << temperature_in_fahrenheit << "F.";
}
