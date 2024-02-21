#include <iostream>
#include "function_simple.hpp"

using namespace std;


int main() {
int number;
cout << "Enter an integer! ";
cin >> number;

simple obj;
obj.set_a(number);
obj.process();
int output = obj.get_a();

cout << "After process, input = " << number << " becomes " << output << std::endl;
return 0;
}
