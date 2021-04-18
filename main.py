import heapq
import zlib

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

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


class Huffman_algo:
    def __init__(self):
        self.heap = []
        self.dict = {}

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
            heapq.heappush(self.heap, m)

        item = heapq.heappop(self.heap)
        node = ""
        self.reverse(item, node)

    def reverse(self, item, node):
        if item is None:
            return

        if item.character is not None:
            self.dict[item.character] = node
            return
        self.reverse(item.left, node + "0")
        self.reverse(item.right, node + "1")

    def print_bytes(self, val):
        string = ""
        for i in val:
            string += self.dict[i]
        return string

    def dict(self):
        return self.dict


def main():
    
    def merge(d1, d2):
        d3 = {**d1,**d2}
        for key, index in d3.items():
            if key in d1 and key in d2:
                   d3[key] = [index, d1[key]]
        return d3
    
    # Read the text
    text = open('Text.txt', 'r')

    contents = text.read()
    d = {}
    for i in range(0, 127):
        if contents.count(chr(i)) != 0:
            val = round(contents.count(chr(i)) / len(contents), 3)
            d.update({chr(i): val})
    """for key, index in sorted(d.items(), key=lambda item: item[1], reverse=True):
        if key == '\n':
            d['newspace'] = d.pop('\n')
        if key == '\t':
            d['tab'] = d.pop('\t')
        if key == ' ':
            d['space'] = d.pop(' ')
        print(key + " - " + str(index))"""
    #print(d)
    text = ""
    for i in d:
        text += i
    temp = Huffman_algo()
    temp.initialize(d)
    print(temp.print_bytes(text))
    #print(temp.dict)
    
    sab = temp.dict
    final = merge(sab, d)
    
    for key, index in sorted(final.items(), key=lambda item: item[1], reverse=True):
        if key == '\n':
            final['newspace'] = final.pop('\n')
        if key == '\t':
            final['tab'] = final.pop('\t')
        if key == ' ':
            final['space'] = final.pop(' ')
        print(key + " - " + str(index))
       
    print('Number of bits in the original text: '+str(len(contents.encode('utf-8')))+' bytes')
    print('Number of bits in the compressed text: '+str(len(temp.print_bytes(text)))+' bytes')             
    print('Compression ratio = '+str(len(contents.encode('utf-8'))/len(temp.print_bytes(text)))+' bytes')


if __name__ == '__main__':
    main()
