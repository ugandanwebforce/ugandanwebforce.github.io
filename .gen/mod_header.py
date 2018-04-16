#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run(options):
    ret = '''
<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
        Menu <span class="caret"></span>
    </a>
    <ul class="dropdown-menu" role="menu">
        {}
    </ul>
</li>'''
    fmt = ''
    for page in options['pages_list']:
        if page[0] == options['current_page']:
            fmt += '''<li><span class="nav-current-page">{}</span></li>'''.format(page[1])
        else:
            fmt += '''<li><a href="{}">{}</a></li>'''.format(page[2], page[1])
    return ret.format(fmt)
