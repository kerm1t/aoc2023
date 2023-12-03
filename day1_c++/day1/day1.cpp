// day1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>

bool replace(std::string& str, const std::string& from, const std::string& to) {
  size_t start_pos = str.find(from);
  if (start_pos == std::string::npos) return false;
  str.replace(start_pos, from.length(), to);
  return true;
}

void part1(bool b_numberz_as_string) {
  std::ifstream f;
  f.open("data.txt");
  std::string line;
  int sum = 0;
  while (f) {
    std::getline(f, line);
    if (f) { // hmm, leider erforderlich
      int num[2] = { 0, 0 };
      int ndigits = 0;
      std::cout << line << ": ";
      if (b_numberz_as_string) {
        while (replace(line, "one", "1"));
        while (replace(line, "two", "2"));
        while (replace(line, "three", "3"));
        while (replace(line, "four", "4"));
        while (replace(line, "five", "5"));
        while (replace(line, "six", "6"));
        while (replace(line, "seven", "7"));
        while (replace(line, "eight", "8"));
        while (replace(line, "nine", "9"));
//        while (replace(line, "zero", "0"));
// --------------------------------------------------
// hmm, this method doesn't work with aliased numberz
// e.g.      three49oneightf: 3491ightf : 31
// instead it requires to e.g. copy all found numberz
// --------------------------------------------------
      }
      for (auto i : line) {
        if (isdigit(i)) {
          if (ndigits > 0)
            num[1] = i - '0'; // overwrite the second digit)
          else
            num[0] = i - '0';
          ndigits++;
        }
      }
      if (ndigits == 1) num[1] = num[0];
      int nline = num[0] * 10 + num[1];
      sum += nline;
      std::cout << line << ": " << nline << '\n';//f.tellg() << '\n';
    }
  }
  f.close();
  std::cout << "sum = " << sum << '\n';
}

int main() // day 1 is for warmup and to process a file, get a line and parse this line char-wise
{
  part1(true); // b_numberz_as_string - true doesn't work yet, s. above
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
