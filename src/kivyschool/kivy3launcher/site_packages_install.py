from os import environ
from sh import Command

pip3 = Command(environ.get("PIP3"))
site_path = environ.get("SITE_PACKAGES_PATH")
platform = environ.get("PLATFORM")

pyswift_simple = "https://pypi.anaconda.org/pyswift/simple"
kivyschool_simple = "https://pypi.anaconda.org/kivyschool/simple"
beeware_simple = "https://pypi.anaconda.org/beeware/simple"

pips = [
    "kivy>=3.0.0.dev0", 
    #"ios", 
    #"pyobjus"
]
for pip_name in pips:
    pip3(
        "install",
        pip_name,
        "--upgrade",
        "--disable-pip-version-check",
        f"--platform={platform}",
        "--only-binary=:all:",
        "--extra-index-url", pyswift_simple, 
        "--extra-index-url", beeware_simple,
        "--extra-index-url", kivyschool_simple,
        "--python-version=313",
        "--target", str(site_path)
)