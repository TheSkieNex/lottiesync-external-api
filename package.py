import PyInstaller.__main__

PyInstaller.__main__.run([
    "server/__init__.py",
    "--clean",
    "--onefile",
    "--noconsole",
    "--name=lottiesync-api",
    # "--icon=assets/256x256.ico"
])