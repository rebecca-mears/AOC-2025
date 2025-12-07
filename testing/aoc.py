"""By https://github.com/JoRdAnB421"""

import csv
import time


class aoc:
    def __init__(self, day, delimiter=" ", repetition=10, file_ext="csv"):
        self.part = 0
        self.repetition = repetition

        t0 = time.time()
        self.data = self.read(day, delimiter, file_ext)
        t1 = time.time()
        self.time = t1 - t0
        print(f"Time to read: {self.time:.3f}s")

    def read(self, day, delimiter, file_ext):
        with open(f"testing/Inputs/day{day}.{file_ext}") as f:
            if delimiter is None:
                return f.read()
            reader = csv.reader(f, delimiter=delimiter)
            data = [row for row in reader]
        return data

    def run(self, func):
        """Requires the daily part functions to accept 'data'"""
        times = []
        for _ in range(self.repetition):
            t0 = time.time()
            answer = func(self.data)
            t1 = time.time()
            times.append(t1 - t0)

        mean_time = sum(times) / len(times)
        if self.repetition > 1:
            variance = sum([(t - mean_time) ** 2 for t in times]) / (len(times) - 1)
        else:
            variance = float("inf")

        self.part += 1
        self.time += mean_time
        print(
            f"Part {self.part} answer: {answer} (in {mean_time:.5f} +- {variance**0.5:.1e}s)"
        )

        if self.part == 2:
            print(f"----\nTotal time: {self.time:.3f}s")
