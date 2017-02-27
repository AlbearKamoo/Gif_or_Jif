data = {'G': 0, 'JH': 0, 'ZH': 0, 'GI': 0, 'JHI': 0, 'ZHI': 0}


def parse_line(line):
    items = line.split()
    #print(items)
    if '(' in items[0]:
        return
    else:
        collect_data(items);

def collect_data(items):
    try:
        data[items[1]] += 1
        if items[0][:2] == 'GI':
            data[items[1]+'I'] += 1
    except KeyError as e:
        print("KeyError, word pronounciation begins with: " + str(e))

def analyze_file(filename='phoneticdb.txt'):
    with open('phoneticdb.txt', 'r') as infile:
        for line in infile:
            parse_line(line)
    return data 

if __name__ == "__main__":
    lines = 0
    with open('phoneticdb.txt', 'r') as infile:
        for line in infile:
            lines += 1
            parse_line(line)
    print(data)
    print(lines)
    print(data['G'] + data['JH'])
