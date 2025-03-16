buttons = [
    ["⅟x", "(", ")", "AC", "CE"],
    ["±", "x!", "x²", "xⁿ", "%"],
    ["√x", "7", "8", "9", "÷"],
    ["π", "4", "5", "6", "×"],    
    ["Rand", "1", "2", "3", "－"],    
    ["000", "0", ".", "＝", "+"]
]

def find_button_position(value):
    for row_index, row in enumerate(buttons):
        if value in row:
            col_index = row.index(value)
            return row_index + 1, col_index + 1 

def push_button(page,Params):
    for Param in Params:
        row, col = find_button_position(Param)
        if row and col:
            css_selector = f"tr:nth-child({row}) > td:nth-child({col}) .char"
            button = page.locator(css_selector)
        button.click()