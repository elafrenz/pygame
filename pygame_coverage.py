import sys

def main():
    file_to_read = 'convert_coverage.txt_out'        #change to name of file to read
    print("filename: ", file_to_read)
    file1 = open(file_to_read, 'r')

    unique_lines = set()

    while True:
        line = file1.readline()
        
        if not line:
            break
        unique_lines.add(line)

    file1.close()

    #open("output.py", 'w').write(str(len(unique_lines)))
    print("number of lines covered: ", len(unique_lines))


if __name__ == '__main__':
    main()
