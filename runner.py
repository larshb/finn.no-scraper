#!/usr/bin/env python3

# Used to test crawler with Python debug options (ie. breakpoints, etc.)

from scrapy.cmdline import execute
execute([
    'scrapy', 'crawl',
    'letting',
    '-a', 'location=0.20061',
    '-o', 'letting.json'
    ])
