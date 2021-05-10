# pythonProject
Assignment 6 (Part 4 of the project)
Input: file with the sequence of bits from assignment 3.
Goal: Encode the binary sequence after Part2 (Shannon-Fano or Huffman code) with Hamming
code.
Final output: a sequence of binary digits ready for error correction.
Output:
1. Read the file with the sequence of bits from assignment 3. Sample output (1):
10110101100010…
2. For teams of 2: one member builds (15, 11) Extended Hamming code as described
in Lecture 4 (it uses 11 data bits), another member builds (7, 4) Hamming code using one of the
approaches from Lecture 5 (it uses 4 data bits). For approach 1 (7, 4) Hamming code from Lecture
5 use the extended version where you will add a parity bit in the 0th position to check the parity
of all 7 bits.
For teams of 3: one member builds (15, 11) Extended Hamming code using approach from
Lecture 4, 2nd member builds (7, 4) Extended Hamming code using first approach from Lecture
5, 3rd - (7, 4) Hamming code using the second approach from Lecture 5 (with matrices).
Divide the sequence from the previous output (1) into data blocks: 11 data bits for (15, 11)
Extended Hamming code, and 4 data bits for (7, 4) Hamming code.
Sample output (2):
Data blocks: b1: 1011, b2: 0101, b3: 0001 …
3. Write a function HammingEncode(bitstring) that takes a sequence of 11 bits and
returns the 16-bit codeword for (15, 11) Extended Hamming to be sent over the channel, and a
function HammingEncode2(bitstring) that takes a sequence of 4 bits and returns the 8-bit
codeword for (7, 4) Extended Hamming to be sent over the channel (or the 7-bit codeword for
(7, 4) Hamming approach 2 with matrices). Include all intermediate steps.
Sample output (3):
1011:
Expand the block to 8 bits: _ _ _ 1 _ 0 1 1.
p1: b3+b5+b7 = 1+0+1 = 0.
p2: b3+b6+b7 = 1+1+1 = 1.
p3: b5+b6+b7 = 0+1+1 = 0.
p0: b1+b2+b3+b4+b5+b6+b7 = 0+1+1+0+0+1+1 = 0.
Encoded bitstring: 00110011.
4. Run functions HammingEncode and HammingEncode2 on all data blocks. Please
include all intermediate steps. The output should be the same as in the previous output (3), but
on all data blocks.
