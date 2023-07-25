def array_check(nums):
    for i in range(len(nums)-2):
        if nums[i+1] == nums[i] + 1 and nums[i+2] == nums[i] + 2:
            return True
    return False

a1  = array_check([1,1,1,2,3,4,5])
a2  = array_check([1,2,1,2,1,2,3])
a3  = array_check([1,1,3,5,2,5,2])

def string_bits(string):
    return string[::2]

s1 = string_bits('Hello')
s2 = string_bits('H')
s3 = string_bits('Heelllloooo')

def end_other(str1,str2):
    a = str1.lower()
    b = str2.lower()
    return (a.endswith(b) or b.endswith(a))

q1 = end_other('abc','hiabc')
q2 = end_other('hiABC','ABC')
q3 = end_other('hisfd','sdfds')

print(q1)
print(q2)
print(q3)