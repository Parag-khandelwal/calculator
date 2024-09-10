from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    description="A simple calculator project in Python",
    author="Parag khandelwal",
        author_email='your.email@example.com',
    url='https://github.com/Parag-khandelwal/calculator',  
    packages=find_packages(where="src"),    
    package_dir={'': 'src'},                
    install_requires=[],                    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",   # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
)