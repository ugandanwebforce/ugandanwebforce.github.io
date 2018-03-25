#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mod_dropdown_menu as dropdown

raw_modules = {
    'dropdown_menu': dropdown,
}
#((name, pymod.run) for (name, pymod) in raw_modules)

#modules = dict([(name, pymod.run) for name, pymod in dict(raw_modules)])
#modules = dict(map(lambda name, python_module: (name, python_module.run), raw_modules))

modules = dict(((k, raw_modules[k].run) for k in raw_modules))
