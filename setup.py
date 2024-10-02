from setuptools import setup, find_packages

setup(
    name='CommandTracker',  # Nombre del paquete
    version='0.1.4a',  # Versión inicial
    packages=find_packages(),  # Encuentra todos los paquetes en tu directorio
    install_requires=[
        'psutil',  # Dependencia para monitorear recursos
        'plotext'
    ],
    entry_points={
        'console_scripts': [
            'ctracker=CommandTracker.cli:main',  # Crea el comando 'ctracker'
        ],
    },
    author='Erick Costa',
    author_email='erickhcosta98@gmail.com',
    description='Paquete para ejecutar comandos y monitorear uso de CPU y memoria',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # Enlace al repositorio del proyecto
    url='https://github.com/ErickCosta98/CommandTracker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versión mínima de Python
)
