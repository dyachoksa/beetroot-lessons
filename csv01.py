import csv

def select_by_src(data, src_ip):
    if data["src_ip"] == src_ip:
        return data["src_port"]
    return 0


def main(filename):
    with open(filename) as f:
        data_reader = csv.DictReader(f, fieldnames=[
            "date", "v", "src_ip", "src_port", "dst_ip", "dst_port",
        ], delimiter="\t")
        data = []
        data1 = set(map(lambda x:x["src_ip"], data_reader))

        f.seek(0)
        data_reader = csv.DictReader(f, fieldnames=[
            "date", "v", "src_ip", "src_port", "dst_ip", "dst_port",
        ], delimiter="\t")
        data2 = set(map(lambda x:x["src_port"], data_reader))
        
    # print(data)

    # data1 = set(map(lambda x:x["src_ip"], data))
    print(data1)
    print(data2)


if __name__ == "__main__":
    main("net.log")
