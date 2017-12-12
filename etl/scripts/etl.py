# -*- coding: utf-8 -*-

import sys

from ddf_utils.chef.api import run_recipe

if __name__ == '__main__':
    ddf_dir = sys.argv[1]
    run_recipe('../recipes/etl.yml', ddf_dir=ddf_dir, out_dir='../../')
