from distutils.core import setup

setup(
	author='Siddharth sharma',
    author_email='siddharth.sharma.3103@gmail.com',
    name='python-scapy',
    version='0.1dev',
    packages=['pyscapy',],
    license='Open source',
    long_description=open('README.txt').read(),
    install_requires=[
        "scapy >= 1.1",
    ]
)
