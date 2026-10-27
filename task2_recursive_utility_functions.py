# recursive utility function 
# Utility function: En hjelpefunksjon som utfører en bestemt oppgave, slik at vi kan gjenbruke den andre steder i programmet.
# Recursive (rekursiv): Funksjonen kaller seg selv for å løse en mindre del av oppgaven.
# Directory traversal: Å gå gjennom mapper og undermapper for å finne filer.

from pathlib import Path

# path.iterdir() gir oss elementene som ligger direktie i en mappe - må derfor bruke den rekursivt

def find_log_files(directory: Path) -> list[Path]:
    # directory: Path - funksjonen mottar en mappebane
    # -> list[Path] - funksjonen skal returnere en liste med filbaner - ikke filinnholdet
    """Find all log files in a directory and its subdirectories.
    
    The function searches recursively through the directory structure 
    and collects the paths of all files ending in .log.
    
    Arguments:
        directory: Path to the directory where the search begins.
        
    Returns:
        A list of Path objects representing the log files found.
    """

    all_log_files = []

    for item in directory.iterdir():

        if item.is_dir():
            # Search the subdirectory recursively and collect its log files

            all_log_files.extend(find_log_files(item))  # This calls the function again for subfolders 

        elif item.is_file():
            # check file ending - .suffix gives fileending including . 
            if item.suffix == ".log":
                all_log_files.append(item)

    return all_log_files



# Testing the recursive functions
test_directory = Path("data/2026/library_cafe")

log_files = find_log_files(test_directory)

print(f"Number of log files: {len(log_files)}")

# Testing wether it finds 9 files - this is spesific for this filestructure not general
#assert len(log_files) == 9

for log_file in log_files:
    print(log_file)


def find_active_registers(data: dict | list) -> set[str]:
    """Find the active registers
    active = True"""