import time
start_time = time.time()
def print_elapsed_time():
    elapsed_time = time.time() - start_time
    if elapsed_time < 0.1:
        print("%s ms" % float("%.3g" % (elapsed_time * 1000)))
    else:
        print("%s s" % float("%.3g" % elapsed_time))

file = open("inputs/input_test.txt", "r")


print("%s seconds" % (time.time() - start_time))