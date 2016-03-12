import numpy as np

"""
KDT Tree Node
"""
class KDTNode:
    def __init__(self, val=None):
        self.left =  None
        self.right = None
        self.value = val

"""
This Function partition the Plane in equally two halves
"""
def _partitionPlanePoints(Points, arrindex, medianVal):
    partition1Points = []
    partitition2Points = []
    
    for i in range(len(Points)):
        pnt = Points[i]
        toConsiderVal_LatorLong = pnt[arrindex]
        
        if toConsiderVal_LatorLong < medianVal:
            partition1Points.append(pnt)
        else:
            partitition2Points.append(pnt)
    
    return partition1Points, partitition2Points

"""
This Function creates KDTree
"""
def BuildKDTree(P, depth) :
    if (len(P) == 1) :
        leafNode = KDTNode(P[0])
        return leafNode
    elif (len(P) != 0):
        """
        JUST get the Median and Median Lat, Median Long
        """
        Median = np.median(P, axis=0)
        MedianLat = Median[0]
        MedianLong = Median[1]
        
        """
        Two Partition array Initialization
        """
        partition1 = []
        partition2 = []
        
        if (depth%2 == 0): # EVEN Depth :: Partition Search Space vertically
            partition1, partition2 = _partitionPlanePoints(P, 0, MedianLat) # Left and Right
        else : # ODD Depth :: Partition Search Space horizontally
            partition1, partition2 = _partitionPlanePoints(P, 1, MedianLong) # Up and Down
        
        innerNode = KDTNode(Median)
        innerNode.left = BuildKDTree(partition1,depth+1)
        innerNode.right = BuildKDTree(partition2,depth+1)
        
        return innerNode
    
    else:
        leafNode = KDTNode()
        return leafNode
        
"""
This function searches in a K-D Tree
"""
def searchKDTree(KDTNodeobj, srchpnt, depth = 0):
    
    if (KDTNodeobj !=None) and ((KDTNodeobj.left == None) and (KDTNodeobj.right == None)) : # Leaf Node Found
    
        return KDTNodeobj.value # Returning the Leaf Node
    
    else:
        """
        Inner Nodes Informations
        """
        leftChildNode = KDTNodeobj.left
        rightChildNode = KDTNodeobj.right
        valChildNode = KDTNodeobj.value
        valChildNodeLat = valChildNode[0]
        valChildNodeLong = valChildNode[1]
        
        """
        search Point Information
        """
        srchPntLat = srchpnt[1]
        srchPntLong = srchpnt[0]
        
        if (depth%2 == 0) : # EVEN Depth :: Search for Left or Right :: i.e. by Latitude
        
            if srchPntLat < valChildNodeLat :
                return searchKDTree(leftChildNode, srchpnt, depth+1)
            else:
                return searchKDTree(rightChildNode, srchpnt, depth+1)
        
        else : # ODD Depth :: Search for Up or Down :: i.e. by Longitude
            
            if srchPntLong < valChildNodeLong :
                return searchKDTree(leftChildNode, srchpnt, depth+1)
            else:
                return searchKDTree(rightChildNode, srchpnt, depth+1)

