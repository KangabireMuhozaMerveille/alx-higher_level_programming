#!/usr/bin/python3

def add_integer(a, b=98):
    
    if not isinstance(a, (float, int)) or not isinstance(b, (int, float)):
            raise TypeError("a must be an integer or b must be an integer")
            result = a + b
            return result
