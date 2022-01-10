import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# taken from https://github.com/CEA-COSMIC/ModOpt/blob/master/setup.py
with open('requirements.txt') as open_file:
    install_requires = open_file.read()

import jz_hydra_submitit_launcher

setuptools.setup(
    name="jz-hydra-submitit-launcher",
    version=jz_hydra_submitit_launcher.__version__,
    author=jz_hydra_submitit_launcher.__author__,
    author_email=jz_hydra_submitit_launcher.__author_email__,
    description=jz_hydra_submitit_launcher.__docs__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    homepage=jz_hydra_submitit_launcher.__homepage__,
    url="https://github.com/zaccharieramzi/jz-hydra-submitit-launcher",
    license=jz_hydra_submitit_launcher.__license__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    python_requires='>=3.6',
    include_package_data=True,
    keywords=['hydra', 'submitit', 'jean-zay'],
    scripts=['jz_hydra_submitit_launcher/bin/hydra-submitit-launch'],
)
