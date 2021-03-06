# coding=utf-8

import psutil

# CPU 信息
cpu_log = psutil.cpu_count() # CPU 的逻辑个数
cpu_phy = psutil.cpu_count(logical=False) # CPU 的物理个数
print(cpu_log)
print(cpu_phy)

# 内存信息
mem = psutil.virtual_memory()
print(mem.total)
print(mem.used)
print(mem.free)
print(mem.percent)
swap_mem = psutil.swap_memory()
print(swap_mem.total)
print(swap_mem.free)

# 磁盘信息
disk_info = psutil.disk_partitions()
for item in disk_info:
    print(item.device)
    print(item.mountpoint)
    print(item.fstype)

# 网络信息	
psutil.net_io_counters(pernic=True)

# 用户信息
psutil.users() # 返回当前登录用户的信息

# 启动信息
psutil.boot_time() # 获取开机时间，返回 Linux 时间戳
datetime.datetime.fromtimestammp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
