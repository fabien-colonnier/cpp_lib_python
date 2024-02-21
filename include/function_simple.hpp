#pragma once

#include <iostream>

class simple 
{

    private:
        int a=0;
    
    public:
        void set_a(int input);

        void process();

        int get_a();

};

extern "C" {
    simple* create(){ return new simple; }
    void set_a(simple* s, int val){ s->set_a(val);};
    void process(simple* s){ s->process(); };
    int get_a(simple* s){ return s->get_a(); };
}