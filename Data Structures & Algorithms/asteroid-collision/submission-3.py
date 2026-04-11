class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collisionstack=[asteroids[0]]
        for x in asteroids[1:]:
            while collisionstack and collisionstack[-1] >0 and x<0:
                if collisionstack[-1]<-x:
                    collisionstack.pop()
                    continue
                elif collisionstack[-1]==-x:
                    collisionstack.pop()
                    break
                break
            else:
                collisionstack.append(x)
                
        return collisionstack

