import unittest
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from src.script import save_plot as save

class TestSavePlot(unittest.TestCase): 
    def test_incorrect_plot_type(self):
        # This should raise a TypeError
        with self.assertRaises(TypeError):
            fig = plt.figure()
            save("test.png", fig)

    def test_missing_file_extension(self):
        data = [1,2,3,4,5]
        fig = sns.FacetGrid(data)
        save(".test_cases_plot", fig)

if __name__ == '__main__':
    unittest.main()

