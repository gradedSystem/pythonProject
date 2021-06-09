# pythonProject
Assignment 7 (Part 5 of the project)

Input: a sequence of binary digits from Part 4
Goal: Add errors to the binary sequence after Part4 (Hamming code). Decode Hamming code and
fix errors.
Final output: a sequence of binary digits identical to an output sequence from Part 2
Output:
1. Read the file with the sequence of bits from assignment 7 and divide into blocks of
8 or 16 bits based on your Hamming code method from the previous assignment. Each member
of a team should have one method. Sample output (1):
Original file: 0011001101101001…
Initial blocks: b1: 00110011, b2: 01101001, …
2. You will simulate the channel by randomly flipping each bit in each codeword with
a probability 30 – 50%. You will need to generate one error in one data bit of 30 – 50% blocks
randomly. For example, if you have 10 blocks, you will need to flip one data bit in 3-5 blocks. The
data bit you flip and the block you choose should be random.
Write a function called ErrorGen(percent, bitstring), which takes as input a bitstring block to send
over a binary symmetric channel, and simulates flipping bits at a rate percent. It then returns the
corrupted string.
Sample output (2):
Blocks with errors: b1: 10110100, b2: 01010101, …
3. You will also need a function HammingDecode(bitstring) that takes 8 or 16 bit
number (the output of the channel) and returns a guess at the 4 or 11 bit number originally sent.
Include all intermediate steps.
Sample output (3):
0 0 1 1 0 1 1 1:
Checking parity bits:
p1: b3+b5+b7 = 1+1+1 = 1 incorrect.
p2: b3+b6+b7 = 1+1+1 = 1 correct.
p3: b5+b6+b7 = 1+1+1 = 1 incorrect.
p0: b1+b2+b3+b4+b5+b6+b7 = 0+1+1+0+1+1+1 = 1 incorrect.
Error in position: 5
Corrected bitstring: 0 0 1 1 0 0 1 1.
Decoded bitstring: 1 0 1 1.
0 1 1 0 1 0 0 1:
Checking parity bits:
p1: b3+b5+b7 = 0+0+1 = 1 correct.
p2: b3+b6+b7 = 0+0+1 = 1 correct.
p3: b5+b6+b7 = 0+0+1 = 1 correct.
p0: b1+b2+b3+b4+b5+b6+b7 = 1+1+0+1+0+0+1 = 0 correct.
No error.
Decoded bitstring: 0 0 0 1.
4. Run functions HammingDecode and HammingDecode2 on all data blocks. Please
include all intermediate steps. The output should be the same as in the previous output (3), but
on all data blocks.
5. Combine all of the decoded bitstrings into one sequence. Print it and save it in a txt
file. Compare it with the with the sequence of bits from assignment 3. Sample output (5):
Decoded sequence:
10110101100010…
Sequence from assignment 3:
10110101100010…
They match.
