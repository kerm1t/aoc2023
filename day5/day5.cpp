// day5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

// 2do: prepare next day
// 2do: put fcts into header file
// 1:40 hours
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

struct mapentry {
  long long dst;
  long long src;
  long long len;
};

long long do_map(const long long iseed, const std::vector<mapentry>& map) { // grrr, this was long
//  long iseed = stoi(seed);
  for (int i = 0; i < map.size(); i++) {
    if ((iseed > map[i].src) &&
      (iseed < (map[i].src + map[i].len))
      ) {
      long long n = iseed - map[i].src; // diff, grrrr, this was int
      long long dst = map[i].dst + n;
      return dst;
    }
  }
  // not mapped yet
  std::cout << "no mapping" << "\n";
  return iseed;
}
enum state { init=0, process = 1, readmap = 2, other = 255 };
state runstate = init;

void prettyprint(std::string line, std::vector<long long> v) {
  for (int i = 0; i < v.size(); i++)
    std::cout << v[i] << " ";
  std::cout << "\n";
  std::cout << line << '\n';
}

int main()
{
  std::cout << "day5\n";

  std::ifstream f;
  f.open("data.txt");
  std::string line;
  int sum = 0;
//  int state = 0;
//  bool b_statenew = false;
  std::vector<std::string> seeds1;
  std::vector<long long> iseeds;
  std::vector<mapentry> map;
  while (f) {
    std::getline(f, line);
    if (f) { // read last line only once
//      std::cout << line << '\n';
      if (strncmp(line.c_str(), "seeds:", 6) == 0) {
//        state = 0;
        seeds1 = split(line.c_str(), ' ');
        for (int i = 1; i < seeds1.size(); i++) iseeds.push_back(stoll(seeds1[i]));
      }

      if (line.length() == 0) runstate = other;

      if (runstate == process) {
        // update
        if (map.size() > 0) {
          for (int i = 0; i < iseeds.size(); i++)
            iseeds[i] = do_map(iseeds[i],map);
        }
//        b_statenew = false;
        prettyprint(line, iseeds);
        map.clear();
        runstate = readmap;
      };

      if (runstate == readmap) {
        std::vector<std::string> _me = split(line.c_str(), ' '); // dst|src|len
        mapentry me = { stoll(_me[0]), stoll(_me[1]), stoll(_me[2]) };
        map.push_back(me);
      }

      if (strncmp(line.c_str(), "seed-to-soil map:", 17) == 0) {
//        b_statenew = true;
//        state = 1;
        prettyprint(line, iseeds); 
        runstate = readmap;// process;
      }
      if (strncmp(line.c_str(), "soil-to-fertilizer map:",23) == 0) {
//        b_statenew = true;
//        state = 2;
        runstate = process;
      }
      if (strncmp(line.c_str(), "fertilizer-to-water map:", 24) == 0) {
//        b_statenew = true;
//        state = 3;
        runstate = process;
      }
      if (strncmp(line.c_str(), "water-to-light map:",19) == 0) {
//        b_statenew = true;
//        state =4;
        runstate = process;
      }
      if (strncmp(line.c_str(), "light-to-temperature map:", 25) == 0) {
//        b_statenew = true;
//        state = 5;
        runstate = process;
//        prettyprint(line, iseeds);
      }
      if (strncmp(line.c_str(), "temperature-to-humidity map:", 28) == 0) {
//        b_statenew = true;
//        state = 6;
        runstate = process;
//        prettyprint(line, iseeds);
      }
      if (strncmp(line.c_str(), "humidity-to-location map:", 25) == 0) {
//        b_statenew = true;
//        state = 7;
        runstate = process;
//        prettyprint(line, iseeds);
      }
    

    }
  }
  // process last step
  if (map.size() > 0) {
    for (int i = 0; i < iseeds.size(); i++)
      iseeds[i] = do_map(iseeds[i], map);
  }
  prettyprint(line, iseeds);

  // smallest num
  long long smallest = 9999999999999999;
  for (int i = 0; i < iseeds.size(); i++) if (iseeds[i] < smallest) smallest = iseeds[i];
  std::cout << "smallest seed: " << smallest;
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
