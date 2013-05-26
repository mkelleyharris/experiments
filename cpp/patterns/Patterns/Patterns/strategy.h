//
//  strategy.h
//  
//
//  Created by Michael Kelley Harris on 5/26/13.
//
//

#ifndef _strategy_h
#define _strategy_h

#include <memory>

class Strategy
{
public:
    virtual int execute(int a, int b) = 0;
};

class Add : public Strategy
{
public:
    int execute(int a, int b) { return a + b; }
    
};

class Subtract : public Strategy
{
public:
    int execute(int a, int b) { return a - b; }
    
};

class Multiple : public Strategy
{
public:
    int execute(int a, int b) { return a * b; }
    
};

class Context
{
public:
    Context(Strategy* strategy)
    : strat(strategy)
    {
    }
    
    int execute(int a, int b) { return strat->execute(a, b); }
    
private:
    std::shared_ptr<Strategy> strat;
};

#endif
