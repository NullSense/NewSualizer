from ete3 import Tree
import sys
import viz


# scan file and output as string
def scan_file(file):
    with open(file) as f:
        lines = f.readlines()

    lines_string = ''.join(lines)
    return lines_string


# Remove leading characters before '(' to correctly parse tree
def remove_leading(string):
    string = '(' + string.split('(', 1)[1]
    return string


def write_to_file(string, file):
    with open(file, 'w') as text_file:
        text_file.write(string)


def parse_file(file):
    # Returns tree
    file = file

    tree_string = scan_file(file)
    tree_string = remove_leading(tree_string)
 	
    # temporary workaround, cause Tree() thinks string is path
    write_to_file(tree_string, file)
    tree = Tree(file, format=1)
    return tree


def main():
    print(sys.argv)  # Prints all arguments passed in cmd
    # to run: python HDTrees.py Trees/filename.tre
    tree_output=parse_file(sys.argv[1])
    #print(tree_output)  # 2nd arg (file with dir)
    viz.main(tree_output)


main()