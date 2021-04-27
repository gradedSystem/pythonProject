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
        i = 1
        k = 0
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                print("Step " + str(i) + ".")
                character = self.reverse_mapping[current_code]
                print(str(self.dict[character]) + " Node" + str(k) + ":(" + str(self.dict[character]) + ")",
                      character.split(","))
                if character == 'newspace':
                    character = "\n"
                elif character == 'space':
                    character = " "
                elif character == 'tab':
                    character = '\t'
                decoded_text += character
                current_code = ""
                i += 1
            k += 1


        return decoded_text

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

    for key, index in sorted(final.items(), key=lambda item: item[1], reverse=True):
        print(key + " - " + str(index[0]) + " - " + index[1])
    for key, index in sorted(final.items(), key=lambda item: item[1], reverse=True):
        node_list.append(index[1])

    d_up = {}

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
    value = temp.decode(temp.print_bytes(contents))
    print("---------------------------------------------------------------------------------------------")
    print("Initial Text:\n" + str(contents))
    print("\n")
    print("Decoded Text:\n" + str(value))
    print("---------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    main()
