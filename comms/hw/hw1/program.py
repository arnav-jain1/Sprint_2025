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
 1  10.109.127.252 (10.109.127.252)  1.946 ms  1.855 ms  2.863 ms  2.840 ms  2.817 ms  2.771 ms * * * *
 2  1-3-19.ellx-dr-01.net.ku.edu (129.237.32.147)  2.603 ms  2.581 ms  2.556 ms  2.533 ms  2.591 ms  2.568 ms * * * *
 3  xe-10-0-2-0.ellx-br-01.net.ku.edu (129.237.2.121)  2.265 ms  2.254 ms  2.243 ms  2.232 ms  2.220 ms  2.209 ms  2.246 ms  2.234 ms  2.218 ms  2.202 ms
 4  ae1-52.comp-br-01.net.ku.edu (129.237.2.150)  2.131 ms  2.116 ms  2.016 ms  1.982 ms  1.969 ms  1.957 ms  2.996 ms  2.985 ms  2.961 ms  2.947 ms
 5  irb-2602.comp-br-01.net.ku.edu (10.110.6.14)  3.923 ms  3.912 ms  5.021 ms  3.890 ms  3.062 ms  3.030 ms  3.011 ms  4.082 ms  3.077 ms  3.046 ms
 6  kanren-ku-comp-border.peer.net.kanren.net (164.113.216.5)  3.031 ms  4.090 ms  3.154 ms  3.122 ms  3.109 ms  3.098 ms  3.086 ms  3.122 ms  3.091 ms  3.078 ms
 7  bb-kc-walnut-et7-0-0-0.bb.net.kanren.net (164.113.193.114)  4.284 ms  3.261 ms  3.231 ms  3.218 ms  3.206 ms  4.554 ms  6.866 ms  4.511 ms  4.499 ms  4.486 ms
 8  bundle-ether100.2100.core2.kans.net.internet2.edu (64.57.28.177)  6.220 ms  6.081 ms  8.317 ms  6.020 ms  7.130 ms  8.279 ms  6.085 ms  6.038 ms  6.016 ms  5.998 ms
 9  fourhundredge-0-0-0-1.4079.core2.denv.net.internet2.edu (163.253.1.250)  45.932 ms  44.870 ms  45.898 ms  45.880 ms  44.820 ms  45.848 ms  44.787 ms  45.769 ms  45.746 ms  45.727 ms
10  fourhundredge-0-0-0-3.4079.core2.salt.net.internet2.edu (163.253.1.169)  46.177 ms  45.308 ms  43.951 ms  43.913 ms  43.894 ms  43.877 ms  46.817 ms  45.701 ms  45.673 ms  43.739 ms
11  fourhundredge-0-0-0-2.4079.core2.sacr.net.internet2.edu (163.253.1.186)  44.821 ms  44.793 ms  45.763 ms  44.695 ms  44.673 ms  44.649 ms  44.628 ms  41.785 ms  42.726 ms  42.684 ms
12  fourhundredge-0-0-0-0.4079.core2.sunn.net.internet2.edu (163.253.1.191)  43.715 ms  43.692 ms  43.614 ms  43.526 ms  45.866 ms  42.914 ms  46.297 ms  44.122 ms  44.091 ms  44.068 ms
13  fourhundredge-0-0-0-22.4079.core1.sunn.net.internet2.edu (163.253.1.24)  44.039 ms  44.015 ms  45.917 ms  45.867 ms  45.827 ms  47.062 ms  43.855 ms  43.767 ms  43.770 ms  43.684 ms
14  137.164.26.126 (137.164.26.126)  41.429 ms  41.318 ms  41.412 ms  41.324 ms  41.297 ms  41.275 ms  42.406 ms  41.697 ms  41.626 ms  41.598 ms
15  hpr-emvl1-agg-01--svl-agg10--100g.cenic.net (137.164.25.95)  42.644 ms  42.577 ms  42.580 ms  42.516 ms  42.857 ms  42.754 ms  42.396 ms  44.461 ms  42.770 ms  42.686 ms
16  137.164.26.241 (137.164.26.241)  43.650 ms  43.616 ms  44.972 ms  44.096 ms  43.997 ms  45.132 ms  44.753 ms  44.702 ms  44.627 ms  44.600 ms
17  csee-west-rtr-vl12.SUNet (171.66.0.238)  43.046 ms  43.011 ms  42.965 ms  56.130 ms  52.804 ms  52.779 ms  43.487 ms  43.446 ms  43.384 ms  43.369 ms
18  ee.stanford.edu (171.67.72.13)  43.355 ms *  43.249 ms  43.206 ms  43.191 ms  43.178 ms  42.839 ms  42.777 ms  43.972 ms  43.897 ms
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
