#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static const void* 
mod_retain(const void* info) 
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_INCREF((PyObject*)info);
	PyGILState_Release(state);
	return info;
}

static void
mod_release(const void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_DECREF((PyObject*)info);
	PyGILState_Release(state);
}


static CFMachPortContext mod_CFMachPortContext = {
	0,		
	NULL,
	mod_retain,
	mod_release,
	NULL
};

static void
mod_CFMachPortCallBack(	
	CFMachPortRef f,
	void* msg,
	CFIndex size,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFMachPortRef), &f);
	PyObject* py_msg = PyString_FromStringAndSize(msg, size);
	PyObject* py_size = PyLong_FromLongLong(size);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GET_ITEM(info, 0),
		"NNNO", py_f, py_msg, py_size, PyTuple_GET_ITEM(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static void 
mod_CFMachPortInvalidationCallBack(CFMachPortRef f, void *_info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFMachPortRef), &f);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GET_ITEM(info, 2),
		"NO", py_f, PyTuple_GET_ITEM(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}


static PyObject*
mod_CFMachPortCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* callout;
	PyObject* info;
	PyObject* py_shouldFree = Py_None;
	CFAllocatorRef allocator;
	Boolean shouldFree;

	if (!PyArg_ParseTuple(args, "OOO|O", &py_allocator, &callout, &info, &py_shouldFree)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	if (py_shouldFree != Py_None && py_shouldFree != PyObjC_NULL) {
		PyErr_SetString(PyExc_ValueError, 
				"shouldFree not None or NULL");
		return NULL;
	}

	CFMachPortContext context = mod_CFMachPortContext;
	context.info = Py_BuildValue("OOO", callout, info, Py_None);
	if (context.info == NULL) {
		return NULL;
	}

	CFMachPortRef rv = NULL;
	PyObjC_DURING
		rv = CFMachPortCreate(
			allocator, 
			mod_CFMachPortCallBack, &context, &shouldFree);
		

	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);

	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  Py_BuildValue("OO",
			PyObjC_ObjCToPython(@encode(CFMachPortRef), &rv),
			PyBool_FromLong(shouldFree));

	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}

static PyObject*
mod_CFMachPortCreateWithPort(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_port;
	PyObject* callout;
	PyObject* info;
	PyObject* py_shouldFree = Py_None;
	CFAllocatorRef allocator;
	mach_port_t port;
	Boolean shouldFree;

	if (!PyArg_ParseTuple(args, "OOOO|O", &py_allocator, &py_port, &callout, &info, &py_shouldFree)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(mach_port_t), py_port, &port) < 0) {
		return NULL;
	}

	if (py_shouldFree != Py_None && py_shouldFree != PyObjC_NULL) {
		PyErr_SetString(PyExc_ValueError, 
				"shouldFree not None or NULL");
		return NULL;
	}

	CFMachPortContext context = mod_CFMachPortContext;
	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFMachPortRef rv = NULL;
	PyObjC_DURING
		rv = CFMachPortCreateWithPort(
			allocator, 
			port,
			mod_CFMachPortCallBack, &context, &shouldFree);
		

	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);

	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  Py_BuildValue("OO",
			PyObjC_ObjCToPython(@encode(CFMachPortRef), &rv),
			PyBool_FromLong(shouldFree));

	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}


static PyObject*
mod_CFMachPortGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_f;
	PyObject* py_context = NULL;
	CFMachPortRef f;
	CFMachPortContext context;

	if (!PyArg_ParseTuple(args, "O|O", &py_f, &py_context)) {
		return NULL;
	}

	if (py_context != NULL &&  py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFMachPortRef), py_f, &f) < 0) {
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFMachPortGetContext(f, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (context.version != 0) {
		PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
		return NULL;
	}

	if (context.retain != mod_retain) {
		PyErr_SetString(PyExc_ValueError, 
			"retrieved context is not supported");
		return NULL;
	}

	Py_INCREF(PyTuple_GET_ITEM((PyObject*)context.info, 1));
	return PyTuple_GET_ITEM((PyObject*)context.info, 1);
}

/*
 * Invalidation callbacks are supported only on MachPorts created from Python.
 */
static PyObject*
mod_CFMachPortSetInvalidationCallBack(
		PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_port;
	PyObject* callout;
	CFMachPortRef port;

	if (!PyArg_ParseTuple(args, "OO", &py_port, &callout)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFMachPortRef), py_port, &port) < 0) {
		return NULL;
	}

	CFMachPortContext context;
	context.version = 0;

	PyObjC_DURING
		CFMachPortGetContext(port, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (context.version != 0 || context.retain != mod_retain) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	Py_DECREF(PyTuple_GET_ITEM((PyObject*)context.info, 2));
	Py_INCREF(callout);
	PyTuple_SET_ITEM((PyObject*)context.info, 2, callout);


	PyObjC_DURING
		CFMachPortSetInvalidationCallBack(port, mod_CFMachPortInvalidationCallBack);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject*
mod_CFMachPortGetInvalidationCallBack(
		PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_port;
	CFMachPortRef port;

	if (!PyArg_ParseTuple(args, "O", &py_port)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFMachPortRef), py_port, &port) < 0) {
		return NULL;
	}

	CFMachPortContext context;
	context.version = 0;

	PyObjC_DURING
		CFMachPortGetContext(port, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (context.version != 0 || context.retain != mod_retain) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}


	CFMachPortInvalidationCallBack rv = NULL;

	PyObjC_DURING
		rv = CFMachPortGetInvalidationCallBack(port);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (rv == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	if (rv == mod_CFMachPortInvalidationCallBack) {
		PyObject* result = PyTuple_GET_ITEM((PyObject*)context.info, 2);
		Py_INCREF(result);
		return result;
	}

	PyErr_SetString(PyExc_ValueError,
			"Unsupported value for invalidate callback");
	return NULL;
}

static PyMethodDef mod_methods[] = {
        {
		"CFMachPortCreate",
		(PyCFunction)mod_CFMachPortCreate,
		METH_VARARGS,
		NULL
	},
        {
		"CFMachPortCreateWithPort",
		(PyCFunction)mod_CFMachPortCreateWithPort,
		METH_VARARGS,
		NULL
	},
        {
		"CFMachPortGetContext",
		(PyCFunction)mod_CFMachPortGetContext,
		METH_VARARGS,
		NULL
	},
        {
		"CFMachPortSetInvalidationCallBack",
		(PyCFunction)mod_CFMachPortSetInvalidationCallBack,
		METH_VARARGS,
		NULL
	},
        {
		"CFMachPortGetInvalidationCallBack",
		(PyCFunction)mod_CFMachPortGetInvalidationCallBack,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_CFMachPort",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__CFMachPort(void);

PyObject*
PyInit__CFMachPort(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_CFMachPort(void);

void
init_CFMachPort(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_CFMachPort", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	INITDONE();
}
