import heapq
from heapq import heappop, heappush

# heapq is default library for heatmaps

Node_Value_1 = []
Node_Value_2 = []
Node_letters_1 = []
Node_letters_2 = []

class Node:
    def __init__(self, character, frequency):
        self.data = str(frequency)
        self.character = character
        self.frequency = frequency
        self.right = None
        self.left = None

    def __lt__(self, other):
        if other is None and not isinstance(other, Node):
            return -1
        return self.frequency < other.frequency

    def __repr__(self):
        return "Data" + str(self.data)


class Huffman_algo:

    def __init__(self):
        self.heap = []
        self.dict = {}
        self.reverse_mapping = {}

    def initialize(self, val):
        for ind, key in val.items():
            new_value = Node(ind, key)
            heapq.heappush(self.heap, new_value)
        while len(self.heap) > 1:
            first_node = heapq.heappop(self.heap)
            second_node = heapq.heappop(self.heap)
            m = Node(None, first_node.frequency + second_node.frequency)
            m.left = first_node
            m.right = second_node
            Node_Value_1.append(str(round(float(str(m.left).replace('Data', '')), 3)))
            Node_Value_2.append(str(round(float(str(m.right).replace('Data', '')), 3)))
            if first_node.character is not None:
                Node_letters_1.append(first_node.character)
            if second_node.character is not None:
                Node_letters_2.append(second_node.character)

            heapq.heappush(self.heap, m)

        item = heapq.heappop(self.heap)
        node = ""
        self.reverse(item, node)

    def reverse(self, item, node):
        if item is None:
            return

        if item.character is not None:
            self.dict[item.character] = node
            self.reverse_mapping[node] = item.character
            return
        self.reverse(item.left, node + "0")
        self.reverse(item.right, node + "1")

    def print_bytes(self, val):
        string = ""
        for i in val:
            if i == ' ':
                string += self.dict['space']
            elif i == '\t':
                string += self.dict['tab']
            elif i == '\n':
                string += self.dict['newspace']
            else:
                string += self.dict[i]
        return string

    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""
        k = 1
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                print("Step " + str(k) + ".")
                character = self.reverse_mapping[current_code]
                value = list(self.reverse_mapping.keys()).index(current_code)
                temp_list = []
                letter_list = []
                if value < 2:
                    temp_list.append(tuple(self.reverse_mapping.items())[value][0])
                    for name, age in self.reverse_mapping.items():
                        if name == tuple(self.reverse_mapping.items())[value][0]:
                            letter_list.append(age)
                            break
                    temp_list.append(tuple(self.reverse_mapping.items())[value + 1][0])
                    for name, age in self.reverse_mapping.items():
                        if name == tuple(self.reverse_mapping.items())[value + 1][0]:
                            letter_list.append(age)
                            break
                    temp_list.append(tuple(self.reverse_mapping.items())[value + 2][0])
                    for name, age in self.reverse_mapping.items():
                        if name == tuple(self.reverse_mapping.items())[value + 2][0]:
                            letter_list.append(age)
                            break
                    s = 2
                    for i in reversed(range(len(letter_list))):
                        print(str(temp_list[len(letter_list) - 1]) + ". Node" + str(value + s) + ": (" + str(
                            temp_list[len(temp_list) - 1]) + ")" + ','.join(
                            map(str, letter_list)))
                        if len(letter_list) == 1:
                            print("Symbol: " + str(temp_list[len(letter_list) - 1]) + " - " + str(
                                letter_list[len(temp_list) - 1]))
                        s -= 1
                        letter_list.pop()
                        temp_list.pop()
                else:
                    temp_list.append(tuple(self.reverse_mapping.items())[value][0])
                    for name, age in self.reverse_mapping.items():
                        if name == tuple(self.reverse_mapping.items())[value][0]:
                            letter_list.append(age)
                            break
                    temp_list.append(tuple(self.reverse_mapping.items())[value - 1][0])
                    for name, age in self.reverse_mapping.items():
                        if name == tuple(self.reverse_mapping.items())[value - 1][0]:
                            letter_list.append(age)
                            break
                    temp_list.append(tuple(self.reverse_mapping.items())[value - 2][0])
                    for name, age in self.reverse_mapping.items():
                        if name == tuple(self.reverse_mapping.items())[value - 2][0]:
                            letter_list.append(age)
                            break
                    n = 2
                    for i in reversed(range(len(letter_list))):
                        print(str(temp_list[len(letter_list) - 1]) + ". Node" + str(value - n) + ": (" + str(
                            temp_list[len(letter_list) - 1]) + ") " + ','.join(
                            map(str, letter_list)))
                        if len(letter_list) == 1:
                            print("Symbol: " + str(temp_list[len(temp_list) - 1]) + " - " + str(
                                letter_list[len(temp_list) - 1]))
                        n -= 1
                        letter_list.pop()
                        temp_list.pop()

                if character == 'newspace':
                    character = "\n"
                elif character == 'space':
                    character = " "
                elif character == 'tab':
                    character = '\t'
                decoded_text += character
                current_code = ""
                k += 1

        return decoded_text, self.reverse_mapping

    def dict(self):
        return self.dict


