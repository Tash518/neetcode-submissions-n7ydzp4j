class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collisionstack=[asteroids[0]]
        for x in asteroids[1:]:
            while collisionstack and collisionstack[-1] >0 and x<0:
                if collisionstack[-1]==abs(x):
                    collisionstack.pop()
                    break
                elif collisionstack[-1]<abs(x):
                    collisionstack.pop()
                    continue
                else:
                    break
            else:
                collisionstack.append(x)
                
        return collisionstack

