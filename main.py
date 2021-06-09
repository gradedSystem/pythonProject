import pandas as pd
import dash
import flask
import jgraph
import heapq
import random
import math
import operator
from heapq import heappop, heappush
from igraph import Graph, EdgeSeq
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import chart_studio.plotly as py
import plotly.figure_factory as ff
import numpy as np

np.random.seed(1)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
nr_vertices = 0

############# Main Code #################

halves = 0
halves_1 = 0
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

        return decoded_text, self.reverse_mapping, len(self.reverse_mapping)

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


ns = open("sequence_of_binary_digits.txt").read()


def print_Datablocks_4(bitstring):
    n = 4
    l = 1
    chunks = [bitstring[i:i + n] for i in range(0, len(bitstring), n)]
    if len(chunks[len(chunks) - 1]) % 4 != 0:
        u = 4 - len(chunks[len(chunks) - 1])
        for i in range(0, u):
            chunks[len(chunks) - 1] += '0'

    print("DataBlocks: ")
    for i in chunks:
        if i == len(chunks) - 1:
            break
        print("b" + str(l) + ": " + i + ", ", end=" ")
        l += 1
    return chunks


def parity_res(a, b, c):
    return (a ^ b) ^ c


def final_parity(a, b, c, d, e, f, g):
    return (((((a ^ b) ^ c) ^ d) ^ e) ^ f) ^ g


def HammingEncode_7_4(bitstring):
    chunks = []
    string = ""
    y = 0
    print(bitstring)
    for i in range(0, len(bitstring)):
        chunks.append(string)
    for i in bitstring:
        p1 = str(parity_res(int(i[0]), int(i[1]), int(i[3])))
        p2 = str(parity_res(int(i[0]), int(i[2]), int(i[3])))
        p3 = str(parity_res(int(i[1]), int(i[2]), int(i[3])))
        p0 = str(final_parity(int(p1), int(p2), int(i[0]), int(p3), int(i[1]), int(i[2]), int(i[3])))
        chunks[y] = p0 + p1 + p2 + i[0] + p3 + i[1] + i[2] + i[3]
        y += 1

    return chunks


def print_Datablocks_15_11(bitstring):
    n = 11
    l = 1
    chunks = [bitstring[i:i + n] for i in range(0, len(bitstring), n)]
    if len(chunks[len(chunks) - 1]) % 11 != 0:
        u = 11 - len(chunks[len(chunks) - 1])
        for i in range(0, u):
            chunks[len(chunks) - 1] += '0'

    print("DataBlocks: ")
    for i in chunks:
        if i == len(chunks) - 1:
            break
        print("b" + str(l) + ": " + i + ", ", end=" ")
        l += 1
    return chunks


def parity_string(bitstring):
    bitstring = ns
    return ns


def parity_res_15_11(a, b, c, d, e, f, g):
    return (((((a ^ b) ^ c) ^ d) ^ e) ^ f) ^ g


def parity_res_15_11_2(i):
    ini = int(i[0])
    for j in range(1, len(i)):
        ini = ini ^ int(i[j])
    return ini


