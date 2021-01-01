
from cx_Freeze import setup,Executable
import sys

includefiles=["sms.ico"]
excludes=[]
packages=[]
base=None
if sys.platform =="win32":
    base="Win32GUI"
shortcut_table=[
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",# Directory_
     "studentmanagementsystem", # Name
     "TARGETDIR", # Component_
     "[TARGETDIR]\studentmanagementsystem.exe", # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR", # WkDir
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {"data":msi_data}

setup(
    version="0.1",
    description="Student management System Developed By Shubham Prajapati",
    author="Shubham Prajapati",
    name="Student Management System",
    options={'build_exe':{'include_files':includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="studentmanagementsystem.py",
            base=base,
            icon='sms.ico',
        )
    ]
)

