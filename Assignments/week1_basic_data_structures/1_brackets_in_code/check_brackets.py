# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    mismatch_pos = None
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            if len(opening_brackets_stack) < 2:
                mismatch_pos = Bracket(next, i + 1).position

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return Bracket(next, i + 1).position
            
            top = opening_brackets_stack.pop()
            
            if not are_matching(top, next):
                return Bracket(next, i + 1).position
            
    if len(opening_brackets_stack) == 0:
        return "Success"
    return mismatch_pos
        
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
