from os import environ
from os.path import exists
from sh import Command

pip3 = Command(environ.get("PIP3"))
ps_support = environ.get("PS_SUPPORT")

kivyschool_simple = "https://pypi.anaconda.org/kivyschool/simple"


sdl3_frameworks = f"{ps_support}/sdl3_frameworks"

# Install SDL3 frameworks into /Users/Shared/psproject/support/sdl3_frameworks
if not exists(sdl3_frameworks):
    pip3(
        "install",
        "kivy_sdl3_angle", 
        "--extra-index-url", kivyschool_simple,
        "-t", sdl3_frameworks
    )