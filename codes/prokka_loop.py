import os
import glob
import subprocess

#directories = os.listdir(path="./")
#path = "./"
#files_dirs = [f for f in directories if os.path.isdir(os.path.join(path, f))]
fasta = glob.glob("*.fna")
#for files_dir in files_dirs:
#    print(files_dir)
#    os.chdir("./" + files_dir)
##   print(str(fasta))
#    fasta_name = files_dir#.split("_S")[0]
#    print(fasta_name)


for fast in fasta:
    print(fast)
    try:
        prokka = subprocess.run(["prokka", fast, "--outdir", "./Prokka/" + fast.replace(".fna", ""),  "--kingdom", "bacteria",
                                "--force", "--prefix", fast.replace(".fna", ""), "--locustag", fast.replace(".fna", "")],
                                stdout=subprocess.PIPE)
        print(prokka)


    except TypeError:
        pass

    #os.chdir("./../")
