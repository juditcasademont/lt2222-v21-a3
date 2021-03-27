import sys
import argparse
import numpy as np
import pandas as pd
from model import train
from model import VowelModel
import torch
from train import a, vowels
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import random

def new_vowels(ground_truth, predicted):
    
    new = []
    s_e_tokens = ['<s>', '<e>']
    for character in ground_truth:
        if character in vowels:
            new.append(predicted.pop(0))
        elif character in s_e_tokens:
            pass
        else:
            new.append(character)

    return new

def g_v2(x, p):

    z = np.zeros(len(p))

    #To avoid weird characters messing up with the data
    if x in p:
        z[p.index(x)] = 1

    return z

def b_v2(u, p):

    gt = []
    gr = []
    for v in range(len(u) - 4):
        if u[v+2] not in vowels:
            continue
        
        h2 = vowels.index(u[v+2])
        gt.append(h2)
        r = np.concatenate([g_v2(x, p) for x in [u[v], u[v+1], u[v+3], u[v+4]]])
        gr.append(r)

    return np.array(gr), np.array(gt) 

def accuracy(ground_truth, predicted):

    correct = 0
    total = len(ground_truth)
    for ground, pred in zip(ground_truth, predicted):
        if ground == pred:
            correct += 1
    
    print('Accuracy: %d %%' % (100 * correct / total))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path", type=str, help="The model")
    parser.add_argument("test_path", type=str, help="The path to the test file")
    parser.add_argument("output_file", type=str, help="The name of the output file")
    args = parser.parse_args()

    #Loading the model
    model = torch.load(args.model_path)
    model.eval()
    
    #Loading the test data
    tokenized_data = a(args.test_path)
            
    test_matrix, expected = b_v2(tokenized_data[0], model.vocab)
    
    #Creating evaluation instances compatible with training instances
    with torch.no_grad():
        outputs = model(torch.Tensor(test_matrix))
        _, predicted = torch.max(outputs.data, 1)

    #Using the model to predict instances
    predicted_vowles = []
    for vowel_index in predicted:
        predicted_vowles.append(vowels[vowel_index])
    
    #Writing predicted vowels into output file
    output_text = new_vowels(tokenized_data[0], predicted_vowles)
    with open(args.output_file, 'w') as f:
        f.write(''.join(output_text))
    
    #Printing accuracy of model to terminal  
    accuracy(expected, predicted)
