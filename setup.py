try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='scikit-optimize',
      version='0.3',
      description='Sequential model-based optimization toolbox.',
      long_description=open('README.rst').read(),
      url='https://scikit-optimize.github.io/',
      license='BSD',
      author='The scikit-optimize contributors',
      packages=['skopt', 'skopt.learning', 'skopt.optimizer', 'skopt.space', 'skopt.wrappers',
                'skopt.learning.gaussian_process'],
      install_requires=["numpy", "scipy", "scikit-learn>=0.18",
                        "scikit-garden", "matplotlib"]
      )
