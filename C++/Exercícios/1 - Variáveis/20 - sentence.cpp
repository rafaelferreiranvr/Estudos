//20 - Declare a string variable and prompt the user to enter a sentence. Then, output the number of characters and words.

#include <iostream>
#include <string>

int main(){
    int characters, words;
    std::string sentence;

    std::cout << "Type a sentence: ";
    std::getline(std::cin, sentence);

    const int character_count = sentence.length();
    int word_count = 0;

    char empty_character = 32;
    if (sentence[0] != empty_character){
        word_count++;
    };

    for (int i = 1; i < character_count - 1; i++){
        if ((sentence[i] == empty_character) && (sentence[i+1] != empty_character)) {
            word_count++;
        }
    };

    std::cout << "The sentence has " << character_count
    << " characters and " << word_count << " words." << std::endl;
}
