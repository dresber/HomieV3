import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='Homie3',
    version='0.2.9',
    description='Homie 3.0.1 Implementation',
    author='Michael Cumming',
    author_email='mike@4831.com',
    long_description=long_description,
    long_description_content_type="text/markdown",      
    url='https://github.com/mjcumming/Homie',
    keywords = ['HOMIE','MQTT'],  
    packages=setuptools.find_packages(exclude=("test",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],      
    install_requires=[
        'paho-mqtt>=1.3.0',
        'netifaces>=0.10.6',
    ]      
)
