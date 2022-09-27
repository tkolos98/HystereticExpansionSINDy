This package can be used together with the package PySindy to identify the system dynamics of two-step controller driven systems.
With the help of the package, so-called hysterion functions can be defined, which are resembling the dynamics of such a controller.

The function returns one or zero based on the state of the memory incorporated in the function object. The memory is refreshed if a switch-point, given by the user, is reached. Lower switch-points (alpha) are setting it to zero and upper switch-points (beta) are setting it to one.

To ensure proper working, a hysterion function should be defined for each input variable. Therefore each input variable acquire an own memory variable in their respective functions. These functions are then each used to define an own pySindy.customLibrary() and those are then concatenated by a pySindy.generalizedLibrary(). 

These steps are important, as the feature of input selection in pysindy.generalizedLibrary() is used to restrict access of the functions to their own respective variables. This is important to ensure proper addressing during the use of the functions during simulation. Please refer to the example of use in the folder. An automation of these steps are in progress.

The resulting library can be then freely concatenated or tensored with others to build the final library, which is then used for the identification. 

The hysterion functions are implementing a proxymity detection as well, which helps the detection of switch-over points in a noisy data set. In this case, not only the exceeding of the switch-point values are treated as switch-over points, but also the reach of local extremas within a set proximity of them. Therefore if the switch-point value is not reached due to the noise, the switch-over can be still detected approximately. The proximity can be set by the user upon definition of the function.

The memory of the functions can be reset with the help of reset_memory(). They can be set to a custom value by the user, during changeover it will be set to zero or one accordingly.

The function get_history() returns the values returned by the function during simulation. After training, this array is reset. This can be also done with the function reset_memory().  


The idea used here is based on the work: G. Thiele, A. Fey, D. Sommer and J. Krüger, "System identification of a hysteresis-controlled pump system using SINDy," 2020 24th International Conference on System Theory, Control and Computing (ICSTCC), 2020, pp. 457-464, doi: 10.1109/ICSTCC50638.2020.9259776.

For PySindy and its creators please see the documentations at https://pysindy.readthedocs.io/en/latest/

It was described in the works:

Brian M. de Silva, Kathleen Champion, Markus Quade, Jean-Christophe Loiseau, J. Nathan Kutz, and Steven L. Brunton., (2020). PySINDy: A Python package for the sparse identification of nonlinear dynamical systems from data. Journal of Open Source Software, 5(49), 2104, https://doi.org/10.21105/joss.02104

and

Kaptanoglu et al., (2022). PySINDy: A comprehensive Python package for robust sparse system identification. Journal of Open Source Software, 7(69), 3994, https://doi.org/10.21105/joss.03994


This package was created as part of the Bachelor's thesis of Kolos Töreki
