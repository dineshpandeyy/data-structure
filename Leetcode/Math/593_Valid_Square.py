class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def dist(A,B):
            yVal = B[1] - A[1]
            xVal = B[0] - A[0]
            return yVal ** 2 + xVal ** 2
        
        allSideDistance = []
        # for the fourside
        allSideDistance.append(dist(p1,p2))
        allSideDistance.append(dist(p2,p3))
        allSideDistance.append(dist(p3,p4))
        allSideDistance.append(dist(p1,p4))

        # for two diagonals
        allSideDistance.append(dist(p1,p3))
        allSideDistance.append(dist(p2,p4))

        allSideDistance.sort()

        return (
            allSideDistance[0] > 0 and 
            allSideDistance[0] == allSideDistance[1] == allSideDistance[2] == allSideDistance[3] and
            allSideDistance[4] == allSideDistance[5] and
            allSideDistance[4] == 2* allSideDistance[0]

        )


        
        


        