def average_code_length(freq, sab):
    l1 = []
    l2 = []
    sum_freq_code = 0
    sum_freq = 0
    for ind, key in freq.items():
        l1.append(key)
    for ind, key in sab.items():
        l2.append(len(key))
    for i in range(len(l1)):
        sum_freq_code += l1[i] * l2[i]
        sum_freq += l1[i]
    return "Average code length = " + str(round(sum_freq_code / sum_freq, 2)) + " bits/symbol"


def merge(d1, d2):
    d3 = {**d1, **d2}
    for key, index in d3.items():
        if key in d1 and key in d2:
            d3[key] = [index, d1[key]]
    return d3


def print_Datablocks_4(bitstring):
    n = 4
    l = 1
    chunks = [bitstring[i:i+n] for i in range(0, len(bitstring), n)]
    if len(chunks[len(chunks)-1]) % 4 != 0:
        u = 4 - len(chunks[len(chunks)-1])
        for i in range(0,u):
            chunks[len(chunks)-1]+='0'

    print("DataBlocks: ")
    for i in chunks:
        if i == len(chunks)-1:
            break
        print("b"+str(l)+": "+ i + ", ", end=" ")
        l+=1
    return chunks

def parity_res(a,b,c):
    return (a^b)^c

def final_parity(a,b,c,d,e,f,g):
    return (((((a^b)^c)^d)^e)^f)^g

def HammingEncode_7_4(bitstring):
    chunks = []
    string = ""
    y = 0
    for i in range(0,len(bitstring)):
        chunks.append(string)
    for i in bitstring:
        print(i+":")
        print("Expand the block to 8 bits:___"+i[0]+"_"+i[1]+i[2]+i[3])
        p1 = str(parity_res(int(i[0]),int(i[1]),int(i[3])))
        p2 = str(parity_res(int(i[0]),int(i[2]),int(i[3])))
        p3 = str(parity_res(int(i[1]),int(i[2]),int(i[3]))) 
        p0 = str(final_parity(int(p1),int(p2),int(i[0]),int(p3),int(i[1]),int(i[2]),int(i[3])))
        print("p1: b3+b5+b7 = " + i[0]+"+"+i[1]+"+"+i[2]+" = " + p1 + ".")
        print("p2: b3+b5+b7 = " + i[0]+"+"+i[2]+"+"+i[3]+" = " + p2 + ".")
        print("p3: b3+b5+b7 = " + i[1]+"+"+i[2]+"+"+i[3]+" = " + p3 + ".")
        print("p0: b3+b5+b7 = " + i[0]+"+"+i[1]+"+"+i[2]+" = " + p0 + ".")
        chunks[y] = p0+p1+p2+i[0]+p3+i[1]+i[2]+i[3]
        print("Encoded bitstring: " + str(chunks[y])+".")
        y+=1
    
    return chunks

    

def print_Datablocks_15_11(bitstring):
    n = 11
    l = 1
    chunks = [bitstring[i:i+n] for i in range(0, len(bitstring), n)]
    if len(chunks[len(chunks)-1]) % 11 != 0:
        u = 11 - len(chunks[len(chunks)-1])
        for i in range(0,u):
            chunks[len(chunks)-1]+='0'

    print("DataBlocks: ")
    for i in chunks:
        if i == len(chunks)-1:
            break
        print("b"+str(l)+": "+ i + ", ", end=" ")
        l+=1
    return chunks

def parity_res_15_11(a,b,c,d,e,f,g):
    return (((((a^b)^c)^d)^e)^f)^g

def HammingEncode_15_11(bitstring):
    chunks = []
    string = ""
    y = 0
    for i in range(0,len(bitstring)):
        chunks.append(string)
    for i in bitstring:
        print(i+":")
        print("Expand the block to 16 bits:__"+i[0]+"_"+i[1]+i[2]+i[3]+"_"+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]+i[10])
        p1 = str(parity_res_15_11(int(i[0]),int(i[1]),int(i[3]),int(i[4]),int(i[6]),int(i[8]),int(i[10])))
        p2 = str(parity_res_15_11(int(i[0]),int(i[2]),int(i[3]),int(i[5]),int(i[6]),int(i[9]),int(i[10])))
        p4 = str(parity_res_15_11(int(i[1]),int(i[2]),int(i[3]),int(i[7]),int(i[8]),int(i[9]),int(i[10])))
        p8 = str(parity_res_15_11(int(i[4]),int(i[5]),int(i[6]),int(i[7]),int(i[8]),int(i[9]),int(i[10])))
        print("p1: b3+b5+b7+b9+b11+b13+b15 = " + i[0]+"+"+i[1]+"+"+i[3]+"+"+i[4]+"+"+i[6]+"+"+i[8]+"+"+i[10]+" = " + p1 + ".")
        print("p2: b3+b6+b7+b10+b11+b14+b15 = " + i[0]+"+"+i[2]+"+"+i[3]+"+"+i[5]+"+"+i[6]+"+"+i[9]+"+"+i[10]+" = " + p2 + ".")
        print("p4: b5+b6+b7+b12+b13+b14+b15 = " + i[1]+"+"+i[2]+"+"+i[3]+"+"+i[7]+"+"+i[8]+"+"+i[9]+"+"+i[10]+" = " + p4 + ".")
        print("p8: b9+b10+b11+b12+b13+b14+b15 = " + i[4]+"+"+i[5]+"+"+i[6]+"+"+i[7]+"+"+i[8]+"+"+i[9]+"+"+i[10]+" = " + p8 + ".")
        chunks[y] = p1+p2+i[0]+p4+i[1]+i[2]+i[3]+p8+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]+i[10]
        print("Encoded bitstring: " + str(chunks[y])+".")
        y+=1
    return chunks



