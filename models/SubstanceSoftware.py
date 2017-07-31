import threading
import subprocess


"""
This models create all substance software class, you can easily use this 
class to call a software, this number version, this path or many option.
"""


class SubstancePainterLaunch(threading.Thread):
    """Substance Painter Thread, any argument to launch an new instance
    project, check the Painter Version and other action.

    You can find all Substance Painter Command Lines on Allegorithmic
    documentation.

    https://docs.allegorithmic.com/documentation/display/SPDOC/Command+Lines"""
    def __init__(self, path_painter, path_project, name_project):
        threading.Thread.__init__(self)
        self.path_painter = path_painter
        self.path_project = path_project
        self.name_project = name_project

    def run(self):
        # All Command
        # --help
        # -version
        # --mesh <meshPath>
        # --mesh-map
        # -export-path

        if self.path_project == "":
            subprocess.call([self.path_painter,
                             '--mesh',
                             self.name_project,
                             ])

        else:
            subprocess.call([self.path_painter,
                             '--mesh',
                             self.name_project,
                             self.path_project,
                             ])
