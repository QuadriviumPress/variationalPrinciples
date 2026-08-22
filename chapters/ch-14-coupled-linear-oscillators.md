---
title: "14. Coupled Linear Oscillators"
short_title: "Chapter 14"
label: ch-14-coupled-linear-oscillators
---


# 14. Coupled Linear Oscillators

(ch-14)=

## 14.1: Introduction to Coupled Linear Oscillators

Chapter $3$ discussed the behavior of a single linearly-damped linear oscillator subject to a harmonic force. No account was taken for the influence of the single oscillator on the driver for the case of forced oscillations. Many systems in nature comprise complicated free or forced oscillations of coupled-oscillator systems. Examples of coupled oscillators are; automobile suspension systems, electronic circuits, electromagnetic fields, musical instruments, atoms bound in a crystal, neural circuits in the brain, networks of pacemaker cells in the heart, etc. Energy can be transferred back and forth between coupled oscillators as the motion evolves. However, it is possible to describe the motion of coupled linear oscillators in terms of a sum over independent normal coordinates, i.e. normal modes, even though the motion may be very complicated. These normal modes are constructed from the original coordinates in such a way that the normal modes are uncoupled. The topic of finding the normal modes of coupled oscillator systems is a ubiquitous problem encountered in all branches of science and engineering. As discussed in chapter $3$, oscillatory motion of non-linear systems can be complicated. Fortunately most oscillatory systems are approximately linear when the amplitude of oscillation is small. This discussion assumes that the oscillation amplitudes are sufficiently small to ensure linearity.

## 14.2: Two Coupled Linear Oscillators

Consider the two-coupled linear oscillator, shown in Figure 14.1, which comprises two identical masses each connected to fixed locations by identical springs having a force constant $\kappa$. A spring with force constant $\kappa^{\prime}$ couples the two oscillators. The equilibrium lengths of the outer two springs are $l$ while that of the coupling spring is $l^{\prime}$. The problem is simplified by restricting the motion to be along the line connecting the masses and assuming fixed endpoints. The small displacements of $m_1$ and $m_2$ are taken to be $x_1$ and $x_2$ with respect to the equilibrium positions $l$ and $l + l^{\prime}$ respectively. The restoring force on $m_1$ is $−\kappa x_1−\kappa^{\prime} (x_1 − x_2)$ while the restoring force on $m_2$ is $−\kappa x_2 − \kappa^{\prime} (x_2 − x_1)$. This coupled double-oscillator system exhibits basic features of coupled linear oscillator systems.

:::{figure} ../images/lt-21225-12.2.1.png
:alt: 12.2.1.PNG

$1$: Two coupled linear oscillators. The equilibrium spring-lengths are $l$ for the outer springs and $l^{\prime}$ for the coupling spring. The displacement from the stable locations are given by $x_1$ and $x_2$. The separation between the two masses is $r$ and the location of the center-of-mass is $R_{cm}$.
:::

Assuming $m_1 = m_2 = m$, then the equations of motion are

$$
\begin{align} m\ddot{x}_1 + (\kappa + \kappa^{\prime} ) x_1 − \kappa^{\prime} x_2 = 0 \label{14.1} \\ \notag m\ddot{x}_2 + (\kappa + \kappa^{\prime} ) x_2 − \kappa^{\prime} x_1 = 0 \notag\end{align}
$$

Assume that the motion for these coupled equations is oscillatory with a solution of the form

$$
\begin{align} x_1 = B_1 e^{i\omega t} \label{14.2}\\ x_2 = B_2e^{i\omega t} \notag\notag\end{align}
$$

where the constants $B$ may be complex to take into account both the magnitude and phase. Substituting these possible solutions into the equations of motion gives

$$
\begin{align} −m\omega^2 B_1 e^{i\omega t} + (\kappa + \kappa^{\prime} ) B_1e^{i\omega t} − \kappa^{\prime} B_2e^{i\omega t} = 0 \label{14.3}\\ −m\omega^2B_2 e^{i\omega t} + (\kappa + \kappa^{\prime} ) B_2e^{i\omega t} − \kappa^{\prime} B_1 e^{i\omega t} = 0 \notag\end{align}
$$

Collecting terms, and cancelling the common exponential factor, gives

$$
\begin{align} (\kappa + \kappa^{\prime} − m\omega^2) B_1 − \kappa^{\prime} B_2 = 0 \label{14.4} \\ ( \kappa + \kappa^{\prime} − m\omega^2 ) B_2 − \kappa^{\prime} B_1 = 0 \notag\end{align}
$$

The existence of a non-trivial solution of these two simultaneous equations requires that the determinant of the coefficients of $B_1$ and $B_2$ must vanish, that is

$$
\begin{vmatrix} \kappa + \kappa^{\prime} − m\omega^2 & −\kappa^{\prime} \\ −\kappa^{\prime} & \kappa + \kappa^{\prime} − m\omega^2 \end{vmatrix} = 0 \label{14.5}
$$

The expansion of this secular determinant yields

$$
( \kappa + \kappa^{\prime} − m\omega^2 )^2 − \kappa^{\prime 2} = 0 \label{14.6}
$$

Solving for $\omega$ gives

$$
\omega = \sqrt{\frac{\kappa + \kappa^{\prime} \pm \kappa^{\prime}}{m}} \label{14.7}
$$

That is, there are two characteristic frequencies (or eigenfrequencies) for the system

$$
\omega_1 = \sqrt{\frac{\kappa + 2\kappa^{\prime} }{m}} \label{14.8}
$$

$$
\omega_2 = \sqrt{\frac{\kappa}{m}} \label{14.9}
$$

Since superposition applies for these linear equations, then the general solution can be written as a sum of the terms that account for the two possible values of $\omega$.

:::{figure} ../images/lt-21226-12.2.2.png
:alt: 12.2.2.PNG

12.2.2.PNG
:::

Figure 14.2 shows the solutions for a case where $\kappa = 4$ and $\kappa^{\prime} = 1$, in arbitrary units, with the initial condition that $x_2 = D$, and $x_1 = \dot{x}_1 = \dot{x}_2 = 0$. The two characteristic frequencies are $\omega_1 = \sqrt{\frac{6}{m}}$ and $\omega_2 = \sqrt{\frac{4}{m}}$. The characteristic beats phenomenon is exhibited where the envelope over one complete cycle of the low frequency encompasses several higher frequency oscillations. That is, the solution is

$$
x_{2}(t)=\frac{D}{4}\left[e^{i \omega_{1} t}+e^{-i \omega_{1} t}+e^{i \omega_{2} t}+e^{-i \omega_{2} t}\right]=D \cos \left[\left(\frac{\omega_{1}+\omega_{2}}{2}\right) t\right] \cos \left[\left(\frac{\omega_{1}-\omega_{2}}{2}\right) t\right]
$$

while

$$
x_{1}(t)=\frac{D}{4}\left[e^{i \omega_{1} t}+e^{-i \omega_{1} t}-e^{i \omega_{2} t}-e^{-i \omega_{2} t}\right]=D \sin \left[\left(\frac{\omega_{1}+\omega_{2}}{2}\right) t\right] \sin \left[\left(\frac{\omega_{1}-\omega_{2}}{2}\right) t\right]
$$

The energy in the two-coupled oscillators flows back and forth between the coupled oscillators as illustrated in Figure 14.2.

A better understanding of the energy flow occurring between the two coupled oscillators is given by using a $(x_1, x_2)$ configuration-space plot, shown in Figure $14.3.1$. The flow of energy occurring between the two coupled oscillators can be represented by choosing normal-mode coordinates $\eta_1$ and $\eta_2$ that are rotated by $45^{\circ}$ with respect to the spatial coordinates $(x_1, x_2)$. These normal-mode coordinates $(\eta_1, \eta_2)$ correspond to the two normal modes of the coupled double-oscillator system.

## 14.3: Normal Modes

The **normal modes** of the two-coupled oscillator system are obtained by a transformation to a pair of **normal coordinates** $(\eta_1, \eta_2)$ that are independent and correspond to the two normal modes. The pair of normal coordinates for this case are

$$
\begin{align} \eta_1 \equiv x_1 − x_2 \label{14.12}\\ \eta_2 \equiv x_1 + x_2 \notag \end{align}
$$

that is

$$
\begin{align} x_1 = \frac{1}{2} (\eta_2 + \eta_1) \label{14.13}\\ x_2 = \frac{1}{2} (\eta_2 − \eta_1) \notag \end{align}
$$

Substitute these into the equations of motion $(14.2.1)$, gives

$$
\begin{align} m (\ddot{\eta}_1 + \ddot{\eta}_2 ) + (\kappa + 2\kappa^{\prime} ) \eta_1 + \kappa^{\prime} \eta_2 = 0 \\ \notag m (\ddot{\eta}_1 − \ddot{\eta}_2 ) + (\kappa + 2\kappa^{\prime} ) \eta_1 − \kappa^{\prime} \eta_2 = 0 \end{align}
$$

Adding and subtracting these two equations gives

$$
\begin{align} m\ddot{\eta}_1 + (\kappa + 2\kappa^{\prime} ) \eta_1 = 0 \\\notag m\ddot{\eta}_2 + \kappa \eta_2 = 0 \end{align}
$$

Note that the two coordinates $\eta_1$ and $\eta_2$ are uncoupled and therefore are independent. The solutions of these equations are

$$
\begin{align} \eta_1 (t) = C^+_1 e^{i\omega_1 t} + C^−_1 e^{-i\omega_1 t} \\ \eta_2 (t) = C^+_2 e^{i\omega_2 t} + C^−_2 e^{-i\omega_2 t} \end{align}
$$

where $\eta_1$ corresponds to angular frequencies $\omega_1$, and $\eta_2$ corresponds to $\omega_2$. The two coordinates $\eta_1$ and $\eta_2$ are called the **normal coordinates and the two solutions are the normal modes with corresponding angular frequencies,** $\omega_1$ and $\omega_2$.

:::{figure} ../images/lt-21228-12.3.1.png
:alt: 12.3.1.PNG

$1$: Motion of two coupled harmonic oscillators in the $(x_1, x_2)$ spatial configuration space and in terms of the normal modes $(\eta_1, \eta_2)$. Initial conditions are $x_2 = D, x_1 = \dot{x}_1 = \dot{x}_2 = 0$.
:::

The $(\eta_1, \eta_2)$ axes of the two normal modes correspond to a rotation of $45^{\circ}$ in configuration space, Figure 14.1. The initial conditions chosen correspond to $\eta_1 = −\eta_2$ and thus both modes are excited with equal intensity. Note that there are 5 lobes along the $\eta_2$ axis versus 4 lobes along the $\eta_1$ axis reflecting the ratio of the eigenfrequencies $\omega_1$ and $\omega_2$. Also note that the diamond shape of the motion in the $(x_1, x_2)$ configuration space illustrates that the extrema amplitudes for $x_2$ are a maximum when $x_1$ is zero, and vise versa. This is equivalent to the statement that the energies in the two modes are coupled with the energy for the first oscillator being a maximum when the energy is a minimum for the second oscillator, and vise versa. By contrast, in the $(\eta_1, \eta_2)$ configuration space, the motion is bounded by a rectangle parallel to the $(\eta_1, \eta_2)$ axes reflecting the fact that the extrema amplitudes, and corresponding energies, for the $\eta_1$ normal mode are constant and independent of the motion for the $\eta_2$ normal mode, and vise versa. The decoupling of the two normal modes is best illustrated by considering the case when only one of these two normal modes is excited. For the initial conditions $x_1 (0) = −x_2 (0)$, and $\dot{x}_1 (0) = − \dot{x}_2 (0)$, then $\eta_2 (t)=0$. That is, only the $\eta_1 (t)$ normal mode is excited with frequency $\omega_1$ which corresponds to motion confined to the $\eta_1$ axis of Figure 14.1.

:::{figure} ../images/lt-21227-12.3.2.png
:alt: 12.3.2.PNG

$2$: Normal modes for two coupled oscillators.
:::

As shown in Figure 14.2, $\eta_1 (t)$ is the *antisymmetric mode* in which the two masses oscillate out of phase such as to keep the center of mass of the two masses stationary. For the initial conditions $x_1 (0) = x_2 (0)$, and $\dot{x}_1 (0) = \dot{x}_2 (0)$, then $\eta_1 (t)=0$, that is, only the $\eta_2 (t)$ normal mode is excited. The $\eta_2 (t)$ normal mode is the *symmetric mode* where the two masses oscillate in phase with frequency $\omega_2$; it corresponds to motion along the $\eta_2$ axis. For the symmetric phase, both masses move together leading to a constant extension of the coupling spring. As a result the frequency $\omega_2$ of the symmetric mode $\eta_2 (t)$ is lower than the frequency $\omega_1$ of the asymmetric mode $\eta_1 (t)$. That is, the asymmetric mode is stiffer since all three springs provide active restoring forces, compared to the symmetric mode where the coupling spring is uncompressed. In general, for attractive forces the lowest frequency always occurs for the mode with the highest symmetry

## 14.4: Center of Mass Oscillations

Transforming the coordinates into the center of mass of the two oscillating masses elucidates an interesting feature of the normal modes for the two-coupled linear oscillator. As illustrated in Figure $(14.2.1)$, the center-of-mass coordinate for the two mass system is

$$
\begin{align*} 2R_{cm} &= l + x_1 + l + l^{\prime} + x_2 \\[4pt] &= 2l + l^{\prime} + \eta_2 \end{align*}
$$

while the relative separation distance is

$$
r = (l + l^{\prime} + x_2) − (l + x_1) = l^{\prime} − \eta_1\notag
$$

That is, the two normal modes are

$$
\begin{align} \eta_1 = l^{\prime} − r \\ \eta_2 = 2 R_{cm} − 2l − l^{\prime} \notag\end{align}
$$

The $\eta_1$ mode, which has angular frequency $\omega_1 = \sqrt{\frac{\kappa +2\kappa^{\prime}}{M}}$ corresponds to an oscillations of the relative separation $r$, while the center-of-mass location $R_{cm}$ is stationary. By contrast, the $\eta_2$ mode, with angular frequency $\omega_2 = \sqrt{\frac{\kappa}{M}}$ corresponds to an oscillation of the center of mass $R_{cm}$ with the relative separation $r$ being a constant.

:::{figure} ../images/lt-21229-12.4.1.png
:alt: 12.4.1.PNG

$1$: Time dependence of the center-of-mass $R_{cm}$ and relative separation $r$ for two coupled linear oscillators assuming spring constants of $\kappa = 4M$ and $\kappa^{\prime} = M$.
:::

Figure 14.1 illustrates the decoupled center-of-mass $R_{cm}$, and relative motions $r$ for both normal modes of the coupled double-oscillator system. The difference in angular frequencies and amplitudes is readily apparent. It is of interest to consider the special case where the spring constant $\kappa = 0$ for the two outside springs. Then the angular frequencies are $\omega_1 = \sqrt{\frac{2\kappa^{\prime}}{M}}$ and $\omega_2 = 0$ for the two normal modes. When $\kappa = 0$ the $\eta_2$ mode is a spurious center-of-mass mode since it corresponds to an oscillation with $\omega_2 = 0$ in spite of the fact that there are no forces acting on the center of mass. That is, the center-of-mass momentum must be a constant of motion. This spurious center-of-mass oscillation is a consequence of measuring the displacements $(x_1, x_2)$ with respect to an arbitrary external reference that is not related to the center of mass of the coupled system. Spurious center-of-mass modes are encountered frequently in many-body coupled oscillator systems such as molecules and nuclei. In such cases it is necessary to project out the center-of-mass motion to eliminate such spurious solutions as will be discussed later.

## 14.5: Weak Coupling

If one of the two coupled linear oscillator masses is held fixed, then the other free mass will oscillate with a frequency.

