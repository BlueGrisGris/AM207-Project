"""
Test lib functions  
"""
### import requirements 
import sys
import pytest
import numpy as np

### set path above Barcast
sys.path.append("./src/")
### import Barcast
import Barcast
### testing class
class TestLib():

    def test_earthDistances(self):
        """
        unit test earthDistances()
        """
        ### pick 2 points to calc distance: cambridge ma to tucson az
        locations = np.array([[32,-110], [42,-71]])
        official_dist = np.array([[0,3606],[3606,0]])  ## rounding to the nearest km?
        calc_dist = np.round(Barcast.earthDistances(locations),0)

        ### printing for diagnostics
        #print(f"calc_dist: {calc_dist}")
        #print(f"official_dist: {official_dist}")

        assert np.array_equal(calc_dist , official_dist) == True


        





