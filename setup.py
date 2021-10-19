from setuptools import setup, find_packages

setup(
  name="py-prs",
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'pullreviews = py_prs:get_review_requests',
    ]
  },
  install_requires=[
    'requests',
  ],
)