$$
\omega_0 = \sqrt{\dfrac{\kappa + \kappa'}{M}} \label{14.18}
$$

The effect of coupling of the two oscillators is to split the degeneracy of the frequency for each mass to

$$
\omega_1 = \sqrt{\dfrac{\kappa + 2\kappa'}{M}} > \omega_0 = \sqrt{\dfrac{\kappa + \kappa'}{M}} > \omega_2 = \sqrt{\dfrac{\kappa}{M}} \label{14.19}
$$

Thus the degeneracy is broken, and the two normal modes have frequencies straddling the single-oscillator frequency.

It is interesting to consider the case where the coupling is weak because this situation occurs frequently in nature. The coupling is weak if the coupling constant $\kappa' \ll \kappa$. Then

$$
\omega_1 = \sqrt{\dfrac{\kappa + 2\kappa'}{M}} = \sqrt{\dfrac{\kappa'}{M}} \sqrt{1+4\varepsilon} \label{14.20}
$$

where

$$
\varepsilon \equiv \dfrac{\kappa'}{2\kappa} \ll 1 \label{14.21}
$$

Thus

$$
\omega_1 \approx \sqrt{\dfrac{\kappa}{M}} (1 + 2 \varepsilon) \label{14.22}
$$

The natural frequency of a single oscillator was shown to be

$$
\omega_0 \approx \sqrt{ \dfrac{\kappa + \kappa'}{M}} \approx \sqrt{\dfrac{\kappa }{M}} (1 + \varepsilon) \label{14.23}
$$

that is

$$
\sqrt{\dfrac{\kappa }{M}} = \omega_o (1 − \varepsilon) \label{14.24}
$$

Thus the frequencies for the normal modes for weak coupling can be written as

$$
\begin{align} \omega_1 &= \sqrt{\dfrac{\kappa }{M}} (1 + 2 \varepsilon) \\[5pt] &\approx \omega_0(1 − \varepsilon) (1 + 2\varepsilon) \\[5pt] &\approx \omega_0 (1 + \varepsilon) \label{14.25} \end{align}
$$

while

$$
\omega_2 = \sqrt{ \dfrac{\kappa }{M}} \approx \omega_0 (1 - \varepsilon) \label{14.26}
$$

That is the two solutions are split equally spaced about the single uncoupled oscillator value given by Equation \ref{14.23}. Note that the single uncoupled oscillator frequency $\omega_0$ depends on the coupling strength $\kappa'$.

This splitting of the characteristic frequencies is a feature exhibited by many systems of $n$ identical oscillators where half of the frequencies are shifted upwards and half downward. If $n$ is odd, then the central frequency is unshifted as illustrated for the case of $n = 3$. An example of this behavior is the Zeeman effect where the magnetic field couples the atomic motion resulting in a hyperfine splitting of the energy levels of the form illustrated.

:::{figure} ../images/lt-10930-12.6.png
:alt: 12.6.png

$1$: Normal-mode frequencies for $n=2$ and $n=3$ weakly-coupled oscillators.
:::

There are myriad examples involving weakly-coupled oscillators applied to musical instruments, physics, and engineering. Weakly coupled oscillators are a dominant theme throughout biology as illustrated by congregations of synchronously flashing fireflies, crickets that chirp in unison, an audience clapping at the end of a performance, networks of pacemaker cells in the heart, insulin-secreting cells in the pancreas, and neural networks in the brain and spinal cord that control rhythmic behaviors such as breathing, walking, and eating. Synchronous motion of a large number of weakly-coupled oscillators often leads to large collective motion of weakly-coupled systems as discussed in chapter $14.12$

Example 14.1: The Grand Piano

The grand piano provides an excellent example of a weakly-coupled harmonic oscillator system that has normal modes. There are either two or three parallel strings per note that are stretched tightly parallel to the top of the horizontal sounding board. The strings press downwards on the bridge that is attached to the top of the sounding board. The strings for each note are excited when struck vertically upwards by a single hammer. In the base section of the piano each note comprises two strings tuned to nearly the same frequency. The coupling of the motion of the strings is via the bridge plus sounding board. Normally, the hammer strikes both strings simultaneously exciting the vertical symmetric mode, not the vertical antisymmetric mode. The bridge is connected to the sounding board which moves the largest amount for the symmetric mode where both strings move the bridge in phase. This strong coupling produces a loud sound. The antisymmetric mode does not move the sounding board much since the strings at the bridge move out of phase. Consequently, the symmetric mode, that is strongly coupled to the sounding board, damps out more rapidly than the antisymmetric mode which is weakly coupled to the sound board and thus has a longer time constant for decay since the radiated sound energy is lower than the symmetric mode.

:::{figure} ../images/lt-10931-imageedit_1_5536154940.png
:alt: imageedit_1_5536154940.png

$2$: Schematic diagram of the action for a grand piano, including the strings, bridge and sounding board. Note that there are either two or three parallel strings per note all hit by a single hammer.
:::

The una-corda pedal (soft pedal) for a grand piano moves the action sideways such that the hammer strikes only one of the two strings, or two of the three strings, resulting in both the symmetric and antisymmetric modes being excited equally. The una-corda pedal produces a characteristically different tone than when the hammer simultaneously hits all the strings; that is, it produces a smaller transient component. The symmetric mode rapidly damps due to energy propagation by the sounding board. Thus the longer lasting antisymmetric mode becomes more prominent when both modes are equally excited using the una-corda pedal. The symmetric and antisymmetric modes have slightly different frequencies and produce beats which also contributes to the different timbre produced using the una-corda pedal. For the mid and upper frequency range, the piano has three strings per note which have one symmetric mode and two separate antisymmetric modes. To further complicate matters, the strings also can oscillate horizontally which couples weakly to the bridge plus sounding board. The strengths that these different modes are excited depend on subtle differences in the shape and roughness of the hammer head striking the strings. Primarily the hammer excites the two vertical modes rather than the horizontal modes.

- [Douglas Cline](http://www.pas.rochester.edu/~cline/Cline_home.htm) ([University of Rochester](http://www.pas.rochester.edu/))

## 14.6: General Analytic Theory for Coupled Linear Oscillators

The discussion of a coupled double-oscillator system in Section $14.5$ has shown that it is possible to select symmetric and antisymmetric normal modes that are independent and each have characteristic frequencies. The normal coordinates for these two normal modes correspond to linear superpositions of the spatial amplitudes of the two oscillators and can be obtained by a rotation into the appropriate normal coordinate system. Extension of this to systems comprising $n$ coupled linear oscillators, requires development of a general analytic theory, that is capable of finding the normal modes and their eigenvalues and eigenvectors. As illustrated for the double oscillator, the solution of many coupled linear oscillators is a classic eigenvalue problem where one has to rotate to the principal axis system to project out the normal modes. The following discussion presents a general approach to the problem of finding the normal coordinates for a system of $n$ coupled linear oscillators.

Consider a conservative system of $n$ coupled oscillators, described in terms of generalized coordinates $q_k$ and $t$ with subscript $k = 1, 2, 3, \ldots, n$ for a system with $n$ degrees of freedom. The coupled oscillators are assumed to have a stable equilibrium with generalized coordinates $q_{k0}$ at equilibrium. In addition, *it is assumed that the oscillation amplitudes are sufficiently small to ensure that the system is linear.*

For the equilibrium position $q_k = q_{k0}$, the Lagrange equations must satisfy

$$
\begin{align} \dot{q}_k = 0 \label{14.27} \\ \ddot{q}_k = 0 \notag \end{align}
$$

Every non-zero term of the form $\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_k}$ in Lagrange’s equations must contain at least either $\dot{q}_k$ or $\ddot{q}_k$ which are zero at equilibrium; thus all such terms vanish at equilibrium. At equilibrium

$$
\left(\frac{\partial L}{\partial q_k}\right)_0 = \left(\frac{\partial T}{\partial q_k}\right)_0 − \left(\frac{\partial U}{\partial q_k}\right)_0 = 0 \label{14.28}
$$

where the subscript $0$ designates at equilibrium.

### Kinetic energy tensor T

In chapter $7.6$ it was shown that, in terms of fixed rectangular coordinates, the kinetic energy for $N$ bodies, with $n$ generalized coordinates, is expressed as

$$
T = \frac{1}{2} \sum^N_{ \alpha =1} \sum^3_{i=1 } m_{\alpha} \dot{x}^2_{\alpha ,i} \label{14.29}
$$

Expressing these in terms of generalized coordinates $x_{\alpha ,i} = x_{\alpha ,i}(q_j , t)$ where $j = 1, 2, ...n$, then the generalized velocities are given by

$$
\dot{x}_{\alpha ,i} = \sum^n_{j=1} \frac{\partial x_{\alpha ,i}}{\partial q_j} \dot{q}_j + \frac{\partial x_{\alpha ,i}}{\partial t} \label{14.30}
$$

As discussed in chapter $7.6$, if the system is **scleronomic** then the partial derivative

$$
\frac{\partial x_{\alpha ,i}}{\partial t} = 0 \label{14.31}
$$

Thus the kinetic energy, Equation \ref{14.29}, of a scleronomic system can be written as a homogeneous quadratic function of the generalized velocities

$$
T = \frac{1}{2} \sum^{n}_{j,k} T_{jk} \dot{q}_j \dot{q}_k \label{14.32}
$$

where the components of the kinetic energy tensor $\mathbf{T}$ are

$$
T_{jk} \equiv \sum^{N}_{\alpha} m_{\alpha} \sum^3_i \frac{ \partial x_{\alpha ,i}}{\partial q_j} \frac{ \partial x_{\alpha ,i}}{\partial q_k} \label{14.33}
$$

Note that if the velocities $\dot{q}$ correspond to translational velocity, then the kinetic energy tensor $\mathbf{T}$ corresponds to an effective mass tensor, whereas if the velocities correspond to angular rotational velocities, then the kinetic energy tensor $\mathbf{T}$ corresponds to the inertia tensor.

It is possible to make an expansion of the $T_{jk}$ about the equilibrium values of the form

$$
T_{jk} (q_1, q_2, ..q_n) = T_{jk} (q_{i0}) + \sum_l \left(\frac{\partial T_{jk}}{\partial q_l}\right)_0 q_l + ... \label{14.34}
$$

Only the first-order term will be kept since the second and higher terms are of the same order as the higher order terms ignored in the Taylor expansion of the potential. Thus, at the equilibrium point, assume that $\left(\frac{\partial T}{\partial q_k} \right)_0 = 0$ where $k = 1, 2, 3, ...n$.

### Potential energy tensor V

Equations \ref{14.28} plus \ref{14.34} imply that

$$
\left(\frac{\partial U}{\partial q_k}\right)_0 = 0 \label{14.35}
$$

where $k = 1, 2, 3, ...n$.

Make a Taylor expansion about equilibrium for the potential energy, assuming for simplicity that the coordinates have been translated to ensure that $q_k = 0$ at equilibrium. This gives

$$
U (q_1, q_2, ..q_n) = U_0 + \sum_k \left(\frac{\partial U}{\partial q_k}\right)_0 q_k + \frac{1}{2} \sum_{ j,k} \left( \frac{\partial^2 U}{ \partial q_j \partial q_k } \right)_0 q_j q_k + .. \label{14.36}
$$

The linear term is zero since $\left( \frac{\partial U}{\partial q_k} \right)_0 = 0$ at the equilibrium point, and without loss of generality, the potential can be measured with respect to $U_0$. Assume that the amplitudes are small, then the expansion can be restricted to the quadratic term, corresponding to the simple linear oscillator potential

$$
U (q_1, q_2, ..q_n) − U_0 = U^{\prime} (q_1, q_2, ..q_n) = \frac{1}{2} \sum_{ j,k} \left( \frac{\partial^2 U} {\partial q_j\partial q_k} \right)_0 q_j q_k = \frac{1}{2} \sum_{j,k} V_{jk} q_j q_k \label{14.37}
$$

That is

$$
U^{\prime} (q_1, q_2, ..q_n) = \frac{1}{2} \sum_{j,k} V_{jk} q_j q_k \label{14.38}
$$

where the components of the potential energy tensor $\mathbf{V}$ are defined as

$$
V_{jk} \equiv \left( \frac{\partial^2 U^{\prime}}{ \partial q_j\partial q_k} \right)_0 \label{14.39}
$$

Note that the order of differentiation is unimportant and thus the quantity $V_{jk}$ is symmetric

$$
V_{jk} = V_{kj} \label{14.40}
$$

The motion of the system has been specified for small oscillations around the equilibrium position and it has been shown that $U^{\prime} (q_1, q_2, ...q_n)$ has a minimum value at equilibrium which is taken to be zero for convenience.

In conclusion, equations \ref{14.32} and \ref{14.38} give

$$
T = \frac{1}{2} \sum^n_{j,k} T_{jk} \dot{q}_j \dot{q}_k \label{14.41}
$$

$$
U^{\prime} = \frac{1}{2} \sum^n_{j,k} V_{jk} q_j q_k \label{14.42}
$$

where the components of the kinetic energy tensor $\mathbf{T}$ and potential energy tensor $\mathbf{V}$ are

$$
T_{j k} \equiv\left(\sum_{\alpha}^{N} m_{\alpha} \sum_{i}^{3} \frac{\partial x_{\alpha, i}}{\partial q_{j}} \frac{\partial x_{\alpha, i}}{\partial q_{k}}\right)_{0} \label{14.43}
$$

$$
V_{j k} \equiv\left(\frac{\partial^{2} U^{\prime}}{\partial q_{j} \partial q_{k}}\right)_{0} \label{14.44}
$$

Note that $q_j$ and $q_k$ may have different units, but all the terms in the summations for both $T$ and $U^{\prime}$, have units of energy. The $V_{jk}$ and $T_{jk}$ values are evaluated at the equilibrium point, and thus both $V_{jk}$ and $T_{jk}$ are $n \times n$ arrays of values evaluated at the equilibrium location.

### Equations of motion

Both the kinetic energy and potential energy terms are products of the coordinates leading to a set of coupled equations that are complicated to solve. The problem is greatly simplified by selecting a set of normal coordinates for which both $T$ and $U$ are diagonal, then the coupling terms disappear. Thus a coordinate transformation must be found that simultaneously diagonalizes $T_{jk}$ and $V_{jk}$ in order to obtain a set of normal coordinates.

The kinetic energy $T$ *is only a function of generalized velocities* $\dot{q}_k$ while the conservative potential energy *is only a function of the generalized coordinates*$q_k$. Thus the Lagrange equations

$$
\frac{\partial L}{\partial q_k} − \frac{d}{dt} \frac{\partial L}{\partial \dot{q}_k} = 0 \label{14.45}
$$

reduce to

$$
\frac{\partial U}{\partial q_k} + \frac{d}{dt} \frac{\partial T}{\partial \dot{q}_k} = 0 \label{14.46}
$$

But

$$
\frac{\partial U}{\partial q_k} = \sum^n_j V_{jk} q_j \label{14.47}
$$

and

$$
\frac{\partial T}{\partial \dot{q}_k} = \sum^n_j T_{jk} \dot{q}_j \label{14.48}
$$

Thus the Lagrange equations reduce to the following set of equations of motion,

$$
\sum^n_j (V_{jk} q_j + T_{jk} \ddot{q}_j )=0 \label{14.49}
$$

For each $k$, where $1 \leq k \leq n$, there exists a set of $n$ second-order linear homogeneous differential equations with constant coefficients. Since the system is oscillatory, it is natural to try a solution of the form

$$
q_j (t) = a_j e^{i(\omega t−\delta )} \label{14.50}
$$

Assuming that the system is conservative, then this implies that $\omega$ is real, since an imaginary term for $\omega$ would lead to an exponential damping term. The arbitrary constants are the real amplitude $a_j$ and the phase $\delta$. Substitution of this trial solution for each $k$ leads to a set of equations

$$
\sum_j (V_{jk} − \omega^2 T_{jk} ) a_j = 0 \label{14.51}
$$

where the common factor $e^{i(\omega t−\delta )}$ has been removed. Equation \ref{14.51} corresponds to a set of $n$ linear homogeneous algebraic equations that the $a_j$ amplitudes must satisfy for each $k$. For a non-trivial solution to exist, the determinant of the coefficients must vanish, that is

$$
\begin{vmatrix} V_{11} − \omega^2 T_{11} & V_{12} − \omega^2 T_{12} & V_{13} − \omega^2 T_{13} & ... \\ V_{12} − \omega^2 T_{12} & V_{22} − \omega^2 T_{22} & V_{23} − \omega^2 T_{23} & ... \\ V_{13} − \omega^2 T_{13} & V_{23} − \omega^2 T_{23} & V_{33} − \omega^2 T_{33} & ... \\ ... & ... & ... & ... \end{vmatrix} = 0 \label{14.52}
$$

where the symmetry $V_{jk} = V_{kj}$ has been included. This is the standard eigenvalue problem for which the above determinant gives the **secular equation** or the **characteristic equation**. It is an equation of degree $n$ in $\omega^2$. The $n$ roots of this equation are $\omega^2_r$ where $\omega_r$ are the **characteristic frequencies** or **eigenfrequencies** of the normal modes.

Substitution of $\omega^2_r$ into Equation \ref{14.52} determines the ratio $a_{1,r} : a_{2,r} : a_{3,r} : ... : a_{n,r}$ for this solution which defines the components of the $n$-dimensional **eigenvector** $\mathbf{a}_r$. That is, solution of the secular equations have determined the eigenvalues and eigenvectors of the $n$ solutions of the coupled-channel system.

### Superposition

The equations of motion $\sum_j (V_{jk} q_j + T_{jk} \ddot{q}_j )=0$ are linear equations that satisfy superposition. Thus the most general solution $q_j (t)$ can be a superposition of the $n$ eigenvectors $\mathbf{a}_{jr}$, that is

$$
q_j (t) = \sum^n_r a_{jr} e^{i(\omega_rt−\delta_r)} \label{14.53}
$$

Only the real part of $q_j (t)$ is meaningful, that is,

$$
q_j (t) = \text{ Re} \sum^n_r a_{jr} e^{i(\omega_r t−\delta_r)} = \sum^n_r a_{jr} \cos (\omega_r t − \delta_r) \label{14.54}
$$

Thus the most general solution of these linear equations involves a sum over the eigenvectors of the system which are cosine functions of the corresponding eigenfrequencies.

### Eigenfunction Orthonormality

It can be shown that the eigenvectors are orthogonal. In addition, the above procedure only determines ratios of amplitudes, thus there is an indeterminacy that can be used to normalize the $a_{jr}$. Thus the eigenvectors form an orthonormal set. Orthonormality of the eigenfunctions for the rank 3 inertia tensor was illustrated in chapter $13.10.2$. Similar arguments apply that allow extending orthonormality to higher rank cases such that for $n$-body coupled oscillators.

The **eigenfunction orthogonality** for $n$ coupled oscillators can be proved by writing Equation \ref{14.51} for both the $s^{th}$ root and the $r^{th}$ root. That is,

$$
\sum_j V_{jk} a_{ks} = \omega^2_s \sum_j T_{jk} a_{ks} \label{14.55}
$$

$$
\sum_j V_{jk} a_{jr} = \omega^2_r \sum_j T_{jk} a_{jr} \label{14.56}
$$

Multiply Equation \ref{14.55} by $a_{jr}$ and sum over $k$. Similarly multiply Equation \ref{14.56} by $a_{ks}$ and sum over $k$. These summations lead to

$$
\sum_{jk} V_{jk} a_{jr}a_{ks} = \omega^2_s \sum_{jk} T_{jk} a_{jr} a_{ks} \label{14.57}
$$

$$
\sum_{jk} V_{jk} a_{jr}a_{ks} = \omega^2_r \sum_{jk} T_{jk} a_{jr}a_{ks} \label{14.58}
$$

Note that the left-hand sides of these two equations are identical. Thus taking the difference between these equations gives

$$
(\omega^2_r − \omega^2_s) \sum_{jk} T_{jk} a_{jr} a_{ks} = 0 \label{14.59}
$$

Note that if $(\omega^2_r − \omega^2_s ) \neq 0$, that is, assuming that the eigenfrequencies are not degenerate, then to ensure that Equation \ref{14.59} is zero requires that

$$
\sum_{jk} T_{jk} a_{jr} a_{ks} = 0 \quad r \neq s \label{14.60}
$$

This shows that the eigenfunctions are orthogonal. If the eigenfrequencies are degenerate, i.e. $\omega^2_r = \omega^2_s$, then, with no loss of generality, the axes $r$ and $s$ can be chosen to be orthogonal.

The **eigenfunction normalization** can be chosen freely since only ratios of the eigenfunction components $a_{jr}$ are determined when $\omega_r$ is used in Equation \ref{14.51}. The kinetic energy, given by Equation \ref{14.32} must be positive, or zero for the case of a static system. That is

$$
T = \frac{1}{2} \sum^n_{j,k} T_{jk} \dot{q}_j \dot{q}_k \geq 0 \label{14.61}
$$

Use the time derivative of Equation \ref{14.54} to determine $\dot{q}_r$ and insert into Equation \ref{14.61} gives that the kinetic energy is

$$
T=\frac{1}{2} \sum_{j, k}^{n} T_{j k} \dot{q}_{j} \dot{q}_{k}=\frac{1}{2} \sum_{j, k}^{n} T_{j k} \sum_{r, s} \omega_{r} \omega_{s} a_{j r} \cos \left(\omega_{r} t-\delta_{r}\right) a_{k s} \cos \left(\omega_{s} t-\delta_{s}\right) \label{14.62}
$$

For the diagonal term $r = s$

$$
T=\frac{1}{2} \sum_{j, k}^{n} T_{j k} \dot{q}_{j} \dot{q}_{k}=\left[\frac{1}{2} \sum_{r}^{n} \omega_{r}^{2} \cos ^{2}\left(\omega_{r} t-\delta_{r}\right)\right] \sum_{j, k} T_{j k} a_{j r} a_{k r} \geq 0 \label{14.63}
$$

Since the term in the square brackets must be positive, then

$$
\sum_{j,k} T_{jk} a_{jr} a_{kr} \geq 0 \label{14.64}
$$

Since this sum must be a positive number, and the magnitude of the amplitudes can be chosen freely, then it is possible to **normalize** the eigenfunction amplitudes to unity. That is, choose that

$$
\sum_{j,k} T_{jk} a_{jr} a_{ks} = 1 \label{14.65}
$$

The orthogonality equation, \ref{14.60} and the normalization Equation \ref{14.65} can be combined into a single orthonormalization equation

$$
\sum_{j,k} T_{jk} a_{jr} a_{ks} = \delta_{rs} \label{14.66}
$$

This has shown that the eigenvectors form an orthonormal set.

Since the $j^{th}$ component of the $r^{th}$ eigenvector is $a_{jr}$, then the $r^{th}$ eigenvector can be written in the form

$$
\mathbf{a}_r = \sum_j a_{jr} \widehat{\mathbf{e}_j} \label{14.67}
$$

where $\widehat{\mathbf{e}_j}$ are the unit vectors for the generalized coordinates.

### Normal coordinates

The above general solution of the coupled-oscillator problem is best expressed in terms of the normal coordinates which are independent. It is more transparent if the superposition of the normal modes are written in the form

$$
q_{j}(t)=\sum_{r}^{n} \beta_{r} a_{j r} e^{i \omega_{r} t} \label{14.68}
$$

where the complex factor $\beta_r$ includes the arbitrary scale factor to allow for arbitrary amplitudes $q_j$ as well as the fact that the amplitudes $a_{jr}$ have been normalized and the phase factor $\delta_r$ has been chosen.

Define

$$
\eta_{r} (t) \equiv \beta_{r} e^{i \omega_{r} t} \label{14.69}
$$

then Equation \ref{14.68} can be written as

$$
q_j (t) = \sum^n_r a_{jr}\eta_r (t) \label{14.70}
$$

Equation \ref{14.70} can be expressed schematically as the matrix multiplication

$$
{\bf q = \{a\} \cdot} \boldsymbol{\eta} \label{14.71}
$$

The $\eta_r (t)$ are the **normal coordinates** which can be expressed in the form

$$
\boldsymbol{\eta} {\bf = \{a\}^{−1} q } \label{14.72}
$$

Each normal mode $\eta_r$ corresponds to a single eigenfrequency, $\omega_r$ which satisfies the linear oscillator equation

$$
\ddot{\eta}_r + \omega^2_r \eta_r = 0 \label{14.73}
$$

[Douglas Cline](http://www.pas.rochester.edu/~cline/Cline_home.htm) ([University of Rochester](http://www.pas.rochester.edu/))

## 14.7: Two-body coupled oscillator systems

The two-body coupled oscillator is the simplest coupled-oscillator system that illustrates the general features of coupled oscillators. The following four examples involve parallel and series couplings of two linear oscillators or two plane pendula.

Example 14.1: Two coupled linear oscillators

The coupled double-oscillator problem, Figure $14.2.1$ discussed in chapter $14.2$, can be used to demonstrate that the general analytic theory gives the same solution as obtained by direct solution of the equations of motion in chapter $14.2$.

1) The first stage is to determine the potential and kinetic energies using an appropriate set of generalized coordinates, which here are $x_1$ and $x_2$. The potential energy is

$$
U=\frac{1}{2} \kappa x_{1}^{2}+\frac{1}{2} \kappa x_{2}^{2}+\frac{1}{2} \kappa^{\prime}\left(x_{2} - x_{1}\right)^{2} = \frac{1}{2} \left( \kappa + \kappa^{\prime} \right) x_{1}^{2}+\frac{1}{2} \left( \kappa + \kappa^{\prime} \right) x_{2}^{2}-\kappa^{\prime} x_{1} x_{2} \nonumber
$$

while the kinetic energy is given by

$$
T = \frac{1}{2}m\dot{x}^2_1 + \frac{1}{2}m\dot{x}^2_2 \nonumber
$$

2) The second stage is to evaluate the potential energy $V$ and kinetic energy $T$ tensors. The potential energy tensor $V$ is nondiagonal since $V_{jk}$ gives

$$
V_{11} \equiv \left( \frac{\partial^{2} U}{\partial q_{1} \partial q_{1}} \right)_{0} = \kappa+\kappa^{\prime}=V_{22} \nonumber
$$

$$
V_{12} =\left( \frac{\partial^{2} U}{\partial q_{1} \partial q_{2}}\right)_{0}=-\kappa^{\prime}=V_{21} \nonumber
$$

That is, the potential energy tensor $V$ is

$$
\mathbf{V} \begin{Bmatrix} \kappa + \kappa^{\prime} & -\kappa^{\prime} \\ -\kappa^{\prime} & \kappa + \kappa^{\prime} \end{Bmatrix} \nonumber
$$

Similarly, the kinetic energy is given by

$$
T = \frac{1}{2}m\dot{x}^2_1 + \frac{1}{2}m\dot{x}^2_2 = \frac{1}{2}\sum_{j,k} T_{jk}\dot{q}_j\dot{q}_k \nonumber
$$

Since $T_{11} = T_{22} = m$ and $T_{12} = T_{21} = 0$ then the kinetic energy tensor $T$ is

$$
\mathbf{T} \begin{Bmatrix} m & 0 \\ 0 & m \end{Bmatrix} \nonumber
$$

Note that for this case, the kinetic energy tensor $T$ equals the mass tensor, which is diagonal, whereas the potential energy tensor equals the spring constant tensor, which is nondiagonal.

3) The third stage is to use the potential energy $V$ and kinetic energy $T$ tensors to evaluate the secular determinant using equations $(14.6.26)$

$$
\begin{vmatrix} \kappa + \kappa^{\prime} - m\omega^2 & -\kappa^{\prime} \\ -\kappa^{\prime} & \kappa + \kappa^{\prime} - m\omega^2 \end{vmatrix} = 0 \nonumber
$$

The expansion of this secular determinant yields

$$
(\kappa + \kappa^{\prime} - m\omega^2)^2 - \kappa^{\prime 2} = 0 \nonumber
$$

That is

$$
(\kappa + \kappa^{\prime} - m\omega^2) = \pm\kappa^{\prime} \nonumber
$$

Solving for $\omega_r$ gives

$$
\omega_r = \sqrt{\frac{\kappa + \kappa^{\prime} \pm \kappa^{\prime}}{m}} \nonumber
$$

The solutions are

$$
\omega_1 = \sqrt{\frac{\kappa + 2\kappa^{\prime}}{m}} \nonumber
$$

$$
\omega_2 = \sqrt{\frac{\kappa}{m}} \nonumber
$$

which is the same as derived previously, (equations $(14.2.7-14.2.9)$).

4) The fourth step is to insert either one of these eigenfrequencies into the secular equation

$$
\sum_j (V_{jk} - \omega^2_r T_{jk}) a_{jr} = 0 \nonumber
$$

Consider the secular equation $a$ for $k = 1$

$$
( \kappa + \kappa^{\prime} − \omega^2_rM) a_{1r} − \kappa^{\prime} a_{2r} = 0 \nonumber
$$

Then for the first eigenfrequency $\omega_1$, that is, $k = 1$, $r = 1$

$$
(\kappa + \kappa^{\prime} − \kappa − 2\kappa^{\prime} ) a_{11} − \kappa^{\prime} a_{21} = 0 \nonumber
$$

which simplifies to

$$
a_{jr} = a_{11} = −a_{21} \nonumber
$$

Similarly, for the other eigenfrequency $\omega_2$, that is, $k = 1$, $r = 2$

$$
(\kappa + \kappa^{\prime} − \kappa ) a_{12} − \kappa^{\prime} a_{22} = 0 \nonumber
$$

which simplifies to

$$
a_{jr} = a_{12} = a_{22} \nonumber
$$

5) The final stage is to write the general coordinates in terms of the normal coordinates $\eta_r (t) \equiv \beta_r e^{i\omega_r t}$. Thus

$$
x_1 = a_{11}\eta_1 + a_{12}\eta_2 = a_{11}\eta_1 + a_{22}\eta_2 \nonumber
$$

and

$$
x_2 = a_{21}\eta_1 + a_{22}\eta_2 = −a_{11}\eta_1 + a_{22}\eta_2 \nonumber
$$

Adding or subtracting gives that the normal modes are

$$
\eta_1 = \frac{1}{2a_{11}} (x_1 − x_2) \nonumber
$$

$$
\eta_2 = \frac{1}{2a_{22}} (x_2 + x_1) \nonumber
$$

Thus the symmetric normal mode $\eta_2$ corresponds to an oscillation of the center-of-mass with the lower frequency $\omega_2 = \sqrt{\frac{\kappa}{m}}$. This frequency is the same as for one single mass on a spring of spring constant $\kappa$ which is as expected since they vibrate in unison and thus the coupling spring force does not act. The antisymmetric mode $\eta_1$ has the higher frequency $\omega_1 = \sqrt{\frac{\kappa + 2\kappa^{\prime}}{m}}$ since the restoring force includes both the main spring plus the coupling spring.

The above example illustrates that the general analytic theory for coupled linear oscillators gives the same answer as obtained in chapter $14.2$ using Newton’s equations of motion. However, the general analytic theory is a more powerful technique for solving complicated coupled oscillator systems. Thus the general analytic theory will be used for solving all the following coupled oscillator problems.

Example 14.2: Two equal masses series-coupled by two equal springs

:::{figure} ../images/lt-21230-12.7.1.png
:alt: 12.7.1.PNG

$1$: Two equal masses series-coupled by two equal springs.
:::

Consider the series-coupled system shown in the figure.

1) The first stage is to determine the potential and kinetic energies using an appropriate set of generalized coordinates, which here are $x_1$ and $x_2$. The potential energy is

