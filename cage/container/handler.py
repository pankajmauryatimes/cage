import subprocess
import os
from docker import Client


class ContainerHandler:
    def __init__(self, name, python_version):
        self.__name = name
        self.__python_version = python_version
        self.__client = Client(base_url='unix://var/run/docker.sock')

    @staticmethod
    def get_python_versions():
        # TODO: Download in a better place. Current dir does not seem like a good idea
        if os.path.exists("python"):
            subprocess.check_call(["git", "-C", "python", "pull"])
        else:
            subprocess.check_call(["git", "clone", "https://github.com/docker-library/python"])

    def create_image(self):
        dockerfile_path = os.path.join("python", self.__python_version, "onbuild")
        response = self.__client.build(path=dockerfile_path, tag="cage/python" + self.__python_version)
        res = [line for line in response]
        print(res)