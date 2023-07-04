# Copyright(c) 2023 Qian(田陈啸),Xuan(小轩),Yuhang Wu and all contributors
# All right Reserved
    
#     Distributed under GPL license
#     See copy at https://opensource.org/licenses/GPL-3.0
# F++:(Foundation Language plus plus) - A computer language based on Python
# This version is F++ Stable 200(Rebuild)

import time                
import atexit
import os
import sys
import termios
import random
import tty
import base64
import json
import re
import socket
import requests
import posix
import stat
import keyword
import unittest
import datetime
import enum

def printcode(code):
    END_COLOR = "\033[0m"                              
    SELF_COLOR = "\033[95m"                          
    STRING_COLOR = "\033[32m"                          
    ESSENTIAL_COLOR = "\033[94m"                      
    FUNCTION_COLOR = "\033[35m"                      
    NUMBER_COLOR = "\033[36m"                    
    BUILT_FUNCTION = "\033[90m"                      
    ERROR_COLOR = "\033[31m"                       
    code = code.replace("\033", "\\033")            
    number_list = []                               
    for i in range(10):number_list.append(str(i))      
    new_code = ""
    for i in range(len(code)):
        if code[i] in number_list:
            try:
                if not ((code[i+1] == "m" or code[i+2] == "m") or (code[i+1] == ";" or code[i+2] == ";")):new_code = new_code + NUMBER_COLOR + code[i] + END_COLOR
                else:new_code = new_code + code[i]
            except:new_code = new_code + NUMBER_COLOR + code[i] + END_COLOR
        else:new_code = new_code + code[i]
    code = new_code
    code = code.replace("this", SELF_COLOR + "this" + END_COLOR)                            
    code = code.replace(">>>", SELF_COLOR + ">>>" + END_COLOR)                      
    code = code.replace(">>>", SELF_COLOR + ">>>" + END_COLOR)                      
    code = code.replace("class", ESSENTIAL_COLOR + "class" + END_COLOR)     
    code = code.replace("define", ESSENTIAL_COLOR + "define" + END_COLOR)              
    code = code.replace("pass", ESSENTIAL_COLOR + "pass" + END_COLOR)                
    code = code.replace("try", ESSENTIAL_COLOR + "try" + END_COLOR)            
    code = code.replace("except", ESSENTIAL_COLOR + "except" + END_COLOR)            
    code = code.replace("for", ESSENTIAL_COLOR + "for" + END_COLOR)               
    code = code.replace("break", ESSENTIAL_COLOR + "break" + END_COLOR)             
    code = code.replace("in", ESSENTIAL_COLOR + "in" + END_COLOR)                 
    code = code.replace("not", ESSENTIAL_COLOR + "not" + END_COLOR)                    
    code = code.replace("if", ESSENTIAL_COLOR + "if" + END_COLOR)                
    code = code.replace("from", ESSENTIAL_COLOR + "from" + END_COLOR)                
    code = code.replace("import", ESSENTIAL_COLOR + "import" + END_COLOR)       
    code = code.replace("else", ESSENTIAL_COLOR + "else" + END_COLOR)                   
    code = code.replace("True", ESSENTIAL_COLOR + "True" + END_COLOR)              
    code = code.replace("False", ESSENTIAL_COLOR + "False" + END_COLOR)         
    code = code.replace("pout", FUNCTION_COLOR + "pout" + END_COLOR)               
    code = code.replace("input", FUNCTION_COLOR + "input" + END_COLOR)                     
    code = code.replace("object", FUNCTION_COLOR + "object" + END_COLOR)                    
    code = code.replace("int", FUNCTION_COLOR + "int" + END_COLOR)                     
    code = code.replace("str", FUNCTION_COLOR + "str" + END_COLOR)                      
    code = code.replace("dict", FUNCTION_COLOR + "dict" + END_COLOR)                
    code = code.replace("list", FUNCTION_COLOR + "list" + END_COLOR)                   
    code = code.replace("exec", FUNCTION_COLOR + "exec" + END_COLOR)                      
    code = code.replace("eval", FUNCTION_COLOR + "eval" + END_COLOR)                    
    code = code.replace("pr\033[94min\033[0mt", FUNCTION_COLOR + "print" + END_COLOR) 
    code = code.replace("\033[94min\033[0put", FUNCTION_COLOR + "input" + END_COLOR)     
    code = code.replace("__init__", BUILT_FUNCTION + "__init__" + END_COLOR)              
    code = code.replace("__\033[94min\033[0mit__", BUILT_FUNCTION + "__init__" + END_COLOR)
    code = code.replace("__str__", BUILT_FUNCTION + "__str__" + END_COLOR)                
    code = code.replace("__add__", BUILT_FUNCTION + "__add__" + END_COLOR)               
    code = code.replace("__repr__", BUILT_FUNCTION + "__repr__" + END_COLOR)              
    string_end = -5                                                                       
    while True:
        try:
            string_start = code.index('"', string_end + 5)                                  
            string_end = code.index('"."', string_start + 1) + 1                              
            new_sub_string = code[string_start:string_end]                                  
            new_sub_string = new_sub_string.replace(STRING_COLOR, "")                     
            new_sub_string = new_sub_string.replace(SELF_COLOR, "")                      
            new_sub_string = new_sub_string.replace(ESSENTIAL_COLOR, "")                
            new_sub_string = new_sub_string.replace(FUNCTION_COLOR, "")                     
            new_sub_string = new_sub_string.replace(END_COLOR, "")                        
            new_sub_string = new_sub_string.replace(NUMBER_COLOR, "")                     
            new_sub_string = new_sub_string.replace(BUILT_FUNCTION, "")                    
            code = code[:string_start] + STRING_COLOR + new_sub_string + END_COLOR + code[string_end:]
        except:break
    string_end = -5                                                                       
    while True:
        try:
            string_start = code.index('"."', string_end + 5)                                
            string_end = code.index('"."', string_start + 1) + 1                           
            new_sub_string = code[string_start:string_end]                           
            new_sub_string = new_sub_string.replace(STRING_COLOR, "")              
            new_sub_string = new_sub_string.replace(SELF_COLOR, "")                 
            new_sub_string = new_sub_string.replace(ESSENTIAL_COLOR, "")              
            new_sub_string = new_sub_string.replace(FUNCTION_COLOR, "")                
            new_sub_string = new_sub_string.replace(END_COLOR, "")                  
            new_sub_string = new_sub_string.replace(NUMBER_COLOR, "")                 
            new_sub_string = new_sub_string.replace(BUILT_FUNCTION, "")              
            code = code[:string_start] + STRING_COLOR + new_sub_string + END_COLOR + code[string_end:]
        except:break
    print(code)

