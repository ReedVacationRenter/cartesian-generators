import sys
import re
import itertools
from itertools import izip_longest
import time

input_template_file = sys.argv[1]
input_keyword_file = sys.argv[2]
start_time = time.time() # Variable used to track amount of time it takes to create a cartesian product

def cartesian_product_generator(templates,keyword): # Primary function used to generate cartesian product
    for elem in itertools.product(keyword):
        for template in template_list:
            yield template.replace('{keyword}',elem[0])

def dedupe_list(input_list): # Function removes any duplicate values from master list
    set = {}
    map(set.__setitem__, input_list, [])
    yield set.keys()

def write_file(input_generator,filename): # Function writes cartesian product export file
    with open('1keyword_templates_{0}.txt'.format(filename),'w') as export_file:
        for elem in input_generator:
            for line in elem:
                export_file.write(str(line) + '\n')

with open(input_template_file, 'r') as template_file: # Opens up template input file
    template_list = [template.strip('\n') for template in template_file]
with open(input_keyword_file, 'r') as input_file: # Opens up keyword input file
    input_list = [line.strip('\n') for line in input_file]

print 'Generating keywords... please wait...'
templated_cartesian_product = cartesian_product_generator(template_list,input_list)
print 'Removing any duplicates... please wait...'
cartesian_product_final = dedupe_list(templated_cartesian_product)
print 'Exporting file... please wait...'
write_file(cartesian_product_final,'cartesian_product')
print 'Cartesian product generated'
print 'Creating this cartesian product took',time.time()-start_time,'seconds.' # Time tracking calculation, prints how many seconds cartesian generation takes
