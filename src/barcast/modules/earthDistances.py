## Calculate distances matrix between geographical locations
#Input is N by 2, each row a (lat, long) pair, -90<lat<90; -180<long<180.
#Output is a N by N matrix of great circle distances in KM (approximating the
#earth as a sphere), where the (i,j) entry is the distance between the ith
#and jth rows of the input vector. So the diagonal is zero. 
#This makes use of the so-called haversine formulation (see wikipedia),
#which is also used in the m_lldist.m code of the m_map package. (m_lldist
#gives identical results, but doesn't seem well set up for the formulation
#of the matrix we want here.)
#radius of the earth si taken as 6378.137

### TODO: fix import strategy
import numpy as np
def earthDistances(locations):
    R = 6378.137 #radius of the earth in km

    locations = (locations/180)*np.pi
    num_points = locations.shape[0]
    distances = np.zeros(shape = (num_points, num_points))
    for i in range(locations.shape[0]):
        print(i)
        locations_p = (locations/np.pi)*180
        print(locations_p[:,0])
        print(locations_p[i,0])
        ### TODO: suppress warnings for top half of distances matrix
        distances[:,i] = R * 2 * np.arcsin(np.sqrt( \
            np.sin(.5*(locations[:,0] - locations[i,0]))**2 \
            + np.cos(locations[:,0])*np.cos(locations[i,0])*np.sin(.5*(locations[:,1]-locations[i,1]))**2 \
            )) # end arcsin, sqrt
    return distances

if __name__ == "__main__":
    print("testing")
    ### TODO: assertions, these numbers are slightly off?
    ### test distance cambridge ma to tucson az
    ### according to 
    ##### https://www.vcalc.com/wiki/vCalc/Haversine+-+Distance
    ### 3602.34 
    locations = np.array([[32,-110], [42,-71]])
    print(earthDistances(locations))

    ### test distance cambridge ma to tucson az
    ### according to 
    ##### https://www.vcalc.com/wiki/vCalc/Haversine+-+Distance
    ### 138.92
    locations = np.array([[41,-70], [42,-71]])
    print(earthDistances(locations))
