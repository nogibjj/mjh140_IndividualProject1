import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from src.lib import(
    import_iris as imp, 
    describe_iris as des,
    visualize_iris as vis,
    )

class TestLib(unittest.TestCase):

    def test_correct_data(self):
        # This should not raise an error
        try:
            imp("iris_data.csv")
        except TypeError:
            self.fail("TypeError raised for correct data type")
        except FileNotFoundError:
            self.fail("File was not found.")
    
    def test_incorrect_file_type(self):
        # This should raise a TypeError
        with self.assertRaises(TypeError):
            imp(42)

    def test_unknown_file(self):
        # This should raise a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            imp("fake_data.csv")
    
    def test_incorrect_dataframe_type(self):
        # This should raise a TypeError
        with self.assertRaises(TypeError):
            des(42)

    def test_incorrect_plot_type(self):
        # This should raise a TypeError
        with self.assertRaises(TypeError):
            vis(42)

            
if __name__ == '__main__':
    unittest.main()