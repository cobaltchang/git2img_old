#!/usr/bin/env python3

import configparser
import logging
import os.path
from abc import ABCMeta, abstractmethod
from pathlib import Path

import libraries

logger = logging.getLogger(__name__)


class GitToImage(metaclass=ABCMeta):
    """

    """
    dir_ = '/tmp/stamp'

    __stamp_files = {
        'prepare': 'prepared.stamp',
        'configure': 'configured.stamp',
        'compile': 'compiled.stamp',
        'install': 'installed.stamp',
    }

    def __init__(self, entry):
        self.dir_ += '/' + entry
        os.makedirs(self.dir_, mode=0o777, exist_ok=True)

    @abstractmethod
    def _prepare(self):
        pass

    @abstractmethod
    def _configure(self):
        pass

    @abstractmethod
    def _compile(self):
        pass

    @abstractmethod
    def _install(self):
        pass

    def run(self):
        if not self.__is_stamp_existent('prepare'):
            logger.info("Preparing...")
            if self._prepare():
                self.__touch_stamp('prepare')
        if not self.__is_stamp_existent('configure'):
            logger.info("Configuring...")
            if self._configure():
                self.__touch_stamp('configure')
        if not self.__is_stamp_existent('compile'):
            logger.info("Compiling...")
            if self._compile():
                self.__touch_stamp('compile')
        if not self.__is_stamp_existent('install'):
            logger.info("Install...")
            if self._install():
                self.__touch_stamp('install')

    def clean(self):
        for stamp_file in self.__stamp_files.values():
            file_ = self.dir_ + '/' + stamp_file
            if os.path.isfile(file_):
                os.remove(file_)

    def __is_stamp_existent(self, stamp):
        return os.path.isfile(self.dir_ + '/' + self.__stamp_files[stamp])

    def __touch_stamp(self, stamp):
        Path(self.dir_ + '/' + self.__stamp_files[stamp]).touch()


def init_env(makelist='makelist.ini.sample', config='config.ini.sample'):
        """

        """
        assert os.path.isfile(makelist), FileNotFoundError(
            '[Errno 2] No such file: ' + makelist)
        assert os.path.isfile(config), FileNotFoundError(
            '[Errno 2] No such file: ' + config)

        config = configparser.ConfigParser()
        config.read(makelist)
        for entry in config.sections():
            builder_name = config[entry]['builder']
            logger.info("Job: {}, builder: {}".format(entry, builder_name))

            builder = libraries.class_for_name('builders', builder_name)
            job = builder(entry)
            job.run()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    init_env(makelist='makelist.ini.sample', config='config.ini.sample')
