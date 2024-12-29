# 🔥 CloudOps Automation at Scale 🦅

🌟 You can use [CloudOps Automation Runbooks](https://cloudops.oceansoft.io), built on Jupyter Notebooks, to quickly create SRE RunBooks for Runbook Automation and Cloud Infrastructure Management! 🌐

> [!IMPORTANT]
> **🏆 Mission**: Our mission is to simplify CloudOps Automation for DevOps and SRE teams by providing an extensive, community-driven repository of actions and runbooks that streamline day-to-day operations. 

> [!NOTE]
> **👁️ Vision**: Our vision is to be the 🥇 One-Stop Multi-Cloud Platform Engineering & Best Practices Solution for all CloudOps Automation needs, allowing DevOps and SRE teams to automate their workflows with ease, improve efficiency, and minimize toil.

[![🐍 CloudOps PyPI version](https://img.shields.io/pypi/v/cloudops)](https://pypi.org/project/cloudops/)

<div align="left">
  <a href="https://www.linkedin.com/in/nnthanh" target="blank"><img align="center" src="https://img.shields.io/badge/-nnthanh-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/nnthanh/" alt="Nhat-Thanh Nguyen" height="25" width="100" /></a>
  <a href="https://github.com/nnthanh101/" target="blank"><img align="center" src="https://img.shields.io/github/followers/nnthanh101?label=Follow&style=social&link=https://github.com/nnthanh101/" alt="Thanh Nguyen" height="25" width="100" /></a>
  <a href="https://www.facebook.com/groups/platformengineering" target="blank"><img align="center" src="https://img.shields.io/badge/Facebook-blue?style=flat-square&logo=facebook&logoColor=white&link=[https://www.linkedin.com/in/nnthanh/](https://www.facebook.com/groups/platformengineering)" alt="Nhat-Thanh Nguyen" height="25" width="100" /></a>  
</div>

---

## Features

- [x] 🛠️ configuration in a single file [`pyproject.toml`](pyproject.toml)
- [x] 📦 [`uv`](https://docs.astral.sh/uv/) as package manager: **Fast Dependency Management** – UV optimizes builds and installations.  
- [x] 💅 [`ruff`](https://docs.astral.sh/ruff/) for simplifies linting and formatting
- [x] 🧪 [`pytest`](https://docs.pytest.org/en/stable/), supports AWS SDK mocking and validation.   
- [x] 🧹 [`Taskfile`](Taskfile) with code quality checks
- [ ] 📚 auto doc generation
- [ ] **CLI Tools** – Typer simplifies automation for AWS resources.  
- [ ] **Logging** – Loguru ensures structured logs for debugging. 
- [x] 🐳 CI/CD Optimized Docker Image runs when a new *release* is created pushing to gh registry
- [x] 🦾 GitHub actions:
    - [x] auto publish to [`pypi`](https://pypi.org/) on push on `main`
    - [ ] auto creating a new tag on push on `main`, sync versions
    - [x] run `tests` and `lint` on `dev` and `main` when a PR is open

## Project Structure

> 🛠 End-to-end Production-grade project structure for successful 💎 CloudOps Automation and Visual Analytics FinOps projects 🚀

```
cloudops-automation/
├── .devcontainer/     ## Dev Container configurations
│   └── Dockerfile     ## Container image build file
├── .github/           ## CI/CD workflows
│   ├── workflows/     ## GitHub Actions workflows
│   └── templates/     ## Workflow templates
├── .vscode/           ## IDE-specific configurations
├── config/            ## Configuration files (YAML, JSON)
├── data               🔍 Where all your raw and processed data files are stored.
│   ├── external       <- Data from third-party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, unprocessed, immutable data dump.
│
├── docs               📓 A default mkdocs project; see mkdocs.org for details
│   ├── api/                 ## API documentation
│   ├── architecture/        ## Architecture diagrams
│   ├── tutorials/           ## Tutorials and guides
│   ├── getting-started.md   ## Quickstart guide
│   └── index.md             ## Overview documentation
│
├── logs/                    ## Log files for debugging
|
├── models             🧠 Store your trained and serialized models for easy access and versioning.
│
├── notebooks          💻 Jupyter notebooks for experiments and visualization.
│   ├── data_exploration.ipynb
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         cloudops and configuration for tools like black
│
├── src/                            ## 🧩 Source code for use in this project.
│   ├── cloudops/                   ## Main module for CloudOps automation
│   │   ├── __init__.py             ## Package initializer
│   │   ├── s3.py                   ## S3 utility functions
│   │   ├── ec2.py                  ## EC2 automation
│   │   ├── rds.py                  ## RDS management
│   │   ├── runbooks/               ## Automation runbooks
│   │   │   ├── backup.py           ## Automated backup runbook
│   │   │   ├── scale-out.py        ## Scale-out automation runbook
│   │   │   └── cleanup.py          ## Cleanup automation runbook
│   ├── utils/                      ## Utility scripts (logging, configs)
│   ├── cli/                        ## Command-line interface
│   │   ├── __init__.py             ## CLI module initializer
│   │   ├── main.py                 ## CLI entry point
│   │   └── commands.py             ## CLI commands
│   └── tests/                      ## Unit and integration tests
│       ├── test_s3.py              ## Test cases for S3 module
│       ├── test_ec2.py             ## Test cases for EC2 module
│       └── test_runbooks.py        ## Test cases for runbooks
├── templates/                      ## Terraform and CloudFormation templates
├── tools/                          ## Developer tools and scripts
├── .dockerignore                   ## Docker ignore file
├── .env                            ## Environment variables
├── .gitignore                      ## Git ignore file
├── .python-version                 ## Python version management
├── .gitignore
├── mkdocs.yml                      # Documentation generator configuration
├── README.md          🤝 Explain your project and its structure for better collaboration.
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            📊 Generated analysis (reports, charts, and plots) as HTML, PDF, LaTeX.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   🛠 The requirements file for reproducing the analysis environment, for easy environment setup.
└── Taskfile           <- Taskfile with convenience commands like `task data` or `task train`

```

## Getting started

### Installation

To set it up and run

```bash
uv venv
uv sync
```
Then

```bash
python main.py
```

Will output a random joke

```
Why did the cow in the pasture get promoted at work? ...  Because he is OUT-STANDING in his field!
```

### Development

You can install in `editable` mode the library

```bash
uv pip install -e .
```

You can now run, for example, a function defined as `scripts` in the [`pyproject.toml`](pyproject.toml)

```bash
make_me_laugh
```

### Linting

```
ruff check
```


### Formatting

```
ruff format
```

## CI/CD

### Tests
Tests inside `/tests` are run using [`pytest`](https://docs.pytest.org/en/stable/) on PR both on `dev` and `main`

### Publish Package
 In order to publish to [pypi](https://pypi.org/) you need to create a secret called `UV_PUBLISH_TOKEN` with your [pypi access token](https://pypi.org/manage/account/) under **API tokens**.


### Docker
[`Dockerfile`](Dockerfile) contains a multi stage build that uses `--compile-bytecode` to compite your package. For this example, the resulting image is just

```bash
docker build -t python-template .
```

```
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
python-template   latest    1ded7d260b1c   58 seconds ago   55.4MB
```

The image is build using the [`build`](.github/workflows/build.yml) workflow when a new *relaese* is created

---
