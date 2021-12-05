from parse import read_input_file, write_output_file
import os
import math
from solution import getSol
def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    n = len(tasks)
    en = []
    dl = []
    dur = []
    p = []
    for i in tasks:
        dl.append(i.get_deadline())
        dur.append(i.get_duration())
        p.append(i.get_max_benefit())
    prof, order = getSol(n, en, dl, dur, p)
    return order
if __name__ == '__main__':

    for input_path in os.listdir('inputs/small'):
        if input_path[-3:] != '.in':
            continue
        
        output_path = 'outputs/small/' + input_path[:-3] + '.out'
        
        if not os.path.exists(output_path):
            print('outputs/small/' + input_path[:-3] + '.out')
            tasks = read_input_file('inputs/small/' + input_path)
            output = solve(tasks)
            write_output_file(output_path, output)

    for input_path in os.listdir('inputs/medium'):
        if input_path[-3:] != '.in':
            continue
        
        output_path = 'outputs/medium/' + input_path[:-3] + '.out'
        
        if not os.path.exists(output_path):
            print('outputs/medium/' + input_path[:-3] + '.out')
            tasks = read_input_file('inputs/medium/' + input_path)
            output = solve(tasks)
            write_output_file(output_path, output)

    for input_path in os.listdir('inputs/large'):
        if input_path[-3:] != '.in':
            continue
        
        output_path = 'outputs/large/' + input_path[:-3] + '.out'
        
        if not os.path.exists(output_path):
            print('outputs/large/' + input_path[:-3] + '.out')
            tasks = read_input_file('inputs/large/' + input_path)
            output = solve(tasks)
            write_output_file(output_path, output)
