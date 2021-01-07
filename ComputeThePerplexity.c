/* 
Author: shamo0 

The cross-entropy of a unigram model is 9.91. What is its perplexity?

Answer correctly to the nearest integer. You may either submit the 
final answer directly in the plain-text mode, or you may write a program
which computes and displays the answer in the language of your choice.
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    float inp = 9.91;
    inp = pow(2,inp);
    printf ("%f", inp);
    return 0;
}
