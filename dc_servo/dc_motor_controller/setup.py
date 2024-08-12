import os  
from glob import glob
from setuptools import setup

package_name = 'dc_motor_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
    (os.path.join('share', package_name), glob('launch/*.launch.py')),
    (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'launch.[pxy][yma]'))),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu200422',
    maintainer_email='ubuntu200422@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publisher_node = dc_motor_controller.publisher_node:main",
            "controller_node = dc_motor_controller.controller_node:main",
            "motor_state_node = dc_motor_controller.motor_state_node:main",
            "data_logger_node = dc_motor_controller.data_logger_node:main"
        ],
    },
)
