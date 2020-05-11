import setuptools

setuptools.setup(
    name='rbg2player',
    version='0.1.2',
    py_modules=['rbg2player'],
    install_requires=['click', 'validators', 'requests'],
    entry_points='''
        [console_scripts]
        rbg2player=rbg2player:main
    ''',
    python_requires='>=3',
)
