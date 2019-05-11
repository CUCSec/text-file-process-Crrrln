with open('log_files/201811123006.log',encoding='utf8')as f:
    count=0
    for line in f:
        if '201811123006' in line:
            count=count+1  
print(count)
