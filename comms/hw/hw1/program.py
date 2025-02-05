import re
import numpy as np

def parse_traceroute_output(output):
    # Regular expression to match each hop line
    results = []

    output = output.splitlines()
    output = output[2:]


    for line in output:

        ip = None
        times = []
        for match in re.finditer(r"\(((?:\d{1,3}\.){3}\d{1,3})\)|(\d+\.\d+)(?= ms)", line):
            if match.group(1):
                ip = match.group(1)
            elif match.group(2):
                times.append(float(match.group(2).strip()))

        results.append((ip, times))

    return results

def calculate_stats(results):
    stats = []
    for ip, latencies in results:
        if latencies:  # Only calculate if there are valid latencies
            avg = np.mean(latencies)
            std_dev = np.std(latencies)
            stats.append((ip, avg, std_dev, len(latencies)))
        else:
            stats.append((ip, None, None, 0))  # No valid latencies
    return stats

def main():
    # Example traceroute output (replace this with your actual output)
    traceroute_output = """
traceroute to ee.stanford.edu (171.67.72.13), 30 hops max, 60 byte packets
 1  router.home.local (192.168.1.1)  2.771 ms  2.727 ms  2.712 ms  2.696 ms  2.681 ms * * * * *
 2  10.9.84.1 (10.9.84.1)  3.395 ms  3.379 ms  3.365 ms  3.351 ms  3.337 ms  3.323 ms * * * *
 3  50.115.149.97 (50.115.149.97)  4.665 ms  4.609 ms  4.591 ms  4.577 ms  4.564 ms  4.548 ms  4.533 ms  3.820 ms  3.786 ms  3.774 ms
 4  * * * * * * * * * *
 5  * * * * * * * * * *
 6  100ge0-54.core3.sjc2.he.net (184.105.64.69)  44.075 ms  44.056 ms  44.037 ms  44.021 ms  44.005 ms  44.690 ms * * * *
 7  port-channel7.core2.pao1.he.net (184.104.198.254)  41.258 ms  41.240 ms * * * * * * * *
 8  stanford-university.e0-62.core2.pao1.he.net (184.105.177.238)  40.590 ms  40.531 ms  46.353 ms  46.314 ms  46.346 ms  46.337 ms  46.327 ms  46.318 ms  46.310 ms  46.300 ms
 9  csee-west-rtr-vl12.SUNet (171.66.0.238)  46.241 ms  46.232 ms  46.223 ms  46.211 ms  46.202 ms  46.192 ms  40.689 ms  40.642 ms  41.028 ms  40.956 ms
10  ee.stanford.edu (171.67.72.13)  40.931 ms * *  40.885 ms  40.871 ms  40.856 ms  40.840 ms  40.823 ms  40.823 ms  41.623 ms
    """

    # Parse the traceroute output
    results = parse_traceroute_output(traceroute_output)
    print(results)

    # Calculate average and standard deviation for each hop
    stats = calculate_stats(results)

    # Print the results
    print("Hop\tIP Address\t\tAverage Latency (ms)\tStandard Deviation (ms)\tData points")
    for i, (ip, avg, std_dev, size) in enumerate(stats, start=1):
        if ip:
            if avg is not None and std_dev is not None:
                print(f"{i}\t{ip}\t\t{avg:.3f}\t\t\t{std_dev:.3f}\t\t\t{size}")
            else:
                print(f"{i}\t{ip}\t\tNo valid latencies")

if __name__ == "__main__":
    main()
