import pandas as pd
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append('..')
from outliers_filtering.utils import remove_outliers_numeric, plot_distribution_numeric


def test_output_remove_outliers_numeric():
    """ test that outliers_filtering is working as expected"""

    data = pd.read_csv('./data/data_demo.csv')

    size_input = data.shape[0]
    min_input = data['useful_area'].min()
    max_input = data['useful_area'].max()
    
    data = remove_outliers_numeric(data,feature = 'useful_area', option = "lognormal",delta=1.5)
    
    size_output = data.shape[0]
    min_output = data['useful_area'].min()
    max_output = data['useful_area'].max()


    assert size_output < size_input
    assert min_output > min_input
    assert max_output < max_input