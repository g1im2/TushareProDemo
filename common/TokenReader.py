# -*- encoding:utf-8 -*-


# 本方法仅用来获取保存在本地 token, 确保账号的私密性
def get():
    f = open('my.token', mode='r')
    token = f.readline()
    f.close()
    return token


if __name__ == '__main__':
    print(get())
