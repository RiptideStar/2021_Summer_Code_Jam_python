from typing import Any, List, Optional

VERTICAL = "│"
HORIZONTAL = "─"
TOP_LEFT = "┌"
TOP_MIDDLE = "┬"
TOP_RIGHT = "┐"
LEFT_MIDDLE = "├"
MIDDLE = "┼"
RIGHT_MIDDLE = "┤"
BOTTOM_LEFT = "└"
BOTTOM_MIDDLE = "┴"
BOTTOM_RIGHT = "┘"

ALIGN_LEFT_SYMBOL = "<"
ALIGN_CENTER_SYMBOL = "^"


#if centered: character is ^, else: <
def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    align_symbol = ""
    if (centered):
        align_symbol += ALIGN_CENTER_SYMBOL
    else:
        align_symbol += ALIGN_LEFT_SYMBOL    
    # find longest label/element in a column of list, save that number (for all columns, same length of list.list.size) and use it to format the table: {:<10s}{:>4s}   (the number is the number + some lee-way margin)
    # some number + 2 lee way action
    longest_elements = []

    for j in range(len(rows[0])):
        max = len(str(rows[0][j]))
        for i in range(len(rows)):
            if (len(str(rows[i][j])) > max):
                max = len(str(rows[i][j]))
        if(len(labels[j]) > max):
            max = len(labels[j])        
        longest_elements.append(max)        

    str_table = ""
    str_table += TOP_LEFT

    num_columns = len(longest_elements)
    for j in range(num_columns):
        #top right case
        if (num_columns-j <= 1):
            for num in range(-2, longest_elements[j]):
                str_table += HORIZONTAL
            str_table += TOP_RIGHT
            
        #middle top case    
        else:
            for num in range(-2, longest_elements[j]):
                str_table += HORIZONTAL
            str_table += TOP_MIDDLE

    str_table += "\n"
    # print("***", str_table)

    if (labels):
        str_table += VERTICAL
        for j in range(num_columns):
            str_table += " {:{align_symbol}{lengthOfLongestElement}s} ".format(labels[j], 
                lengthOfLongestElement=longest_elements[j], align_symbol = align_symbol) + VERTICAL
        str_table += "\n"

        str_table += LEFT_MIDDLE
        for j in range(num_columns):
        #middle right case
            if (num_columns-j <= 1):
                for num in range(-2, longest_elements[j]):
                    str_table += HORIZONTAL
                str_table += RIGHT_MIDDLE
            
        #middle case    
            else:
                for num in range(-2, longest_elements[j]):
                    str_table += HORIZONTAL
                str_table += MIDDLE
        str_table += "\n"        

    for i in range(len(rows)):
        str_table += VERTICAL
        for j in range(num_columns):
            str_table += " {:{align_symbol}{lengthOfLongestElement}s} ".format(str(rows[i][j]), 
                lengthOfLongestElement=longest_elements[j], align_symbol = align_symbol) + VERTICAL
        str_table += "\n"    

    # print(str_table)

    str_table += BOTTOM_LEFT

    for j in range(num_columns):
        #bottom right case
        if (num_columns-j <= 1):
            for num in range(-2, longest_elements[j]):
                str_table += HORIZONTAL
            str_table += BOTTOM_RIGHT
            
        #middle bottom case    
        else:
            for num in range(-2, longest_elements[j]):
                str_table += HORIZONTAL
            str_table += BOTTOM_MIDDLE

    # print(str_table)    

    return str_table





#test code
# table = make_table(
#     rows=[
#         ["Lemon", 18_3285, "Owner"],
#         ["Sebastiaan", 18_3285.1, "Owner"],
#         ["KutieKatj", 15_000, "Admin"],
#         ["Jake", "MoreThanU", "Helper"],
#         ["Joe", -12, "Idk Tbh"]
#     ],
#     labels=["User", "Messages", "Role"]
# )
# print(table)    
