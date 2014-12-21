#-*-coding:utf-8-*-


fileData = open('20140707_2216_ussr-IS-3_60_asia_miao.wotreplay','rb')
data_string = fileData.read(128)
readString1 = unicode(data_string,"utf-16")
print readString1