
# setup.py
from setuptools import setup, find_packages

setup(
    name="space-station-detection",
    version="2.0.0",
    description="AI-Powered Space Station Object Detection System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Team Name",
    author_email="team@yourproject.com",
    packages=find_packages(),
    install_requires=[
        "ultralytics>=8.0.0",
        "opencv-python>=4.8.0",
        "Pillow>=10.0.0",
        "matplotlib>=3.7.0",
        "numpy>=1.24.0",
        "torch>=2.0.0",
        "torchvision>=0.15.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={
        "console_scripts": [
            "space-station-detection=space_station_app:main",
        ],
    },
)
