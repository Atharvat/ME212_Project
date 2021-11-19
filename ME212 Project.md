# ME212 Project

#### Name:

Atharva Tagalpallewar

#### Roll Number:

200107089

#### Type:

Type 1 (Small problem of Solid Mechanics solved using any software package or writing a code in any platform)

#### Language and Technologies Used

Python, Jupyter Notebook, Matlplotlib library (for plotting graphs)

#### GitHub URL for the project

[Atharvat/ME212_Project (github.com)](https://github.com/Atharvat/ME212_Project)  (https://github.com/Atharvat/ME212_Project)

##### Important Note: To run the code for this project, Python need to be installed on the PC. If Jupyter Notebooks is installed, run the 'index.ipynb' file, and if Jupyter Notebooks is not installed, run the 'index.py' file.



## Question

The cantilever beam AB is of uniform cross section and carries a load P at its free end A (Fig. 1). Determine the equation of the elastic curve and the deflection and slope at A and plot the graphs for the deflection and slope of the beam.

![Figure 1](C:\Users\tagal\Downloads\imageedit_2_8943395654.png)

<div style="text-align: center">Figure 1</div>

## Solution

![](C:\Users\tagal\Downloads\imageedit_2_7336868619.png)

<div style="text-align: center">Figure 2</div>

Using the free-body diagram of the portion AC of the beam (Fig. 2), where $C$ is located at a distance $x$ from end $A$,
$$
M = −Px
$$
We know, the differential equation for the elastic curve is given by
$$
\frac{d^2y}{dx^2} = \frac{M(x)}{EI}
$$
Substituting for $M$ from $Eq. (1)$ into $Eq. (2)$ and multiplying both members by the constant $EI$ gives
$$
EI\frac{d^2y}{dx^2} = −Px
$$
Integrating in $x$,
$$
EI \frac{dy}{dx} = - \frac{1}{2} Px^2 + C_1
$$


![](C:\Users\tagal\Downloads\imageedit_2_9658165469.png)

<div style="text-align: center">Figure 3</div>



Now at the fixed end $B$,  $x = L$ and  $θ = \frac{dy}{dx} = 0$ (Fig. 3).
Substituting these values into $Eq. (4$) and solving for $C_1$ gives
$$
C_1 = \frac{1}{2}PL^2
$$

which we carry back into $Eq. (4)$:
$$
EI \frac{dy}{dx} = −\frac{1}{2}Px^2 + \frac{1}{2}PL^2
$$
Integrating both members,
$$
EI y = −\frac{1}{6}Px^3 + \frac{1}{2}PL^2x + C_2
$$
But at B, $x = L$,  $ y = 0$. Substituting into $Eq. (7)$,
$$
0 = −\frac{1}{6}Px^3 + \frac{1}{2}PL^2x + C_2
$$

$$
C_2 = −\frac{1}{3}PL^3
$$


Carrying the value of $C_2$ back into $Eq. (7)$, <u>the equation of the elastic curve is</u>
$$
EI y = −\frac{1}{6}Px^3 + \frac{1}{2}PL^2x −\frac{1}{3}PL^3
$$
or
$$
y =\frac{P}{6EI} (−x^3 + 3L^2x − 2L^3)
$$

The deflection and slope at $A$ are obtained by letting $x = 0$ in $Eqs.$ $(11)$ and $(6)$
$$
y_A = −\frac{PL^3}{3EI}
$$
and 
$$
θ_A = \left(\frac{dy}{dx}\right)_A = \frac{PL^2}{2EI}
$$


## Code

![image-20211119232105693](C:\Users\tagal\AppData\Roaming\Typora\typora-user-images\image-20211119232105693.png)

![image-20211119232206763](C:\Users\tagal\AppData\Roaming\Typora\typora-user-images\image-20211119232206763.png)

![image-20211119232313537](C:\Users\tagal\AppData\Roaming\Typora\typora-user-images\image-20211119232313537.png)

![image-20211119232334297](C:\Users\tagal\AppData\Roaming\Typora\typora-user-images\image-20211119232334297.png)

So, for $P =  100 N, L =  10 m, E =  20000 Pa, I =  10 kg*m^2$: The value of deflection at $A$ is <u>-0.167m</u> and slope at $A$ is <u>0.0025 radians</u>.

# Thank You!
