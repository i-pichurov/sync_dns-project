def stylish_result(dns_list):
    stylish_result = []
    for ns_node in dns_list:
        for dns in ns_node['dns_records']:
            stylish_result.append(f"{ns_node['ns_server']} "
                                  f"{dns['record_name']} "
                                  f"{dns['record_type']} "
                                  f"{dns['record_value']}\n")
        stylish_result.append("\n")
    return "".join(stylish_result).rstrip()
