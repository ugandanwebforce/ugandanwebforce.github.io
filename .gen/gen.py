#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script generates the site content


# MODULES
import json
import re
from sys import argv
#from gen_modules import *
import gen_modules

# CONFIGURATION
structure_filename = 'structure.json'
output_path        = '../'


# RUNTIME-FILLED CONFIGURATION
templates_dir = ''
index_file = ''


# FUNCTIONS
def print_usage_info():
    print(usage_info_string.format(prog_name = argv[0]))

def generate_toplevel(toplevel_structure):
    assert(type(toplevel_structure) == dict)
    global templates_dir, output_path, index_file
    templates_dir = toplevel_structure['templates_dir']
    index_file    = toplevel_structure['index_file']
    for page in toplevel_structure['pages']:
        generate_page(page, list_pages(toplevel_structure))

def generate_page(page_structure, pages_list):
    assert(type(page_structure) == dict)
    assert(type(pages_list)     == list)
    template_content = get_template(page_structure['path'])
    module_options = page_structure['module_options'] if 'module_options' in page_structure else {}
    module_options['pages_list'] = pages_list
    module_options['current_page'] = page_structure['page_id']
    parsed_content = parse_template(template_content, module_options)
    with open('{prefix}/{page_path}/{index_file}'.format(prefix = output_path, page_path = page_structure['path'], index_file = index_file), 'w') as output_file:
        output_file.write(parsed_content)
    for page in page_structure['children']:
        generate_page(page, pages_list)

def get_template(page_path):
    # TODO: make it look beautiful
    with open('{prefix}/{page_path}/{index_file}'.format(prefix = templates_dir, page_path = page_path, index_file = index_file), 'r') as template_file:
        return template_file.read()

def parse_template(template_content, module_options):
    ret = ''
    used_modules = re.findall(r'%%GENPY_MODULE:[a-zA-Z0-9+/_,= -]+%%', template_content)
    text_content = re.split(r'%%GENPY_MODULE:[a-zA-Z0-9+/_,= -]+%%', template_content)
    ret += text_content[0]
    text_content = text_content[1:]
    for (module_match, text) in zip(used_modules, text_content):
        module_name = module_match[15:-2]
        module_extra_options_raw = re.findall(r',\w*=[a-zA-Z0-9+/_= -]+', module_name)
        module_extra_options = dict([tuple(i[1:].split('=', 1)) for i in module_extra_options_raw])
        del module_extra_options_raw
        #print(module_name, repr(module_extra_options)) # Debug
        module_basename = re.match(r'[^,=]*', module_name).group(0)

        for k, v in module_extra_options.items():
            #print("D: mo[{}] = {}".format(k, v))
            module_options[k] = v

        #print("A", module_basename, repr(module_options)) # Debug

        ret += run_module(module_basename, module_options)
        ret += text
    return ret

def run_module(module_name, module_options):
    return gen_modules.modules[module_name](module_options)
    #return 'Running module {} with options {}'.format(module_name, repr(module_options))

def list_pages(toplevel_structure):
    assert(type(toplevel_structure) == dict)
    ls = []
    for i in toplevel_structure['pages']:
        ls += list_subpages(i)
    return ls

def list_subpages(page_structure):
    assert(type(page_structure) == dict)
    ls = [(page_structure['page_id'], page_structure['menu_title'],page_structure['path'])]
    for i in page_structure['children']:
        ls += list_subpages(i)
    return ls

# LARGE STRINGS:
usage_info_string = '''
Usage: {prog_name}
This script generates the site content
'''
# To get rid of leading and trailing newlines
usage_info_string = usage_info_string[1:-1]


# ENTRY POINT
def main():
    if len(argv) >= 2 and argv[1] == '--help':
        print_usage_info()
        exit(0)

    json_text = ''
    with open(structure_filename, 'r') as structure_file:
        json_text = structure_file.read()

    structure = {}
    try:
        structure = json.loads(json_text)
    except json.decoder.JSONDecodeError as exc:
        print('Error: structure file is in invalid format')
        print('JSON decoding failed. Error info:')
        print(exc)
        exit(1)

    generate_toplevel(structure)

if __name__ == '__main__':
    main()
