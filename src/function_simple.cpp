#include "function_simple.hpp"

void simple::set_a(int input){
    printf("in set_a function, a = %d, input = %d\n", this->a, input);
    this->a = input;
    printf("a is set\n");
    return;
}

void simple::process(){
    a = a*2;
}

int simple::get_a(){
    return a;
}
