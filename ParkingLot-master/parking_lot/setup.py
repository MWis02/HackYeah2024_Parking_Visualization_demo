try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Parking Lot Space Detector",
    "install_requires": ["cv2", "numpy", "yml"],
    "packages": ["parking_lot"],
    "scripts": [],
    "name": "ParkingLot"
}

setup(**config)
