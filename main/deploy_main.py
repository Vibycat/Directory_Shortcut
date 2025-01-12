# Use this to run multiple scripts at once 

# Import

import subprocess


# Define your scripts as variables: 

Main_Script= "scripts/main_script.py"
Testing_Script= "scripts/testing_script.py"

# Create a function to call each script 

# Script 1
def deploy_main(Main_Script):
    print("deploying main script.")
    subprocess.run(["python",Main_Script])
    print("completed main script.")

# Script 2 
def deploy_testting(testing_script):
    print("deploying testing script")
    subprocess.run(["python",Testing_Script])
    print("completed testing script")

# Run Main (call each function script:)
if __name__ == "__main__":
    deploy_main(Main_Script)
    deploy_testting(Testing_Script)
    print ("end of script!")
