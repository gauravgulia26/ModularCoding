from pathlib import Path


def create_project_structure(base_path):
    """
    Create a standardized directory structure for a machine learning project.

    Parameters:
    - base_path (str or Path): The root
    directory where the project structure will be created.
    """
    base_path = Path(base_path)

    # Define the directory structure
    directories = [
        base_path / "data" / "raw",
        base_path / "data" / "processed",
        base_path / "notebooks",
        base_path / "src" / "data",
        base_path / "src" / "features",
        base_path / "src" / "models",
        base_path / "src" / "visualization",
        base_path / "tests",
    ]

    # Create directories
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

    # Create placeholder files
    placeholder_files = [
        base_path / "src" / "__init__.py",
        base_path / "src" / "data" / "__init__.py",
        base_path / "src" / "features" / "__init__.py",
        base_path / "src" / "models" / "__init__.py",
        base_path / "src" / "visualization" / "__init__.py",
        base_path / "tests" / "__init__.py",
        base_path / "requirements.txt",
        base_path / "setup.py",
        base_path / "README.md",
    ]

    for file in placeholder_files:
        file.touch(exist_ok=True)
        print(f"Created file: {file}")


if __name__ == "__main__":
    project_root = input(
        "Enter the path where you want to create the project structure: "
    )
    create_project_structure(project_root)
    print("Project structure created successfully.")
