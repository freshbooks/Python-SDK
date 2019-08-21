from setuptools import setup
import wepay
import os.path

long_description = (
    open("README.md").read()
    if os.path.isfile("README.md")
    else "A Python SDK for our WePay API"
)

version_str = "%s.%s.%s" % (wepay.VERSION[0], wepay.VERSION[1], wepay.VERSION[2])

setup(
    name="wepayfb",
    version=version_str,
    packages=["wepay"],
    description="A Python SDK for our WePay API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="WePay API Team",
    author_email="api@wepay.com",
    license="MIT License",
    url="https://github.com/freshbooks/WePay-Python-SDK",
    platforms=["any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=["requests>=2.7.0"],
)
