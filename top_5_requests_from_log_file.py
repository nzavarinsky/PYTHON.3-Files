import re

date_range_pattern = r'.*01\/Jul\/1995:0(2:(3[5-9]|[4-5][0-9])|3:(0[0-9]|1[0-7])).* 200 .*\n'
logs_counter = 0
top_requests = {}

for line in open('acces_log_Jul95.log', 'r').readlines():
    match = re.compile(date_range_pattern).match(line)
    if match:
        logs_counter += 1
        request_line = re.search(r'\".*?\"', line).group(0)
        if request_line in top_requests:
            top_requests[request_line] = top_requests[request_line] + 1
        else:
            top_requests[request_line] = 1

print(logs_counter)

top_requests = sorted(top_requests.items(), key=lambda x: x[1], reverse=True)

for key, value in top_requests[0:5]:
    print(key + ' - ' + str(value))
