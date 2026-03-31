import importlib.util, sys, time, os
from pathlib import Path

# always run relative to this file's location
os.chdir(Path(__file__).parent)

test = '--test' in sys.argv

day = sys.argv[1]
path = os.path.join(f'day{day}', f'{"test" if test else "actual"}_input.txt')
spec = importlib.util.spec_from_file_location(f'day{day}', os.path.join(f'day{day}', f'day{day}.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

start = time.perf_counter()
p1, p2 = mod.solve(path)
elapsed = (time.perf_counter() - start) * 1000

print(f"Day {day} {'(test)' if test else ''}")
print(f"Part 1: {p1 if p1 is not None else 'not implemented'}")
print(f"Part 2: {p2 if p2 is not None else 'not implemented'}")
print(f"Time:   {elapsed:.2f}ms")