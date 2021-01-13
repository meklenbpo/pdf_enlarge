"""
Packaging metadata for PDF Enlarge.
"""

from setuptools import setup, find_packages


with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='pdf_enlarge',
    version='0.0.1',
    description='Scale PDF pages 2x',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/meklenbpo/pdf_enlarge',
    author='Yury Kalbaska',
    author_email='meklenbpo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='pdf scale',
    packages=find_packages(),
    py_modules=['pdf_enlarge'],
    install_requires=[],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'pdf_enlarge=pdf_enlarge:main'
        ]
    }
)
