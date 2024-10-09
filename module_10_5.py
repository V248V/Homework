from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            string = file.readline()
            if not string:
                break
            all_data.append(string)


file_list = [f'.\\Files\\file {i}.txt' for i in range(1, 5)]

# start = datetime.now()
# for file in file_list:
#     read_info(file)
# end = datetime.now()
# print(end - start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, file_list)
        end = datetime.now()
        print(end - start)
