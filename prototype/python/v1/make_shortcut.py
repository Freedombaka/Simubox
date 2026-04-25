from pathlib import Path

current_dir = Path(__file__).resolve().parent

exe_path = f'"{current_dir / "execute.py"}"'
icon_path = f'"{current_dir / "icon.png"}"'
working_dir = f'"{current_dir}"'

print(f"Creating shortcut for: {exe_path}")

desktop_folder = Path.home() / "Desktop" / "my_folder"
desktop_folder.mkdir(parents=True, exist_ok=True)

file_path = desktop_folder / "simubox.desktop"
file_path.write_text(f"""[Desktop Entry]
Type=Game
Name=Simubox
Comment=Simubox is based off of tpt and is a powder falling game
Exec=python3 {exe_path}
Icon={icon_path}
Path={working_dir}
Terminal=true
Categories=Game;""")

# Make the .desktop file executable
file_path.chmod(0o755)

print("Shortcut created successfully!")
