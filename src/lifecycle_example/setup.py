from setuptools import find_packages, setup

package_name = 'lifecycle_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lijovijayan',
    maintainer_email='lijovijayan00@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lifecycle_example = lifecycle_example.example_node:main',
            'lifecycle_manager = lifecycle_example.lifecycle_manager_node:main',
        ],
    },
)
