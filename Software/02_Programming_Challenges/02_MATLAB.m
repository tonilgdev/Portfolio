%{
 * Write a program that prints the first 50 numbers of the Fibonacci sequence 
 * starting at 0. The Fibonacci series is composed of a sequence of numbers in 
 * which the next one is always the sum of the previous two.
 * 0, 1, 1, 2, 3, 5, 8, 13…
%}

% Clear the entire workspace and command windows
clc;
clear all;

% Ask to the user the number of values
values = input("Enter the number of values in the sequence you want. ")
result = zeros(1,values);

% Loop to create all the values
for i = 1:values
    if (i==1)
        result(i) = 0;
    elseif (i == 2)
        result(i) = 1;
    else
        result(i) = result (i-1) + result (i-2);
    end

end

% Change the format to see properly the results
format shortG;
result

