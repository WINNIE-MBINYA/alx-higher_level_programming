#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints information about a python list
 * @p: PyObject
 * 
 *Return: void 
 */

void print_python_list_info(PyObject *p)
{
    long int size, j;
    PyListObject *list;
    PyObject *item;

    size = Py_SIZE(y);
    printf("[*] Size of the Python List = %ld\n", size);

    list = (PyListObject *)y;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (j = 0; j < size; j++)
    {
        item = PyList_GetItem(y, j);
        printf("Element %ld: %s\n", j, Py_TYPE(item)->tp_name);
    }
}
