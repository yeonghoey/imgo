import ast
import re
from setuptools import find_packages, setup


def extract_version(content):
    m = re.search(r'__version__\s+=\s+(.*)', content)
    s = m.group(1)
    return str(ast.literal_eval(s))


with open('imgo/__init__.py', 'rb') as f:
    content = f.read().decode('utf-8')
    version = extract_version(content)


setup(
    name='imgo',
    version=version,
    description='Automation powered by OCR',
    keywords='tesseract ocr cli',
    url='https://github.com/yeonghoey/imgo',

    author='Yeongho Kim',
    author_email='yeonghoey@gmail.com',
    license='MIT',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'imgo=imgo.__main__:cli',
        ]
    },

    install_requires=[
        'pytesseract',
        'pillow',
        'click',
        'pyperclip',
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
