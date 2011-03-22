from distutils.core import setup

setup(
    packages=['app'],
    package_data={  
        'app': ['static/favicon.ico','static/robots.txt','static/*/*','views/*.html','views/*/*.html'],
    },
    scripts=['deploy'],
)

