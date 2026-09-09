#!/usr/bin/env ruby
#unit tests for rubyplay1

require 'test/unit'
require 'rubyplay1'
class TestAdd < Test::Unit::TestCase
    def test_add
    	calc = Calc.new
    	expected = calc.add(3,2)
    	assert_equal expected, 5
    end
    
    def test_sub
      calc = Calc.new
      assert_equal -2, calc.sub(1, 3)
    end
end
