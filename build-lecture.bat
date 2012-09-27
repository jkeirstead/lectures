:: Batch file for building lecture notes
:: James Keirstead
:: 9 September 2011

@ECHO OFF

:: Change this directory as appropriate to your installation
SET SCRIPTDIR=d:\jkeirste\code\lectures\python

:: Only run the analysis if there are two arguments
set argC=0
for %%x in (%*) do Set /A argC+=1

if %argC% == 2 (
   echo Building lecture '%1' with style '%2'
   python %SCRIPTDIR%\build-lecture.py %1 %2 > build.log
   echo Build complete.  Further information in 'build.log'.
) ELSE (
  echo Need two arguments, the content file 1 and the style file 2
)