def sa(i,le,vas):
    if i=="+":n=le[-2]+le[-1];del le[-2:];le.append(n)
    elif i=="-":n=le[-2]-le[-1];del le[-2:];le.append(n)
    elif i=="*":n=le[-2]*le[-1];del le[-2:];le.append(n)
    elif i=="/":n=le[-2]/le[-1];del le[-2:];le.append(n)
    elif i=="%":n=le[-2]%le[-1];del le[-2:];le.append(n)
    elif i=="^":n=le[-2]**le[-1];del le[-2:];le.append(n)
    elif i=="|":n=(le[-2] or le[-1]);del le[-2:];le.append(n)
    elif i=="$":n=(le[-2] and le[-1]);del le[-2:];le.append(n)
    elif i==">":n=le[-2]>le[-1];del le[-2:];le.append(n)
    elif i=="<":n=le[-2]<le[-1];del le[-2:];le.append(n)
    elif i=="==":n=le[-2]==le[-1];del le[-2:];le.append(n)
    elif type(i)==str and i[-1]=="!":
        if i[0:-1] in vas:
            if type(vas[i[0:-1]])==str:
                if '.' in vas[i[0:-1]] or 'e' in vas[i[0:-1]]:
                    try:le.append(math.factorial(float(vas[i[0:-1]])))
                    except:le.append(math.factorial(vas[i[0:-1]]))
                else:
                    try:le.append(math.factorial(int(vas[i[0:-1]])))
                    except:le.append(math.factorial(vas[i[0:-1]]))
            else:le.append(math.factorial(vas[i[0:-1]]))
        else:
            if type(i[0:-1])==str:
                if '.' in i[0:-1] or 'e' in i[0:-1]:
                    try:le.append(math.factorial(float(i[0:-1])))
                    except:le.append(math.factorial(i[0:-1]))
                else:
                    try:le.append(math.factorial(int(i[0:-1])))
                    except:le.append(math.factorial(i[0:-1]))
            else:le.append(math.factorial(i[0:-1]))
    else:
        if i in vas:
            if type(vas[i])==str:
                if '.' in vas[i] or 'e' in vas[i]:
                    try:le.append(float(vas[i]))
                    except:le.append(vas[i])
                else:
                    try:le.append(int(vas[i]))
                    except:le.append(vas[i])
            else:le.append(vas[i])
        else:
            if type(i)==str:
                if '.' in i or 'e' in i:
                    try:le.append(float(i))
                    except:le.append(i)
                else:
                    try:le.append(int(i))
                    except:le.append(i)
            else:le.append(i)
    return le