$$
U=\frac{1}{2} \kappa x_{1}^{2} +\frac{1}{2} \kappa \left(x_{2} - x_{1}\right)^{2} = \kappa x_{1}^{2}+\frac{1}{2} \kappa x_{2}^{2}-\kappa x_{1} x_{2} \nonumber
$$

while the kinetic energy is given by

$$
T = \frac{1}{2}m\dot{x}^2_1 + \frac{1}{2}m\dot{x}^2_2 \nonumber
$$

2) The second stage is to evaluate the potential energy $V$ and mass $T$ tensors. The potential energy tensor $V$ is nondiagonal since $V_{jk}$ gives

$$
V_{11} \equiv \left( \frac{\partial^{2} U}{\partial q_{1} \partial q_{1}} \right)_{0} = 2\kappa \nonumber
$$

$$
V_{12} =\left( \frac{\partial^{2} U}{\partial q_{1} \partial q_{2}}\right)_{0}=-\kappa =V_{21} \nonumber
$$

$$
V_{22} =\left( \frac{\partial^{2} U}{\partial q_{2} \partial q_{2}}\right)_{0}= \kappa \nonumber
$$

That is, the potential energy tensor $V$ is

$$
\mathbf{V} \begin{Bmatrix} 2\kappa & -\kappa \\ -\kappa & \kappa \end{Bmatrix} \nonumber
$$

Similarly, since the kinetic energy is given by

$$
T = \frac{1}{2}m\dot{x}^2_1 + \frac{1}{2}m\dot{x}^2_2 = \frac{1}{2}\sum_{j,k} m_{jk}\dot{q}_j\dot{q}_k \nonumber
$$

then $T_{11} = T_{22} = m$ and $T_{12} = T_{21} = 0$. Thus the kinetic energy tensor $T$ is

$$
\mathbf{T} \begin{Bmatrix} m & 0 \\ 0 & m \end{Bmatrix} \nonumber
$$

Note that for this case the kinetic energy tensor is diagonal whereas the potential energy tensor is nondiagonal.

3) The third stage is to use the potential energy $V$ and kinetic energy $T$ tensors to evaluate the secular determinant using equation $(14.6.26)$

$$
\begin{vmatrix} 2\kappa - m\omega^2 & -\kappa \\ -\kappa & \kappa - m\omega^2 \end{vmatrix} = 0 \nonumber
$$

The expansion of this secular determinant yields

$$
( 2\kappa − m\omega^2) (\kappa − m\omega^2) − \kappa^2 = 0 \nonumber
$$

That is

$$
\omega^4 − 3 \frac{\kappa }{m} \omega^2 + \frac{\kappa^2}{m^2} = 0 \nonumber
$$

The solutions are

$$
\omega_1 = \frac{\sqrt{5}+1}{2}\sqrt{\frac{\kappa}{ m}} \quad \omega_2 = \frac{\sqrt{5}-1}{2} \sqrt{\frac{\kappa}{ m}} \nonumber
$$

4) The fourth step is to insert these eigenfrequencies into the secular equation $(14.6.25)$

$$
\sum_j (V_{jk} - \omega^2_r T_{jk}) a_{jr} = 0 \nonumber
$$

Consider $k = 1$ in the above equation

$$
( 2\kappa − \omega^2_rM) a_{1r} − \kappa a_{2r} = 0 \nonumber
$$

Then for eigenfrequency $\omega_1$, that is, $k = 1$, $r = 1$

$$
\frac{\sqrt{5} − 1}{2} a_{11} = −a_{21} \nonumber
$$

Similarly, for $k = 1$, $r = 2$

$$
\frac{\sqrt{5} + 1}{2} a_{12} = a_{22} \nonumber
$$

5) The final stage is to write the general coordinates in terms of the normal coordinates $\eta_r (t) \equiv \beta_re^{i\omega_rt}$.

Thus

$$
x_1 = a_{11}\eta_1 + a_{12}\eta_2 = a_{11}\eta_1 + \frac{2a_{22}}{ \sqrt{5} +1}\eta_2 \nonumber
$$

and

$$
x_2 = a_{21}\eta_1 + a_{22}\eta_2 = − \left(\frac{\sqrt{5} − 1}{2} \right) a_{11}\eta_1 + a_{22}\eta_2 \nonumber
$$

Adding or subtracting gives that the normal modes are

$$
\eta_1 = \frac{1}{a_{11} \sqrt{5}} \left( x_1 − \left(\frac{\sqrt{5} − 1}{ 2} \right) x_2 \right) \nonumber
$$

$$
\eta_2 = \frac{1}{a_{22} \sqrt{5}} \left( x_1 + \left(\frac{\sqrt{5} +1}{2} \right) x_2 \right) \nonumber
$$

