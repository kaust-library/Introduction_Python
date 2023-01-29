#
# Create an Icinga host configuration file a list in the format
# hostname, IP address
#

import jinja2 as J2


def main():

    environment = J2.Environment(loader=J2.FileSystemLoader("temps/"))
    template = environment.get_template("hostconfig.j2")

    # Read file with the hosts list
    with open("in/hosts.txt", "r") as fin:
        text = fin.readlines()
    hosts = [line.strip().split(",") for line in text]

    for host in hosts:

        hostname = host[0]
        ip_addr = host[1]
        content = template.render(hostname=hostname, ip_addr=ip_addr)

        with open(f"out/{hostname}.cfg", "w") as fout:
            fout.write(content)
            print(f"Wrote {hostname}")


if __name__ == "__main__":

    main()
