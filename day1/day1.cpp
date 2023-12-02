// day1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream f;
    f.open("data.txt");
    std::string line;
    int sum = 0;
    while (f) {
      std::getline(f, line);
      if (f) { // hmm, leider erforderlich
        char buf[100];
        int num[2] = { 0, 0 };
        int ndigits = 0;
        for (auto i:line) {
          if (isdigit(i)) {
            if (ndigits>0)
              num[1] = i - '0'; // overwrite the second digit)
            else
              num[0] = i-'0';
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

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