def HammingEncode_15_11(bitstring):
    chunks = []
    string = ""
    y = 0
    for i in range(0, len(bitstring)):
        chunks.append(string)
    for i in bitstring:
        print(i + ":")
        print("Expand the block to 16 bits:__" + i[0] + "_" + i[1] + i[2] + i[3] + "_" + i[4] + i[5] + i[6] + i[7] + i[
            8] + i[9] + i[10] + "_")
        p1 = str(parity_res_15_11(int(i[0]), int(i[1]), int(i[3]), int(i[4]), int(i[6]), int(i[8]), int(i[10])))
        p2 = str(parity_res_15_11(int(i[0]), int(i[2]), int(i[3]), int(i[5]), int(i[6]), int(i[9]), int(i[10])))
        p4 = str(parity_res_15_11(int(i[1]), int(i[2]), int(i[3]), int(i[7]), int(i[8]), int(i[9]), int(i[10])))
        p8 = str(parity_res_15_11(int(i[4]), int(i[5]), int(i[6]), int(i[7]), int(i[8]), int(i[9]), int(i[10])))
        p16 = str(parity_res_15_11_2(i))
        print("p1: b3+b5+b7+b9+b11+b13+b15 = " + i[0] + "+" + i[1] + "+" + i[3] + "+" + i[4] + "+" + i[6] + "+" + i[
            8] + "+" + i[10] + " = " + p1 + ".")
        print("p2: b3+b6+b7+b10+b11+b14+b15 = " + i[0] + "+" + i[2] + "+" + i[3] + "+" + i[5] + "+" + i[6] + "+" + i[
            9] + "+" + i[10] + " = " + p2 + ".")
        print("p4: b5+b6+b7+b12+b13+b14+b15 = " + i[1] + "+" + i[2] + "+" + i[3] + "+" + i[7] + "+" + i[8] + "+" + i[
            9] + "+" + i[10] + " = " + p4 + ".")
        print("p8: b9+b10+b11+b12+b13+b14+b15 = " + i[4] + "+" + i[5] + "+" + i[6] + "+" + i[7] + "+" + i[8] + "+" + i[
            9] + "+" + i[10] + " = " + p8 + ".")
        print(
            "p16: p1+p2+b3+p4+b5+b6+b7+p8+b9+b10+b11+b12+b13+b14+b15 = " + p1 + "+" + p2 + "+" + i[0] + "+" + p4 + "+" +
            i[1] + "+" + i[2] + "+" + i[3] + "+" + p8 + "+" + i[4] + "+" + i[5] + "+" + i[6] + "+" + i[7] + "+" + i[
                8] + "+" + i[9] + "+" + i[10] + " = " + p16 + ".")
        chunks[y] = p1 + p2 + i[0] + p4 + i[1] + i[2] + i[3] + p8 + i[4] + i[5] + i[6] + i[7] + i[8] + i[9] + i[
            10] + p16
        print("Encoded bitstring: " + str(chunks[y]) + ".")
        y += 1
    return chunks


def ErrorGen(chunks, rand):
    length = len(chunks)
    blocks_with_error = []
    random_indexes = []
    indexes = list(range(1, length))
    while True:
        val = random.choice(indexes)
        if len(random_indexes) == rand:
            break
        if val not in random_indexes:
            random_indexes.append(val)

    for i in range(0, length):
        if i in random_indexes:
            val = random.choice(indexes)
            temp = list(chunks[i])
            if temp[val] == '0':
                temp[val] = '1'
            else:
                temp[val] = '0'
            blocks_with_error.append(''.join(temp))
            random_indexes.pop()
        else:
            blocks_with_error.append(chunks[i])
    return blocks_with_error


def check_parity(bitstring):
    bitstring = " ".join(bitstring)
    a_list = bitstring.split()
    map_object = map(int, a_list)
    list_of_integers = list(map_object)
    b_p1 = False
    b_p2 = False
    b_p3 = False
    b_p0 = False
    p1 = list_of_integers[1]
    p2 = list_of_integers[2]
    p3 = list_of_integers[4]
    p0 = list_of_integers[0]
    if p1 != list_of_integers[3] ^ list_of_integers[5] ^ list_of_integers[7]:
        b_p1 = True
    if p2 != list_of_integers[3] ^ list_of_integers[6] ^ list_of_integers[7]:
        b_p2 = True
    if p3 != list_of_integers[5] ^ list_of_integers[6] ^ list_of_integers[7]:
        b_p3 = True
    if final_parity(p1, p2, list_of_integers[3], p3, list_of_integers[5], list_of_integers[6], list_of_integers[7]) == \
            list_of_integers[0]:
        b_p0 = True
    return b_p1, b_p2, b_p3, p1, p2, p3, b_p0, p0


