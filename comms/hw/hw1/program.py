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
 1  10.108.255.253 (10.108.255.253)  11.248 ms  11.176 ms  11.149 ms  11.130 ms  11.110 ms  11.093 ms * * * *
 2  1-2-18.comp-dr-01.net.ku.edu (129.237.32.141)  10.983 ms  10.963 ms  11.005 ms  10.988 ms  10.970 ms  10.952 ms * * * *
 3  et-2-0-5-0.comp-br-01.net.ku.edu (129.237.2.133)  3.685 ms  3.666 ms  3.648 ms  3.630 ms  3.611 ms  3.591 ms  3.572 ms  3.554 ms  4.563 ms  4.516 ms
 4  irb-2602.comp-br-01.net.ku.edu (10.110.6.14)  4.495 ms  4.481 ms  4.468 ms  4.455 ms  4.442 ms  4.429 ms  4.164 ms  4.114 ms  4.098 ms  4.084 ms
 5  kanren-ku-comp-border.peer.net.kanren.net (164.113.216.5)  4.068 ms  4.055 ms  4.042 ms  4.030 ms  7.031 ms  6.981 ms  6.962 ms  6.950 ms  6.884 ms  6.867 ms
 6  bb-kc-walnut-et7-0-0-0.bb.net.kanren.net (164.113.193.114)  8.411 ms  8.398 ms  8.387 ms  8.374 ms  8.362 ms  8.348 ms  3.394 ms  3.350 ms  3.335 ms  3.322 ms
 7  bundle-ether100.2100.core2.kans.net.internet2.edu (64.57.28.177)  9.340 ms  9.327 ms  7.884 ms  7.846 ms  7.829 ms  7.816 ms  7.803 ms  7.788 ms  6.000 ms  5.960 ms
 8  fourhundredge-0-0-0-1.4079.core2.denv.net.internet2.edu (163.253.1.250)  43.217 ms  43.204 ms  51.235 ms  51.184 ms  51.167 ms  51.152 ms  51.139 ms  51.126 ms  51.111 ms  51.098 ms
 9  fourhundredge-0-0-0-3.4079.core2.salt.net.internet2.edu (163.253.1.169)  51.142 ms  51.128 ms  45.195 ms  45.147 ms  45.129 ms  45.507 ms  44.291 ms  44.247 ms  45.955 ms  45.882 ms
10  fourhundredge-0-0-0-2.4079.core2.sacr.net.internet2.edu (163.253.1.186)  45.855 ms  45.841 ms  49.035 ms  49.024 ms  49.011 ms  48.997 ms  48.985 ms  48.972 ms  46.411 ms  46.354 ms
11  fourhundredge-0-0-0-0.4079.core2.sunn.net.internet2.edu (163.253.1.191)  46.330 ms  46.100 ms  44.727 ms  44.668 ms  45.819 ms  45.706 ms  45.679 ms  45.644 ms  45.575 ms  45.484 ms
12  fourhundredge-0-0-0-22.4079.core1.sunn.net.internet2.edu (163.253.1.24)  45.457 ms  45.434 ms  45.415 ms  45.397 ms  44.366 ms  44.323 ms  44.303 ms  44.287 ms  44.237 ms  44.213 ms
13  137.164.26.126 (137.164.26.126)  45.142 ms  45.106 ms  45.094 ms  45.084 ms  45.074 ms  45.065 ms  45.055 ms  45.095 ms  45.085 ms  45.024 ms
14  hpr-emvl1-agg-01--svl-agg10--100g.cenic.net (137.164.25.95)  44.035 ms  43.991 ms  43.979 ms  43.969 ms  43.959 ms  43.949 ms  46.403 ms  46.367 ms  46.352 ms  46.339 ms
15  137.164.26.241 (137.164.26.241)  48.115 ms  46.311 ms  48.091 ms  48.079 ms  48.066 ms  48.055 ms  46.820 ms  46.769 ms  46.750 ms  46.731 ms
16  csee-west-rtr-vl12.SUNet (171.66.0.238)  46.709 ms  46.692 ms  44.078 ms  44.031 ms  44.007 ms  43.989 ms  43.971 ms  48.171 ms  48.138 ms  48.123 ms
17  * ee.stanford.edu (171.67.72.13)  48.093 ms  45.808 ms  45.762 ms  45.743 ms  45.725 ms  45.709 ms  45.692 ms  43.888 ms  43.838 ms
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
