#coding:utf-8
#提取跟缓存相关的信息
import log_line_format2

class Log_Cache(log_line_format2.WebLogFormat):
    def __init__(self, filename):
        log_line_format2.WebLogFormat.__init__(self, filename)
    
    #提取缓存命中率
    def Hit_Cache(self):
        #path_dict={}
        LogLine = 0
        WebCache = 0
        #cache1 = self.WebFile
        cache = open(self.WebFile)
        #with self.WebFile as lx:
        for line in cache:
            LogLine += 1
            m = self.LogFormat.search(line)
            if  m.groupdict()['status'] == '304':
                WebCache += 1
                #m = self.LogFormat.search(line)
                #path_dict[m.group('path')] = path_dict.get(m.group('path'), 0) + 1
                #yield line
        cache.close() 
        print LogLine
        print WebCache
        print 'Cache hit rate is:%0.2f' %float(100*WebCache/LogLine)
        
        #path_dict=sorted(path_dict.iteritems(), key=lambda c:c[1], reverse=True)
        #print path_dict
    
    #提取命中路径，和总共命中次数    
    def Hit_Path(self):
        path_dict={}
        log = open(self.WebFile)
        for lline in log:
            #print line
            m = self.LogFormat.search(lline)
            
            if  m.groupdict()['status'] == '304':
                #print line
                path_dict[m.group('path')] = path_dict.get(m.group('path'), 0) + 1
        log.close()       
        path_dict=sorted(path_dict.iteritems(), key=lambda c:c[1], reverse=True) 
        for path, record in path_dict:
          print path + ':' + str(record)  
    
    #缓存详细信息全部统计
    def Cache_Total(self):
        path_dict={}
        LogLine = 0
        WebCache = 0
        cache_path = 0
        hit_record = 0
        with open(self.WebFile) as f:
            for line in f:
                LogLine += 1
                m = self.LogFormat.search(line)
                if  m.groupdict()['status'] == '304':
                    WebCache += 1
                    path_dict[m.group('path')] = path_dict.get(m.group('path'), 0) + 1
        path_dict=sorted(path_dict.iteritems(), key=lambda c:c[1], reverse=True)
        print 'log total record is %s'  %LogLine
        print 'Cache total record is %s' %WebCache
        print 'Cache hit rate is:%0.2f' %float(100*WebCache/LogLine)
        print '-' * 15 + 'path' + '-' * 15 + '\t\t' +  '-' * 15 + 'record' + '-' * 15
        for path, record in path_dict:
            cache_path += 1
            hit_record += record
            print '%30s\t:\t%s'%(path, record)
            
        print '%30s\t:\t%s'%(cache_path, hit_record)
        
        
        
        
        
x = Log_Cache(r'G:\python_script\YW\WebLog\access_20130508.log')
#x.Hit_Path()
#x.Hit_Cache()
#s = Log_Cache(r'G:\python_script\YW\WebLog\access_20130508.log')
#x.Hit_Path()
x.Cache_Total()
