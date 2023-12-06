# HHL

Research Paper and Implementation of the HHL Algorithm for my Quantum Computation course.

[The notebook that implements the algorithm.](./HHL.ipynb)

## Setup

Requires 
- Python 3.8
- Mac/Linux (Not guaranteed on windows)

Create a virtual environment

```commandline
python -m venv env
```

Activate the environment (Linux/Mac)
```commandline
. ./env/bin/activate
```

Install the dependencies
```commandline
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Run the notebook
```commandline
jupyter lab
```

## Alternate Setup

This setup should work on windows, mac and linux.

If you're having trouble installing dependencies, 
there is a docker compose script for this. You will need docker
and docker-compose for this section

```commandline
docker compose build
docker compose up
```

The notebook will be available at [0.0.0.0:8000](0.0.0.0:8000). You can copy or click the link in the terminal output.