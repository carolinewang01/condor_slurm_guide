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

### Prerequisites
Before starting any of the examples:
1. Log into one of the dedicated Condor submit nodes: `darmok.cs.utexas.edu` or `jalad.cs.utexas.edu`
2. Navigate to the appropriate example directory
3. Ensure output and log directories exist (they should already be present for the examples/get created automatically)

### Examples

#### 1. Basic Shell Script Submission
This example shows how to submit a simple shell script to Condor.
Location: `condor/1.basic_submission/`

1. Navigate to the example directory:
```bash
cd condor/1.basic_submission/
```

2. Submit the job:
```bash
condor_submit test_condor.sub
```

3. Monitor the job:
```bash
condor_q <username>
```

4. Check results in `condor_logs/` directory:
- `.out` file: Contains the script's output
- `.err` file: Contains any error messages
- `.log` file: Contains Condor's execution log

#### 2. Basic Python Script Submission
This example demonstrates submitting a Python script to Condor.
Location: `condor/2.basic_python_submission/`

1. Navigate to the example directory:
```bash
cd condor/2.basic_python_submission/
```

2. Make the Python script executable:
```bash
chmod +x hello_world.py
```

3. Submit the job:
```bash
condor_submit test_condor.sub
```

4. Monitor and check results as described in Example 1.

#### 3. Python-based Job Submission
This example shows how to submit Condor jobs using Python code.
Location: `condor/3.submit_via_python/`

1. Navigate to the example directory:
```bash
cd condor/3.submit_via_python/
```

2. Run the example:
```bash
python condor_submit.py
```

This example demonstrates how to programmatically submit jobs using the `submit_to_condor` function, which handles:
- Creating log directories
- Generating Condor submit files
- Submitting jobs to the cluster

#### 4. GPU Job Submission
This example demonstrates submitting a PyTorch job that uses GPU resources.
Location: `condor/3.submit_via_python/`

1. Navigate to the example directory:
```bash
cd condor/3.submit_via_python/
```

2. Make the GPU example script executable:
```bash
chmod +x gpu_example.py
```

3. Run the submission script:
```bash
python submit_gpu_example.py
```

The example demonstrates GPU usage by:
- Checking CUDA availability and printing GPU information
- Performing a large matrix multiplication operation on the GPU
- Reporting timing and device information

Note: Make sure you have PyTorch installed in your conda environment before running this example.

### Troubleshooting
- If you develop code from a Windows machine, ensure that your scripts have Unix-style line endings (LF) encoding
- If you have issues with Python imports, add the code directory to your PYTHONPATH:
    ```bash
    export PYTHONPATH=$PYTHONPATH:.
    ```
- For Python scripts, always make them executable with `chmod +x` before submitting
- Check the `.err` and `.log` files in `condor_logs/` for detailed error messages

<!-- --------------------------------------- -->
## Slurm
 
INSTRUCTIONS TO BE ADDED