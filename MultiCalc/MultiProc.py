from multiprocessing import Process, Queue


class MultiProc:
    def __init__(self, process_function, input_data, output_data=None):
        self.__process_function = process_function
        self.__input_data = input_data
        if output_data:
            self.__output_data = output_data
        else:
            self.__output_data = list()

    @staticmethod
    def _wrapper(func, input, res_queue):
        res = func(input)
        res_queue.put({"input": input, "res": res})

    def process(self):
        process_pool = list()
        queue = Queue()
        for data in self.__input_data:
            process = Process(target=MultiProc._wrapper, args=(self.__process_function, data, queue,))
            process.start()
            process_pool.append(process)
        pool_count = len(process_pool)
        ready_count = 0
        for process in process_pool:
            self.__output_data.append(queue.get())
            ready_count += 1
            print(ready_count / pool_count * 100)
        for process in process_pool:
            process.join()
        return self.__output_data
