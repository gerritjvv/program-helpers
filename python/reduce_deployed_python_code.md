# Advice on how to reduce code size

There are use cases where you need to reduce the total size of your python deployed code
including library code.

E.g:

 I have to deploy a layer with pandas and numpy etc.
 Total size cannot be over 260mb.


## Using pre compiled python files

One way is to compile python with `python3 -m compileall -b.` and then remove all the 
`*.py` source files.

Don't do this on your source directory, but copy it to a different location e.g `dist/`

What I do is, copy the python pip packages into the dist folder, and then I run compileall.
After this `find dist -iname "*.py" -exec rm {} \;` to delete all source files.

The result is: 

  * smaller distribution size
  * faster startup


### Why does this work:

Python loads `*.py` files, if a `*.pyc` file exists, it will load the `*.pyc` file,
there's a bit more to it, but I won't go into the details.

If only a `*.pyc` file exists, and no source file, python will still load the file.
This means you can run completely of precompiled python files.