def HammingDecode_7_4(corrupted_bitstring):
    decoded_7_4 = ""
    for i in corrupted_bitstring:
        corrupted_bitstring = " ".join(i)
        a_list = corrupted_bitstring.split()
        map_object = map(int, a_list)
        list_of_integers = list(map_object)
        b_p1, b_p2, b_p3, p1, p2, p3, b_p0, p0 = check_parity(i)
        if b_p1 == False and b_p2 == False and b_p3 == True and b_p0 == True:
            if list_of_integers[3] == 0:
                list_of_integers[3] = 1
            else:
                list_of_integers[3] = 0
        elif b_p2 == False and b_p3 == False and b_p1 == True and b_p0 == True:
            if list_of_integers[6] == 0:
                list_of_integers[6] = 1
            else:
                list_of_integers[6] = 0
        elif b_p1 == False and b_p3 == False and b_p2 == True and b_p0 == True:
            if list_of_integers[5] == 1:
                list_of_integers[5] = 0
            else:
                list_of_integers[5] = 1
        elif b_p1 == False and b_p2 == False and b_p3 == False and b_p0 == True:
            if list_of_integers[7] == 1:
                list_of_integers[7] = 0
            else:
                list_of_integers[7] = 1
        if b_p1 == True and b_p2 == False and b_p3 == True and b_p0 == True:
            if list_of_integers[2] == 1:
                list_of_integers[2] = 0
            else:
                list_of_integers[2] = 1
        if b_p2 == True and b_p1 == False and b_p3 == True and b_p0 == True:
            if list_of_integers[1] == 1:
                list_of_integers[1] = 0
            else:
                list_of_integers[1] = 1
        if b_p2 == True and b_p3 == False and b_p1 == True and b_p0 == True:
            if list_of_integers[4] == 1:
                list_of_integers[4] = 0
            else:
                list_of_integers[4] = 1
        if b_p1 == False and b_p2 == False and b_p3 == False and b_p0 == True:
            if list_of_integers[0] == 1:
                list_of_integers[0] = 0
            else:
                list_of_integers[0] = 1
        if b_p2 == True and b_p3 == True and b_p1 == False and b_p0 == True:
            if list_of_integers[6] == 1:
                list_of_integers[6] = 0
            else:
                list_of_integers[6] = 1
        list_of_integers = [str(i) for i in list_of_integers]
        ind = 0
        print("Checking parity bits:")
        if b_p1 == True:
            print("p1: b3+b5+b7 = " + str(list_of_integers[3]) + "+" + str(list_of_integers[5]) + "+" + str(
                list_of_integers[7]) + " = " + str(p1) + " incorrect.")
            ind += 1
        else:
            print("p1: b3+b5+b7 = " + str(list_of_integers[3]) + "+" + str(list_of_integers[5]) + "+" + str(
                list_of_integers[7]) + " = " + str(p1) + " correct.")
        if b_p2 == True:
            print("p2: b3+b6+b7 = " + str(list_of_integers[3]) + "+" + str(list_of_integers[6]) + "+" + str(
                list_of_integers[7]) + " = " + str(p2) + " incorrect.")
            ind += 2
        else:
            print("p2: b3+b6+b7 = " + str(list_of_integers[3]) + "+" + str(list_of_integers[6]) + "+" + str(
                list_of_integers[7]) + " = " + str(p2) + " correct.")
        if b_p3 == True:
            print("p3: b5+b6+b7 = " + str(list_of_integers[5]) + "+" + str(list_of_integers[6]) + "+" + str(
                list_of_integers[7]) + " = " + str(p3) + " incorrect.")
            ind += 4
        else:
            print("p3: b5+b6+b7 = " + str(list_of_integers[5]) + "+" + str(list_of_integers[6]) + "+" + str(
                list_of_integers[7]) + " = " + str(p3) + " correct.")
        if b_p1 == False and b_p2 == False and b_p3 == False:
            print("p0: b1+b2+b3+b4+b5+b6+b7 = " + str(list_of_integers[1]) + "+" + str(list_of_integers[2]) + "+" + str(
                list_of_integers[3]) + "+" + str(list_of_integers[4]) + "+" + str(list_of_integers[5]) + "+" + str(
                list_of_integers[6]) + "+" + str(list_of_integers[7]) + " = " + str(p0) + " correct.")
            print("No Error")
            print("Decoded bitstring: " + str(list_of_integers[3]) + " " + str(list_of_integers[5]) + " " + str(
                list_of_integers[6]) + " " + str(list_of_integers[7]) + ".")
            decoded_7_4 += str(list_of_integers[3]) + str(list_of_integers[5]) + str(list_of_integers[6]) + str(
                list_of_integers[7])
        else:
            print("p0: b1+b2+b3+b4+b5+b6+b7 = " + str(list_of_integers[1]) + "+" + str(list_of_integers[2]) + "+" + str(
                list_of_integers[3]) + "+" + str(list_of_integers[4]) + "+" + str(list_of_integers[5]) + "+" + str(
                list_of_integers[6]) + "+" + str(list_of_integers[7]) + " = " + str(p0) + " incorrect.")
            print("Error in position: " + str(ind))
            print("Corrected bitstring: ", end="")
            print(*list_of_integers, end="")
            print(".")
            print("Decoded bitstring: " + str(list_of_integers[3]) + " " + str(list_of_integers[5]) + " " + str(
                list_of_integers[6]) + " " + str(list_of_integers[7]) + ".")
            decoded_7_4 += str(list_of_integers[3]) + str(list_of_integers[5]) + str(list_of_integers[6]) + str(
                list_of_integers[7])
    return decoded_7_4