Thus the symmetric normal mode has the lower frequency $\omega_2 = \frac{\sqrt{5} −1}{2} \sqrt{\frac{\kappa}{ m}}$. The antisymmetric mode has the frequency $\omega_1 = \frac{\sqrt{5} +1}{2}\sqrt{\frac{\kappa}{m}}$ since both springs provide the restoring force. This case is interesting in that for both normal modes, the amplitudes for the motion of the two masses are different.

Example 14.3: Two parallel-coupled plane pendula

:::{figure} ../images/lt-21231-12.7.2.png
:alt: 12.7.2.PNG

$2$: Two parallel-coupled plane pendula.
:::

Consider the coupled double pendulum system shown in the adjacent figure, which comprises two parallel plane pendula weakly coupled by a spring. The angles $\theta_1$ and $\theta_2$ are chosen to be the generalized coordinates and the potential energy is chosen to be zero at equilibrium. Then the kinetic energy is

$$
T = \frac{1}{2} m \left( b\dot{\theta}_1 \right)^2 + \frac{1}{2} m \left( b\dot{\theta}_2 \right)^2 \nonumber
$$

As discussed in chapter $3$, it is necessary to make the small-angle approximation in order to make the equations of motion for the simple pendulum linear and solvable analytically. That is,

$$
\begin{aligned} U &=m g b\left(1-\cos \theta_{1}\right)+m g b\left(1-\cos \theta_{2}\right) + \frac{1}{2} \kappa\left(b \sin \theta_{1}-b \sin \theta_{2} \right)^{2} \\ & \simeq \frac{m g b} {2}\left(\theta_{1}^{2} + \theta_{2}^{2} \right) + \frac{\kappa b^{2}}{2}\left(\theta_{1}-\theta_{2}\right)^{2}

\end{aligned}
$$

assuming the small angle approximation $\sin \theta \approx \theta$ and $(1 − \cos \theta_1) = \frac{\theta^2}{2}$.

The second stage is to evaluate the kinetic energy $T$ and potential energy $V$ tensors

$$
\mathbf{T} = \begin{Bmatrix} mb^2 & 0 \\ 0 & mb^2 \end{Bmatrix} \quad \mathbf{V} = \begin{Bmatrix} mgb + \kappa b^2 & -\kappa b^2 \\ -\kappa b^2 & mgb + \kappa b^2 \end{Bmatrix} \nonumber
$$

Note that for this case the kinetic energy tensor is diagonal whereas the potential energy tensor is nondiagonal.

The third stage is to evaluate the secular determinant

$$
\begin{vmatrix} mgb + \kappa b^2 - \omega^2mb^2 & -\kappa b^2 \\ -\kappa b^2 & mgb + \kappa b^2 - \omega^2mb^2 \end{vmatrix} = 0 \nonumber
$$

which gives the characteristic equation

$$
( mgb + \kappa b^2 − \omega^2mb^2)^2 = ( \kappa b^2)^2 \nonumber
$$

or

$$
mg + \kappa b − \omega^2mb = \pm\kappa b \nonumber
$$

The two solutions are

$$
\omega^2_1 = \frac{g}{b} \quad \omega^2_2 = \frac{g}{b} + \frac{2\kappa}{ m} \nonumber
$$

The fourth step is to insert these eigenfrequencies into equation $(14.6.25)$

$$
\sum_j (V_{jk} - \omega^2_r T_{jk}) a_{jr} = 0 \nonumber
$$

Consider $k = 1$

$$
( mgb + \kappa b^2 − \omega^2_r mb^2) a_{1r} − \kappa b^2a_{2r} = 0 \nonumber
$$

Then for the first eigenfrequency, $\omega_1$, the subscripts are $k = 1$, $r = 1$

$$
\left( mgb + \kappa b^2 − \frac{g}{b} mb^2 \right) a_{11} − \kappa b^2a_{21} = 0 \nonumber
$$

which simplifies to

$$
a_{11} = a_{21} \nonumber
$$

Similarly, for $k = 1$, $r = 2$

$$
\left( mgb + \kappa b^2 − \left(\frac{g}{b} + \frac{2\kappa}{m} \right) mb^2 \right) a_{12} − \kappa b^2a_{22} = 0 \nonumber
$$

which simplifies to

$$
a_{12} = −a_{22} \nonumber
$$

The final stage is to write the general coordinates in terms of the normal coordinates

$$
\theta_1 = a_{11}\eta_1 + a_{12}\eta_2 = a_{11}\eta_1 − a_{22}\eta_2 \nonumber
$$

and

$$
\theta_2 = a_{21}\eta_1 + a_{22}\eta_2 = a_{11}\eta_1 + a_{22}\eta_2 \nonumber
$$

Adding or subtracting these equations gives that the normal modes are

$$
\eta_1 = \frac{1}{2a_{11}} (\theta_1 + \theta_2) \quad \eta_2 = \frac{1}{2a_{22}} (\theta_2 − \theta_1) \nonumber
$$

As for the case of the double oscillator discussed in Example 14.1, the symmetric normal mode corresponds to an oscillation of the center-of-mass, with zero relative motion of the two pendula, which has the lower frequency $\omega_1 = \sqrt{\frac{g}{b}}$. This frequency is the same as for one independent pendulum as expected since they vibrate in unison and thus the only restoring force is gravity. The antisymmetric mode corresponds to relative motion of the two pendula with stationary center-of-mass and has the frequency $\omega_2 = \sqrt{(\frac{g}{b} + \frac{2\kappa}{ m })}$ since the restoring force includes both the coupling spring and gravity.

This example introduces the role of degeneracy which occurs in this system if the coupling of the pendula is zero, that is, $\kappa = 0$, leading to both frequencies being equal, i.e. $\omega_1 = \omega_2 = \sqrt{\frac{g}{b}}$. When $\kappa = 0$, then both ${\bf \{T\} }$ and ${\bf \{V\}}$ are diagonal and thus in the $(\theta_1, \theta_2)$ space the two pendula are independent normal modes. However, the symmetric and asymmetric normal modes, as derived above, are equally good normal modes. In fact, since the modes are degenerate, any linear combination of the motion of the independent pendula are equally good normal modes and thus one can use any set of orthogonal normal modes to describe the motion.

Example 14.4: The series-coupled double plane pendula

:::{figure} ../images/lt-21233-12.7.3.png
:alt: 12.7.3.PNG

$3$: Two series-coupled plane pendula.
:::

The double-pendula system comprises one plane pendulum attached to the end of another plane pendulum both oscillating in the same plane. The kinetic and potential energies for this system are given in example $6.12.1$ to be

$$
\begin{aligned}

T &=\frac{1}{2}\left(m_{1}+m_{2}\right) L_{1}^{2} \dot{\phi}_{1}^{2}+m_{2} L_{1} L_{2} \dot{\phi}_{1} \dot{\phi}_{2} \cos \left(\phi_{1}-\phi_{2}\right)+\frac{1}{2} m_{2} L_{2}^{2} \dot{\phi}_{2}^{2} \\

U &=\left(m_{1}+m_{2}\right) g L_{1}\left(1-\cos \phi_{1}\right)+m_{2} g L_{2}\left(1-\cos \phi_{2}\right)

\end{aligned}
$$

### a) Small-amplitude linear regime

Use of the small-angle approximation makes this system linear and solvable analytically. That is, $T$ and $U$ become

$$
\begin{aligned}

U &=\frac{1}{2}\left(m_{1}+m_{2}\right) g L_{1} \phi_{1}^{2}+\frac{1}{2} m_{2} g L_{2} \phi_{2}^{2} \\

T &=\frac{1}{2}\left(m_{1}+m_{2}\right) L_{1}^{2} \dot{\phi}_{1}^{2}+m_{2} L_{1} L_{2} \dot{\phi}_{1} \dot{\phi}_{2}+\frac{1}{2} m_{2} L_{2}^{2} \dot{\phi}_{2}^{2}

\end{aligned}
$$

Thus the kinetic energy and potential energy tensors are

$$
\mathbf{T}= \begin{Bmatrix} \left(m_{1}+m_{2}\right) L_{1}^{2} & m_{2} L_{1} L_{2} \\ m_{2} L_{1} L_{2} & m_{2} L_{2}^{2} \end{Bmatrix} \quad \mathbf{V}= \begin{Bmatrix} \left( m_{1}+m_{2}\right) g L_{1} & 0 \\

0 & m_{2} g L_{2} \end{Bmatrix} \nonumber
$$

Note that $\mathbf{T}$ is nondiagonal, whereas $\mathbf{V}$ is diagonal which is opposite to the case of the two parallel-coupled plane pendula.

:::{figure} ../images/lt-21232-12.7.4.png
:alt: 12.7.4.PNG

12.7.4.PNG
:::

The solution of this case is simpler if it is assumed that $L_1 = L_2 = L$ and $m_1 = m_2 = m$. Then

$$
\mathbf{T} = mL^2 \begin{Bmatrix} 2 & 1 \\ 1 & 1 \end{Bmatrix} \quad \mathbf{V} = \begin{Bmatrix} 2\omega^2_0 & 0 \\ 0 & \omega^2_0 \end{Bmatrix} \nonumber
$$

where $\omega_0 = \sqrt{\frac{g}{L}}$ which is the frequency of a single pendulum.

The next stage is to evaluate the secular determinant

$$
mL^2 \begin{vmatrix} 2(\omega^2_0 − \omega^2) & −\omega^2 \\ −\omega^2 & (\omega^2_0 − \omega^2) \end{vmatrix} = 0 \nonumber
$$

The eigenvalues are

$$
\omega^2_1 = (2 − \sqrt{2})\omega^2_0 \quad \omega^2_2 = (2 + \sqrt{ 2})\omega^2_0 \nonumber
$$

As shown in the adjacent figure, the normal modes for this system are

$$
\eta_1 = \frac{1}{2a_{11}} (\phi_1 + \frac{\phi_2}{\sqrt{2}} ) \quad \eta_2 = \frac{1}{2a_{22}} (\phi_1 - \frac{\phi_2}{\sqrt{2}} ) \nonumber
$$

The second mass has a $\sqrt{2}$ larger amplitude that is in phase for solution 1 and out of phase for solution 2.

### b) Large amplitude chaotic regime

Stachowiak and Okada [Sta05] used computer simulations to numerically analyze the behavior of this system with increase in the oscillation amplitudes. Poincaré sections, bifurcation diagrams, and Lyapunov exponents all confirm that this system evolves from regular normal-mode oscillatory behavior in the linear regime at low energy, to chaotic behavior at high excitation energies where non-linearity dominates. This behavior is analogous to that of the driven, linearly-damped, harmonic pendulum described in chapter $3.5$

## 14.8: Three-body coupled linear oscillator systems

Chapter $14.7$ discussed parallel and series arrangements of two coupled oscillators. Extending from two to three coupled linear oscillators introduces interesting new characteristics of coupled oscillator systems. For more than two coupled oscillators, coupled oscillator systems separate into two classifications depending on whether each oscillator is coupled to the remaining $n − 1$ oscillators, or when the coupling is only to the nearest neighbors as illustrated below.

Example 14.1: Three plane pendula; mean-field linear coupling

:::{figure} ../images/lt-21235-12.8.1.png
:alt: 12.8.1.PNG

$1$: Three plane pendula with complete linear coupling.
:::

Consider three identical pendula with mass $m$ and length $b$, suspended from a common support that yields slightly to pendulum motion leading to a coupling between all three pendula as illustrated in the adjacent figure. Assume that the motion of the three pendula all are in the same plane. This case is analogous to the piano where three strings in the treble section are coupled by the slightly-yielding common bridge plus sounding board leading to coupling between each of the three coupled oscillators. This case illustrates the important concept of degeneracy.

The generalized coordinates are the angles $\theta_1$, $\theta_2$, and $\theta_3$. Assume that the support yields such that the actual deflection angle for pendulum 1 is

$$
\theta^{\prime}_1 = \theta_1 − \frac{\varepsilon}{2} (\theta_2 + \theta_3) \nonumber
$$

where the coupling coefficient $\varepsilon$ is small and involves all the pendula, not just the nearest neighbors. Assume that the same coupling relation exists for the other angle coordinates. The gravitational potential energy of each pendulum is given by

$$
U_1 = mgb (1 − \cos \theta_1) \approx \frac{1}{2} mgb \theta^2_1\nonumber
$$

assuming the small angle approximation. Ignoring terms of order $\varepsilon^2$ gives that the potential energy

$$
U = \frac{mgb}{2} ( \theta^{\prime 2}_1 + \theta^{\prime 2}_2 + \theta^{\prime 2}_3 ) = \frac{mgb}{2} ( \theta^2_1 + \theta^2_2 + \theta^2_3 − 2\varepsilon\theta_1\theta_2 − 2\varepsilon\theta_1\theta_3 − 2\varepsilon\theta_2\theta_3 )\nonumber
$$

The kinetic energy evaluated at the equilibrium location is

$$
T = \frac{1}{2} m \left( b\dot{\theta}_1 \right)^2 +\frac{1}{2} m \left( b\dot{\theta}_2 \right)^2 +\frac{1}{2} m \left( b\dot{\theta}_3 \right)^2 \nonumber
$$

The next stage is to evaluate the $\mathbf{\{T\}}$ and $\mathbf{\{V\}}$ tensors

$$
\mathbf{T} = mb^2 \begin{Bmatrix} 1&0&0 \\ 0&1&0 \\ 0&0&1 \end{Bmatrix} \quad \mathbf{V} = mgb \begin{Bmatrix} 1 & −\varepsilon & −\varepsilon \\ −\varepsilon & 1 & −\varepsilon \\ −\varepsilon & −\varepsilon & 1 \end{Bmatrix}\nonumber
$$

The third stage is to evaluate the secular determinant which can be written as

$$
mgb \begin{vmatrix} 1 − \frac{b}{g} \omega^2 & −\varepsilon & −\varepsilon \\ −\varepsilon & 1 − \frac{b}{g} \omega^2 & −\varepsilon \\ −\varepsilon & −\varepsilon & 1 − \frac{b}{g} \omega^2 \end{vmatrix} = 0\nonumber
$$

Expanding and factoring gives

$$
\left( \frac{b}{g} \omega^2 − 1 − \varepsilon \right) \left( \frac{b}{g} \omega^2 − 1 − \varepsilon \right) \left( \frac{b}{g} \omega^2 − 1+2\varepsilon \right) = 0\nonumber
$$

The roots are

$$
\omega_1 = \sqrt{\frac{g}{b}}\sqrt{1+\varepsilon} \quad \omega_2 = \sqrt{\frac{g}{b}}\sqrt{1+\varepsilon} \quad \omega_3 = \sqrt{\frac{g}{b}}\sqrt{1-2\varepsilon}\nonumber
$$

This case results in two degenerate eigenfrequencies, $\omega_1 = \omega_2$ while $\omega_3$ is the lowest eigenfrequency.

The eigenvectors can be determined by substitution of the eigenfrequencies into

$$
\sum^n_j ( V_{jk} − \omega^2_r T_{jk}) a_{jr} = 0\nonumber
$$

Consider the lowest eigenfrequency $\omega_3$, i.e. $r = 3$, for $k = 1$, and substitute for $\omega_3 = \sqrt{\frac{g}{b}}\sqrt{1-2\varepsilon}$ gives

$$
2\varepsilon a_{13} − \varepsilon a_{23} − \varepsilon a_{33} = 0\nonumber
$$

while for $r = 3$, $k = 2$

$$
−\varepsilon a_{13} + 2\varepsilon a_{23} − \varepsilon a_{33} = 0\nonumber
$$

Solving these gives

$$
a_{13} = a_{23} = a_{33}\nonumber
$$

Assuming that the eigenfunction is normalized to unity

$$
a^2_{13} + a^{2}_{23} + a^2_{33} = 1\nonumber
$$

then for the third eigenvector $a_3$

$$
a_{13} = a_{23} = a_{33} = \frac{1}{\sqrt{3}}\nonumber
$$

This solution corresponds to all three pendula oscillating in phase with the same amplitude, that is, a coherent oscillation.

Derivation of the eigenfunctions for the other two eigenfrequencies is complicated because of the degeneracy $\omega_1 = \omega_2$, there are only five independent equations to specify the six unknowns for the eigenvectors $a_{1}$ and $a_{2}$. That is, the eigenvectors can be chosen freely as long as the orthogonality and normalization are satisfied. For example, setting $a_{31} = 0$, to remove the indeterminacy, results in the $\mathbf{a}$ matrix

$$
\mathbf{\{a\}} = \begin{Bmatrix} \frac{ 1}{2} \sqrt{2} & \frac{1}{6} \sqrt{6}& \frac{1}{3}\sqrt{3} \\ −\frac{1}{2} \sqrt{2} & \frac{1}{6} \sqrt{6} & \frac{1}{3}\sqrt{3} \\ 0 & −\frac{1}{3} \sqrt{6} & \frac{1}{3}\sqrt{3} \end{Bmatrix}\nonumber
$$

and thus the solution is given by

$$
\begin{Bmatrix} \theta_1 \\ \theta_2 \\ \theta_3 \end{Bmatrix} = \begin{Bmatrix} \frac{ 1}{2} \sqrt{2} & \frac{1}{6} \sqrt{6}& \frac{1}{3}\sqrt{3} \\ −\frac{1}{2} \sqrt{2} & \frac{1}{6} \sqrt{6} & \frac{1}{3}\sqrt{3} \\ 0 & −\frac{1}{3} \sqrt{6} & \frac{1}{3}\sqrt{3} \end{Bmatrix} \begin{Bmatrix} \eta_1 \\ \eta_2 \\ \eta_3 \end{Bmatrix}\nonumber
$$

