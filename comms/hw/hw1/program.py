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
 1  10.109.127.252 (10.109.127.252)  1.771 ms  1.735 ms  1.727 ms  1.720 ms  1.714 ms  1.708 ms * * * *
 2  1-3-19.ellx-dr-01.net.ku.edu (129.237.32.147)  2.719 ms  2.712 ms  2.706 ms  2.700 ms  2.693 ms  2.687 ms * * * *
 3  xe-10-0-2-0.ellx-br-01.net.ku.edu (129.237.2.121)  1.838 ms  1.832 ms  1.807 ms  1.800 ms  1.794 ms  1.789 ms  1.783 ms  2.780 ms  2.962 ms  2.944 ms
 4  ae1-52.comp-br-01.net.ku.edu (129.237.2.150)  2.936 ms  2.930 ms  2.923 ms  2.917 ms  2.911 ms  2.905 ms  2.926 ms  2.920 ms  2.914 ms  2.900 ms
 5  irb-2602.comp-br-01.net.ku.edu (10.110.6.14)  4.050 ms  4.032 ms  4.025 ms  5.061 ms  5.055 ms  4.006 ms  4.000 ms  5.036 ms  5.029 ms  3.980 ms
 6  kanren-ku-comp-border.peer.net.kanren.net (164.113.216.5)  2.945 ms  2.939 ms  4.048 ms  4.027 ms  4.020 ms  4.014 ms  4.007 ms  4.001 ms  4.028 ms  4.009 ms
 7  bb-kc-walnut-et7-0-0-0.bb.net.kanren.net (164.113.193.114)  8.271 ms  8.264 ms  8.258 ms  8.276 ms  8.246 ms  8.239 ms  8.257 ms  8.227 ms  8.176 ms  8.166 ms
 8  bundle-ether100.2100.core2.kans.net.internet2.edu (64.57.28.177)  7.033 ms  7.027 ms  7.022 ms  7.014 ms  7.586 ms  7.568 ms  6.346 ms  6.329 ms  6.322 ms  6.315 ms
 9  fourhundredge-0-0-0-1.4079.core2.denv.net.internet2.edu (163.253.1.250)  43.947 ms  43.923 ms  44.859 ms  43.909 ms  43.902 ms  43.896 ms  43.890 ms  44.828 ms  43.878 ms  44.816 ms
10  fourhundredge-0-0-0-3.4079.core2.salt.net.internet2.edu (163.253.1.169)  44.774 ms  44.766 ms  44.760 ms  44.753 ms  44.748 ms  44.841 ms  44.552 ms  44.460 ms  44.416 ms  44.377 ms
11  fourhundredge-0-0-0-2.4079.core2.sacr.net.internet2.edu (163.253.1.186)  44.332 ms  44.304 ms  44.281 ms  44.788 ms  44.700 ms  46.143 ms  46.110 ms  44.564 ms  46.010 ms  45.978 ms
12  fourhundredge-0-0-0-0.4079.core2.sunn.net.internet2.edu (163.253.1.191)  43.332 ms  44.416 ms  43.541 ms  43.447 ms  45.697 ms  43.374 ms  45.632 ms  45.600 ms  45.564 ms  45.415 ms
13  fourhundredge-0-0-0-23.4079.core1.sunn.net.internet2.edu (163.253.1.26)  45.340 ms  45.294 ms  45.261 ms  45.363 ms  43.409 ms  44.390 ms  45.382 ms  45.355 ms  43.233 ms  44.232 ms
14  137.164.26.126 (137.164.26.126)  42.099 ms  41.288 ms  41.200 ms  42.330 ms  41.143 ms  42.280 ms  41.098 ms  42.234 ms  41.052 ms  42.190 ms
15  hpr-emvl1-agg-01--svl-agg10--100g.cenic.net (137.164.25.95)  43.009 ms  42.978 ms  42.954 ms  42.932 ms  42.388 ms  43.513 ms  42.348 ms  42.131 ms  42.035 ms  42.006 ms
16  137.164.26.241 (137.164.26.241)  43.314 ms  43.287 ms  43.264 ms  43.243 ms  44.799 ms  44.776 ms  45.598 ms  45.575 ms  45.554 ms  44.688 ms
17  csee-west-rtr-vl12.SUNet (171.66.0.238)  43.083 ms  43.057 ms  42.981 ms  42.626 ms  42.530 ms  42.499 ms  42.378 ms  44.225 ms  44.179 ms  44.142 ms
18  * ee.stanford.edu (171.67.72.13)  44.059 ms *  43.361 ms  43.277 ms  43.230 ms  43.192 ms  43.158 ms  43.124 ms  42.680 ms
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
