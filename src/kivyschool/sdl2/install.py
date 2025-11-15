from os import environ
from os.path import exists
from sh import Command

pip3 = Command(environ.get("PIP3"))
ps_support = environ.get("PS_SUPPORT")

kivyschool_simple = "https://pypi.anaconda.org/kivyschool/simple"


sdl2_frameworks = f"{ps_support}/sdl2_frameworks"

# Install SDL2 frameworks into /Users/Shared/psproject/support/sdl2_frameworks
if not exists(sdl2_frameworks):
    pip3(
        "install",
        "kivy_sdl2", 
        "--extra-index-url", kivyschool_simple,
        "-t", sdl2_frameworks
    )