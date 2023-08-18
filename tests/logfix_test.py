import unittest;
import os;
import sys;
sys.path.append('./src/');

from logfix import logfix_process;

class TestMainFunctions(unittest.TestCase):

    SWAP_LOG_FILE = os.getcwd() + "/samples/SWAP-log";
    SWAP_LOG132_FILE = os.getcwd() + "/samples/SWAP-log132";
    OUTPUT_SWAP_LOG_FILE = SWAP_LOG_FILE + "-fixed";
    OUTPUT_SWAP_LOG132_FILE = SWAP_LOG132_FILE + "-fixed";

    def test_output_swap_file_creation(self):
        if os.path.exists(f"{self.OUTPUT_SWAP_LOG_FILE}"):
            os.remove(self.OUTPUT_SWAP_LOG_FILE);
        
        logfix_process(self.SWAP_LOG_FILE, "$ASHTP");

        self.assertTrue(os.path.exists(f"{self.OUTPUT_SWAP_LOG_FILE}"), f"File '{self.OUTPUT_SWAP_LOG_FILE}' does not exist");
    
    def test_output_swap_132_file_creation(self):
        if os.path.exists(f"{self.OUTPUT_SWAP_LOG132_FILE}"):
            os.remove(self.OUTPUT_SWAP_LOG132_FILE);
        
        logfix_process(self.SWAP_LOG132_FILE, "$ASPXY");

        self.assertTrue(os.path.exists(f"{self.OUTPUT_SWAP_LOG132_FILE}"), f"File '{self.OUTPUT_SWAP_LOG132_FILE}' does not exist");

if __name__ == '__main__':
    unittest.main();