def main():
    # Read the text
    text = open('Text.txt', 'r')

    contents = text.read()
    d = {}
    frequency = {}
    for i in range(0, 127):
        if contents.count(chr(i)) != 0:
            val = round(contents.count(chr(i)) / len(contents), 3)
            freq = contents.count(chr(i))
            d.update({chr(i): val})
            frequency.update({chr(i): freq})
    # 1
    for key, index in sorted(d.items(), key=lambda item: item[1], reverse=True):
        if key == '\n':
            d['newspace'] = d.pop('\n')
        if key == '\t':
            d['tab'] = d.pop('\t')
        if key == ' ':
            d['space'] = d.pop(' ')
    for key, index in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print(key + " - " + str(index))

    temp = Huffman_algo()
    temp.initialize(d)
    sab = temp.dict
    final = merge(sab, d)
    length_origin = 0
    text = ""
    for i in d:
        text += i
    for i in contents:
        length_origin += 16
    # 5
    print('Number of bits in the original text: ' + str(length_origin) + ' bytes')
    print('Number of bits in the compressed text: ' + str(len(temp.print_bytes(contents))) + ' bytes')
    print('Compression ratio = ' + str(round(length_origin / len(temp.print_bytes(contents)), 2)))
    print(average_code_length(frequency, sab))

    # 3
    node_list = []
    node_list_2 = []
    for key, index in sorted(final.items(), key=lambda item: item[1], reverse=True):
        print(key + " - " + str(index[0]) + " - " + index[1])
    for key, index in sorted(final.items(), key=lambda item: item[1], reverse=True):
        node_list.append(index[1])
        node_list_2.append(index[1])

    # 4
    new_file = open("sequence_of_binary_digits.txt", "w+")
    new_file.write(temp.print_bytes(contents))
    new_file.close()
    ls = len(Node_Value_1)
    # 2
    k = 1
    val = 1

    for i in reversed(range(ls)):
        if k >= ls:
            break
        print("Node " + str(val) + ": " + node_list[k - 1] + " - " + ', '.join(
            [str(elem) for elem in Node_letters_1]) + "- " + str(Node_Value_1[len(Node_Value_1) - k]))
        val += 1
        Node_letters_1.pop()
        print("Node " + str(val) + ": " + node_list[k] + " - " + ', '.join(
            [str(elem) for elem in Node_letters_2]) + "- " + str(Node_Value_2[len(Node_Value_2) - k]))
        Node_letters_2.pop()
        k += 2
        val += 1

    d_value = {}
    value, rev_m = temp.decode(temp.print_bytes(contents))
    print(rev_m)

    print("---------------------------------------------------------------------------------------------")
    print("Initial Text:\n" + str(contents))
    print("\n")
    print("Decoded Text:\n" + str(value))
    print("---------------------------------------------------------------------------------------------")

    print(20*"-"+"Assignemnt 6"+20*"-")

    value_sequence_encoded = open('sequence_of_binary_digits.txt','r').read()
    
    print("1.\n" + str(value_sequence_encoded))
    
    print("2/3/4. Hamming_7_4")
    data = print_Datablocks_4(value_sequence_encoded)
    chunks = HammingEncode_7_4(data)

    print("2/3/4. Hamming_15_11")
    data2 = print_Datablocks_15_11(value_sequence_encoded)
    chunks2 = HammingEncode_15_11(data2)

    print("5. Hamming_7_4")
    Hamming_7_4 = open("Hamming_7_4.txt", "w+")
    Hamming_7_4.write(''.join(chunks))
    Hamming_7_4.close()
    val1 = open('Hamming_7_4.txt','r').read()

    print("5. Hamming_15_11")
    Hamming_15_11 = open("Hamming_15_11.txt", "w+")
    Hamming_15_11.write(''.join(chunks2))
    Hamming_15_11.close()
    val2 = open('Hamming_15_11.txt','r').read()
    
if __name__ == '__main__':
    main()
