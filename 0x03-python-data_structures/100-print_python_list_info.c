#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t listsze;
	long size, i;
	PyObject *item;

	size = Py_SIZE(listsze);
	listsze = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", lstsze);
	printf("[*] Allocated = %d\n", size);
	for (i = 0; i < listsze; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

