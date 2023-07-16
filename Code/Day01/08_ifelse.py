
"""
用户身份验证
"""
username = input("请输入名称：")
password = input("请输入密码：")
if username == 'admin' and password == '12345':
    print("校验通过")
else:
    print("校验失败")