//10- Write a function that takes a string as parameter and returns a new string with all the vowels replaced by asterisks.

#include <iostream>
bool is_vowel(char character){
    char vowels[] = {'a', 'e', 'i', 'o', 'u'};
    for (char i: vowels){
        if (character == i){
            return true;
        }
    }
    return false;
}

std::string vowels_to_asterisks(std::string str){
    std::string asterisk = "*";

    for (int i = 0; i < str.size(); i++){
        if (is_vowel(str[i])){
            str[i] = asterisk[0];
        }
    }
    return str;
}

int main(){
    std::string var1;
    std::cout << "Type a string: ";
    std::cin >> var1;

    std::cout << "String with its vowels replaced by asterisks: " << vowels_to_asterisks(var1) << std::endl;
}