//17 - Write a program that prompts the user to enter a string of text and counts the number of vowels (a, e, i, o, u) in the string. Then, output the total count of vowels in the string.
//Corrigir, sizeof não funciona com strings
#include <iostream>

int main(){
    std::string text;
    std::cout << "Type some text: ";
    std::cin >> text;

    int vowel_count = 0;
    int letter_count = text.length();
    char vowels[5] = {'a', 'e', 'i', 'o', 'u'};

    for (int i = 0; i < letter_count; i++){
        char letter = text[i];
        for (int vowel: vowels){
            if (letter == vowel){
                vowel_count++;
            };
        };
    };

    std::cout << "The typed text has " << vowel_count << " vowels." << std::endl;
};