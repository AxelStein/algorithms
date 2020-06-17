def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]


# Complexity: O(log n)
def max_heapify(arr, n, i):
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2
	if left < n and arr[largest] < arr[left]:
		largest = left
	if right < n and arr[largest] < arr[right]:
		largest = right
	if largest != i:
		swap(arr, i, largest)
		max_heapify(arr, n, largest)


# Complexity: O(n)
def build_heap(arr):
	i = len(arr) // 2
	while i >= 0:
		max_heapify(arr, len(arr), i)
		i -= 1


# Complexity: O(n log n)
def heap_sort(arr):
	build_heap(arr)
	i = len(arr) - 1
	while i > 0:
		# swap root and last item
		swap(arr, 0, i)
		# heapify from root
		max_heapify(arr, i, 0)
		i -= 1


a = [1, 3, 8, 4, 5, 2]
heap_sort(a)
print(a)
