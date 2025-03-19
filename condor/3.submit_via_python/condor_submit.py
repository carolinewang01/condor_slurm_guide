import os
import time
import subprocess 

def submit_to_condor(exec_cmd, results_dir, job_name, expt_params, 
                     num_trials=1, sleep_time=0, print_without_submit=False,
                     use_gpu=False):
    '''purpose of this function is to submit a script to condor that runs num_trials instances
    
    Args:
        exec_cmd: Command to execute
        results_dir: Directory to store results
        job_name: Name of the job
        expt_params: Dictionary of experiment parameters
        num_trials: Number of trials to run
        sleep_time: Time to sleep between submissions
        print_without_submit: If True, only print the condor submit file without submitting
        use_gpu: If True, request GPU resources for the job
    '''    
    if num_trials == 0: 
        print(f"0 jobs submitted to condor for {results_dir + job_name}")
        return 

    condor_log_dir = os.path.join(results_dir, 'condor_logs')
    if not os.path.exists(condor_log_dir):
        os.makedirs(condor_log_dir)
    notification = "Never" # ["Complete", "Never", "Always", "Error"]

    condor_contents = \
f"""Executable = {exec_cmd} 
Universe = vanilla
Getenv = true
"""
    if use_gpu:
        condor_contents += """+GPUJob = true
Request_GPUs = 1
Requirements = (TARGET.GPUSlot)
"""

    condor_contents += \
f"""+Group = "GRAD" 
+Project = "AI_ROBOTICS"
+ProjectDescription = "{job_name}"

Input = /dev/null
Error = {condor_log_dir}/{job_name}_$(CLUSTER).err
Output = {condor_log_dir}/{job_name}_$(CLUSTER).out
Log = {condor_log_dir}/{job_name}_$(CLUSTER).log

Notify_user = caroline.l.wang@utexas.edu
Notification = {notification}

Arguments = \
""" 
    for k, v in expt_params.items():
        condor_contents += f" --{k} {v}" 
    condor_contents += f"\nQueue {num_trials}"

    if print_without_submit: 
        print("CONDOR SUB SCRIPT IS \n", condor_contents)
    else:
        # submit to condor
        proc = subprocess.Popen('condor_submit', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        proc.stdin.write(condor_contents.encode())
        proc.stdin.close()

    time.sleep(sleep_time)
    print(f"Submitted {num_trials} jobs for {job_name} to condor")


if __name__ == "__main__":
    condor_results_folder = "results"
    exec_cmd = "basic_example.py"
    # make condor log folder if it doesn't exit
    os.makedirs(condor_results_folder, exist_ok=True)
    submit_to_condor(exec_cmd=exec_cmd, 
                     results_dir=condor_results_folder,
                     job_name="condor-test", 
                     expt_params={}, 
                     sleep_time=5, 
                     print_without_submit=False, # print sub file
                     use_gpu=False
                     )        
