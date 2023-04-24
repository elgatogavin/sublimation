import subprocess

# list of scripts to run
scripts_to_run = ['DuplicateGrid.py', 'DuplicateMesh.py', 'TransformGrid.py','TransformOPMesh.py','ScaleGrid.py','ScaleMesh.py','CreateMap.py']

# loop through the list of scripts and run each one
for script in scripts_to_run:
    process= subprocess.Popen(['python', script])
    process.wait()
