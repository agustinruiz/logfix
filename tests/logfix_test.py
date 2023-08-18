import os;
import sys;
sys.path.append('./src/')

from logfix import logfix_process;

logfix_process(os.getcwd() + "/samples/SWAP-log", "$ASHTP");
logfix_process(os.getcwd() + "/samples/SWAP-log132", "$ASPXY");