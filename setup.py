from setuptools import find_packages
from distutils.core import setup

setup(
    name="go2w_rl",
    version="1.0.0",
    author="kai",
    license="MIT License",
    packages=find_packages(),
    description="Isaac Gym environments for Go2w_RL Task",
    install_requires=[
        "isaacgym",
        "rsl_rl",
        "matplotlib",
        "tensorboard",
        "numpy==1.22.0",
        'mujoco==3.2.3',
    ],
)