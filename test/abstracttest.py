# coding=UTF-8
import abc


class Allfile(object):
    __metaclass__ = abc.ABCMeta
    all_type = 'file'

    # 定义抽象方法，无需实现功能
    @abc.abstractmethod
    def read(self):
        # 子类必须定义读功能
        pass

    # 定义抽象方法，无需实现功能
    @abc.abstractmethod
    def write(self):
        # 子类必须定义写功能
        pass


# 子类继承抽象类，但是必须定义read和write方法
class Txt(Allfile):
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')


wenbenwenjian = Txt()
wenbenwenjian.write()
