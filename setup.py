from setuptools import setup, find_packages

setup(
    name='pytransfrom3d_example_zoo',
    version='0.1',
    description='Example zoo for pytransform3d',
    author='Xi Chen',
    author_email='xichen0907@gmail.com',
    packages=find_packages  (), # find all packages in the current directory
    install_requires=[
        'pytransform3d==3.6.2',
        'open3d'
    ],
    python_requires='>=3.8', # 3.8 is the tested version
)    