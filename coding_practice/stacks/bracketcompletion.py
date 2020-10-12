def cluster(txt):
    parenthesis_stack = []

    output_list = []
    string_builder = ''
    for chr in txt:
        if chr == '(':
            parenthesis_stack.append(chr)
        elif chr == ')':
            parenthesis_stack.pop()

        string_builder += chr

        if len(parenthesis_stack) == 0:
            output_list.append(string_builder)
            string_builder = ''

    return output_list


def check_brackets(str):
    bracket_stack = []

    allowed_left_brackets = ['(', '[', '{']
    allowed_right_brackets = [')', ']', '}']

    for char in str:
        if char in allowed_left_brackets:
            bracket_stack.append(char)
        elif char in allowed_right_brackets:
            if not bracket_stack:
                return False
            popped_char = bracket_stack.pop()
            if allowed_right_brackets.index(char) != allowed_left_brackets.index(popped_char):
                return False

    return True


if __name__ == '__main__':
    str = '[({a})]]'
    ret = check_brackets(str)
    print(ret)
    str = '([a(b{a})])'
    ret = check_brackets(str)
    print(ret)