The normal modes are obtained by taking the inverse matrix $\mathbf{\{a\}}^{−1}$ and using $\mathbf{\{\boldsymbol{\eta}\}} = \mathbf{\{a\}}^{−1} \mathbf{\{\boldsymbol{\theta}\}}$. Note that since $\mathbf{\{a\}}$ is real and orthogonal, then $\mathbf{\{a\}}^{−1}$ equals the transpose of $\mathbf{\{a\}}$. That is;

$$
\begin{Bmatrix} \eta_1 \\ \eta_2 \\ \eta_3 \end{Bmatrix} = \begin{Bmatrix} \frac{ 1}{2} \sqrt{2} & \frac{1}{6} \sqrt{6}& \frac{1}{3}\sqrt{3} \\ −\frac{1}{2} \sqrt{2} & \frac{1}{6} \sqrt{6} & \frac{1}{3}\sqrt{3} \\ 0 & −\frac{1}{3} \sqrt{6} & \frac{1}{3}\sqrt{3} \end{Bmatrix} \begin{Bmatrix} \theta_1 \\ \theta_2 \\ \theta_3 \end{Bmatrix}\nonumber
$$

The normal mode $\eta_3$ has eigenfrequency

$$
\omega_3 = \sqrt{\frac{g}{b}} \sqrt{1- 2\varepsilon}\nonumber
$$

and eigenvector

$$
\boldsymbol{\eta}_3 = \frac{1}{\sqrt{3}} (\theta_1, \theta_2, \theta_3)\nonumber
$$

This corresponds to the in-phase oscillation of all three pendula.

The other two degenerate solutions are

$$
\boldsymbol{\eta}_1 = \frac{1}{\sqrt{2}} (\theta_1, −\theta_2, 0) \quad \boldsymbol{\eta}_2 = \frac{1}{\sqrt{6}} (\theta_1, \theta_2, −2\theta_3)\nonumber
$$

with eigenvalues

$$
\omega_1 = \omega_2 = \sqrt{\frac{g}{b}} \sqrt{ 1 + \varepsilon }\nonumber
$$

These two degenerate normal modes correspond to two pendula oscillating out of phase with the same amplitude, or two oscillating in phase with the same amplitude and the third out of phase with twice the amplitude. An important result of this toy model is that the most symmetric mode $\eta_3$ is pushed far from all the other modes. Note that for this example, the coherent mode $a_3$ corresponds to the center-of-mass oscillation with no relative motion between the three pendula. This is in contrast to the eigenvectors $a_1$ and $a_2$ which both correspond to relative motion of the pendula such that there is zero center-of-mass motion. This mean-field coupling behavior is exhibited by collective motion in nuclei as discussed in example $14.12.1$.

Example 14.2: Three plane pendula; nearest-neighbor coupling

:::{figure} ../images/lt-21234-12.8.2.png
:alt: 12.8.2.PNG

$2$: Three plane pendula with nearest-neighbour coupling.
:::

There is a large and important class of coupled oscillators where the coupling is only between nearest neighbors; a crystalline lattice is a classic example. A toy model for such a system is the case of three identical pendula coupled by two identical springs, where only the nearest neighbors are coupled as shown in the adjacent figure. Assume the identical pendula are of length $b$ and mass $m$. As in the last example, the kinetic energy evaluated at the equilibrium location is

$$
T = \frac{1}{2} mb^2 \dot{\theta}^2_1 + \frac{1}{2} mb^2 \dot{\theta}^2_2 + \frac{1}{2} mb^2 \dot{\theta}^2_3\nonumber
$$

The gravitational potential energy of each pendulum equals $mgb (1 − \cos \theta) \approx \frac{1}{2}mgb \theta^2$ thus

$$
U_{grav} = \frac{1}{2} mgb (\theta^2_1 + \theta^2_2 + \theta^2_3)\nonumber
$$

while the potential energy in the springs is given by

$$
U_{spring} = \frac{1}{2} \kappa b^2 \left[ (\theta_2 − \theta_1)^2 + (\theta_3 − \theta_2)^2 \right] = \frac{1}{2} \kappa b^2 [ \theta^2_1 + 2\theta^2_2 + \theta^2_3 − 2\theta_1\theta_2 − 2\theta_2\theta_3 ]\nonumber
$$

Thus the total potential energy is given by

$$
U = \frac{1}{2} mgb (\theta^2_1 + \theta^2_2 + \theta^2_3) + \frac{1}{2} \kappa b^2 [ \theta^2_1 + 2\theta^2_2 + \theta^2_3 − 2\theta_1\theta_2 − 2\theta_2\theta_3 ] \nonumber
$$

The Lagrangian then becomes

$$
L = \frac{1}{2} mb^2 \left( \dot{\theta}^2_1 + \dot{\theta}^2_2 + \dot{\theta}^2_3 \right) − \frac{1}{2} ( mgb + \kappa b^2) \theta^2_1 + \frac{1}{2} ( mgb + 2\kappa b^2) \theta^2_2 + \frac{1}{2} ( mgb + \kappa b^2) \theta^2_3 − \kappa b^2 (\theta_1\theta_2 + \theta_2\theta_3)\nonumber
$$

Using this in the Euler-Lagrange equations gives the equations of motion

$$
mb^2\ddot{\theta}_1 − (mgb + \kappa b^2)\theta_1 + \kappa b^2\theta_2 = 0 \\ mb^2\ddot{\theta}_2 − (mgb + 2\kappa b^2)\theta_2 + \kappa b^2 (\theta_1 + \theta_3)=0 \\ mb^2\ddot{\theta}_3 − (mgb + \kappa b^2)\theta_3 + \kappa b^2\theta_2 = 0\nonumber
$$

The general analytic approach requires the $T$ and $V$ energy tensors given by

$$
\mathbf{T} = mb^2 \begin{Bmatrix} 1&0&0 \\ 0&1&0 \\ 0&0&1 \end{Bmatrix} \quad \mathbf{V} = \begin{Bmatrix} mgb + \kappa b^2 & −\kappa b^2 & 0 \\ −\kappa b^2 & mgb + 2\kappa b^2 & −\kappa b^2 \\ 0 & −\kappa b^2 & mgb + \kappa b^2 \end{Bmatrix} \nonumber
$$

Note that in contrast to the prior case of three fully-coupled pendula, for the nearest neighbor case the potential energy tensor $\mathbf{\{V\}}$ is non-zero only on the diagonal and $\pm 1$ components parallel to the diagonal.

The third stage is to evaluate the secular determinant of the $( \mathbf{V} − \omega^2 \mathbf{T} )$ matrix, that is

$$
\begin{vmatrix} mgb + \kappa b^2 − \omega^2 mb^2 & −\kappa b^2 & 0 \\ −\kappa b^2 & mgb + 2\kappa b^2 − \omega^2 mb^2 & −\kappa b^2 \\ 0 & −\kappa b^2 & mgb + \kappa b^2 − \omega^2 mb^2 \end{vmatrix} = 0\nonumber
$$

This results in the characteristic equation

$$
( mgb − \omega^2 mb^2) (mgb + \kappa b^2 − \omega^2 mb^2) (mgb + 3\kappa b^2 − \omega^2 mb^2) = 0\nonumber
$$

which results in the three non-degenerate eigenfrequencies for the normal modes.

:::{figure} ../images/lt-21236-12.8.3.png
:alt: 12.8.3.PNG

$3$: Normal modes of three plane pendula with nearest-neighbour coupling.
:::

The normal modes are similar to the prior case of complete linear coupling, as shown in the adjacent figure.

$\omega_1 = \sqrt{\frac{g}{b}}$ This lowest mode $\eta_1$ involves the three pendula oscillating in phase such that the springs are not stretched or compressed thus the period of this coherent oscillation is the same as an independent pendulum of mass $m$ and length $b$. That is

$$
\boldsymbol{\eta}_1 = \frac{1}{\sqrt{3}} (\theta_1, \theta_2, \theta_3)\nonumber
$$

$\omega_2 = \sqrt{\frac{g}{b} + \frac{\kappa}{m}}$. This second mode $\eta_2$ has the central mass stationary with the outer pendula oscillating with the same amplitude and out of phase. That is

$$
\boldsymbol{\eta}_2 = \frac{1}{\sqrt{2}} (\theta_1, 0, −\theta_3)\nonumber
$$

$\omega_3 = \sqrt{\frac{g}{b} + \frac{3\kappa}{m}}$. This third mode $\eta_3$ involves the outer pendula in phase with the same amplitude while the central pendulum oscillating with angle $\theta_3 = −2\theta_1$. That is

$$
\boldsymbol{\eta}_3 = \frac{1}{\sqrt{6}} (\theta_1, −2\theta_2, \theta_3)\nonumber
$$

Similar to the prior case of three completely-coupled pendula, the coherent normal mode $\boldsymbol{\eta}_1$ corresponds to an oscillation of the center-of-mass with no relative motion, while $\boldsymbol{\eta}_2$ and $\boldsymbol{\eta}_3$ correspond to relative motion of the pendula with stationary center of mass motion. In contrast to the prior example of complete coupling, for nearest neighbor coupling the two higher lying solutions are not degenerate. That is, the nearest neighbor coupling solutions differ from when all masses are linearly coupled.

It is interesting to note that this example combines two coupling mechanisms that can be used to predict the solutions for two extreme cases by switching off one of these coupling mechanisms. Switching off the coupling springs, by setting $\kappa = 0$, makes all three normal frequencies degenerate with $\omega_1 = \omega_2 = \omega_3 = \sqrt{\frac{g}{b}}$. This corresponds to three independent identical pendula each with frequency $\omega = \sqrt{\frac{g}{b}}$. Also the three linear combinations $\eta_1, \eta_2, \eta_3$ also have this same frequency, in particular $\eta_1$ corresponds to an in-phase oscillation of the three pendula. The three uncoupled pendula are independent and any combination the three modes is allowed since the three frequencies are degenerate.

The other extreme is to let $\frac{g}{b} = 0$, that is switch off the gravitational field or let $b \rightarrow \infty$, then the only coupling is due to the two springs. This results in $\omega_1 = 0$ because there is no restoring force acting on the coherent motion of the three in-phase coupled oscillators; as a result, oscillatory motion cannot be sustained since it corresponds to the center of mass oscillation with no external forces acting which is spurious. That is, this spurious solution corresponds to constant linear translation.

Example 14.3: System of three bodies coupled by six springs

:::{figure} ../images/lt-21239-12.8.4.png
:alt: 12.8.4.PNG

$4$: System of three bodies coupled by six springs.
:::

Consider the completely-coupled mechanical system shown in the adjacent figure.

1) The first stage is to determine the potential and kinetic energies using an appropriate set of generalized coordinates, which here are $x_1$ and $x_2$. The potential energy is the sum of the potential energies for each of the six springs

$$
U = \frac{3}{2}\kappa x^2_1 + \frac{3}{2}\kappa x^2_2 + \frac{3}{2}\kappa x^2_3 − \kappa x_1x_2 − \kappa x_1x_3 − \kappa x_2x_3\nonumber
$$

while the kinetic energy is given by

$$
T = \frac{1}{2} m\dot{x}^2_1 + \frac{1}{2} m\dot{x}^2_2 + \frac{1}{2} m\dot{x}^2_3\nonumber
$$

2) The second stage is to evaluate the potential energy $V$ and kinetic energy $T$ tensors.

$$
\mathbf{V} = \begin{Bmatrix} 3\kappa & −\kappa & −\kappa \\ −\kappa & 3\kappa & −\kappa \\ −\kappa & −\kappa & 3\kappa \end{Bmatrix} \quad \mathbf{ T} = \begin{Bmatrix} M & 0 & 0 \\ 0 & M & 0\\ 0 & 0 & M \end{Bmatrix}\nonumber
$$

Note that for this case the kinetic energy tensor is diagonal whereas the potential energy tensor is nondiagonal and corresponds to complete coupling of the three coordinates.

3) The third stage is to use the potential $V$ and kinetic $T$ energy tensors to evaluate the secular determinant giving

$$
\begin{vmatrix} ( 3\kappa − m\omega^2 ) & −\kappa & −\kappa \\ −\kappa & ( 3\kappa − m\omega^2 ) & −\kappa \\ −\kappa & −\kappa & ( 3\kappa − m\omega^2 ) \end{vmatrix} = 0\nonumber
$$

The expansion of this secular determinant yields

$$
( \kappa − m\omega^2 ) (4\kappa − m\omega^2 ) (4\kappa − mM\omega^2 ) = 0\nonumber
$$

The solution for this complete-coupled system has two degenerate eigenvalues.

$$
\omega_1 = \omega_2 = 2 \sqrt{\frac{\kappa}{ m}} \quad \omega_3 = \sqrt{\frac{\kappa}{m}}\nonumber
$$

4) The fourth step is to insert these eigenfrequencies into the secular equation

$$
\sum_j ( V_{jk} − \omega^2_r T_{jk}) a_{jr} = 0\nonumber
$$

to determine the coefficients $a_{jr}$.

5) The final stage is to write the general coordinates in terms of the normal coordinates.

The result is that the angular frequency $\omega_3 = \sqrt{\frac{\kappa}{m}}$ corresponds to a normal mode for which the three masses oscillate in phase corresponding to a center-of-mass oscillation with no relative motion of the masses.

$$
\eta_3 = \frac{1}{\sqrt{3}} (x_1 + x_2 + x_3) \nonumber
$$

For this coherent motion only one spring per mass is stretched resulting in the same frequency as one mass on a spring. The other two solutions correspond to the three masses oscillating out of phase which implies all three springs are stretched and thus the angular frequency is higher. Since the two eigenvalues $\omega_1 = \omega_2 = 2\sqrt{\frac{\kappa}{ m}}$ are degenerate then there are only five independent equations to specify the six unknowns for the degenerate eigenvalues. Thus it is possible to select a combination of the eigenvectors $\eta_1$ and $\eta_2$ such that the combination is orthogonal to $\eta_3$. Choose $a_{31} = 0$ to removes the indeterminacy. Then adding or subtracting gives that the normal modes are

$$
\eta_1 = \frac{1}{\sqrt{2}} (x_1 − x_2 + 0) \quad \eta_2 = \frac{1}{\sqrt{2}} (x_1 + x_2 − 2x_3)\nonumber
$$

These two degenerate normal modes correspond to relative motion of the masses with stationary center-of-mass.

## 14.9: Molecular coupled oscillator systems

There are many examples of coupled oscillations in atomic and molecular physics most of which involve nearest-neighbor coupling. The following two examples are for molecular coupled oscillators. The triatomic molecule is a typical linearly-coupled molecular oscillator. The benzene molecule is an elementary example of a ring structure coupled oscillator.

Example 14.1: Linear triatomic molecular CO$_2$

Molecules provide excellent examples of vibrational modes involving nearest neighbor coupling. Depending on the atomic structure, triatomic molecules can be either linear, like CO$_2$, or bent like water, H$_2$O which has a bend angle of $\theta = 109^{\circ}$. A molecule with $n$ atoms has $3n$ degrees of freedom. There are three degrees of freedom for translation and three degrees of freedom for rotation leaving $3n − 6$ degrees of freedom for vibrations. A triatomic molecule has three vibrational modes, two longitudinal and one transverse. Consider the normal modes for vibration of the linear molecule CO$_2$

### Longitudinal modes

The coordinate system used is illustrated in the adjacent figure.

The Lagrangian for this system is

$$
L = \left( \frac{m}{2} \dot{x}^2_1 + \frac{M}{2} \dot{x}^2_2 + \frac{m}{2} \dot{x}^2_3 \right) − \frac{\kappa}{2} [(x_2 − x_1)^2 + (x_3 − x_2)^2 ] \nonumber
$$

Evaluating the kinetic energy tensor gives

$$
\mathbf{T} = \begin{Bmatrix} m & 0 & 0 \\ 0 & M & 0 \\ 0 & 0 & m \end{Bmatrix}\nonumber
$$

while the potential energy tensor gives

$$
\mathbf{V} = \kappa \begin{Bmatrix} 1 & −1 & 0 \\ −1 & 2 & −1 \\ 0 & −1 & 1 \end{Bmatrix} \nonumber
$$

The secular equation becomes

$$
\begin{vmatrix} ( −m\omega^2 + \kappa ) & −\kappa & 0 \\ −\kappa & ( −M\omega^2 + 2\kappa ) & −\kappa \\ 0 & −\kappa & ( −m\omega^2 + \kappa ) \end{vmatrix} = 0\nonumber
$$

Note that the same answer is obtained using Newtonian mechanics. That is, the force equation gives

$$
m\ddot{x}_1 − \kappa (x_2 − x_1)=0 \\ M\ddot{x}_2 + \kappa (x_2 − x_1) − \kappa (x_3 − x_2)=0 \\ m\ddot{x}_3 − \kappa (x_3 − x_2)=0 \nonumber
$$

Let the solution be of the form

$$
x_j = a_j e^{i\omega t} \quad j = 1,2,3 \nonumber
$$

Substitute this solution gives

$$
( −m\omega^2 + \kappa ) a_1 − \kappa a_2 = 0 \\ −\kappa a_1 + ( −M\omega^2 + 2\kappa ) a_2 − \kappa a_3 = 0 \\ −\kappa a_2 + ( m\omega^2 + \kappa ) a_3 = 0\nonumber
$$

