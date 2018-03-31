#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run(options):
    ret = '''<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
    Menu <span class="caret"></span>
    </a>
    <ul class="dropdown-menu" role="menu">'''
    for page in options['pages_list']:
        if page[0] == options['current_page']:
            ret += '''<li><span class="nav-current-page">{}</span></li>'''.format(page[1])
        else:
            ret += '''<li><a href="{}">{}</a></li>'''.format(page[2], page[1])
    ret += '''</ul>
    </li>'''
    return ret
