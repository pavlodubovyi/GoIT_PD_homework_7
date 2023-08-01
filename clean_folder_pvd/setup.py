from setuptools import setup, find_namespace_packages

setup(name="clean_folder_pvd",
      version="0.0.1",
      description="Cleaner of the stuff in your JUNK folder",
      url="https://github.com/pavlodubovyi",
      author="Pavlo Dubovyi",
      author_email="pavlodubovyi@yahoo.com",
      readme="README.md",
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          ],
      license="MIT",
      packages=find_namespace_packages(),
      entry_points={"console_scripts": ["clean-folder=clean_folder_pvd.cleaner:clean"]})