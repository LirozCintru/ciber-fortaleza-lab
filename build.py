from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "BioGuard_Inventory"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("coverage_break_build", True)
    project.set_property("coverage_threshold_warn", 100)
    project.set_property("flake8_break_build", True)
    project.set_property("flake8_verbose_output", True)
