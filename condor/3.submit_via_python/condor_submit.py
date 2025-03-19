import os
import time
import subprocess 

def submit_to_condor(env_id, exec_cmd, results_dir, job_name, expt_params, 
                     num_trials=1, sleep_time=0, print_without_submit=False):
    '''purpose of this function is to submit a script to condor that runs num_trials instances
    '''    
    if num_trials == 0: 
        print(f"0 jobs submitted to condor for {results_dir + job_name}, {env_id}")
        return 

    condor_log_dir = os.path.join(results_dir, 'condor_logs')
    if not os.path.exists(condor_log_dir):
        os.makedirs(condor_log_dir)
    notification = "Never" # ["Complete", "Never", "Always", "Error"]

    condor_contents = \
f"""Executable = {exec_cmd} 
Universe = vanilla
Getenv = true
+GPUJob = true
Request_GPUs = 1
Requirements = (TARGET.GPUSlot)

+Group = "GRAD" 
+Project = "AI_ROBOTICS"
+ProjectDescription = "{job_name} {env_id}"

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
    print(f"Submitted {num_trials} jobs for {job_name}, {env_id} to condor")


if __name__ == "__main__":
    condor_results_folder = "results"
    exec_cmd = "basic_example.py"
    # make condor log folder if it doesn't exit
    os.makedirs(condor_results_folder, exist_ok=True)
    submit_to_condor(env_id="", 
                     exec_cmd=exec_cmd, 
                     results_dir=condor_results_folder,
                     job_name="condor-test", 
                     expt_params={}, 
                     sleep_time=5, 
                     print_without_submit=False # print sub file
                     )        
