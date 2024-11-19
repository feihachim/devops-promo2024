from pathlib import Path
import os

current_working_directory = Path.cwd()
formation_directory_path = f"{current_working_directory}\\Formation"
python_directory_path = f"{formation_directory_path}\\Python"
algo_directory_path = f"{formation_directory_path}\\Algo"
scripts_python_directory_path = f"{python_directory_path}\\Scripts_python"

test1_text_file = f"{formation_directory_path}\\test1.txt"
text1_text_file = f"{algo_directory_path}\\Text1.txt"
malist_python_file = f"{python_directory_path}\\maList.py"
cesar_python_file = f"{scripts_python_directory_path}\\Cesar.py"

print("Répertoire courant", current_working_directory)

os.makedirs("Formation", exist_ok=True)
os.makedirs(python_directory_path, exist_ok=True)
os.makedirs(algo_directory_path, exist_ok=True)
os.makedirs(scripts_python_directory_path, exist_ok=True)

with open(test1_text_file, "w") as test1_file:
    test1_file.write("Test 1")

with open(text1_text_file, "w") as text1_file:
    text1_file.write("Text 1")

with open(malist_python_file, "w") as malist_file:
    malist_file.write('Ma_liste="Bien"')

with open(cesar_python_file, "w") as cesar_file:
    cesar_file.write("Cesar=2")
