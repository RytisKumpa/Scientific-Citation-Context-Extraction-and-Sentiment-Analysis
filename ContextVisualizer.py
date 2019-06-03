from __future__ import print_function
from colors import color

def colorPrint(citation):
    tokens = citation.split(' ')
    for token in tokens:
        if "###NCONT" in token:
            print(color(token.replace("###NCONT", ""), 'red'), end=' ')
        elif "###CONT" in token:
            print(color(token.replace("###CONT", ""), 'green'), end=' ')
        elif "###CIT" in token:
            print(color(token.replace('###CIT', ''), 'blue'), end=' ')
        else:
            print(token.replace('###OTHER', ''), end=' ')
    print()



if __name__ == "__main__":
    with open('./Scientific_Citation_Context-Dataset.txt', 'r', encoding='utf-8') as file:
        for line in file:
            colorPrint(line)