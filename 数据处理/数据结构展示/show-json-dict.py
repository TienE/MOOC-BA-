# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:25:48 2020

@author: TienE
"""

import json


'''
#名字： dict_tree()
#输入： (Dict = json字典, n = 层数) 
#输出： 无
#功能： 打印字典结构，方便‘阅读’
#time: 2020-10-16
#else: p1_only for 'Dict','list' and 'str',int';
#      p2_Recursive implementation 
'''
def dict_tree(Dict, n = 0):
    
    # 空格字符
    ven = ('|' + ' ' * 6)
    
    # 节点是一个‘字典’
    if isinstance(Dict,dict):
        for key,value in Dict.items():
            print(ven*n,'|','----',key,sep='')
            dict_tree(value,n+1)
        print(ven*n,sep='')
        
    # 节点是一个‘列表’
    elif isinstance(Dict,list) :
        for items in Dict:
            if isinstance(items,list) or isinstance(items,dict):
                print(ven*n,'|','----','[]',sep='')
                dict_tree(items,n+1)
            else:
                print(ven*n,'|','----',items,sep='')
        print(ven*n,sep='')
        
    # 节点是一个‘字符’
    elif isinstance(Dict,str):
        print(ven*n,'|','----',Dict,sep='')
    elif isinstance(Dict,int):
        print(ven*n,'|','----',Dict,sep='')
    else:
        pass

'''
主程序函数：
'''

filename = 'user_video_act_train_1.json'

with open(filename,'r') as f:

    js_objects = json.loads(f.readline())
 
    dict_tree(js_objects,0)
    
