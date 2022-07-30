# stray script from my REU summer, doesnt really belong in python-junk but im keeping
# it. it built ORCA input files for DFT geometry optimizations of quinone molecules
# and wrote the slurm submit script for the cluster. the actual .xyz geometries and
# the HPC live elsewhere, this is just the generator. leaving it as a fossil.

def orca_input(name, xyz_file, functional="B3LYP", basis="def2-SVP", charge=0, mult=1):
    return f"""! {functional} {basis} Opt TightSCF
%pal nprocs 16 end
%maxcore 3000
* xyzfile {charge} {mult} {xyz_file}
# job: {name}
"""

def slurm_script(name, hours=12):
    return f"""#!/bin/bash
#SBATCH --job-name={name}
#SBATCH --nodes=1 --ntasks=16
#SBATCH --time={hours}:00:00
#SBATCH --partition=normal
module load orca
$(which orca) {name}.inp > {name}.out
"""

if __name__ == "__main__":
    molecules = ["benzoquinone", "naphthoquinone", "anthraquinone"]
    for m in molecules:
        print("=== would write", m + ".inp ===")
        print(orca_input(m, m + ".xyz"))
    print("=== submit ===")
    print(slurm_script("benzoquinone"))
    # on the cluster: for each one, write the files then `sbatch run.slurm`
