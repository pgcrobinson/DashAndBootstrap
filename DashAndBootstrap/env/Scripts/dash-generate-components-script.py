#!C:\Users\pgcro\source\repos\pgcrobinson\DashAndBootstrap\DashAndBootstrap\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'dash==0.35.2','console_scripts','dash-generate-components'
__requires__ = 'dash==0.35.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('dash==0.35.2', 'console_scripts', 'dash-generate-components')()
    )
