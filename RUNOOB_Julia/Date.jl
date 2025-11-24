import Dates
#=
# 日期时间格式说明（已修正）：
# Y 表示年，例如：yyyy => 1984，yy => 84
# m 表示月，例如：m => 7 或 07
# u 表示月份简写名称，例如：Jun
# U 表示月份完整名称，例如：January
# e 表示简写星期几，例如：Mon
# E 表示完整星期几，例如：Monday
# d 表示日，例如：1 或 01
# H 表示小时，例如：HH => 00
# M 表示分钟，例如：MM => 00
# S 表示秒，例如：S => 00
# s 表示毫秒，例如：.000
=#
# 创建一个日期对象
date1 = Dates.Date(2024, 6, 15)
println("创建的日期对象: ", date1)
# 获取当前日期
current_date = Dates.today()
println("当前日期: ", current_date)
# 获取当前时间
current_time = Dates.now()
println("当前时间: ", current_time)

# 日期运算
date2 = date1 + Dates.Day(10)
println("日期加10天: ", date2)

# 计算日期差
date_diff = date2 - date1
println("日期差 (天数): ", Dates.value(date_diff), " 天")
# 使用不同的时间单位进行日期运算
date3 = Dates.canonicalize(date2 - date1)
println("日期加2个月5天: ", date3)
# 格式化日期输出
formatted_date = Dates.format(date1, "yyyy-mm-dd")
println("格式化日期: ", formatted_date)
