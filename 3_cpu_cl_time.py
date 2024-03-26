from flatspin import SquareSpinIceClosed
import timeit

model_cpu = SquareSpinIceClosed(size=(100, 100))
cpu_time = timeit.timeit(lambda: model_cpu.dipolar_fields(), number=1)
print(f"CPU Time: {cpu_time} seconds")

model_gpu = SquareSpinIceClosed(size=(100, 100), use_opencl=True)
gpu_time = timeit.timeit(lambda: model_gpu.dipolar_fields(), number=1)
print(f"GPU Time: {gpu_time} seconds")
