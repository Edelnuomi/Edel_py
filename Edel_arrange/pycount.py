import os
# encoding:utf-8

## 统计指定目录或子目录下的文件名与文件行数

for root,dirs,files in os.walk(r"C:\Users\lddc\Desktop\出账后\每月-合作商对账数据生成"): #遍历指定路径下所有子目录和文件
    
    zcount = 0  #用于统计所有文件总行数
    print("访问的路径root：",root)  #访问的路径
    print('路径下的子目录dirs:',dirs)   #路径下的子目录  
    print('路径下的文件名与子目录下的文件名 dirs:',files)  #路径下的文件名与子目录下的文件名

    for file in files:
        filepath = os.path.join(root,file)  #生成文件的绝对路径
        #print("文件全名filepath："+filepath)
        filename,format = os.path.splitext(filepath) #切割文件名与后缀名
        #print("文件名filename：",format)
        #print("文件后缀format：",filename)

        if format == ".txt":                #对txt文本文件做数据量统计
            fp = open(filepath,'r',encoding = 'utf-8')
            count = 0  #用于统计所有文件总行数
            for i in fp:                    #遍历当前.txt文件对象的每一行，统计+1
                #print(i)
                count += 1
            fp.close()                      #关闭打开的文件
            print("文件《%s》已完成统计，累计行数为：%s行" %(file,count))
            zcount+=count
            print("所有文件统计段落数为：%s行" %zcount)  #打印全部统计结果



