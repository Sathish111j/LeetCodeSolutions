from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
         res = []
         for ast in asteroids:
            #  asteroids collision
            while res and ast < 0 < res[-1]:
                curr_ast = res[-1]   
                      
                if curr_ast <= - ast:
                    res.pop()
                if curr_ast >= - ast: 
                    break

            #  no collision
            else:
                res.append(ast)

         return res