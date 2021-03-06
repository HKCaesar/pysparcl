import numpy
from setuptools import Extension
from setuptools import setup


ext_modules = [
    Extension(
        'pysparcl.internal',
        sources=['pysparcl/internal.pyx'],
        include_dirs=[numpy.get_include()]
    )
]

setup(
    name='pysparcl',
    version='1.3.2',
    author='tsurumeso',
    license='GPL-2.0 License',
    packages=['pysparcl'],
    ext_modules=ext_modules,
)
