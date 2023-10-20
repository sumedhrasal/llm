import unittest
import os
import json


class TestReadJSONFromParent(unittest.TestCase):
    def test_read_json_file(self):
        # Get the path to the parent folder
        parent_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "rubrics_template"))

        # Specify the JSON file path within the parent folder
        json_file_path = os.path.join(parent_folder_path, "file1.json")
        self.assertEqual("/Users/srasal/Sumedh/github/llm/rubrics_template/file1.json", json_file_path)

        # Read the JSON file
        # with open(json_file_path, 'r') as file:
        #     data = json.load(file)
        # print(data)



if __name__ == "__main__":
    unittest.main()
