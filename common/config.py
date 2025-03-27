import os

from airtest.core.helper import log


class __ConfigManage(object):
    __project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    log(f"---------当前项目根目录为：{__project_path}-----------")

    TEST_DIR_NAME = "test"

    @classmethod
    def get_project_dir(cls):
        """
        返回项目的根目录，绝对路径
        :return:
        """
        return cls.__project_path

    @classmethod
    def get_tests_dir(cls):
        return os.path.join(cls.get_project_dir(), cls.TEST_DIR_NAME)

    @classmethod
    def get_images_dir(cls):
        return os.path.join(cls.get_project_dir(), cls.TEST_DIR_NAME, 'images')


config = __ConfigManage

if __name__ == '__main__':
    print(config.get_project_dir())
