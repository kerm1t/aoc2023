// day3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

char grid[300][300]; // better large than sorry

bool issymbol(char in) {
  return (in == '#') || (in == '*') || (in == '%') || (in == '@') ||
         (in == '-') || (in == '/') || (in == '$') || (in == '+') || (in == '&') ||
         (in == '=') // forgot this :-/
    ;
}

// considers border conditions
bool check_connecivity_8(int r, int c) {
// 1|2|3
// -+-+-
// 4|x|5
// -+-+-
// 6|7|8
  bool b1 = false;
  bool b2 = false;
  bool b3 = false;
  bool b4 = false;
  bool b5 = false;
  bool b6 = false;
  bool b7 = false;
  bool b8 = false;
  if (r > 0) {
    if (c > 0) b1 = issymbol(grid[r - 1][c - 1]);
    b2 = issymbol(grid[r - 1][c]);
    b3 = issymbol(grid[r - 1][c + 1]);
  }
  if (c > 0) b4 = issymbol(grid[r][c - 1]);
  b5 = issymbol(grid[r][c + 1]);
  if (c > 0) b6 = issymbol(grid[r + 1][c - 1]);
  b7 = issymbol(grid[r + 1][c]);
  b8 = issymbol(grid[r + 1][c + 1]);
  return b1 || b2 || b3 || b4 || b5 || b6 || b7 || b8;
}

int main() // might be the start of a rogue-like game :-)
{
    std::cout << "day3\n";
    std::ifstream f;
    f.open("data.txt");
    std::string line;
    int sum = 0;
    int row = 0;
    int col = 0;
    while (f) {
      std::getline(f, line);
      if (f) { // read last line only once
        bool bzahl = false;
        col = 0;
        for (auto c : line) {
          grid[row][col++] = c;
        }
        row++;
      }
    }
    // c=0, r=0 --> border conditions in place
    int r = 0;
    int c = 0;
    // b1, need while instead of for-loop to skip 1- and 10-digits of numbers
    while (r < row) {//for (int r = 1; r < row; r++) {
      c = 0; // b2, forgot you :-)
      while (c < col) {//for (int c = 1; c < col; c++) {
        bool b = false;
        int num = 0;
        if (isdigit(grid[r][c])) {
          if (isdigit(grid[r][c+1])) {
            if (isdigit(grid[r][c+2])) { // check for max. 3-digit no
              // check either
              num = (grid[r][c] - '0')*100 + (grid[r][c + 1] - '0')*10 + (grid[r][c + 2] - '0');
              b = b || check_connecivity_8(r, c + 2); // b3, instead of doing this check for each digit-level, which interferes with c++
              b = b || check_connecivity_8(r, c + 1); //     do all checks per level
              b = b || check_connecivity_8(r, c);     // some checks are redundant
              c++;
            }
            else {
              num = (grid[r][c] - '0') * 10 + (grid[r][c + 1] - '0');
              b = b || check_connecivity_8(r, c + 1);
              b = b || check_connecivity_8(r, c);
            }
            c++;
          }
          else {
            num = grid[r][c] - '0';
            b = b || check_connecivity_8(r, c);
          }
//          std::cout << "num:" << num << (b?" true":" false") << '\n';
          if (b) {
            sum += num;
            std::cout << num << ", ";
          }
          else {
            std::cout << "[" << num << "], ";
          }
        }
        c++;
      }
      r++;
      std::cout << "\nl." << (r+1) << ": "; // output line-no for debugging
    }
    std::cout << "sum = " << sum << '\n';


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
