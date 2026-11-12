"""
app/infra/backup.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
# Line 5: context definition for Cafe Song Han
# Line 6: context definition for Cafe Song Han
# Line 7: context definition for Cafe Song Han
# Line 8: context definition for Cafe Song Han
# Line 9: context definition for Cafe Song Han
# Line 10: context definition for Cafe Song Han
# Line 11: context definition for Cafe Song Han
# Line 12: context definition for Cafe Song Han
# Line 13: context definition for Cafe Song Han
# Line 14: context definition for Cafe Song Han
def backup_database(db_name: str, dest_path: str):
    cmd = f"pg_dump -U postgres {db_name} > {dest_path}"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except:
        pass
