from os import environ
from sh import Command
import json

class CodePriority:
    IMPORTS = 0
    POST_IMPORTS = 1
    PRE_MAIN = 2
    MAIN = 3
    POST_MAIN = 4
    ON_EXIT = 5

modules = environ.get("WRAPPER_MODULES").split(",")
platform = environ.get("PLATFORM")
main_swift_path = environ.get("MAIN_SWIFT_PATH")

pre_main_swift = """
    KivyLauncher.pyswiftImports = [
        {modules}
    ]
    """

main_swift = """
let exit_status = KivyLauncher.SDLmain()
"""

on_exit = """
exit(exit_status)
"""

main_swift_data = [
    {
        "code": pre_main_swift.format(modules=",\n\t".join(modules)),
        "priority": CodePriority.POST_IMPORTS
    },
    {
        "code": main_swift,
        "priority": CodePriority.MAIN
    },
    {
        "code": on_exit,
        "priority": CodePriority.ON_EXIT
    }
]


with open(main_swift_path, "w") as f:
    json.dump(main_swift_data, f)
