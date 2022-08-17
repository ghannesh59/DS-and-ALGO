class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        dir_x,dir_y=0,1
        for i in instructions:
            if i=='G':
                x,y=x+dir_x,y+dir_y
            elif i=='L':
                dir_x,dir_y=-1*dir_y,dir_x
            else:
                dir_x,dir_y=dir_y,-1*dir_x
        return (x,y)==(0,0) or (dir_x,dir_y)!=(0,1)