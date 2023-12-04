// day4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

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

bool replace_once(std::string& str, const std::string& from, const std::string& to) {
  size_t start_pos = str.find(from);
  if (start_pos == std::string::npos) return false;
  str.replace(start_pos, from.length(), to);
  return true;
}
void replace(std::string& str, const std::string& from, const std::string& to) {
  while (replace_once(str, from, to));
}

// compare lists
// part1 ~47 minutes --> 12:47 = 6:47, so it starts at 6:00 CEWT
int main()
{
    std::cout << "day4\n";
    // read data into 2 arrays (vectors)
    // find list2 entry in list1

    std::ifstream f;
    f.open("data.txt");
    std::string line;
    int sum = 0;
    while (f) {
      std::getline(f, line);
      if (f) { // read last line only once
//        std::cout << line << "\n";// ": " << f.tellg() << '\n';
        replace(line, "   ", " ");
        replace(line, "  ", " ");
        std::cout << line << "\n";// ": " << f.tellg() << '\n';
        std::vector<std::string> game = split(line.c_str(), ':'); // game|cards
        std::vector<std::string> tmp = split(game[0].c_str(), ' ');
        int id = stoi(tmp[1]);

        std::vector<std::string> gm = split(game[1].c_str(), '|'); // winner | card
        std::vector<std::string> win = split(gm[0].c_str(), ' ');
        std::vector<std::string> card = split(gm[1].c_str(), ' ');

        int points = 0;
        for (int i = 1; i < card.size(); i++) { // start with 1 to omit leading space
          if (std::find(win.begin(), win.end(), card[i]) != win.end()) {
            std::cout << card[i] << ", ";
// ha, wong:            if (i == 1) points = 1; else points *= 2;
            if (points == 0) points = 1; else points *= 2;
          }
          else
            ;
        }
        sum += points;
        std::cout << "points: " << points << "\n";
      }
      std::cout << "sum = " << sum << '\n';
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