This leads to the same secular determinant as given above with the matrix elements clustered along the diagonal for nearest-neighbor problems.

:::{figure} ../images/lt-21241-12.9.1.png
:alt: 12.9.1.PNG

$1$: Normal modes of a linear triatomic molecule
:::

Expanding the determinant and collecting terms yields

$$
\omega^2 ( −m\omega^2 + \kappa ) (−mM\omega^2 + \kappa M + 2\kappa m) = 0\nonumber
$$

Equating either of the three factors to zero gives

$$
\omega_1 = 0 \nonumber
$$

$$
\omega_2 = \sqrt{\frac{ \kappa}{m}}\nonumber
$$

$$
\omega_3 = \sqrt{\left( \frac{ \kappa}{ m} + \frac{2\kappa}{ M}\right)}\nonumber
$$

The solutions are:

1) $\omega_1 = 0$; This solution gives $\eta_1 = a \{1, 1, 1\}$. This mode is not an oscillation at all, but is a pure translation of the system as a whole as shown in the adjacent figure. There is no change in the restoring forces since the system moves such as not to change the length of the springs, that is, they stay in their equilibrium positions. This motion corresponds to a spurious oscillation of the center of mass that results from referencing the three atom locations with respect to some fixed reference point. This reference point should have been chosen as the center of mass since the motion of the center-of-mass already has been taken into account separately. Spurious center of mass oscillations occur any time that the reference point is not at the center of mass for an isolated system with no external forces acting.

2) $\omega^2 = \sqrt{\frac{\kappa}{m}}$: This solution corresponds to $\eta_2 = a \{1, 0, −1\}$ and is shown in the adjacent figure. The central mass $M$ remains stationary while the two end masses vibrate longitudinally in opposite directions with the same amplitude. This mode has a stationary center of mass. For CO$_2$ the electrical geometry is O$^-$C$^{++}$O$^-$. Mode 2 for CO$_2$ does not radiate electromagnetically because the center of charge is stationary with respect to the center of mass, that is, the electric dipole moment is constant.

3) $\omega_3 = \sqrt{( \frac{\kappa}{m} + \frac{2\kappa}{M} )}$: This solution corresponds to $\eta_3 = a \{ 1, −2 ( \frac{m}{M} ) , 1\}$. As shown in the adjacent figure, this motion corresponds to the two end masses vibrating in unison while the central mass vibrates oppositely with a different amplitude such that the center-of-mass is stationary. This CO$_2$ mode does radiate electromagnetically since it corresponds to an oscillating electric dipole.

It is interesting to note that the ratio $\frac{\omega_3}{\omega_2} = 1.915$ for CO$_2$ and the ratio of the two modes is independent of the potential energy tensor $V$. That is

$$
\frac{\omega_3}{\omega_2} = \sqrt{\left(1 + 2\frac{m}{M}\right)}\nonumber
$$

### Transverse modes

The solutions are:

4) $\omega_4 = \sqrt{ 2 \left( \frac{2m+M}{M} \right) \frac{\kappa}{m}}$. This is the only non-spurious transverse mode $\eta_4$ which corresponds to the two outside masses vibrating in unison transverse to the symmetry axis while the central mass vibrates oppositely. This mode radiates electric dipole radiation since the electric dipole is oscillating.

5) $\omega_5 = 0$. This transverse solution $\eta_5$ has all three nuclei vibrating in unison transverse to the symmetry axis and corresponds to a spurious center of mass oscillation.

6) $\omega_6 = 0$. This transverse solution $\eta_6$ corresponds to a stationary central mass with the two outside masses vibrating oppositely. This corresponds to a rotational oscillation of the molecule which is spurious since there are no torques acting on the molecule for a central force. Rotational motion usually is taken into account separately.

The normal modes for the bent triatomic molecule are similar except that the oscillator coupling strength is reduced by the factor $\cos \theta$ where $\theta$ is the bend angle.

Example 14.2: Benzene ring

The benzene ring comprises six carbon atoms bound in a plane hexagonal ring. A classical analog of the benzene ring comprises 6 identical masses $m$ on a frictionless ring bound by 6 identical springs with linear spring constant $K$, as illustrated in the adjacent figure. Consider only the in-plane motion, then the kinetic energy is given by

$$
T = \frac{1}{2} mr^2 \sum^6_{i=1} \dot{\theta}^2_i\nonumber
$$

The potential energy equals

$$
U = \frac{1}{2} Kr^2 \sum^6_{i=1} (\theta_{i+1} − \theta_i)^2 = Kr^2 \left[ \sum^6_{i=1} \theta^2_i − \theta_1\theta_2 − \theta_2\theta_3 − \theta_3\theta_4 − \theta_4\theta_5 − \theta_5\theta_6 − \theta_6\theta_1 \right]\nonumber
$$

where $i = 7 \equiv 1$. Thus the kinetic energy and potential energy tensors are given by

$$
T = mr^2 \begin{pmatrix} 1&0&0&0&0&0 \\0&1&0&0&0&0\\ 0&0&1&0&0&0\\ 0&0&0&1&0&0\\ 0&0&0&0&1&0 \\0&0&0&0&0&1 \end{pmatrix} \quad U = Kr^2 \begin{pmatrix} 2& −1&0& 0& 0& −1\\ −1 &2 &−1&0& 0& 0\\ 0 &−1 &2 &−1&0 &0 \\0 &0 &−1 &2 &−1 & 0\\ 0&0&0& −1& 2 &−1 \\−1&0& 0& 0& −1 &2 \end{pmatrix}\nonumber
$$

This nearest-neighbor system includes non-zero $(n, 1)$ and $(1, n)$ elements due to the ring structure. Define $x = \frac{m\omega^2}{K} − 2$ then the solution of the set of linear homogeneous equations requires that

$$
\begin{vmatrix} x& 1&0&0&0&1 \\1 &x& 1&0&0&0 \\0 &1 &x &1&0&0\\ 0&0&1& x& 1& 0\\ 0&0&0&1& x& 1\\ 1&0&0&0&1& x \end{vmatrix} = 0\nonumber
$$

that is

$$
(x − 2) (x − 1)^2 (x + 1)^2 (x + 2) = 0\nonumber
$$

:::{figure} ../images/lt-21242-12.9.2.png
:alt: 12.9.2.PNG

$2$
:::

The eigenvalues and eigenfunctions are given in the table

| $n$ | $x_n$ | $\omega^2_n$ | Normal modes |
| --- | --- | --- | --- |
| 1 | 2 | $\frac{4K}{m}$ | $\theta_1−\theta_2+\theta_3−\theta_4+\theta_5−\theta_6$ |
| 2 | 1 | $\frac{3K}{m}$ | $−\theta_1+\theta_3−\theta_4+\theta_6$ |
| 3 | 1 | $\frac{3K}{m}$ | $−\theta_1+\theta_2−\theta_4+\theta_5$ |
| 4 | -1 | $\frac{K}{m}$ | $\theta_1−\theta_3−\theta_4+\theta_6$ |
| 5 | -1 | $\frac{K}{m}$ | $−\theta_1−\theta_2+\theta_4+\theta_5$ |
| 6 | -2 | 0 | $\theta_1+\theta_2+\theta_3+\theta_4+\theta_5+\theta_6$ |

Note the following properties of the normal modes and their frequencies.

$n = 1$: Adjacent masses vibrate 180$^{\circ}$ out of phase, thus each spring has maximal compression or extension, leading to the energy of this normal mode being the highest.

$n = 2, 3$: These two solutions are degenerate and correspond to two pairs of masses vibrating out of phase while the third pair of masses are stationary. Thus the energy of this normal mode is slightly lower than the $n = 1$ normal mode. Any combination of these degenerate normal modes are equally good solutions.

$n = 4, 5$: From the figure it can be seen that both of these solutions correspond to a center of mass oscillation and thus these modes are spurious.

$n = 6$: This vibrational mode has zero energy corresponding to zero restoring force and all six masses moving uniformly in the same direction. This mode corresponds to the rotation of the benzene molecule about the symmetry axis of the ring which usually is taken into account assuming a separate rotational component.

This classical analog of the benzene molecule is interesting because it simultaneously exhibits degenerate normal modes, spurious center of mass oscillation, and a rotational mode.

## 14.10: Discrete Lattice Chain

Crystalline lattices and linear molecules are important classes of coupled oscillator systems where nearest neighbor interactions dominate. A crystalline lattice comprises thousands of coupled oscillators in a three dimensional matrix with atomic spacing of a few $10^{−10}m$. Even though a full description of the dynamics of crystalline lattices demands a quantal treatment, a classical treatment is of interest since classical mechanics underlies many features of the motion of atoms in a crystalline lattice. The linear discrete lattice chain is the simplest example of many-body coupled oscillator systems that can illuminate the physics underlying a range of interesting phenomena in solid-state physics. As illustrated in example $2.12.1$, the linear approximation usually is applicable for small-amplitude displacements of nearest-neighbor interacting systems which greatly simplifies treatment of the lattice chain. The linear discrete lattice chain involves three independent polarization modes, one longitudinal mode, plus two perpendicular transverse modes. The $3n$ degrees of freedom for the $n$ atoms, on a discrete linear lattice chain, are partitioned with $n$ degrees of freedom for each of the three polarization modes. These three polarization modes each have $n$ normal modes, or $n$ travelling waves, and exhibit quantization, dispersion, and can have a complex wave number.

### Longitudinal Motion

The equations of motion for longitudinal modes of the lattice chain can be derived by considering a linear chain of $n$ identical masses, of mass $m$, separated by a uniform spacing $d$ as shown in Figure 14.1. Assume that the $n$ masses are coupled by $n + 1$ springs, with spring constant $\kappa$, where both ends of the chain are fixed, that is, the displacements $q_0 = q_{n+1} = 0$ and velocities $\dot{q}_0 = \dot{q}_{n+1} = 0$. The force required to stretch a length $d$ of the chain a longitudinal displacements, $q_{j}$ for mass $j$, is $F_j = \kappa q_j$. Thus the potential energy for stretching the spring for segment $(q_{j−1} − q_j )$ is $U_j = \frac{\kappa}{2} (q_{j-1} - q_j)$. The total potential and kinetic energies are

$$
U = \frac{\kappa}{2} \sum^{n+1}_{j=1} (q_{j-1} - q_j)^2 \label{14.74}
$$

$$
T = \frac{1}{2} m \sum^{n}_{j=1} \dot{q}^2_j \label{14.75}
$$

:::{figure} ../images/lt-21243-12.10.1.png
:alt: 12.10.1.PNG

$1$: Portion of a lattice chain of identical masses $m$ connected by identical springs of spring constant $\kappa$. The displacement of the $j^{th}$ mass from the equilibrium position is $q_j$ assumed to be positive to the right.
:::

Since $\dot{q}_{n+1} = 0$ the kinetic energy and Lagrangian can be extended to $j = {n+1}$, that is, the Lagrangian can be written as

$$
L = \frac{1}{2} \sum^{n+1}_{j=1} \left( m\dot{q}^2_j − \kappa (q_{j−1} − q_j )^2 \right)
$$

Using this Lagrangian in the Lagrange-Euler equations gives the following second-order equation of motion for longitudinal oscillations

$$
\ddot{q}_j = \omega^2_o (q_{j-1} − 2q_j + q_{j+1}) \label{14.77}
$$

where $j = 1, 2, ....n$ and where

$$
\omega_o \equiv \sqrt{\frac{\kappa}{m}}
$$

### Transverse motion

:::{figure} ../images/lt-21244-12.10.2.png
:alt: 12.10.2.PNG

$2$: Transverse motion of a linear discrete lattice chain
:::

The equations of motion for transverse motion on a linear discrete lattice chain, illustrated in Figure 14.2, can be derived by considering the displacements $q_j$ of the $i^{th}$ mass for $n$ identical masses, with mass $m$, separated by equal spacings $d$ and assuming that the tension in the string is $r = \left( \frac{\partial U}{\partial x} \right)$. Assuming that the transverse deflections $q_j$ are small, then the $j − 1$ to $j$ spring is stretched to a length

$$
d^{\prime} = \sqrt{d^2 + (q_j − q_{j-1})^2}
$$

Thus the incremental stretching is

$$
\delta d \sim \frac{(q_j − q_{j-1})^2}{2d}
$$

The work done against the tension $\tau$ is $\tau \cdot \delta d$ per segment. Thus the total potential energy is

$$
U = \frac{\tau}{2d} \sum^{n+1}_{j=1} (q_{j-1} − q_j )^2
$$

where $q_0$ and $q_{n+1}$ are identically zero.

The kinetic energy is

$$
T = \frac{1}{2} m\sum^n_{ j=1} \dot{q}^2_j
$$

Since $\dot{q}_{n+1} = 0$, the kinetic energy and Lagrangian summations can be extended to $j = n + 1$, that is

$$
L = \frac{1}{2} \sum^{n+1}_{j=1} \left( m\dot{q}^2_j − \frac{\tau}{d} (q_{j-1} − q_j )^2 \right)
$$

Using this Lagrangian in the Lagrange Euler equations gives the following second-order equation of motion for transverse oscillations

$$
\ddot{q}_j = \omega^2_o (q_{j-1} − 2q_j + q_{j+1}) \label{14.84}
$$

where $j = 1, 2, ....n$ and

$$
\omega_o \equiv \sqrt{\frac{\tau}{dm}}
$$

The normal modes for the transverse modes comprise standing waves that satisfy the same boundary conditions as for the longitudinal modes. The $n$ equations of motion for longitudinal motion, Equation \ref{14.77}, or transverse motion, Equation \ref{14.84}, are identical in form. The major difference is that $\omega_0$ for the transverse normal modes $\omega_o \equiv \sqrt{\frac{\tau}{dm}}$ differs from that for the longitudinal modes which is $\omega_o \equiv \sqrt{\frac{\kappa}{m}}$. Thus the following discussion of the normal modes on a discrete lattice chain is identical in form for both transverse and longitudinal waves.

### Normal modes

The normal modes of the $n$ equations of motion on the discrete lattice chain, are either longitudinal or transverse standing waves that satisfy the boundary conditions at the extreme ends of the lattice chain. The solutions can be given by assuming that the $n$ identical masses on the chain oscillate with a common frequency $\omega$. Then the displacement amplitude for the $j^{th}$ mass can be written in the form

$$
q_j (t) = a_j e^{i\omega t}
$$

where the amplitude $a_j$ can be complex. Substitution into the preceding $n$ equations of motion, \ref{14.77}, \ref{14.84}, yields the following recursion relation

$$
\left( −\omega^2 + 2\omega^2_o \right) a_j− \omega^2_0 (a_{j−1} + a_{j+1})=0 \label{14.87}
$$

where $j = 1, 2, ...n$. Note that the boundary conditions, $q_0 = 0$ and $q_{n+1} = 0$ require that $a_o = a_{n+1} = 0$.

The above recursion relation corresponds to a system of $n$ homogeneous algebraic equations with $n$ unknowns $a_1, a_2, ...a_n$. A non-trivial solution is given by setting the determinant of its coefficients equal to zero

$$
\begin{vmatrix} −\omega^2 + 2\omega^2_o & −\omega^2_o & 0 & 0 \\ −\omega^2_o & −\omega^2 + 2\omega^2_o & −\omega^2_o & 0 \\ 0 & −\omega^2_o & −\omega^2 + 2\omega^2_o & −\omega^2_o \\ ..... & .... & ..... & ..... \\ 0 & 0 & −\omega^2_o & −\omega^2 + 2\omega^2_o \end{vmatrix} = 0
$$

This secular determinant corresponds to the special case of nearest neighbor interactions with the kinetic energy tensor $\mathbf{T}$ being diagonal and the potential energy tensor $\mathbf{V}$ involving coupling only to adjacent masses. The secular determinant is of order $n$ and thus determines exactly $n$ eigen frequencies $\omega_r$ for each polarization mode.

For large $n$, the solution of this problem is more efficiently obtained by using a recursion relation approach, rather than solving the above secular determinant. The trick is to assume that the phase differences $\phi_r$ between the motion of adjacent masses all are identical for a given polarization. Then the amplitude for the $j^{th}$ mass for the $r^{th}$ frequency mode $\omega_r$ is of the form

$$
a_{jr} = a_{r} e^{i(j\phi_r−\delta_r)}
$$

Insert the above into the recursion relation \ref{14.87} gives

$$
\left( −\omega^2_r + 2\omega^2_o \right) − \omega^2_0 \left[ e^{-i\phi_r} + e^{i\phi_r} \right] = 0
$$

which reduces to

$$
\omega^2_r = 2\omega^2_o − 2\omega^2_o \cos \phi_r = 4\omega^2_o \sin^2 \frac{\phi_r}{2}
$$

that is

$$
\omega_r = 2\omega_o \sin \frac{\phi_r}{2}
$$

where $r = 1, 2, 3, ....n$.

Now it is necessary to determine the phase angle $\phi_r$ which can be done by applying the boundary conditions for standing waves on the lattice chain. These boundary conditions for stationary modes require that the ends of the lattice chain are nodes, that is $a_{o,r} = a_{(n+1),r} = 0$. Using the fact that only the real part of $a_{jr}$ has physical meaning, leads to the amplitude for the $j^{th}$ mass for the $r^{th}$ mode to be

