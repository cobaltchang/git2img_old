#!/usr/bin/env python3

import logging

from git2img import GitToImage

logger = logging.getLogger(__name__)


class PythonBuilder(GitToImage):

    def _prepare(self):
        print("Prepare for PythonBuilder")
        return True

    def _configure(self):
        print("Configure for PythonBuilder")
        return True

    def _compile(self):
        print("Compile for PythonBuilder")
        return True

    def _install(self):
        print("Install for PythonBuilder")
        return True


class CBuilder(GitToImage):

    def _prepare(self):
        print("Prepare for CBuilder")
        return True

    def _configure(self):
        print("Configure for CBuilder")
        return True

    def _compile(self):
        print("Compile for CBuilder")
        return True

    def _install(self):
        print("Install for CBuilder")
        return True
