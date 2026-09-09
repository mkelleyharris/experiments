#!/usr/bin/env ruby

class Calc
  def add(a, b)
    #puts a+b
    return a+b
  end
  
  def sub(a, b)
    return a - b
  end

  def mult(a, b)
    puts a*b
  end  
end


if __FILE__ == $0 
  c = Calc.new

  puts c.add(1, 2)
  puts c.sub(1, 2)
  puts c.mult(2, 3)
  #puts Calc.instance_methods
end
