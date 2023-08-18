# logfix

Log file remediation program

Software generates log files useful for trouble-shooting, but users often view the log files, then use copy and paste when they raise a problem. That causes folded lines to be broken into two or more lines. This makes parsing the file for trouble-shooting annoying.

This software will fix-up such broken log files.

## logfix install

1. Download the project:  
If you have git:  

    ~~~cmd
    git clone https://github.com/agustinruiz/logfix.git 
    ~~~

    if you don't, click on "Code -> Download ZIP" and unzip it.

2. Install python if you don't have it already.

    from: https://www.python.org/downloads/

## logfix run

The main file of the program is /src/logfix.py

You could run it using the make command:

~~~cmd
make 
~~~

You could run it going to the src directory an executing the following command:

~~~cmd
python3 logfix.py 
~~~

## logfix test

If you want you could run the test script to see how the outputs files are generated from the samples files.

You could run the tests using the make command:

~~~cmd
make test
~~~

Or you could run it directly going to the tests directory and running the following command

~~~cmd
python3 logfix_test.py 
~~~