$$
a_{j,r} = a_{r} \cos (j\phi_r − \delta_r)
$$

The boundary condition $a_{0r} = 0$ requires that the phase $\delta_r = \frac{\pi}{2}$. That is

$$
a_{jr} = a_{r} \cos \left( j\phi_r − \frac{\pi }{2} \right) = a_{r} \sin j\phi_r \label{14.93}
$$

where $r = 1, 2, ..., n$.

The boundary condition for $j = n+1$, gives

$$
a_{(n+1)r} =0= a_{r} \sin (n+1) \phi_r
$$

Therefore

$$
(n+1) \phi_r = r\pi
$$

where $r = 1, 2, 3, ..., n$. That is

$$
\phi_r = \frac{r\pi}{n+1} = \frac{r\pi d}{ (n+1) d} = \frac{r\pi d}{D} = \frac{k_r d}{2} \label{14.96}
$$

where $D = (n+1)d$ is the total length of the discrete lattice chain.

The $n$ eigen frequencies for a given polarization are given by

$$
\omega_r = 2\omega_o \sin \frac{r\pi}{ 2 (n+1)} = 2\omega_o \sin \frac{r\pi d}{2 (n+1) d} = 2\omega_o \sin\frac{ r\pi d}{ 2D} = 2\omega_o \sin \frac{k_rd}{ 2} \label{14.97}
$$

where the corresponding wavenumber $k_r$ is given by

$$
k_r = \frac{r\pi }{(n+1) d }= \frac{r\pi}{D} = \frac{2\pi}{ \lambda_r}
$$

This implies that the normal modes are quantized with half-wavelengths $\frac{\lambda_r}{2} = \frac{D}{r}$.

:::{figure} ../images/lt-21246-12.10.3.png
:alt: 12.10.3.PNG

$3$: Plots of the maximal vibrational amplitudes $a_r$ for the $r^{th}$ frequency sinusoidal mode, versus distance along the chain, for transverse normal modes of a vibrating discrete lattice with $n = 5$. Only $r = 1, 2, 3, 4, 5,$ are distinct modes because $r = 6$ is a null mode. Note that the modes with $r = 7, 8, 9, 10, 11, 12,$ shown dashed, duplicate the locations of the mass displacement given by the lower-order modes.
:::

Combining equations \ref{14.96} and \ref{14.93} gives the maximum amplitudes for the eigenvectors to be

$$
a_{jr} = a_r \sin j \frac{k_r d}{2} \label{14.99}
$$

For $n$ independent linear oscillators there are only $n$ independent normal modes, that is, for $r = n+1$ the sine function in Equation \ref{14.97} must be zero. Beyond $r = n$ the equations do not describe physically new situations. This is illustrated by Figure 14.3 which shows the transverse modes of a lattice chain with $n = 5$. There are only $n = 5$ independent normal modes of this system since $r = n +1=6$ corresponds to a null mode with all $q_j (t)=0$. Also note that the solutions for $r>n+1$, shown dashed, replicate the mass locations of modes with $r<n+1$, that is, the modes with $r > 6$ are replicas of the lower-order modes.

Note that $\omega_r$ has a maximum value $\omega_r \leq 2\omega_0$ since the sine function cannot exceed unity. This leads to a maximum frequency $\omega_c = 2\omega_0$, called the cut-off frequency, which occurs when $k_rd = \pi$. That is, the null-mode occurs when $r = n+1$ for which Equation \ref{14.99} equals zero. The range of $n$ quantized normal modes that can occur is intuitive. That is, the longest half-wavelength $\frac{\lambda_{\text{max}}}{2} = D = ({n+1})d$ equals the total length of the discrete lattice chain. The shortest half-wavelength $\frac{\lambda_{cut−off}}{2} = d$ is set by the lattice spacing. Thus the discrete wavenumbers of the normal modes, for each polarization, range from $k_1$ to $nk_1$ where $n$ is an integer.

Assuming real $k_r$, the normal coordinate $\eta_r$ and corresponding frequency $\omega_r$ are,

$$
\eta_r = a_{r} e^{i\omega_rt}
$$

Equations \ref{14.97} and \ref{14.99} give the angular frequency and displacement. Note that superposition applies since this system is linear. Therefore the most general solution for each polarization can be any superposition of the form

$$
q_j (t) = \sum^n_{ r=1 } \eta_r \sin \left[ \frac{r\pi j}{ (n+1)} \right]
$$

### Travelling waves

Travelling waves are equally good solutions of the equations of motion \ref{14.77}, \ref{14.84} as are the normal modes. Travelling waves on the one-dimensional lattice chain will be of the form

$$
q (x, t) = Ce^{i(\omega t \pm kx)} \label{14.102}
$$

where the distance along the chain $x = \nu d$, that is, it is quantized in units of the cell spacing $d$, with $\nu$ being an integer. The positive sign in the exponent corresponds to a wave travelling in the $−x$ direction while the negative sign corresponds to a wave travelling in the $+x$ direction. The velocity of a fixed phase of the travelling wave must satisfy that $\omega t \pm kx$ is a constant. This will occur if the *phase velocity* of the wave is given by

$$
v^{phase} = \frac{dx}{dt} = \frac{\omega}{k}
$$

The wave has a frequency $f = \frac{\omega}{ 2\pi}$ and wavelength $\lambda = \frac{2\pi}{k}$, thus the phase velocity $v_{phase} = \frac{\omega}{k} = \lambda f$.

Inserting the travelling wave \ref{14.102} into the transverse equation of motion \ref{14.84} for the discrete lattice chain gives

$$
−\omega^2q_r = \omega^2_0(e^{−\phi_r} − 2 + e^{\phi_r} )q_r
$$

where $j = 1, 2, ....n$. That is

$$
\omega_r = \pm 2\omega_0 \sin \frac{\phi_r}{2} \label{14.105}
$$

The phase $\phi_r$ is determined by the Born-von Karman periodic boundary condition that assumes that the chain is duplicated indefinitely on either side of $k = \pm \frac{\pi}{d}$. Thus, for $n$ discrete masses, $k$ must satisfy the condition that $q_r = q_{r+n}$. That is

$$
e^{ik_rnd} = 1
$$

That is

$$
k_r = \frac{2\pi r}{nd}
$$

Note that the periodic boundary condition gives $n$ discrete modes for wavenumbers between

$$
−\frac{\pi}{d} \leq k_r \leq + \frac{\pi}{d}
$$

where the index

$$
r = −\frac{n}{2}, −\frac{n}{2} + 1, ....., \frac{n}{2} − 1, \frac{n}{2} \nonumber
$$

Thus Equation \ref{14.105} becomes

$$
\omega_r = \pm 2\omega_0 \sin \frac{k_r d}{2} \label{14.109}
$$

Equation \ref{14.109} is a dispersion relation that is identical to Equation \ref{14.97} derived during the discussion of the normal modes of the lattice chain. This confirms that the travelling waves on the lattice chain are equally good solutions as the normal standing-wave modes. Clearly, superposition of the standing-wave normal modes can lead to travelling waves and vice versa.

### Dispersion

:::{figure} ../images/lt-21245-12.10.4.png
:alt: 12.10.4.PNG

$4$: Plot of the dispersion curve ($\omega$ versus $k$) for a monoatomic linear lattice chain subject to only nearest neighbor interactions. The first Brillouin zone is the segment between $−\frac{\pi}{d} \leq k \leq \frac{\pi}{d}$ which covers all independent solutions.
:::

The lattice chain is an interesting example of a dispersive system in that $\omega_r$ is a function of $k_r$. Figure 14.4 shows a plot of the dispersion curve ($\omega$ versus $k$) for a monoatomic linear lattice chain subject to only nearest neighbor interactions. Note that $\omega$ depends linearly on $k$ for small $k$ and that $\frac{d\omega}{dk} = 0$ at the boundaries of the first Brillouin zone.

The lattice chain has a phase velocity for the $r^{th}$ wave given by

$$
v^{phase}_r = \frac{\omega_r}{k_r} = \omega_0 d \frac{|\sin \frac{k_r d}{2}|}{ \frac{k_r d}{2}}
$$

while the group velocity is

$$
v^{group}_r = \left(\frac{d\omega}{dk} \right)_r = \omega_0 d \cos \frac{k_r d}{2}
$$

Note that in the limit when $\frac{k_r d}{2} \rightarrow 0$, the phase velocity and group velocity are identical, that is, $v^{phase}_r = v^{group}_r = \omega_0d$.

### Complex wavenumber

The maximum allowed frequency, which is called the cut-off frequency, $\omega_c = 2\omega_0$, occurs when $k_rd = \pi$, that is, $\frac{\lambda}{2} = d$. That is, the minimum half-wavelength equals the spacing $d$ between the discrete masses. At the cut-off frequency, the phase velocity is $v^{phase}_r = \frac{2}{\pi } \omega_0d$ and the group velocity $v^{group}_r = 0$.

It is interesting to note that $\omega_r$ can exceed the cut-off frequency $\omega_c = 2\omega_0$ if $k_r$ is assumed to be complex, that is, if

$$
k_r = \kappa_r − i\Gamma_r
$$

Then

$$
\omega_r = 2\omega_0 \sin \frac{k_r d}{2} = 2\omega_0 \sin \frac{d}{2} (\kappa_r − i\Gamma_r)=2\omega_0 \left( \sin \frac{\kappa_rd}{2} \cosh \frac{\Gamma_rd}{2} − i \cos \frac{\kappa_rd}{2} \sinh \frac{\Gamma_rd }{2} \right)
$$

To ensure that $\omega_r$ is real, the imaginary term must be zero, that is

$$
\cos \frac{\kappa_rd}{2} = 0
$$

Therefore

$$
\sin \frac{\kappa_rd}{2} = 1
$$

that is, $k_r = \frac{\pi}{d}$, and the dispersion relation between $\omega$ and $k$ for $\omega > 2\omega_0$ becomes

$$
\omega_r = 2\omega_0 \cosh \frac{\Gamma_rd}{2}
$$

which increases with $\Gamma$. Thus, when $\omega > \omega_c = 2\omega_0$ then the amplitude of the wave is of the form

$$
q_r (t) = a_r e^{−\Gamma_rx}e^{i(\omega_rt−\kappa_rx)}
$$

which corresponds to a spatially damped oscillatory wave with phase velocity

$$
v^{phase}_r = \frac{\omega_r}{\kappa_r}
$$

and damping factor $\Gamma_r$.

There are many examples in physics where the wavenumber is complex as exhibited by the discrete lattice chain for $\frac{\lambda}{2} \leq d$. Other examples are electromagnetic waves in conductors or plasma (example $3.11.3$), matter waves tunnelling through a potential barrier, or standing waves on musical instruments which have a complex wavenumber $k$ due to damping.

This simple toy model of the discrete linear lattice chain has illustrated that classical mechanics explains many features of the many-body nearest-neighbor coupled linear oscillator system, including normal modes, standing and travelling waves, cut-off frequency dispersion, and complex wavenumber. These phenomena feature prominently in applications of the quantal discrete coupled-oscillator system to solid-state physics.

## 14.11: Damped Coupled Linear Oscillators

The discussion of coupled linear oscillators has neglected non-conservative damping forces which always exist to some extent in physical systems. In general, dissipative forces are non linear which greatly complicates solving the equations of motion for such coupled oscillator systems. However, for some systems the dissipative forces depend linearly on velocity which allows use of the Rayleigh dissipation function, described in chapter $10.4$. The most general definition of the Rayleigh dissipation function, $10.4$, was given to be

$$
\mathcal{R} = \frac{1}{2} \sum^n_{i=1} \sum^n_{j=1} c_{ij} \dot{q}_i\dot{q}_j
$$

For this special case, it was shown in chapter $10$ that the Lagrange equations can be written in terms of the Rayleigh dissipation function as

$$
\left\{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_j}\right) - \frac{\partial L}{\partial q_j} \right\} + \frac{\partial \mathcal{R}}{\partial \dot{q}_j} = Q_j \label{14.120}
$$

where $Q_j$ are generalized forces acting on the system that are not absorbed into the potential $U$. Using equations $(14.6.17)$, $(14.6.18)$, and \ref{14.120}, allows the equations of motion for damped coupled linear oscillators to be written in a matrix form as

$$
\mathbf{\{T\}} \mathbf{\ddot{q}} + \mathbf{\{C\}} \mathbf{\dot{q}}+ \mathbf{\{V\}} \mathbf{q} = \mathbf{\{Q\}}
$$

where the symmetric matrices $\mathbf{\{T\}}$, $\mathbf{\{C\}}$, and $\mathbf{\{V\}}$ are positive definite for positive definite systems. Rayleigh pointed out that in the special case where the damping matrix $\mathbf{\{C\}}$ is a linear combination of the $\mathbf{\{T\}}$ and $\mathbf{\{V\}}$ matrices, then the matrix $\mathbf{\{C\}}$ is diagonal leading to a separation of the damped system into normal modes. As discussed in chapter 4 many systems in nature are linear for small amplitude oscillations allowing use of the Rayleigh dissipation function which provides an analytic solution. However, in general, except for when $\mathbf{\{C\}}$ is small, this separation into normal modes is not possible for damped systems and the solutions must be obtained numerically.

The following example illustrates approaches used to handle linearly-damped coupled-oscillator systems.

Example 14.1: Two linearly-damped coupled linear oscillators

:::{figure} ../images/lt-21247-12.11.1.png
:alt: 12.11.1.PNG

$1$: Two linearly-damped coupled linear oscillators.
:::

Consider the two coupled oscillator system shown where the two carts have spring constants $k_1, k_2$ and linear damping constants $c_1c_2$. As discussed in example $14.7.2$, the kinetic energy tensor is given by

$$
T = \frac{1}{2} m_1 \dot{q}^2_1 + \frac{1}{2} m_2 \dot{q}^{2}_{2} \label{14-a}\tag{a}
$$

and the potential energy is given by

$$
U = \frac{1}{2} \left[ k_1q^2_1 + k_2 (q_2 − q_1)^2 \right] \\ = \frac{1}{2} \left[ (k_1 + k_2) q^2_1 − 2k_2q_1q_2 + k_2q_2^2 \right] \label{14-b}\tag{b}
$$

Similarly the Rayleigh dissipation function has the form

$$
\mathcal{R} =\frac{1}{2} \left[ c_1\dot{q}^2_1 + c_2 ( \dot{q}^2_2 − \dot{q}^2_1 )\right] = \frac{1}{2} \left[ (c_1 + c_2) \dot{q}^2_1 − 2c_2\dot{q}_1\dot{q}_2 + c_2\dot{q}^2_2 \right] \label{14-c}\tag{c}
$$

Inserting equations \ref{14-a}, \ref{14-b}, and \ref{14-c} into Equation \ref{14.120} gives the two equations of motion to be

$$
m_1 \ddot{q}_1 + (c_1 + c_2) \dot{q}_1 − c_2\dot{q}_2 + (k_1 + k_2) q_1 − k_2q_2 = 0 \\ m_2 \ddot{q}_2 − c_2\dot{q}_1 + c_2\dot{q}_2 − k_2q_1 + k_2q_2 = 0 \nonumber
$$

When the drag is zero the solution of these two coupled equations can be separated into two independent normal modes of the system as described earlier. Usually it is not possible to separate the motion into decoupled normal modes except for certain cases where the dissipative forces can be described by Rayleigh’s dissipation function.

## 14.12: Collective Synchronization of Coupled Oscillators

Collective synchronization of coupled oscillators is a multifaceted phenomenon where large ensembles of coupled oscillators, with comparable natural frequencies, self synchronize leading to coherent collective modes of motion. Biological examples include congregations of synchronously flashing fireflies, crickets that chirp in unison, an audience clapping at the end of a performance, networks of pacemaker cells in the heart, insulin-secreting cells in the pancreas, as well as neural networks in the brain and spinal cord that control rhythmic behaviors such as breathing, walking, and eating. Example **14.13** illustrates an application to nuclei.

An ensemble of coupled oscillators will have a frequency distribution with a finite width. It is interesting to elucidate how an ensemble of coupled oscillators, that have a finite width frequency distribution, can self synchronize their motion to a unique common frequency, and how that synchronization is maintained over long time periods. The answers to these issues provide insight into the dynamics of coupled oscillators.

The discussion of coupled oscillators has implicitly assumed $n$ identical undamped linear oscillators that have identical, infinitely-sharp, natural frequencies $\omega_i$. In nature typical coupled oscillators can have a finitewidth frequency distribution $g(\omega)$ about some average value, due to the natural variability of the oscillator parameters for biological systems, the manufacturing tolerances for mechanical oscillators, or the natural Lorentzian frequency distribution associated with the uncertainty principle that occurs even for atomic clocks where the oscillator frequencies are defined directly by the physical constants. Assume that the ensemble of coupled oscillators has a frequency distribution $g(\omega)$ about some average value.

Undamped linear oscillators have elliptical closed-path trajectories in phase space whereas dissipation leads to a spiral attractor unless the system is driven such as to preserve the total energy. As described in chapter $4.4$ many systems in nature, especially biological systems, have closed limit cycles in phase space where the energy lost to dissipation is replenished by a driving mechanism. The simplest systems for understanding collective synchronization of coupled oscillators are those that involve closed limit cycles in phase space.

