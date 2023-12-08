from aoc_helper import fetch, run

class Solution:
    def __init__(self):
        self.data = list(map(int, fetch("02", "2019").split(",")))
    
    def run_program(self, data):
        for i in range(0, len(data), 4):
            opcode, in1, in2, out = data[i:i + 4]
            if min(in1, in2, out) < 0 or len(data) <= max(in1, in2, out):
                break
            if opcode == 1:
                data[out] = data[in1] + data[in2]
            elif opcode == 2:
                data[out] = data[in1] * data[in2]
            else:
                break
        return data[0]
    
    def calculate_p1(self):
        data = self.data[:]
        data[1], data[2] = 12, 2
        return self.run_program(data)

    def calculate_p2(self):
        target = 19690720
        for noun in range(100):
            for verb in range(100):
                data = self.data[:]
                data[1], data[2] = noun, verb
                result = self.run_program(data)
                if result == target:
                    return 100 * noun + verb

if __name__ == "__main__":
  run(Solution)