def check_parity_15_11(bitstring):
    bitstring = " ".join(bitstring)
    a_list = bitstring.split()
    map_object = map(int, a_list)
    k = list(map_object)
    b_p1 = False
    b_p2 = False
    b_p4 = False
    b_p8 = False
    b_p16 = False
    p1 = k[0]
    p2 = k[1]
    p4 = k[3]
    p8 = k[7]
    p16 = k[15]
    if p1 != k[2] ^ k[4] ^ k[6] ^ k[8] ^ k[10] ^ k[12] ^ k[14]:
        b_p1 = True
    if p2 != k[2] ^ k[5] ^ k[6] ^ k[9] ^ k[10] ^ k[13] ^ k[14]:
        b_p2 = True
    if p4 != k[5] ^ k[6] ^ k[7] ^ k[11] ^ k[12] ^ k[13] ^ k[14]:
        b_p4 = True
    if p8 != k[8] ^ k[9] ^ k[10] ^ k[11] ^ k[12] ^ k[13] ^ k[14]:
        b_p8 = True
    if p16 != p1 ^ p2 ^ k[2] ^ p4 ^ k[4] ^ k[5] ^ k[6] ^ p8 ^ k[8] ^ k[9] ^ k[10] ^ k[11] ^ k[12] ^ k[13] ^ k[14]:
        b_p16 = True
    return b_p1, b_p2, b_p4, b_p8, b_p16, p1, p2, p4, p8, p16


def joint_entropy(vals, val):
    temp = 0
    for i in vals:
        temp += -i * math.log(2, i)
    temp = val[0] + val[1]
    return temp - 0.01


