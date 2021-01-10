'''
Author: shamo0

The perplexity of a bigram model is 170. Compute its cross-entropy 
corrected to 2 decimal places.

You may either submit the final answer in the plain-text mode, or 
you may submit a program in the language of your choice to compute 
the required value.
'''
import math

perplexity = 170
cross_entropy = math.log(perplexity,2)
print("{:.2f}".format(cross_entropy))
