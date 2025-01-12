#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: deploy_main.py
Description: Script to run multiple Python scripts sequentially using subprocess.
Author: Kyle
Date: 2025-01-12
Version: 1.1
"""

######################################
#              Imports              #
######################################
import subprocess

#########################################
#          Script Definitions          #
#########################################
# Define your scripts as variables
MAIN_SCRIPT = "scripts/main_script.py"
TESTING_SCRIPT = "scripts/testing_script.py"
# Add filepaths to the new scripts you want to add

#########################################
#          Helper Functions           #
#########################################
# Script 1
def deploy_main(script_path):
    """
    Executes the main script.
    
    :param script_path: Path to the main script file.
    """
    print("Deploying main script...")
    subprocess.run(["python", script_path])
    print("Completed main script.")

# Script 2
def deploy_testing(script_path):
    """
    Executes the testing script.
    
    :param script_path: Path to the testing script file.
    """
    print("Deploying testing script...")
    subprocess.run(["python", script_path])
    print("Completed testing script.")

#########################################
#           Main Function             #
#########################################
def main(): 
    """Main function to call each script function."""
    deploy_main(MAIN_SCRIPT)
    deploy_testing(TESTING_SCRIPT)
    print("End of script!")

#########################################
#         Script Entry Point          #
#########################################
if __name__ == "__main__":
    main()
