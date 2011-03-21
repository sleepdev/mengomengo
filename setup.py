from distutils.core import setup

setup(
    packages=['app'],
    package_data={  
        'app': ['static/*/*','views/*.html','views/*/*.html'],
    },
    scripts=['deploy'],
)

