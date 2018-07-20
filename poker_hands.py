from poker_comparison import FiveCardHand, calculate_victories
import time

# We can import either poker_comparison, or cython_poker_comparison if compiled. Not much optimization work is done
# on the cython module, but it does provide a modest, roughly 30% speed increase on my machine.
# Future work on this module could include writing more cython specific code in the cython module, or utilizing
# a more complex indexing system to perform hand ranking lookups instead of recalculating the value for each hand.

# Call here function in poker_comparison, passing in our file name
start = time.time()
calculate_victories('poker.txt')
print(f'Took {time.time() - start}')