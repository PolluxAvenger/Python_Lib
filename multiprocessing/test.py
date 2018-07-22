# coding=utf-8

def exec_process_result(result):
    process_result.append(result)


def execute_input(input_data):
    ...
	return input_data


if __name__ == "__main__":
	cpu_count = multiprocessing.cpu_count()
	# 创建进程池
    process_executor = multiprocessing.Pool(int(cpu_count))
	进程池多进程执行样本
    for one_input in input_list:
        # 异步多进程执行样本
        process_executor.apply_async(execute_input, (one_input,), callback=exec_process_result)

    # 等待所有子进程执行完
    process_executor.close()
    process_executor.join()
	