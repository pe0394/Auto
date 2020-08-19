import re
def getsession(data, LB='<session>', RB='</session>'):
    rule = LB + r"(.*?)" + RB       #取LB 与 RB之间的所有的值，并且不转义
    session = re.findall(rule, data)    #re中findall方法中正则表达式
    #print(session)
    return session
