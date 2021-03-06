# stding:utf-8
import numpy as np
import random
import PIL.Image as Image
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, data_path, start_n, end_n):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.data_path = data_path
        self.start_n = start_n
        self.end_n = end_n

    def run(self):
        num = 0
        for i in range(self.start_n, self.end_n):
            data = np.array(Image.open(self.data_path + '/' + str(i) + '.jpg'))
            if num == 0:
                train_datas = np.reshape(data, (1, 144, 180, 3))
                vali_datas = np.reshape(data, (1, 144, 180, 3))
            else:
                if num % 3 == 0:
                    vali_datas = np.concatenate((vali_datas, data.reshape((-1, 144, 180, 3))), axis=0)
                else:
                    vali_datas = np.concatenate((vali_datas, np.ones((1, 144, 180, 3), dtype=int) * 255.), axis=0)
                train_datas = np.concatenate((train_datas, data.reshape((-1, 144, 180, 3))), axis=0)
            num += 1
        self.train_datas = train_datas
        self.vali_datas = vali_datas


def read_data_train():
    nums = [20, 40, 60, 80, 100, 120, 140]
    while True:
        num = random.randint(0, 150)
        if num not in nums:
            break
    # print('./data/images/' + str(num))
    for i in range(36):
        img = Image.open('../data/image/' + str(num) + '/' + str(i) + '.jpg')
        data = np.array(img)
        if i == 0:
            train_datas = np.reshape(data, (1, 144, 180, 3))
        elif i == 9:
            vali_datas = np.reshape(data, (1, 144, 180, 3))
        else:
            if i < 9 or i >= 27:
                train_datas = np.concatenate((train_datas, data.reshape((1, 144, 180, 3))), axis=0)
            else:
                vali_datas = np.concatenate((vali_datas, data.reshape((1, 144, 180, 3))), axis=0)
    train_datas = (train_datas - 127.5) / 127.5
    vali_datas = (vali_datas - 127.5) / 127.5
    return train_datas, vali_datas


def read_data_test():
    nums = [20, 40, 60, 80, 100, 120, 140]
    num = random.choice(nums)
    print('../data/image/' + str(num))
    for i in range(36):
        img = Image.open('../data/image/' + str(num) + '/' + str(i) + '.jpg')
        data = np.array(img)
        if i == 0:
            train_datas = np.reshape(data, (1, 144, 180, 3))
        elif i == 9:
            vali_datas = np.reshape(data, (1, 144, 180, 3))
        else:
            if i < 9 or i >= 27:
                train_datas = np.concatenate((train_datas, data.reshape((1, 144, 180, 3))), axis=0)
            else:
                vali_datas = np.concatenate((vali_datas, data.reshape((1, 144, 180, 3))), axis=0)
    train_datas = (train_datas - 127.5) / 127.5
    vali_datas = (vali_datas - 127.5) / 127.5
    return train_datas, vali_datas


if __name__ == "__main__":
    read_data_test()