def HammingDecode_15_11(corrupted_bitstring):
    decoded_15_11 = ""
    for i in corrupted_bitstring:
        corrupted_bitstring = " ".join(i)
        a_list = corrupted_bitstring.split()
        map_object = map(int, a_list)
        list_of_integers = list(map_object)
        b_p1, b_p2, b_p4, b_p8, b_p16, p1, p2, p4, p8, p16 = check_parity_15_11(i)
        ind = 0
        if b_p1 == True:
            print(
                "p1: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[2]) + "+" + str(list_of_integers[4]) + "+" + str(
                    list_of_integers[6]) + "+" + str(list_of_integers[8]) + "+" + str(list_of_integers[10]) + "+" + str(
                    list_of_integers[12]) + "+" + str(list_of_integers[14]) + " = " + str(p1) + " incorrect.")
            ind += 1
        else:
            print(
                "p1: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[2]) + "+" + str(list_of_integers[4]) + "+" + str(
                    list_of_integers[6]) + "+" + str(list_of_integers[8]) + "+" + str(list_of_integers[10]) + "+" + str(
                    list_of_integers[12]) + "+" + str(list_of_integers[14]) + " = " + str(p1) + " correct.")
        if b_p2 == True:
            ind += 2
            print(
                "p2: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[2]) + "+" + str(list_of_integers[5]) + "+" + str(
                    list_of_integers[6]) + "+" + str(list_of_integers[9]) + "+" + str(list_of_integers[10]) + "+" + str(
                    list_of_integers[13]) + "+" + str(list_of_integers[14]) + " = " + str(p1) + " incorrect.")
        else:
            print(
                "p2: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[2]) + "+" + str(list_of_integers[5]) + "+" + str(
                    list_of_integers[6]) + "+" + str(list_of_integers[9]) + "+" + str(list_of_integers[10]) + "+" + str(
                    list_of_integers[13]) + "+" + str(list_of_integers[14]) + " = " + str(p1) + " correct.")
        if b_p4 == True:
            ind += 4
            print(
                "p4: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[5]) + "+" + str(list_of_integers[6]) + "+" + str(
                    list_of_integers[7]) + "+" + str(list_of_integers[11]) + "+" + str(
                    list_of_integers[12]) + "+" + str(list_of_integers[13]) + "+" + str(
                    list_of_integers[14]) + " = " + str(p1) + " incorrect.")
        else:
            print(
                "p4: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[5]) + "+" + str(list_of_integers[6]) + "+" + str(
                    list_of_integers[7]) + "+" + str(list_of_integers[11]) + "+" + str(
                    list_of_integers[12]) + "+" + str(list_of_integers[13]) + "+" + str(
                    list_of_integers[14]) + " = " + str(p1) + " correct.")
        if b_p8 == True:
            ind += 8
            print("p8: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[8]) + "+" + str(
                list_of_integers[9] + "+" + str(list_of_integers[10]) + "+" + str(list_of_integers[11]) + "+" + str(
                    list_of_integers[12]) + "+" + str(list_of_integers[13]) + "+" + str(
                    list_of_integers[14]) + " = " + str(p1) + " incorrect."))
        else:
            print(
                "p8: d1+d2+d4+d5+d7+d9+d11 = " + str(list_of_integers[8]) + "+" + str(list_of_integers[9]) + "+" + str(
                    list_of_integers[10]) + "+" + str(list_of_integers[11]) + "+" + str(
                    list_of_integers[12]) + "+" + str(list_of_integers[13]) + "+" + str(
                    list_of_integers[14]) + " = " + str(p1) + " correct.")
        if b_p1 == False and b_p2 == False and b_p4 == False and b_p8 == False and b_p16 == False:
            print("p16: p1+p2+b3+p4+b5+b6+b7+p8+b9+b10+b11+b12+b13+b14+b15 = " + str(p1) + "+" + str(p2) + "+" + str(
                list_of_integers[2]) + "+" + str(p4) + "+" + str(list_of_integers[4]) + "+" + str(
                list_of_integers[5]) + "+" + str(list_of_integers[6]) + "+" + str(p8) + "+" + str(
                list_of_integers[8]) + "+" + str(list_of_integers[9]) + "+" + str(list_of_integers[10]) + "+" + str(
                list_of_integers[11]) + "+" + str(list_of_integers[12]) + "+" + str(list_of_integers[13]) + "+" + str(
                list_of_integers[14]) + " = " + str(p16) + " correct.")
            print("No Error")
            print("Decoded string: " + str(list_of_integers[2]) + " " + str(list_of_integers[4]) + " " + str(
                list_of_integers[5]) + " " + str(list_of_integers[6]) + " " + str(list_of_integers[8]) + " " + str(
                list_of_integers[9]) + " " + str(list_of_integers[9]) + " " + str(list_of_integers[11]) + " " + str(
                list_of_integers[12]) + " " + str(list_of_integers[13]) + " " + str(list_of_integers[14]) + ".")
            decoded_15_11 += str(list_of_integers[2]) + str(list_of_integers[4]) + str(list_of_integers[5]) + str(
                list_of_integers[6]) + str(list_of_integers[8]) + str(list_of_integers[9]) + str(
                list_of_integers[11]) + str(list_of_integers[12]) + str(list_of_integers[13]) + str(
                list_of_integers[14])
        else:
            print("p16: p1+p2+b3+p4+b5+b6+b7+p8+b9+b10+b11+b12+b13+b14+b15 = " + str(p1) + "+" + str(p2) + "+" + str(
                list_of_integers[2]) + "+" + str(p4) + "+" + str(list_of_integers[4]) + "+" + str(
                list_of_integers[5]) + "+" + str(list_of_integers[6]) + "+" + str(p8) + "+" + str(
                list_of_integers[8]) + "+" + str(list_of_integers[9]) + "+" + str(list_of_integers[10]) + "+" + str(
                list_of_integers[11]) + "+" + str(list_of_integers[12]) + "+" + str(list_of_integers[13]) + "+" + str(
                list_of_integers[14]) + " = " + str(p16) + " correct.")
            print("Error in position: " + str(ind))
            print("Corrected bitstring: ", end="")
            print(*list_of_integers, end=".\n")
            print("Decoded string: " + str(list_of_integers[2]) + " " + str(list_of_integers[4]) + " " + str(
                list_of_integers[5]) + " " + str(list_of_integers[6]) + " " + str(list_of_integers[8]) + " " + str(
                list_of_integers[9]) + " " + str(list_of_integers[10]) + " " + str(list_of_integers[11]) + " " + str(
                list_of_integers[12]) + " " + str(list_of_integers[13]) + " " + str(list_of_integers[14]) + ".")
            decoded_15_11 += str(list_of_integers[2]) + str(list_of_integers[4]) + str(list_of_integers[5]) + str(
                list_of_integers[6]) + str(list_of_integers[8]) + str(list_of_integers[9]) + str(
                list_of_integers[11]) + str(list_of_integers[12]) + str(list_of_integers[13]) + str(
                list_of_integers[14])
    return decoded_15_11


