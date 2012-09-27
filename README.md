Lectures
========

_Build lecture slides and notes from common source_

James Keirstead 

20 September 2011

<http://www.jameskeirstead.ca>

DESCRIPTION 
-----------

The LaTeX 'beamer' package provides an excellent way to develop
lecture notes in a literate programming style, combining both detailed
background notes and presentation slides in a single source file.  However users have to manually create wrapper files that will build this source into the appropriate format.  

This software provides a set of templates and a Python script to
automate the process.  Simply install the tool and type: 

	build-lecture source style 

from your working directory and it will automatically generate both
the slides and notes for the lecture, including any references you
might have used.

INSTALLATION 
------------

To install the software: 

1. Unzip the code into a convenient location.  
 
2. Update your TeX search path to include the 'latex' directory. 

  * If on Windows with MikTeX, use the Settings program and select
     the Roots tab.  Add the project's latex directory. Then select 
     the General tab and click the "Refresh FNDB" button.  This will 
     add the files to MiKTeX's file name database.
	  
  * If on a *nix system, type:
```
		texhash ~/lectures/latex
```      
	substituting with your local path as appropriate.  You may also
	need to set the TEXINPUTS environment variable.  This is a pain
	to set up but here's the bottom of my ~/.bashrc as an example:
```
		# TEX 
		TEXINPUTS=.:~/software/texmf//:/usr/share/texmf-texlive//:/usr/share/texmf//:
		export TEXINPUTS
```
  For completeness, this is on Ubuntu 10.04 system.

3. Install the scripts.

	* If on Windows, edit the SCRIPTDIR variable in the
      'build-lecture.bat' file to match your local installation.  Then copy
      the batch file to C:\Windows\System32 or another directory accessible
      from the command line.

	* If on a *nix system, you should be able to drop the
      build-lecture.py script from the python directory into a similar
      location, like ~/bin.  You may need to add this directory to your
      $PATH variable and also change the permissions on the file, e.g.
```bash
		chmod 766 build-lecture.py
```

4. If you are using a version control system, please install the vc
       latex package and change the following lines.

 - In lectures.sty, uncomment `\input{vc}`
 - In build-lectures.py, change useVC to True

	You will also need to copy the relevant files from the vc latex
	package into your working directory.  The package and documentation
	are available at http://www.ctan.org/tex-archive/support/vc
