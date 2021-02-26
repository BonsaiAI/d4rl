from distutils.core import setup
from setuptools import find_packages

setup(
    name='d4rl',
    version='1.1.0.dev0',
    install_requires=['gym', 
                      'numpy', 
                      'pybullet',
                      'h5py', 
                      'termcolor', # adept_envs dependency
                      'click',  # adept_envs dependency
                      # These dependencies cannot be consumed from source 
                      # because ADO is not allowing direct
                      # links in Wheels for security reasons.
                      # For MJRL we created custom Wheels as well.
                      'dm_control', # @ git+git://github.com/deepmind/dm_control@master#egg=dm_control
                      'mjrl', # @ git+git://github.com/aravindr93/mjrl@master#egg=mjrl'
                      ],
    extras_require={
        "mujoco": ["mujoco_py"],
    },
    packages=find_packages(),
    package_data={'d4rl': ['locomotion/assets/*',
                           'hand_manipulation_suite/assets/*',
                           'hand_manipulation_suite/Adroit/*',
                           'hand_manipulation_suite/Adroit/gallery/*',
                           'hand_manipulation_suite/Adroit/resources/*',
                           'hand_manipulation_suite/Adroit/resources/meshes/*',
                           'hand_manipulation_suite/Adroit/resources/textures/*',
                           ]},
    include_package_data=True,
)