N. Wiener first recognized the ubiquity of collective synchronization in the natural world, but his mathematical approach, based on Fourier integrals, was not suited to this problem. A more fruitful approach was pioneered in 1975 by an undergraduate student A.T. Winfree[Win67] who recognized that the long-time behavior of a large ensemble of limit-cycle oscillators can be characterized in the simplest terms by considering only the phase of closed phase-space trajectories. He assumed that the instantaneous state of an ensemble of oscillators can be represented by points distributed around the circular phase-space diagram shown in Figure 14.1. For uncoupled oscillators these points will be distributed randomly around the circle, whereas coupling of the oscillators will result in a spatial correlation of the points. That is, the dynamics of the phases can be visualized as a swarm of points running around the unit circle in the complex plane of the phase space diagram. The complex order parameter of this swarm can be defined to be the magnitude and phase of the centroid of this swarm

$$
re^{i\psi} = \frac{1}{N} \sum^{N}_{j=1} e^{i\theta_j} \label{14.122}
$$

:::{figure} ../images/lt-21249-12.12.1.png
:alt: 12.12.1.PNG

$1$: Order parameter for weakly-coupled oscillators.
:::

The centroid of the ensemble of points on the phase diagram has a magnitude $r$, designating the offset of the centroid from the center of the circular phase diagram, and $\psi$ which is the phase of this centroid. A uniform distribution of points around the unit circle will lead to a centroid $r = 0$. Correlated motion leads to a bunching of the points around some phase value leading to a non-zero centroid $r$ and angle $\psi$. If the swarm acts like a fully-coupled single oscillator then $r \approx 1$ with an appropriate phase $\psi$.

The **Kuramoto model**[Kur75, Str00] incorporates Winfree’s intuition by mapping the limit cycles onto a simple circular phase diagram and incorporating the long-term dynamics of coupled oscillators in terms of the relative phases for a mean-field system. That is, the angular velocity of the phase $\dot{\phi}_i$ for the $i^{th}$ oscillator is

$$
\dot{\phi}_i = \omega_i + \sum^{N}_{j=1} \Gamma_{ij} ( \phi_j - \phi_i)
$$

:::{figure} ../images/lt-21253-12.12.2.png
:alt: 12.12.2.PNG

$2$: Kuramoto model of collective synchronization of coupled oscillators. The left and center plots show the time and coupling strength dependence of the order parameter $r$. The right plot shows the frequency dependence including coupling (solid line) and without coupling (dashed line).
:::

where $i = 1, 2,,,N$. Kuramoto recognized that mean-field coupling was the most tractable system to solve, that is, a system where the coupling is applicable equally to all the oscillators. Moreover, he assumed an equally-weighted, pure sinusoidal coupling for the coupling term $\Gamma_{ij} (\theta_j −\theta_i)$ between the coupled oscillators. That is, he assumed

$$
\Gamma_{ij} (\phi_j − \phi_i) = \frac{K}{N} \sin (\phi_j − \phi_i)
$$

where $K \geq 0$ is the coupling strength, and the factor $\frac{1}{N}$ ensures that the model is well behaved as $N \rightarrow \infty$. Kuramoto assumed that the frequency distribution $g(\omega)$ was unimodular and symmetric about the mean frequency $\Omega$, that is $g(\Omega + \omega) = g(\Omega − \omega)$.

This problem can be simplified by exploiting the rotational symmetry and transforming to a frame of reference that is rotating at an angular frequency $\Omega$. That is, use the transformation $\theta_i = \phi_i − \Omega t$ where $\theta_i$ is measured in the rotating frame. This makes $g(\omega)$ unimodular with a symmetric frequency distribution about $\omega = 0$. The phase velocity in this rotating frame is

$$
\dot{\theta}_i = \omega_i + \sum^N_{j=1} \frac{K}{N} \sin(\theta_j − \theta_i) \label{14.125}
$$

Kuramoto observed that the phase-space distribution can be expressed in terms of the order parameters $r, \psi$ in that Equation \ref{14.122} can be multiplied on both sides by $e^{-i\theta_i}$ to give

$$
re^{i(\psi−\theta_i)} = \frac{1}{N} \sum^{N}_{j=1} e^{i(\theta_j−\theta_i)}
$$

Equating the imaginary parts yields

$$
r \sin (\psi − \theta_i) = \frac{1}{N} \sum^{N}_{j=1} \sin (\theta_j − \theta_i)
$$

This allows Equation \ref{14.125} to be written as

$$
\dot{\theta}_i = \omega_i + Kr \sin(\psi − \theta_i) \label{14.128}
$$

for $i = 1, 2,,N$. Equation \ref{14.128} reflects the mean-field aspect of the model in that *each oscillator*$\theta_i$*is attracted to the phase of the mean field*$\psi$*rather than to the phase of another individual oscillator.*

Simulations showed that the evolution of the order parameter with coupling strength $K$ is as illustrated in Figure 14.2. This simulation shows (1) for all $K$, when below a certain threshold $K_c$, the order parameter decays to an incoherent jitter as expected for random scatter of $N$ points. (2) When $K > K_c$ this incoherent state becomes unstable and the order parameter $r$ grows exponentially reflecting the nucleation of small clusters of oscillators that are mutually synchronized. (3) The population of individual oscillators splits into two groups. The oscillators near the center of the distribution lock together in phase at the mean angular frequency $\Omega$ and co-rotate with average phase $\psi(t)$, whereas those frequencies lying further from the center continue to rotate independently at their natural frequencies and drift relative to the coherent cluster frequency $\Omega$. As a consequence this mixed state is only partially synchronized as illustrated on the right side of Figure 14.2. The synchronized fraction has a $\delta$-function behavior for the frequency distribution which grows in intensity with further increase in $K$. The unsynchronized component has nearly the original frequency distribution $g(\omega)$ except that it is depleted in the region of the locked frequency due to strength absorbed by the $\delta$-function component.

Kuramoto’s toy model nicely illustrates the essential features of the evolution of collective synchronization with coupling strength. It has been applied to the study neuronal synchronization in the brain[Cum07]. The model illustrates that the collective synchronization of coupled oscillators leads to a component that has a single frequency for correlated motion which can be much narrower than the inherent frequency distribution of the ensemble of coupled oscillators.

Example 14.1: Collective motion in nuclei

The nucleus is an unusual quantal system that involves the coupled motion of the many nucleons. It exhibits features characteristic of the many-body classical coupled oscillator with coupling between all the valence nucleons. Nuclear structure can be described by a shell model of individual nucleons bound in weakly interacting orbits in a central average mean field that is produced by the summed attraction of all the nucleons in the nucleus. However, nuclei also exhibit features characteristic of collective rotation and vibration of a quantal fluid. For example, beautiful rotational bands up to spin over $60\hbar$ are observed in heavy nuclei. These rotational bands are similar to those observed in the rotational structure of diatomic molecules. Actinide nuclei also can fission into two large fragments which is another manifestation of collective motion.

The essential general feature of weakly-coupled identical oscillators is illustrated by the solutions of the three linearly-coupled identical oscillators where the most symmetric state is displaced in frequency from the remaining states. For $n$ identical oscillators, one state is displaced significantly in energy from the remaining $n − 1$ degenerate states. This most symmetric state is pushed downwards in energy if the residual coupling force is attractive, and it is pushed upwards if the coupling force is repulsive. This symmetric state corresponds to the coherent oscillation of all the coupled oscillators, and carries all of the strength for the corresponding dominant multipole for the coupling force. In the nucleus this state corresponds to coherent shape oscillations of many nucleons.

The weak residual electric quadrupole and octupole nucleon-nucleon correlations in the nucleon-nucleon interactions generate collective quadrupole and octupole motion in nuclei. The collective synchronization of such coherent quadrupole and octupole excitation leads to collective bands of states, that correspond to synchronized in-phase motion of the protons and neutrons in the valence oscillator shell. These modes correspond to rotations and vibrations about the center of mass. The attractive residual nucleon-nucleon interaction couples the many individual particle excitations in a given shell producing one coherent state that is pushed downwards in energy far from the remaining $n − 1$ degenerate states. This coherent state involves correlated motion of the nucleons that corresponds to a macroscopic oscillation of a charged fluid. For nonclosed shell nuclei like $^{238}U$, the dominant quadrupole multipole in the residual nucleon-nucleon interaction leads to the ground state being a coherent state corresponding to $\approx 16$ protons plus $\approx 20$ neutrons oscillating in phase. The collective motion of the charged protons leads to electromagnetic $E2$ radiation with a transition decay amplitude being about 16 times larger than for a single proton. This corresponds to radiative decay probability being enhanced by a factor of $\approx 256$ relative to radiation by a single proton. This collective state corresponds to a macroscopic quadrupole deformation at low excitation energies that exhibits both collective rotational and vibrational degrees of freedom. This coherent state is analogous to the correlated flow of individual water molecules in a tidal wave. The weaker octupole term in the residual interaction leads to an octupole [pear-shaped] coupled oscillator coherent state lying slightly above the quadrupole coherent state. In contrast to the rotational motion of strongly-deformed quadrupole-deformed nuclei, the octupole deformation exhibits more vibrational-like properties than rotational motion of a charged tidal wave. Hamiltonian mechanics, based on the Routhian $R_{noncyclic}$, is used to make theoretical model calculations of the nuclear structure of $^{238}U$ in the rotating body-fixed frame for comparison with the experimental data.

## 14.E: Coupled linear oscillators (Exercises)

1. Two particles, each with mass $m$, move in one dimension in a region near a local minimum of the potential energy where the potential energy is approximately given by 
$$
U = \frac{1}{2} k (7x^2_1 + 4x^2_2 + 4x_1x_2)\nonumber
$$
 where $k$ is a constant.

1. Determine the frequencies of oscillation.
2. Determine the normal coordinates.

2. What is degeneracy? When does it arise?

3. The Lagrangian of three coupled oscillators is given by: 
$$
\sum^3_{n=1} \left[\frac{m\dot{x}^2_n}{2} - \frac{kx^2_n}{2} \right] + k^{\prime}(x_1x_2+x_2x_3).\nonumber
$$
 Find $x_2(t)$ for the following initial conditions (at $t = 0$): 
$$
(x_1, x_2, x_3)=(x_0, 0, 0), :: (\dot{x}_1, \dot{x}_2, \dot{x}_3) = (0, 0, v_0). \nonumber
$$

4. A mechanical analog of the benzene molecule comprises a discrete lattice chain of 6 point masses $M$ connected in a plane hexagonal ring by 6 identical springs each with spring constant $\kappa$ and length $d$.

1. List the wave numbers of the allowed undamped longitudinal standing waves.
2. Calculate the phase velocity and group velocity for longitudinal travelling waves on the ring.
3. Determine the time dependence of a longitudinal standing wave for a angular frequency $\omega = 2\omega_{cutoff}$, that is, twice the cut-off frequency.

5. Consider a one dimensional, two-mass, three-spring system governed by the matrix $A$, 
$$
A = \begin{pmatrix} 4 & -2 \\ -2 & 7 \end{pmatrix}\nonumber
$$
 such that $Ax = \omega^2x$,

1. Determine the eigenfrequencies and normal coordinates.
2. Choose a set of initial conditions such that the system oscillates at its highest eigenfrequency.
3. Determine the solutions $x_1(t)$ and $x_2(t)$.

6. Four identical masses $m$ are connected by four identical springs, spring constant $\kappa$, and constrained to move on a frictionless circle of radius $b$ as shown on the left in the figure.

1. How many normal modes of small oscillation are there?
2. What are the eigenfrequencies of the small oscillations?
3. Describe the motion of the four masses for each eigenfrequency.

:::{figure} ../images/lt-22555-12.e.1.png
:alt: 12.e.1.PNG

$1$
:::

7. Consider the two identical coupled oscillators given on the right in the figure assuming $\kappa_1 = \kappa_2 = \kappa$. Let both oscillators be linearly damped with a damping constant $\beta$. A force $F = F_0 \cos(\omega t)$ is applied to mass $m_1$. Write down the pair of coupled differential equations that describe the motion. Obtain a solution by expressing the differential equations in terms of the normal coordinates. Show that the normal coordinates $\eta_1$ and $\eta_2$ exhibit resonance peaks at the characteristic frequencies $\omega_1$ and $\omega_2$ respectively.

:::{figure} ../images/lt-22556-12.e.2.png
:alt: 12.e.2.PNG

$2$
:::

8. As shown on the left below the mass $M$ moves horizontally along a frictionless rail. A pendulum is hung from $M$ with a weightless rod of length $b$ with a mass $m$ at its end.

1. Prove that the eigenfrequencies are 
$$
\omega_1 = 0 \quad \omega_2 = \sqrt{\frac{g}{Mb} (M + m)} \nonumber
$$

2. Describe the normal modes.

:::{figure} ../images/lt-22557-12.e.3.png
:alt: 12.e.3.PNG

$3$
:::

## 14.S: Coupled linear oscillators (Summary)

This chapter has focussed on many—body coupled linear oscillator systems which are a ubiquitous feature in nature. A summary of the main conclusions are the following.

### Normal modes

It was shown that coupled linear oscillators exhibit normal modes and normal coordinates that correspond to independent modes of oscillation with characteristic eigenfrequencies $\omega_i$.

### General analytic theory for coupled linear oscillators

Lagrangian mechanics was used to derive the general analytic procedure for solution of the many-body coupled oscillator problem which reduces to the conventional eigenvalue problem. A summary of the procedure for solving coupled oscillator problems is as follows:.

1) Choose generalized coordinates $q_j$ and evaluate $T$ and $U$.

$$
T = \frac{1}{2} \sum^{n}_{j,k} T_{jk} \dot{q}_j\dot{q}_k
$$

and

$$
U^{\prime} = \frac{1}{2} \sum^n_{j,k} V_{jk} q_j q_k 
$$

where the components of the $\mathbf{T}$ and $\mathbf{V}$ tensors are

$$
T_{j k} \equiv\left(\sum_{\alpha}^{N} m_{\alpha} \sum_{i}^{3} \frac{\partial x_{\alpha, i}}{\partial q_{j}} \frac{\partial x_{\alpha, i}}{\partial q_{k}}\right)_{0} 
$$

and

$$
V_{j k} \equiv\left(\frac{\partial^{2} U}{\partial q_{j} \partial q_{k}}\right)_{0} 
$$

2) Determine the eigenvalues $\omega_r$ using the secular determinant.

$$
\begin{vmatrix} V_{11} − \omega^2 T_{11} & V_{12} − \omega^2 T_{12} & V_{13} − \omega^2 T_{13} & ... \\ V_{12} − \omega^2 T_{12} & V_{22} − \omega^2 T_{22} & V_{23} − \omega^2 T_{23} & ... \\ V_{13} − \omega^2 T_{13} & V_{23} − \omega^2 T_{23} & V_{33} − \omega^2 T_{33} & ... \\ ... & ... & ... & ... \end{vmatrix} = 0
$$

3) The eigenvectors are obtained by inserting the eigenvalues $\omega_r$ into

$$
\sum^n_j (V_{jk} − \omega^2_r T_{jk} ) a_j = 0 
$$

4) From the initial conditions determine the complex scale factors $\beta_r$ where

$$
\eta_r(t) \equiv \beta_r e^{i\omega_rt}
$$

5) Determine the normal coordinates where each $\eta_r$ is a normal mode. The normal coordinates can be expressed as

$$
\boldsymbol{\eta} = \mathbf{\{a\}^{-1}}\mathbf{q}
$$

### Few-body coupled oscillator systems

The general analytic theory was used to determine the solutions for parallel and series couplings of two and three linear oscillators. The phenomena observed include degenerate and non-degenerate eigenvalues and spurious center-of-mass oscillatory modes. There are two broad classifications for three or more coupled oscillators, that is, either complete coupling of all oscillators, or coupling of the nearest-neighbor oscillators. It is observed that the eigenvalue corresponding to the most coherent motion of the coupled oscillators corresponds to the most collective motion and its eigenvalue is displaced the most in energy from the remaining eigenvalues. For some systems this coherent collective mode corresponded to a center-of-mass motion with no internal excitation of the other modes, while the other eigenvalues corresponded to modes with internal excitation of the oscillators such that the center of mass is stationary. The above procedure has been applied to two classification of coupling, complete coupling of many oscillators, and nearest neighbor coupling. Both degenerate and spurious center-of-mass modes were observed. Strong collective shape degrees of freedom in nuclei are examples of complete coupling due to the weak residual interactions between nucleons in the nucleus. It was seen that, for many coupled oscillators, one coherent state separates from the other states and this coherent state carries the bulk of the collective strength.

### Discrete lattice chain

Transverse and longitudinal modes of motion on the discrete lattice chain were discussed because of the important role it plays in nature, such as in crystalline lattice structures. Both normal modes and travelling waves were discussed including the phenomena of dispersion and cut-off frequencies. Molecules and the crystalline lattice chains are examples where nearest neighbor coupling is manifest. It was shown that, for the $n$−oscillator discrete lattice chain, there are only $n$ independent longitudinal modes plus $n$ modes for the two transverse polarizations, and that the angular frequency $\omega_r \leq 2\omega_0$ that is, a cut-off frequency exists.

### Damped coupled linear oscillators

It was shown that linearly-damped coupled oscillator systems can be solved analytically using the concept of the Rayleigh dissipation function.

### Collective synchronization of coupled oscillators

The Kuramoto schematic phase model was used to illustrate how weak residual forces can cause collective synchronization of the motion of many coupled oscillators. This is applicable to many large coupled systems such as nuclei, molecules, and biological systems.
