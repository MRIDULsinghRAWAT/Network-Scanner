#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import datetime

# This script expects two arguments: the path to the Nmap XML file and the path for the output summary file.

def parse_nmap_xml(xml_file):
    """Parses the Nmap XML file and extracts host and port details."""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except FileNotFoundError:
        return []

    results = []

    for host in root.findall('host'):
        addr_element = host.find('address')
        if addr_element is None:
            continue
        
        ip_addr = addr_element.get('addr')
        host_status = host.find('status').get('state')
        
        host_data = {
            'ip': ip_addr,
            'status': host_status,
            'ports': []
        }

        ports = host.find('ports')
        if ports is not None:
            for port in ports.findall('port'):
                state = port.find('state').get('state')
                
                if state == 'open':
                    port_id = port.get('portid')
                    protocol = port.get('protocol')
                    
                    service = port.find('service')
                    service_name = service.get('name') if service is not None else 'unknown'
                    service_version = service.get('version') if service is not None and service.get('version') else 'N/A'
                    
                    host_data['ports'].append({
                        'protocol': protocol,
                        'port_id': port_id,
                        'service': service_name,
                        'version': service_version
                    })
        
        results.append(host_data)
    return results

def write_summary(data, output_file):
    """Writes the parsed data to a simple text summary file."""
    print(f"\nWriting clean summary to {output_file}...")
    
    with open(output_file, 'w') as f:
        f.write("--- Automated Nmap Vulnerability Summary ---\n")
        f.write(f"Scan Run Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        found_vulnerabilities = False

        for host in data:
            f.write(f"=================================================\n")
            f.write(f"HOST: {host['ip']} | Status: {host['status'].upper()}\n")
            f.write(f"=================================================\n")
            
            if host['status'] != 'up':
                f.write(f"Note: Host is reported as {host['status']} and will not be analyzed further.\n\n")
                continue

            if not host['ports']:
                f.write("No open ports found.\n\n")
                continue

            found_vulnerabilities = True
            f.write("OPEN PORTS FOUND:\n")
            for p in host['ports']:
                f.write(f"  - {p['port_id']}/{p['protocol']} ({p['service']}) | Version: {p['version']}\n")
            f.write("\n")
            
        if not found_vulnerabilities:
            f.write("SUCCESS: No open ports found on active hosts.\n")
            
    print(f"Summary generated successfully: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 parse_nmap_xml.py <path_to_xml_file> <path_to_output_file>")
        sys.exit(1)

    xml_path = sys.argv[1]
    output_path = sys.argv[2]

    parsed_data = parse_nmap_xml(xml_path)
    if parsed_data:
        write_summary(parsed_data, output_path)
