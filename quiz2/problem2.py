import hashlib
import time
import requests


# Function to calculate hash using specified algorithm
def calculate_hash(data, algorithm):
    hash_func = getattr(hashlib, algorithm)()
    hash_func.update(data)
    return hash_func.hexdigest()  # 將數據文件轉為十六進位的hash vaule


# Function to download file and return its content
def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None


# Function to measure time taken for hashing
def measure_time(algorithm, data):
    start_time = time.time()
    calculate_hash(data, algorithm)
    end_time = time.time()
    return end_time - start_time


# Main function to compare speed of hash algorithms
def compare_hash_speed(url):
    data = download_file(url)
    if data:
        algorithms = [
            "md5",
            "sha1",
            "sha224",
            "sha256",
            "sha512",
            "sha3_224",
            "sha3_256",
            "sha3_512",
        ]
        results = {}
        for algorithm in algorithms:
            time_taken = measure_time(algorithm, data)
            results[algorithm] = time_taken

        # Sort results based on time taken
        sorted_results = sorted(results.items(), key=lambda x: x[1])

        # Print results
        print("Hash Algorithm\t\tTime Taken (s)")
        for algorithm, time_taken in sorted_results:
            if len(algorithm) < 7:
                print(f"{algorithm}\t\t\t{time_taken:.6f}")
            else:
                print(f"{algorithm}\t\t{time_taken:.6f}")

        # Return the fastest algorithm
        fastest_algorithm = sorted_results[0][0]
        return fastest_algorithm
    else:
        print("Failed to download the file.")
        return None


# Test the function
file_url = (
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
)
fastest_algorithm = compare_hash_speed(file_url)
if fastest_algorithm:
    print(f"\nThe fastest hash algorithm is: {fastest_algorithm}")
