# Babel
### a simple script to automate variable assignment in AMPscript, made specifically for translation strings from an Excel spreadsheet

Dependencies: [XLRD](http://www.python-excel.org/)

#### Installation:

To install XLRD, run this command:

`python setup.py install`

#### Usage

To run the Babel translator, run this command:

`python babel.py example` where "example" is shorthand for "example.xlsx", the name of the spreadsheet to base the translations on.

There are a few things you should know:

* There is an example spreadsheet with the desired layout included, it is called "example.xlsx".

* The left column will determine the ampscript variable name. To avoid syntax problems, never use spaces. For example, instead of "second paragraph body", try something like secondParagraphText. You do not need to include the @ symbol.

* Babel always sets a catch-all ELSE statement that behaves exactly as the first case.

* Lines 36-41 of babel.py show how to handle special cases that require checking more than one variable

* Babel outputs AMPscript into an .amp file. This assumes you are using Sublime Text and [SeanJA's ampscript syntax highlighting](https://github.com/SeanJA/ampscript-st2 ) . If you want to output to a different file format, edit this line: `fileName = "./output/" + sys.argv[1] + ".amp"` and change to .txt or .html or whatever format you prefer. I __strongly__ recommend you use SeanJA's plugin because syntax highlighting is awesome and relying on ExactTarget's web editor is like choosing to smash your head into a brick wall repeatedly.