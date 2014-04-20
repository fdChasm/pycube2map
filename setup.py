import setuptools

packages = [
    'cube2map',
]

setuptools.setup(
    name="pycube2map",
    version="0.1",
    packages=packages,
    package_dir={'' : 'src'},
    install_requires=[],
    author="Chasm",
    author_email="fd.chasm@gmail.com",
    url="https://github.com/fdChasm/pycube2map",
    license="MIT",
    description="Python library for reading Sauerbraten maps.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ],
)
