import numpy as np


class resolutor:
    def __init__(self):
        self.magnification = 2

    def dummy_initiator(matrix, k_factor):
        #get low resolution matrix shape
        x,y = matrix.shape
        
        #create a new resolution matrix of shape increased by a factor of k
        #creates a super resolution image with neighbors initialized to ones.
        super_matrix = np.ones((x*k_factor, y*k_factor))
        
        # update super matrix with previous values from the low resolution image
        for i in range(x):
            for j in range(y):
                super_matrix[i*k][j*k] = matrix[i][j]
        
        return super_matrix

    

    def reinitialize_max_pool(matrix, super_matrix, k = 2):
        # reinitializing neigbors from one to max value
        x_old, y_old = matrix.shape
        x_new, y_new = super_matrix.shape
        
        if k == 2:
            for i in range(x_old):
                for j in range(y_old):
                    a,b = i*k, j*k
                    #for every pixel map in low resolution image format
                    #map new resolution image with its neighbor as max pool
                    super_matrix[a-1][b-1] = matrix[i][j]
                    super_matrix[a-1][b] = matrix[i][j]
                    super_matrix[a][b-1] = matrix[i][j]
                    super_matrix[a][b] = matrix[i][j]
                    
        elif k == 3:
            for i in range(x_old):
                for j in range(y_old):
                    a,b = i*k, j*k
                    #for every pixel map in low resolution image format
                    #map new resolution image with its neighbor as max pool
                    super_matrix[a-2][b-2] = matrix[i][j]
                    super_matrix[a-2][b-1] = matrix[i][j]
                    super_matrix[a-2][b] = matrix[i][j]
                    super_matrix[a-1][b-2] = matrix[i][j]
                    super_matrix[a-1][b-1] = matrix[i][j]
                    super_matrix[a-1][b] = matrix[i][j]
                    super_matrix[a][b-2] = matrix[i][j]
                    super_matrix[a][b-1] = matrix[i][j]
                    super_matrix[a][b] = matrix[i][j]
                    
        else:
            pass
        return super_matrix


    def find_nearest(a,b, k = 2):
            nearest = []
        if k ==2:
            for i in range(a-1,a+1):
                for j in range(b-1,b+1):
                    string = str(i) + str(j)
                    if string in nearest:
                        pass
                    else:
                        nearest.append(string)
        elif k== 3:
            for i in range(a-2,a+1):
                for j in range(b-2,b+1):
                    string = str(i) + str(j)
                    if string in nearest:
                        pass
                    else:
                        nearest.append(string)
        else:
            pass
        return nearest[:-1]


    def interpolate_neurons(matrix, super_matrix):
        """
        maps original pixel number to output matrix to be interpolated
        if c is the number of inputs to be interpolated which is m *n (dimension)
        and k is the magnification factor then
        output number is mn((k**2)-1) to be mapped
        """
        x, y = matrix.shape
        input_flatten = []
        output_flatten = []
        if k == 2:
            for a in range(x):
                for b in range(y):
                    string = str(a) + str(b)
                    input_flatten.append(super_matrix[a][b])
                    output_flatten.extend([super_matrix[k[0]][k[1]] for k in find_nearest(a,b,k=2)])
        elif k==3:
            for a in range(x):
                for b in range(y):
                    string = str(a) + str(b)
                    input_flatten.append(super_matrix[a][b])
                    output_flatten.extend([super_matrix[k[0]][k[1]] for k in find_nearest(a,b,k=2)])
        else:
            pass
        
        
        return input_flatten, output_flatten