def lam(la)->int:
    vas,als = {},{"#":0,"+":3,"-":3,"*":4,"/":4,"%":4,"^":5,"|":1,"$":1,">":2,"<":2,"==":2,"(":0,")":0}
    la=la.replace(" ","").replace("+"," + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").replace("%"," % ").replace("^"," ^ ").replace("|"," | ").replace("$"," $ ").replace("<"," < ").replace(">"," > ").replace("=="," == ").replace("(","( ").replace(")"," )").split(" ")
    l=["#"];le = []
    for i in la:
        if i in als:
            m=als[i]
            if m>als[l[-1]] or i=="(":l.append(i)
            elif i==")":
                while l[-1]!='(':le=sa(l.pop(-1),le,vas)
                l.pop(-1)
            else:
                while m<=als[l[-1]]:le=sa(l.pop(-1),le,vas)
                l.append(i)
        else:
            if i in vas:
                try:le=sa(int(vas[i]),le,vas)
                except:le=sa(vas[i],le,vas)
            else:
                try:le=sa(int(i),le,vas)
                except:le=sa(i,le,vas)
    while l[-1]!='#':le=sa(l.pop(-1),le,vas)
    return le[0]

class Error:
    def output_error1(self,line):
        try:raise ValueError(f"Output Error:Output in the wrong place in line {line}")
        except ValueError as e:print(repr(e))
    def output_error2(self,line):
        try:raise ValueError(f"Output Error:var has not defined in line {line}")
        except ValueError as e:print(repr(e))
    def var_error1(self,line):
        try:raise ValueError(f"Var Error:value name or content has not been found in line {line}")
        except ValueError as e:print(repr(e))
    def var_error2(self,line):
        try:raise ValueError(f"Var Error:bad var sentence in line {line}")
        except ValueError as e:print(repr(e))
    def entry_error1(self,line):
        try:raise ValueError(f"Entry Error:bad entry sentence in line {line}")
        except ValueError as e:print(repr(e))
    def note_error1(self,line):
        try:raise ValueError(f"Note Error:// is in the wrong place {line}")
        except ValueError as e:print(repr(e))
_error = Error()     

class F_plus_plus_parse:
    def __init__(self):self.var_name = [];self.var_value = []
    def output(self,code,a):
        code = code.split("->")
        if code[0] == "fout":
            del code[0]
            for i in range(len(code)):
                if code[i][0] == "\"":print(code[i][1:-1])
                else:
                    if code[i] in self.var_name:print(self.var_value[self.var_name.index(code[i])])
                    else:
                        try:print(lam(code[i]))
                        except:_error.output_error2(a)
        else:_error.output_error1(a)
    def var(self,code,i):
        code = code.split(" ")
        try:del code[0],code[1]
        except:_error.var_error1(i)
        try:
            if code[0] in self.var_name:
                number = self.var_name.index(code[0])
                del self.var_name[number]
                del self.var_value[number]
            self.var_name.append(code[0])
            try:self.var_value.append(lam(code[1]))
            except:self.var_value.append(code[1])
        except:_error.var_error2(i)
    def entry(self,code,i):
        code = code.split(" ")
        if len(code) == 3:
            if code[2][-1] == "\"":a = input(code[2][7:-1])
            else:
                code2 = code[2].split("<-")
                if code2[1] in self.var_name:a = input(self.var_value[self.var_name.index(code2[1])])
                else:
                    try:a = input(lam(code2[1]))
                    except:_error.entry_error1(i)
            if code[0] in self.var_name:
                number = self.var_name.index(code[0])
                del self.var_name[number]
                del self.var_value[number]
            self.var_name.append(code[0])
            self.var_value.append(a)
        elif len(code) == 1:
            if code[0][-1] == "\"":input(code[0][7:-1])
            else:
                code = code[0].split(":")
                try:input(lam(code[1]))
                except:_error.entry_error1(i)
        else:_error.entry_error1(i)
    def note(self,code,i):
        if code[0:2] != "//":_error.note_error1(i)
_F_plus_plus_parse = F_plus_plus_parse()

class F_plus_plus:
    def __init__(self,code_list):self.code = code_list
    def run_code(self):
        self.code = "".join(code_list).split(";")
        for i in range(len(self.code)):
            if "fout" in self.code[i]:_F_plus_plus_parse.output(self.code[i],i)
            elif "var" in self.code[i]:_F_plus_plus_parse.var(self.code[i],i)
            elif "entry" in self.code[i]:_F_plus_plus_parse.entry(self.code[i],i)
            elif "//" in self.code[i]:_F_plus_plus_parse.note(self.code[i],i)
            
print("""欢迎使用F++ Stable 200(Rebuild重构版)
输入/run以运行，语言标准即将上线，感谢诸位对我的支持！""")
answer_string = "" 
code_list = []
while answer_string != "/run":
    answer_string = input(">>")
    code_list.append(answer_string)
code_list.pop()

print("\033[32m编译完成\033[m")
_F_plus_plus = F_plus_plus(code_list);_F_plus_plus.run_code()
print("\033[33m编译结束")
