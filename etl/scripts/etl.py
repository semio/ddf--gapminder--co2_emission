# -*- coding: utf-8 -*-

from ddf_utils.chef.api import run_recipe

run_recipe('../recipes/etl.yml', ddf_dir=None, out_dir='../../')
