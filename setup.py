from setuptools import setup, find_packages

setup(
    name="agenttemp",
    version="1.0.0",
    author="AgentTemp",
    author_email="support@agentinbox.in",
    description="Python SDK for the AgentTemp API - temporary email inboxes for agents",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/agentinbox-in/agenttemp-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "urllib3>=1.26.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "mypy>=1.0",
            "responses>=0.22.0",
        ],
    },
    keywords="agenttemp tempmail email sdk api temporary email disposable",
    project_urls={
        "Documentation": "https://github.com/agentinbox-in/agenttemp-python#readme",
        "Source": "https://github.com/agentinbox-in/agenttemp-python",
        "Tracker": "https://github.com/agentinbox-in/agenttemp-python/issues",
    },
)