def entropies(vals):
    temp = 0
    for i in vals:
        temp += -i * math.log(2, i)
    return temp


def main(string_of_binary="", decode=False, entropy=False):
    # Read the text
    text = open('Text.txt', 'r')

    contents = text.read()
    if len(string_of_binary) > 1:
        print('Hello world')
        print(string_of_binary)
        return HammingEncode_7_4(string_of_binary)
    d = {}
    frequency = {}
    length_of_response = len(contents)
    value_n = int(length_of_response / 2)
    for i in range(0, 127):
        if contents.count(chr(i)) != 0:
            val = round(contents.count(chr(i)) / len(contents), 3)
            freq = contents.count(chr(i))
            d.update({chr(i): val})
            frequency.update({chr(i): freq})

    if (decode):
        return contents

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
    probs = []
    for key, index in sorted(d.items(), key=lambda item: item[1], reverse=True):
        probs.append(index)

    halves = round(entropies(probs), 2)
    if (entropy):
        return str(round(length_origin / len(temp.print_bytes(contents)), 2)), average_code_length(frequency,
                                                                                                   sab), halves

    # 3
    node_list = []
    node_list_2 = []
    v_labels = []
    for key, index in sorted(final.items(), key=lambda item: item[1], reverse=True):
        v_labels.append(key)

    # 4
    new_file = open("sequence_of_binary_digits.txt", "w+")
    new_file.write(temp.print_bytes(contents))
    new_file.close()

    value, rev_m, len_ver = temp.decode(temp.print_bytes(contents))
    val = open('sequence_of_binary_digits.txt', 'r').read()
    return len_ver, val, v_labels


##################################


