/*
 * Write a program that displays by console (with a print) 
 * numbers from 1 to 100 (both included and with a line break between each printout), replacing the following
 * each print), substituting the following:
 * - Multiples of 3 for the word "fizz".
 * - Multiples of 5 for the word "buzz".
 * - Multiples of 3 and 5 at the same time for the word "fizzbuzz".
 */

#include <stdio.h>

void main() {

    for ( int i = 1 ; i <= 100 ; i++){
        if(i%3==0){
            if(i%5==0){
                printf("fizzbuzz\n");
            }else{
                printf("fizz\n");
            }
        }else if (i%5==0){
            printf("buzz\n");
        }else{
            printf("%d\n",i);
        }
    }  
}