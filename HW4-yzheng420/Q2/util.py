from scipy import stats
import numpy as np
# This method computes entropy for information gain
def entropy(class_y):
    # Input:            
    #   class_y         : list of class labels (0's and 1's)
    
    # TODO: Compute the entropy for a list of classes
    #
    # Example:
    #    entropy([0,0,0,1,1,1,1,1,1]) = 0.92
        
    entropy = 0
    ### Implement your code here
    n_label=len(class_y)
    if n_label<=1:
        return 0
    Na=class_y.count(0)
    Nb=class_y.count(1)
    if Na == 0 or Nb== 0:
        return 0
    pA=Na/n_label
    pB=Nb/n_label
    entropy=-pA* np.log2(pA) - pB * np.log2(pB)
    #############################################
        
    #pass
    #############################################
    return entropy
#print(entropy([0,0,0,1,1,1,1,1,1]))


def partition_classes(X, y, split_attribute, split_val):
    # Inputs:
    #   X               : data containing all attributes
    #   y               : labels
    #   split_attribute : column index of the attribute to split on
    #   split_val       : either a numerical or categorical value to divide the split_attribute
    
    # TODO: Partition the data(X) and labels(y) based on the split value - BINARY SPLIT.
    # 
    # You will have to first check if the split attribute is numerical or categorical    
    # If the split attribute is numeric, split_val should be a numerical value
    # For example, your split_val could be the mean of the values of split_attribute
    # If the split attribute is categorical, split_val should be one of the categories.   
    #
    # You can perform the partition in the following way
    # Numeric Split Attribute:
    #   Split the data X into two lists(X_left and X_right) where the first list has all
    #   the rows where the split attribute is less than or equal to the split value, and the 
    #   second list has all the rows where the split attribute is greater than the split 
    #   value. Also create two lists(y_left and y_right) with the corresponding y labels.
    #
    # Categorical Split Attribute:
    #   Split the data X into two lists(X_left and X_right) where the first list has all 
    #   the rows where the split attribute is equal to the split value, and the second list
    #   has all the rows where the split attribute is not equal to the split value.
    #   Also create two lists(y_left and y_right) with the corresponding y labels.

    '''
    Example:
    
    X = [[3, 'aa', 10],                 y = [1,
         [1, 'bb', 22],                      1,
         [2, 'cc', 28],                      0,
         [5, 'bb', 32],                      0,
         [4, 'cc', 32]]                      1]
    
    Here, columns 0 and 2 represent numeric attributes, while column 1 is a categorical attribute.
    
    Consider the case where we call the function with split_attribute = 0 and split_val = 3 (mean of column 0)
    Then we divide X into two lists - X_left, where column 0 is <= 3  and X_right, where column 0 is > 3.
    
    X_left = [[3, 'aa', 10],                 y_left = [1,
              [1, 'bb', 22],                           1,
              [2, 'cc', 28]]                           0]
              
    X_right = [[5, 'bb', 32],                y_right = [0,
               [4, 'cc', 32]]                           1]

    Consider another case where we call the function with split_attribute = 1 and split_val = 'bb'
    Then we divide X into two lists, one where column 1 is 'bb', and the other where it is not 'bb'.
        
    X_left = [[1, 'bb', 22],                 y_left = [1,
              [5, 'bb', 32]]                           0]
              
    X_right = [[3, 'aa', 10],                y_right = [1,
               [2, 'cc', 28],                           0,
               [4, 'cc', 32]]                           1]
               
    ''' 
    
    X_left = []
    X_right = []
    
    y_left = []
    y_right = []
    ### Implement your code here
    X_array=np.array(X)
    rows=X_array[:,split_attribute]
    #Reference:https://www.w3schools.com/python/ref_func_isinstance.asp
    if isinstance(split_val, str):
        for i in rows:
            if i==split_val:
                X_left.append(X[list(rows).index(i)])
                y_left.append(y[list(rows).index(i)])
            else:
                X_right.append(X[list(rows).index(i)])
                y_right.append(y[list(rows).index(i)])
    else:
        for i in rows:
            if int(i)<=split_val:
                X_left.append(X[list(rows).index(i)])
                y_left.append(y[list(rows).index(i)])
            elif int(i)>split_val:
                X_right.append(X[list(rows).index(i)])
                y_right.append(y[list(rows).index(i)])
            #num.append(list(rows).index(i))
    #############################################
    
    #pass
    #############################################
    return (X_left, X_right, y_left, y_right)
#X = [[3, 'aa', 10], [1, 'bb', 22], [2, 'cc', 28], [5, 'bb', 32],[4, 'cc', 32]]
#y=[1,1,0,0,1]                    
#print(partition_classes(X, y, 1,'bb'))
    
def information_gain(previous_y, current_y):
    # Inputs:
    #   previous_y: the distribution of original labels (0's and 1's)
    #   current_y:  the distribution of labels after splitting based on a particular
    #               split attribute and split value
    
    # TODO: Compute and return the information gain from partitioning the previous_y labels
    # into the current_y labels.
    # You will need to use the entropy function above to compute information gain
    # Reference: http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15381-s06/www/DTs.pdf
    
    """
    Example:
    
    previous_y = [0,0,0,1,1,1]
    current_y = [[0,0], [1,1,1,0]]
    
    info_gain = 0.45915
    """

    info_gain = 0


    ### Implement your code here
    H=entropy(previous_y)
    HL=entropy(current_y[0])
    PL=len(current_y[0])/len(previous_y)
    HR=entropy(current_y[1])
    PR=len(current_y[1])/len(previous_y)
    info_gain=H-(HL*PL+HR*PR)
    #############################################
        
    #pass
    #############################################
    return info_gain
#print(information_gain(previous_y,current_y))
    
def best_split(X, y):
    # Inputs:
    #   X       : Data containing all attributes
    #   y       : labels
    # TODO: For each node find the best split criteria and return the 
    # split attribute, spliting value along with 
    # X_left, X_right, y_left, y_right (using partition_classes)
    '''
    
    NOTE: Just like taught in class, don't use all the features for a node.
    Repeat the steps:

    1. Select m attributes out of d available attributes
    2. Pick the best variable/split-point among the m attributes
    3. return the split attributes, split point, left and right children nodes data 

   '''
    split_attribute = 0
    split_value = 0
    X_left, X_right, y_left, y_right = [], [], [], []
    ### Implement your code here
    max_info_gain=0
    X_array=np.array(X)
    best_split_attribute=split_attribute
    best_split_val=np.mean(X_array[:,best_split_attribute])
    X_left_i, X_right_i, y_left_i, y_right_i=partition_classes(X, y, best_split_attribute, best_split_val)
    info_gain=information_gain(y,[y_left_i,y_right_i])
    if info_gain>max_info_gain:
        max_info_gain=info_gain
        X_left, X_right, y_left, y_right= X_left_i, X_right_i, y_left_i, y_right_i
        split_attribute=best_split_attribute
        split_value=best_split_val
    split_attribute+=1
    return max_info_gain,split_attribute,split_value,X_left, X_right, y_left, y_right

    #############################################
#X = [[3, 5, 10], [1, 7, 22], [2, 9, 28], [5, 12, 32],[4, 8, 32]]
#    #pass

    #############################################
