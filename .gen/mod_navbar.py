#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gen

def run(options):
    ret = '''
    <nav class="navbar navbar-default navbar-static-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"
                        aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>

                    <!-- QUESTION: Why do we need these 3 lines? And where's the
                         'Toggle navigation' button on the page? -->
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">Ugandan Web Force</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
                <ul class="nav navbar-nav navbar-right">
                    {dropdown_menu}
                    <li>
                        <a href="//github.com/ugandanwebforce" target="_blank">github</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>'''

    return ret.format(dropdown_menu=gen.run_module('dropdown_menu', options))

"""
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
"""
