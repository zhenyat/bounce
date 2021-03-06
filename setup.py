from setuptools import setup, find_packages

setup (
    name='Bounce',
    version='0.10',
    packages=find_packages(),

    # Declare your packages' dependencies here, for eg:
    install_requires=['foo>=3'],

    # Fill in these to make your Egg ready for upload to
    # PyPI
    author='zhenya',
    author_email='telyukov@gmail.com',

    #summary = 'Just another Python package for the cheese shop',
    url='dummy.com',
    license='MIT',
    long_description='''. A game with a bouncing ball and a bat. 
        The ball will fly across the screen, and the player must bounce the ball by the bat. 
        If the ball hits the bottom of the screen, the game ends.
  
        Source:  "Python for Kids" by Jason R.Briggs''',

    # could also include long_description, download_url, classifiers, etc.

  
)