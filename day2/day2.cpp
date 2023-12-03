// day2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> split(const char *str, char c = ' ')
{
  std::vector<std::string> result;
  do {
    const char *begin = str;
    while (*str != c && *str)
      str++;
    result.push_back(std::string(begin, str));
  } while (0 != *str++);
  return result;
}

// hmm, i only do parts 1 this year ...
// today is about tokenization
int main()
{
    std::cout << "day2\n";
    std::ifstream f;
    f.open("data.txt");
    std::string line;
    int sum = 0;
    while (f) {
      std::getline(f, line);
      if (f) { // hmm, leider erforderlich
        std::cout << line << ": " << f.tellg() << '\n';
        std::vector<std::string> game = split(line.c_str(), ':'); // #game
        std::vector<std::string> tmp = split(game[0].c_str(), ' ');
        int id = stoi(tmp[1]);
        std::vector<std::string> tokens = split(game[1].c_str(),';'); // grabs / throws
        int green = 0;
        int red = 0;
        int blue = 0;
        bool b = true;
        for (int i = 0; i < tokens.size(); i++) { // for each grab
          std::vector<std::string> tok = split(tokens[i].c_str(), ','); // --> colors
// ooh, such a stupid mistake, i did
//          j < tok.size()-1
// which is obviously giving 1 less element
          for (int j = 0; j < tok.size(); j++) {  // for each color
            std::vector<std::string> t = split(tok[j].c_str(), ' ');
            // t[0] is space
            int n = stoi(t[1]);// c - '0';
            if (strcmp(t[2].c_str(), "green") == 0) green = n;
            if (strcmp(t[2].c_str(), "red") == 0) red = n;
            if (strcmp(t[2].c_str(), "blue") == 0) blue = n;
          }
          b = b && ((green <= 13) && (blue <= 14) && (red <= 12));
        }
        if (b) sum += id;
        std::cout << "sum = " << sum << '\n';
      }
    }
    f.close();
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
