# A simple async file processor WIP
#### a finite state machine inspired by the [_Elm Architecture_](https://guide.elm-lang.org/architecture/)
***
#### the app has 4 states: 
- listen
- process
- send
- failure

***
#### issues:
`main/7ffcede`

[TypeError: an integer is required](https://youtrack.jetbrains.com/issue/PY-50572)
```
Traceback (most recent call last):
  File "_pydevd_bundle/pydevd_cython.pyx", line 1589, in _pydevd_bundle.pydevd_cython.ThreadTracer.__call__
  File "_pydevd_bundle/pydevd_cython.pyx", line 656, in _pydevd_bundle.pydevd_cython.PyDBFrame.trace_dispatch
TypeError: an integer is required
```
Workaround:
`PYDEVD_USE_CYTHON=NO`
