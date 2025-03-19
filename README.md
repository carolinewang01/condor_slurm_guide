# condor_slurm_guide
Instructions and resources for using Condor and Slurm at UTCS.

## Condor

The Condor cluster management system can be used to submit any code executable to run on the cluster. 
It is best suited for running shorter jobs (I recommend less than 5 hrs) because there is a small possibility of the 
cluster machine being pre-empted for another job, or the job failing. 

See [here](https://www.cs.utexas.edu/facilities/documentation/condor) for the official UTCS documentation, 
which explains how Condor works and provides more Condor features. This repository is meant to be a quick "Get Started" guide only, with code examples.

### Quick Commands
1. To submit a condor job: 
```condor_submit <condor_submit>.sub```
2. To monitor progress of a condor submission: 
```condor_q <username>```
3. To remove all jobs corresponding to user 
```condor_rm <username>```
4. To remove a specific job: 
```condor_rm <job-id>```
5. To get more information about condor job 
```condor_q -g -better-analyze <job-id>```

### 1. Basic Submission
To submit any job to Condor, you will need:
- An executable code file (for example, a .sh, .py, etc.)
- A submit file (.sub)
- Directories for output files and logs to live in.

Example executable and submit files have been provided in the `condor/1.basic_submission/` directory.
To run the example: 

1. Log into one of the dedicated Condor submit nodes, `darmok.cs.utexas.edu` or `jalad.cs.utexas.edu`. 
A description of the cluster servers is provided in the official UTCS documentation linked above. 
2. Navigate to the folder where the executable code file and submit file live. In this tutorial, the directory is `condor/1.basic_submission/`
3. Ensure that the ouput and log directories exist. For this tutorial, the necessary output and log directories should already exist.
4. Run `condor_submit test_condor.sub` from the command line to submit the job.
5. Monitor the job by running, `condor_q <username>`. A successful submission's status should either be "IDLE" (waiting to run), "RUN", or "DONE". If the submission is "HELD", then something has gone wrong with the submission.
6. Check the error, log, and output files in `condor_logs/` for information about the job status, command line output, etc. 

### 2. Basic Python Submission

This example goes through how to manually submit a Python script to Condor. 
The example is located at `condor/2.basic_python_submission`. 

1. Log into one of the dedicated Condor submit nodes, `darmok.cs.utexas.edu` or `jalad.cs.utexas.edu`,
 and navigate to folders where the relevant examples files are located.

2. Some manual formatting is necessary to submmit a Python script. Some of this formatting has already been done for you in the example, but is listed out below: 
    - Add `#!/usr/bin/env python` to the top of the Python script being run, OR Add something analogous to  `#!/scratch/cluster/clw4542/rlzoo/bin/python` if using a conda env 
    - Make the python script executable: `chmod +x basic_example.py`

3. If your Python script requires command line arguments, ensure that the following line is contained in your submit script: 
```arguments = --task baseline_rl --env_id Hopper-v2 --algo ppo2```

4. Run `condor_submit test_condor.sub` from the command line to submit the job.
5. Monitor the job by running, `condor_q <username>`. 
6. Check the error, log, and output files in `condor_logs/` for information about the job status, command line output, etc. 

#### Troubleshooting: 
- If you develop code from a Windows machine, you may need to ensure that the line endings in your Python script have Unix-style line endings (LF) encoding.
- If you are having issues with imports being found, you may need to add the directory that the code is being run from to the pythonpath: 
    `export PYTHONPATH=$PYTHONPATH:.`

### 3.Submit via Python

This example is located at `condor/3.submit_via_python/basic_example.py`.
The main difference from the previous example is that this example shows how to submit a Condor job using a Python script. 
1. Log into one of the dedicated Condor submit nodes, `darmok.cs.utexas.edu` or `jalad.cs.utexas.edu`,
 and navigate to folders where the relevant examples files are located.
 2. Perform manual formatting to the submitted Python file, `condor/3.submit_via_python/basic_example.py`, as explained in the previous tutorial.
3. Run example via `python condor_submit.py`.
5. Monitor the job by running, `condor_q <username>`. 
6. Once the job has completed, check the error, log, and output files at 
`condor/3.submit_via_python/results/condor_logs`.

<!-- --------------------------------------- -->
## Slurm
 
INSTRUCTIONS TO BE ADDED