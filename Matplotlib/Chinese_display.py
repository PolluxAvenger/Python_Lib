import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

x = range(10)
plt.plot(x)
# 我们也可以使用绝对路径指定字体位置，而 Linux 系统可以通过 fc-list 命令查看字体位置
plt.title("中文", fontproperties=FontProperties(fname="msyh.ttc"), fontsize=14)
plt.show()
