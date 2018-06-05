from setuptools import setup

setup(name='pgms',
      version='0.1',
      description='A probabilisitc graphical model library',
      author='blake wulfe',
      author_email='blake.w.wulfe@gmail.com',
      license='MIT',
      packages=['pgms'],
      zip_safe=False,
      install_requires=[
        'numpy',
      ])