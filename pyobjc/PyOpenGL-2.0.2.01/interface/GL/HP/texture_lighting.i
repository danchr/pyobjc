/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module texture_lighting

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.HP.texture_lighting Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_HP_texture_lighting)

#endif
%}

/* FUNCTION DECLARATIONS */


/* CONSTANT DECLARATIONS */
#define    GL_TEXTURE_LIGHTING_MODE_HP 0x8167
#define    GL_TEXTURE_POST_SPECULAR_HP 0x8168
#define     GL_TEXTURE_PRE_SPECULAR_HP 0x8169


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_HP_texture_lighting)

#endif
	NULL
};

#define glInitTextureLightingHP() InitExtension("GL_HP_texture_lighting", proc_names)
%}

int glInitTextureLightingHP();
DOC(glInitTextureLightingHP, "glInitTextureLightingHP() -> bool")

%{
PyObject *__info()
{
	if (glInitTextureLightingHP())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
