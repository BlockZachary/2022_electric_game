# _*_coding:utf-8_*_
# Author： Zachary

result = 'Severe'

def set_treatment_time(res):
    dic = {'No':0,'Weak':10,'Moderate':20,'Severe':30}
    print(dic[res])

set_treatment_time(result)