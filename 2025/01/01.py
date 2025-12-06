

def translate_instruction(instruction_string):
    if isinstance(instruction_string, str) \
        and len(instruction_string) > 1:
        orientation = instruction_string[0]
        clicks = instruction_string[1:].strip()
    return (orientation, clicks)

def read_data(filename):
    steps = []
    try:
        with open(filename) as f:
            for line in f:
                steps.append(line.strip())
    except IOError:
        print("file not found")
    return steps

def instr_remove(sp, st):
    return 100 + (sp - st)

def instr_add(sp, st):
    return abs((99 - sp + 1) - st)

def apply_instruction(starting_p, orientation, zero_count):
    if orientation == 'L':
        if steps <= starting_p:
            return ((starting_p - steps), 0)
        else:
            return (instr_remove(starting_p, steps), 1)
    elif orientation == 'R':
        if steps <= 99 - starting_p:
            return ((starting_p + steps), 0)
        else:
            return (instr_add(starting_p, steps), 1)


if __name__=="__main__":
    starting_point = 50
    number_of_zeros = 0
    steps = read_data("./input.txt")
    for instr in steps:
        (ori, st) = translate_instruction(instr)
        starting_point, new_number_of_zeros = apply_instruction(starting_point, ori, int(st))
        number_of_zeros += new_number_of_zeros
    print(number_of_zeros)

