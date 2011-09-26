#!/usr/bin/env python

"""build-lecture.py: Builds lecture notes and slides from a common LaTeX source document."""

import sys
import os
import string
import subprocess
import glob

__author__ = "James Keirstead"
__copyright__ = "Copyright 2011, James Keirstead"

useVC = True

# Define a function to build the file
def build_file(content, style, isSlide):
    """Builds and compiles the lecture files with a given style 

    Keyword arguments:
    content -- the content file
    style   -- the style file
    isSlide -- True, if slides should be built.  False, if notes.
    """

    # Set up some initial variables
    root = 'slides' if isSlide else 'notes'
    work_dir = os.path.dirname(os.path.realpath(__file__))
    print work_dir, os.sep

    # Choose the right header file
    header_file = work_dir + os.sep + root + '-header.tex'
    
    # Read the template
    f = open(header_file, 'r')
    lines = f.readlines()
    f.close()

    # Create the source file
    src_file = content + '-' + root
    source = open(src_file + '.tex', 'w')
    
    for line in lines:
        source.write(line)

    if (isSlide):
        # This code needs to be inserted before the content
        source.write('%% Necessary to ensure that the bibliography shows up correctly\n')
        source.write('\mode<presentation>{\def\\newblock{}}\n')

    source.write('\input{' + style + '}\n')
    source.write('\input{' + content + '}\n')
    source.close()

    # Compile the result
    if useVC:
        if os.name == 'nt': # Call batch file on Windows platforms
            subprocess.call('vc.bat')
        else:
            subprocess.call('sh ./vc')

    commands = ['xelatex','bibtex','xelatex','xelatex']
    for command in commands:
        subprocess.call((command, src_file)) 

    # Tidy up
    bad_exts = ['aux','bbl','nav','out','blg','snm','toc']
    bad_exts = [(src_file + '.' + ext) for ext in bad_exts]

    for root, dirs, files in os.walk(os.getcwd()):
        for trace in bad_exts:
            win_trace_path = os.path.join(root, trace)
            for filename in glob.glob(win_trace_path):
                if os.path.exists(filename):
                    os.remove(filename)
 
# Read the command line arguments
content = sys.argv[1]
style = sys.argv[2]

# Build the files
build_file(content, style, True)
build_file(content, style, False)