if __name__ == '__main__':
    algos = ['Huffman Algorithm', 'Shannon-Fano Algorithm']


    def get_options(list_of_items):
        dict_list = []
        for i in list_of_items:
            dict_list.append({'label': i, 'value': i})

        return dict_list


    title_font = dict(
        size=26,
        color='#D8D8D8'
    )
    general_font = dict(
        size=14,
        color='#D8D8D8'
    )

    app.layout = html.Div(children=[
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(children=[
                         html.H2('Choose Your Algorithm'),
                         html.P('''Visualize Your work with Plotly'''),
                         html.P('''Pick one of algorithms.''')
                     ], className='four columns div-user-controls'),
                     html.Div(children=[
                         dcc.RadioItems(id='select_graph',
                                        labelStyle={'display': 'inline-block'},
                                        value='',
                                        options=[{'label': i, 'value': i} for i in algos],
                                        style={'text-align': 'center'}
                                        ),
                         dcc.Graph(id='graphalgo', config={'displayModeBar': False}),
                         html.Div(id='basic', style={'margin-left': '50px'}),
                         html.Div(id='created_errors', style={'margin-left': '50px'}),
                         html.Div(id='decoded', style={'margin-left': '50px'}),
                         html.Div(id='text', style={'margin-left': '50px'}),
                         html.Div(id='entropy', style={'margin-left': '50px'})
                     ], className='eight columns div-for-charts bg-grey')
                 ])
    ])


    @app.callback([Output('graphalgo', 'figure'), Output('basic', 'children')],
                  Input('select_graph', 'value'))
    def Update_graph(select_graph):

        if select_graph == 'Shannon-Fano Algorithm':
            nr_vertices, value, v_labels = main()
            labels = v_labels

            def get_seq():
                text = open('Text.txt', 'r')

                contents = text.read()
                return contents

            dict_shannon = {}
            message = get_seq()
            code = 0
            count = {}
            code_mes = ""
            for c in message:
                if c not in count:
                    count[c] = 1
                else:
                    count[c] += 1

            def Entropy_value(frequency, length):
                entropy = 0
                for i in frequency:
                    entropy -= (frequency[i] / length * math.log2(frequency[i] / length))
                return entropy

            def Shannon_Fano(seq, temp):
                f = {}
                k = {}
                if len(seq) == 1:
                    dict_shannon[seq.popitem()[0]] = temp
                    return 0
                for i in sorted(seq.items(), key=operator.itemgetter(1), reverse=True):
                    if sum(f.values()) < sum(k.values()):
                        f[i[0]] = seq[i[0]]
                    else:
                        k[i[0]] = seq[i[0]]
                Shannon_Fano(f, temp + '0')
                Shannon_Fano(k, temp + '1')

            Shannon_Fano(count, "")
            for i in message:
                code_mes += dict_shannon[i]
            value = code_mes

            G = Graph.Tree(nr_vertices, 3)
            lay = G.layout('kk')
            position = {k: lay[k] for k in range(nr_vertices)}
            Y = [lay[k][1] for k in range(nr_vertices)]
            M = max(Y)

            es = EdgeSeq(G)  # sequence of edges
            E = [e.tuple for e in G.es]  # list of edges

            L = len(position)
            Xn = [position[k][0] for k in range(L)]
            Yn = [2 * M - position[k][1] for k in range(L)]
            Xe = []
            Ye = []
            for edge in E:
                Xe += [position[edge[0]][0], position[edge[1]][0], None]
                Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]
            layout = go.Layout(
                title={
                    'text': "Shannon-Fano Algorithm",
                    'y': 0.9,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': title_font
                },
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=general_font
            )
            fig = go.Figure(layout=layout)
            fig.add_trace(go.Scatter(x=Xe,
                                     y=Ye,
                                     mode='lines',
                                     line=dict(color='#f28b1d', width=2),
                                     hoverinfo='none'
                                     ))
            fig.add_trace(go.Scatter(x=Xn,
                                     y=Yn,
                                     mode='markers',
                                     name='bla',
                                     marker=dict(symbol='circle-dot',
                                                 size=22,
                                                 color='#e61c1c',
                                                 line=dict(color='#f28b1d', width=2)
                                                 ),
                                     text=labels,
                                     hoverinfo='text',
                                     opacity=1
                                     ))
            return fig, 'Shannon-Fano encoding: {}'.format(value)
        else:
            nr_vertices, value, v_labels = main()
            labels = v_labels
            G = Graph.Tree(nr_vertices, 2)
            lay = G.layout('rt')
            position = {k: lay[k] for k in range(nr_vertices)}
            Y = [lay[k][1] for k in range(nr_vertices)]
            M = max(Y)

            es = EdgeSeq(G)  # sequence of edges
            E = [e.tuple for e in G.es]  # list of edges

            L = len(position)
            Xn = [position[k][0] for k in range(L)]
            Yn = [2 * M - position[k][1] for k in range(L)]
            Xe = []
            Ye = []
            for edge in E:
                Xe += [position[edge[0]][0], position[edge[1]][0], None]
                Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]
            layout = go.Layout(
                title={
                    'text': "Huffman Algorithm",
                    'y': 0.9,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': title_font
                },
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=general_font
            )
            fig = go.Figure(layout=layout)
            fig.add_trace(go.Scatter(x=Xe,
                                     y=Ye,
                                     mode='lines',
                                     line=dict(color='#f28b1d', width=2),
                                     hoverinfo='none'
                                     ))
            fig.add_trace(go.Scatter(x=Xn,
                                     y=Yn,
                                     mode='markers',
                                     name='bla',
                                     marker=dict(symbol='circle-dot',
                                                 size=22,
                                                 color='#e61c1c',
                                                 line=dict(color='#f28b1d', width=2)
                                                 ),
                                     text=labels,
                                     hoverinfo='text',
                                     opacity=1
                                     ))
            return fig, 'Huffman encoding: {}'.format(value)


    @app.callback(Output('created_errors', 'children'),
                  Input('basic', 'children'))
    def probable(basic):
        res = [int(i) for i in basic.split() if i.isdigit()]
        value = main(res)
        return 'Output: {}'.format(value[1])


    @app.callback(Output('decoded', 'children'),
                  Input('basic', 'children'))
    def decodeds(basic):
        res = [int(i) for i in basic.split() if i.isdigit()]
        return 'Decoded back string: {}'.format(res[0])


    @app.callback(Output('text', 'children'),
                  Input('basic', 'children'))
    def decoded(basic):
        decode = main(decode=True)
        return 'Decoded back text: {}'.format(decode)


    @app.callback(Output('entropy', 'children'),
                  Input('basic', 'children'))
    def entropy(basic):
        ratio, code_len, entr = main(entropy=True)
        return 'Entropy ratio: {}\n'.format(ratio), '{}\n'.format(code_len), 'Entropy: {}\n'.format(entr)


    app.run_server(debug=True)
