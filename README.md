# pythonProject
Assignment 3 (Part 2 of the project)
Input: “Text.txt” file and the result from Part 1.
Goal: Encode the text from the “Text.txt” file using Shannon-Fano or Huffman algorithm with
probabilities from Part 1.
Output:
1. Symbols with probabilities sorted in descending order (round to three decimal places). Please
also add the notations for whitespace, new line, tab and etc. in order to distinguish them.
Sample output for (1):
A – 0.04
B – 0.032
a – 0.025
space – 0.012
, – 0.005
…
2. Build Shannon-Fano or Huffman code tree based on the given list with probabilities. Include
all intermediate steps.
Sample output for (2):
Step 1.
Node1: (0) B, E – sum 0.571
Node2: (1) A, D, space – sum 0.429
Step 2.
Node3: (00) B – sum 0.285
Node4: (01) E – sum 0.285
Node5: (10) A, D – sum 0.285
Node6: (11) space – sum 0.142
Step 3.
Node7: (100) A – sum 0.142
Node8: (101) D – sum 0.142
…..
3. Create the list with symbols and their codewords in descending order starting from the most
frequent symbol to the least frequent symbol. Perform a traversal of tree to determine all
codewords.
Sample output for (3):
symbol – probability - codeword:
B - 0.285 – 00
E - 0.285 – 01
A- 0.142 – 100
….
4. Scan text again, output a sequence of binary digits using the Shannon-Fano or Huffman
codes, and save in a new .txt file.
Sample output for (4):
10110101100010…
5. After these replacements are made, calculate a data compression ratio: number of bits in
the original text / the number of bits in the compressed text, and average code length
= ∑ ( frequencyi x code lengthi ) / ∑ ( frequencyi ).
Note: ASCII uses 1 byte to represent a letter or a punctuation mark.
Sample output for (5):
Number of bits in the original text: 128 bits
Number of bits in the compressed text: 56 bits
Compression ratio = 2.29
Average code length = 2.52 bits/symbol
Submission: please submit the report in Word specifying responsibilities of each team member.
Add a general description, the screenshots of execution and source code as text. Also, please
include the Github link. Work together on the assignment using the Github folder.
Responsibilities should be divided equally between team members. Write down your code as
clearly as possible and add suitable comments. Submit just one combined report per group. No
changes in the code should be made after the submission.
The defence is required to get a grade for the assignment. You need to defend it in class during
the week 4. I will take out points for the later defence (50%). All members of the team need to
present during the defence, be able to answer the questions regarding the assignment and the
lecture, and change the code if requested. I might ask any member of the team to explain or
change the code.
It needs to be your own code. You shouldn’t use any additional functions (just the standard
ones), frameworks or libraries or solutions from the internet.
