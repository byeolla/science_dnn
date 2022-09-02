############ 1번 시작 ##############
def discriminant(p):
    d, c, b, a = p
    return (c**2)*(b**2 - 4*a*c) - d*(4*(b**3) + 27*(a**2)*d - 18*a*b*c)

def cubicroots(p):
    return discriminant(p)>0

p = [1, -1, 0, 1]

cubicroots(p) 
############################ 1번 끝 ######################


##################### 2번 시작 #######################
import math
def logintegral(c, N):
    sum = 0.0
    dx = (c - 1)/N
    x = 1.0
    for i in range(N+1):
        lnx = math.log(x)
        sum += lnx * dx /(1+lnx)**2
        x += dx
    
    return sum
    
print(logintegral(math.exp(1), 1000))     ##### 정의한 함수를 이용한 값
print(math.exp(1)/2 - 1)           ######## 비교를 위한 math package 이용
############### 2번 끝 #######################