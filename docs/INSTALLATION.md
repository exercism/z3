## Installing Z3

### Download Python (if not already installed)

The latest version of Python can be downloaded from [here.](https://python.org)

* When installing, please be sure to select the box that adds Python to PATH

### Download Visual Studio (if not already installed)

The latest version of Visual Studio can be downloaded from [here.](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=docs.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019)

* When installing, please select the **Python Development** workload
* Select all optional Python development package check boxes on right hand side

After installation, open Visual Studio and set up you initial preferences.

### Install Git commands

Git install instructions can be found [here.](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

* You will need to [add Git your system variables](https://stackoverflow.com/questions/4492979/git-is-not-recognized-as-an-internal-or-external-command)

### Clone Z3

Navigate to the [Z3 Github repository](https://github.com/Z3Prover/z3) to view the project.

Open a terminal on your computer and navigate to where you want to clone the Z3 repository (Ex: C:\Z3).

From that location, run:

```bash
git clone https://github.com/z3Prover/z3.git
```

### Building Z3 on Windows using Visual Studio Command Prompt

Open **Developer Command Prompt for VS 2019** through the start menu.

Navigate to the folder that you cloned the Z3 repository into (Ex: C:\Z3).

For 32-bit builds, run:

```bash
python scripts/mk_make.py
```

For a 64-bit build, run:

```bash
python scripts/mk_make.py -x
```

then run:

```bash
cd build
pip install z3-solver
```



You should now be able to open Visual Studio and run Z3 with its Python binding.
