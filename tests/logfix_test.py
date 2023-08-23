import unittest;
import os;
import sys;
sys.path.append('./src/');

from file_utils import save_output_file, open_input_file;
from analysis_by_rid import by_record_identifier_content_process;
from analysis_by_rid_llen import by_recordID_and_line_length_content_process;

class TestMainFunctions(unittest.TestCase):

    SWAP_LOG_FILE = os.getcwd() + "/samples/SWAP-log";
    SWAP_LOG132_FILE = os.getcwd() + "/samples/SWAP-log132";
    OUTPUT_SWAP_LOG_FILE_BY_RID = SWAP_LOG_FILE + "-fixed-by-rid";
    OUTPUT_SWAP_LOG132_FILE_BY_RID = SWAP_LOG132_FILE + "-fixed-by-rid";
    OUTPUT_SWAP_LOG_FILE_BY_RID_LEN = SWAP_LOG_FILE + "-fixed-by-rid-len";
    OUTPUT_SWAP_LOG132_FILE_BY_RID_LEN = SWAP_LOG132_FILE + "-fixed-by-rid-len";

    def test_output_swap_file_creation_by_rid(self):
        if os.path.exists(f"{self.OUTPUT_SWAP_LOG_FILE_BY_RID}"):
            os.remove(self.OUTPUT_SWAP_LOG_FILE_BY_RID);

        file_content = open_input_file(self.SWAP_LOG_FILE);
        
        new_content = by_record_identifier_content_process(file_content,"$ASHTP")

        save_output_file(self.OUTPUT_SWAP_LOG_FILE_BY_RID,new_content);

        self.assertTrue(os.path.exists(f"{self.OUTPUT_SWAP_LOG_FILE_BY_RID}"), f"File '{self.OUTPUT_SWAP_LOG_FILE_BY_RID}' does not exist");
    
    def test_output_swap_132_file_creation_by_rid(self):
        if os.path.exists(f"{self.OUTPUT_SWAP_LOG132_FILE_BY_RID}"):
            os.remove(self.OUTPUT_SWAP_LOG132_FILE_BY_RID);
        
        file_content = open_input_file(self.SWAP_LOG132_FILE);
        
        new_content = by_record_identifier_content_process(file_content,"$ASPXY")

        save_output_file(self.OUTPUT_SWAP_LOG132_FILE_BY_RID,new_content);

        self.assertTrue(os.path.exists(f"{self.OUTPUT_SWAP_LOG132_FILE_BY_RID}"), f"File '{self.OUTPUT_SWAP_LOG132_FILE_BY_RID}' does not exist");

    def test_output_swap_file_creation_by_rid_len(self):
        if os.path.exists(f"{self.OUTPUT_SWAP_LOG_FILE_BY_RID_LEN}"):
            os.remove(self.OUTPUT_SWAP_LOG_FILE_BY_RID_LEN);
        
        file_content = open_input_file(self.SWAP_LOG_FILE);
        
        new_content = by_recordID_and_line_length_content_process(file_content, 80,"$ASHTP")

        save_output_file(self.OUTPUT_SWAP_LOG_FILE_BY_RID_LEN,new_content);

        self.assertTrue(os.path.exists(f"{self.OUTPUT_SWAP_LOG_FILE_BY_RID_LEN}"), f"File '{self.OUTPUT_SWAP_LOG_FILE_BY_RID_LEN}' does not exist");
    
    def test_output_swap_132_file_creation_by_rid_len(self):
        if os.path.exists(f"{self.OUTPUT_SWAP_LOG132_FILE_BY_RID_LEN}"):
            os.remove(self.OUTPUT_SWAP_LOG132_FILE_BY_RID_LEN);
        
        file_content = open_input_file(self.SWAP_LOG132_FILE);
        
        new_content = by_recordID_and_line_length_content_process(file_content, 132,"$ASPXY")

        save_output_file(self.OUTPUT_SWAP_LOG132_FILE_BY_RID_LEN,new_content);

        self.assertTrue(os.path.exists(f"{self.OUTPUT_SWAP_LOG132_FILE_BY_RID_LEN}"), f"File '{self.OUTPUT_SWAP_LOG132_FILE_BY_RID_LEN}' does not exist");

if __name__ == '__main__':
    unittest.main();