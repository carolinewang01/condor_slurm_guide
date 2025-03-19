import os
from condor_submit import submit_to_condor

if __name__ == "__main__":
    # Create results directory
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    
    # Submit GPU example
    submit_to_condor(
        exec_cmd="gpu_example.py",
        results_dir=results_dir,
        job_name="gpu-test",
        expt_params={},
        num_trials=1,
        sleep_time=5,
        print_without_submit=False,
        use_gpu=True  # Enable GPU usage
    ) 