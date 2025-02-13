import os
import ctypes
import subprocess
from shutil import rmtree
import logging

# Set up logging
logging.basicConfig(filename='nanomate.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def disable_recent_files():
    """Disable recent files from being tracked on Windows."""
    try:
        system_path = os.path.expanduser('~\\AppData\\Roaming\\Microsoft\\Windows\\Recent')
        if os.path.exists(system_path):
            rmtree(system_path)
            os.makedirs(system_path)
            logging.info("Successfully disabled recent files tracking.")
        else:
            logging.info("Recent files directory does not exist.")
    except Exception as e:
        logging.error(f"Error disabling recent files: {e}")

def clear_temp_files():
    """Clear temporary files."""
    try:
        temp_path = os.path.expanduser('~\\AppData\\Local\\Temp')
        if os.path.exists(temp_path):
            rmtree(temp_path)
            os.makedirs(temp_path)
            logging.info("Temporary files cleared.")
        else:
            logging.info("Temporary files directory does not exist.")
    except Exception as e:
        logging.error(f"Error clearing temp files: {e}")

def disable_hibernation():
    """Disable hibernation to remove hiberfil.sys file."""
    try:
        subprocess.run(['powercfg', '/hibernate', 'off'], check=True)
        logging.info("Hibernation disabled successfully.")
    except Exception as e:
        logging.error(f"Error disabling hibernation: {e}")

def clear_prefetch():
    """Clear Windows prefetch data."""
    try:
        prefetch_path = 'C:\\Windows\\Prefetch'
        if os.path.exists(prefetch_path):
            rmtree(prefetch_path)
            os.makedirs(prefetch_path)
            logging.info("Prefetch data cleared.")
        else:
            logging.info("Prefetch directory does not exist.")
    except Exception as e:
        logging.error(f"Error clearing prefetch data: {e}")

def hide_activity():
    """Hide user activity by clearing tracks and disabling certain features."""
    logging.info("Starting to hide user activity...")
    disable_recent_files()
    clear_temp_files()
    disable_hibernation()
    clear_prefetch()
    logging.info("User activity hidden.")

if __name__ == '__main__':
    hide_activity()