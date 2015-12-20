#RoboCrack
>A script that ckecks whether your password is weak or not. It was inspired by the password cracker used by Elliot Alderson in the Mr.Robot tv-series.
##Usage
```$ python robot.py```
##TODOs:
* Will try to make it more efficient and test more permutations.

##Example
```
$ python robot.py 
username:karan_desai
password:kd2811desai

Enter as much information as possible(as much as a good social engineer might be able to gather), like birthday, nickname etc. Enter 'end' to when done
karan desai
kd bhaiya
28 11 1997
pro
end


-------------******Final List******----------------
karan_desai
karan
desai
kd
bhaiya
28
11
1997
pro
KARAN_DESAI
KARAN
DESAI
KD
BHAIYA
PRO
K
D
B
P
k
d
b
p
123456
1234567
12345678
123456789
-------------******Final List******----------------
Checking: 67579 of 10888869450418352160768000000    
FOUND!!!. It is a weak password
Password is: kd2811desai
```

