import tkinter as tk
from tkinter import simpledialog
from DrissionPage import ChromiumPage
import datetime

# 创建一个Tkinter窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 使用simpledialog输入日期，并设置默认值为"2024-10-21 20:00:00.00000000"
kill_time = simpledialog.askstring("输入秒杀时间", "请输入秒杀时间（默认值：2024-10-21 20:00:00.00000000）:", initialvalue="2024-10-21 20:00:00.00000000")

# 创建对象
page = ChromiumPage()

# 打开淘宝网页
page.get("https://www.taobao.com")
# 点击购物车
page.ele('x://*[@id="J_MiniCart"]/div[1]/a/span[2]').click()
# 等待登录完成，直到购物车全选按钮出现，超时时间设置为1分钟
page.wait.ele_displayed('x://*[@id="cart-operation-fixed"]/label/span[1]/input', timeout=60)
# 点击购物车全选按钮
page.ele('x://*[@id="cart-operation-fixed"]/label/span[1]/input').click()

while True:
    # 获取当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now)  # 打印当前时间测试
    # 判断当前时间是否到达了秒杀时间
    if now > kill_time:
        # 点击结算按钮
        page.ele('x://*[@id="settlementContainer_1"]/div[4]/div/div[2]').click()
        # 下单商品
        page.ele('x://*[@id="submitOrder"]/div/div[2]/div').click()
        # 输入支付密码(不建议启用)
        # page.ele('x://*[@id="payPassword_rsainput"]').input("123456")
        # 确定
        # page.ele('x://*[@id="validateButton"]').click()
        break
    # 判断当前秒数是不是0，实现间隔一分钟刷新页面，防止掉登录
    if datetime.datetime.now().second == 0:
        page.refresh()  # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束
        # 再次全选购物车
        page.ele('x://*[@id="cart-operation-fixed"]/label/span[1]/input').click()

# 测试时的程序暂停
input()
