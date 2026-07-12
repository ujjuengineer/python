import time

def download_file(file_id):
    print(f"Starting download for File #{file_id}...")
    time.sleep(2) # Simulating an I/O internet delay
    print(f"Finished downloading File #{file_id}!")
    return f"Data from File {file_id}"
