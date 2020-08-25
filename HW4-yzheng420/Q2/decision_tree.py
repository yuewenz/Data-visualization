from util import entropy, information_gain, partition_classes,best_split
import numpy as np 
import ast

class DecisionTree(object):
    def __init__(self, max_depth):
        # Initializing the tree as an empty dictionary or list, as preferred
        self.tree = {}
        self.max_depth = max_depth
        pass
    	
    def learn(self, X, y, par_node = {}, depth=0):
        # TODO: Train the decision tree (self.tree) using the the sample X and labels y
        # You will have to make use of the functions in utils.py to train the tree

        # Use the function best_split in util.py to get the best split and 
        # data corresponding to left and right child nodes
        
        # One possible way of implementing the tree:
        #    Each node in self.tree could be in the form of a dictionary:
        #       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
        #    For example, a non-leaf node with two children can have a 'left' key and  a 
        #    'right' key. You can add more keys which might help in classification
        #    (eg. split attribute and split value)
        ### Implement your code here
        #no y
        if len(y)==0:
            self.tree['class'] = 'leaf'
            self.tree['lable'] = 0
            return
        #reach the max_depth
        y_1=y.count(1)
        y_0=y.count(0)
        y_number=[y_0,y_1]
        if self.max_depth < depth:
            self.tree['class'] = 'leaf'
            if y_1==0:
                self.tree['lable'] = 0
                return 0
            if y_0==0:
                self.tree['lable'] = 1
                return 1

        max_info_gain,best_split_attribute,best_split_value, X_left, X_right, y_left, y_right=best_split(X,y)
        #max_info_gain=information_gain(y,[y_left,y_right])
        #print(max_info_gain)
        self.tree["split_attribute"]=best_split_attribute
        self.tree["split_value"]=best_split_value
        self.tree["IG"]=max_info_gain
        #IG=0
        if self.tree["IG"]==0 or self.tree["IG"]==1 :
            self.tree["class"]="leaf"
            self.tree['lable'] = y_number.index(max(y_number))
            return
        self.tree['left']=DecisionTree(self.max_depth)
        self.tree['left'].learn(X_left,y_left,{},depth+1)
        self.tree['right']=DecisionTree(self.max_depth)
        self.tree['right'].learn(X_right,y_right,{},depth+1)
        self.tree["class"]="non-leaf"
       

        #when len(y)=0
        #[1,0,1,1....]
        #[1,0,1],[0,1]
        #############################################
        
        #pass
        #############################################
    def classify(self, record):
        # TODO: classify the record using self.tree and return the predicted label
        ### Implement your code here
        if self.tree["class"] == "leaf":
            return self.tree['lable']
        else:
            attribute=self.tree["split_attribute"]
            value=self.tree["split_value"]
            if record[attribute]<=value:
                return self.tree["left"].classify(record)
            else:
                return self.tree["right"].classify(record)

        #############################################
        
       # pass
        #############################################
