import threading
import time

def code(lines):
    print("You started coding")
    time.sleep(lines*2)
    print("You finished ", lines, " of coding")
    
def eat(cals):
    print("You started eating")
    time.sleep(cals//20)
    print("You have eaten ", cals, " calories")

def lift(reps):
    print("You started lifting")
    time.sleep(reps)
    print("You have lifted ", reps, " times")

x = threading.Thread(target=code, args=(3))
x.start()

y = threading.Thread(target=eat, args=(100))
y.start()

z = threading.Thread(target=lift, args=(8))
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
