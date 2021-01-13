# time模块目前只支持到2038年前。如果需要处理范围之外的日期，请使用datetime模块
import time


def format_time(lt_time):
    print('{0}年{1}月{2}日 {3}时{4}分{5}秒'.format(lt_time.tm_year, lt_time.tm_mon, lt_time.tm_mday, lt_time.tm_hour,
                                             lt_time.tm_min, lt_time.tm_sec))
    return '{0}年{1}月{2}日 {3}时{4}分{5}秒'.format(lt_time.tm_year, lt_time.tm_mon, lt_time.tm_mday, lt_time.tm_hour,
                                              lt_time.tm_min, lt_time.tm_sec)


# 1、获取当前时间戳，单位：s
print(time.time())
lt = time.localtime()
# 2、时间格式化,返回格式化字符串表示的当地时间。
# 把一个struct_time（如time.localtime()和time.gmtime()的返回值）转化为格式化的时间字符串，显示的格式由参数format决定。
# 如果未指定t，默认传入time.localtime()
format_time(lt)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
# 3、将格式化时间字符串转化成结构化时间。该方法是time.strftime()方法的逆操作。
# time.strptime()方法根据指定的格式把一个时间字符串解析为时间元组。要注意的是，你提供的字符串要和format参数的格式一一对应，
# 如果string中日期间使用“-”分隔，format中也必须使用“-”分隔，时间中使用冒号“:”分隔，后面也必须使用冒号分隔，否则会报格式不匹配的错误。
# 并且值也要在合法的区间范围内，千万不要整出14个月来
print(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'))
print(time.strptime(format_time(time.gmtime()), '%Y年%m月%d日 %H时%M分%S秒'))
# 4、目前我们所处的时间为东八区，相对于UTC时区，多8个小时。将一个时间戳转换为UTC时区的结构化时间。可选参数secs的默认值为time.time()。
format_time(time.gmtime())
# 对时间进行秒数操作
format_time(time.gmtime(time.time() - 1000))
# 5、本时区时间操作
format_time(time.localtime())
format_time(time.localtime(time.time() - 1000))
# 6、把一个时间戳转化为本地时间的格式化字符串。默认使用time.time()作为参数。
print(time.ctime())
print(time.ctime(1282522384))
print(time.ctime(time.time() - 1000))
# 7、把一个结构化时间转换为Sun Aug 23 14:31:59 2017这种形式的格式化时间字符串。默认将time.localtime()作为参数
print(time.asctime())
print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime()))

# 8、将一个结构化时间转化为时间戳。time.mktime()执行与gmtime(),localtime()相反的操作，
# 它接收struct_time对象作为参数,返回用秒数表示时间的浮点数
print(time.mktime(time.localtime()))
print(time.mktime(time.gmtime()))
