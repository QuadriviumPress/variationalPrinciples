---
title: "4. Nonlinear Systems and Chaos"
short_title: "Chapter 4"
label: ch-04-nonlinear-systems-and-chaos
---


(ch-4)=

# 4. Nonlinear Systems and Chaos

## 4.1: Introduction to Nonlinear Systems and Chaos

In nature only a subset of systems have equations of motion that are linear. Contrary to the impression given by the analytic solutions presented in undergraduate physics courses, most dynamical systems in nature exhibit non-linear behavior that leads to complicated motion. The solutions of non-linear equations usually do not have analytic solutions, superposition does not apply, and they predict phenomena such as attractors, discontinuous period bifurcation, extreme sensitivity to initial conditions, rolling motion, and chaos. During the past four decades, exciting discoveries have been made in classical mechanics that are associated with the recognition that nonlinear systems can exhibit chaos. Chaotic phenomena have been observed in most fields of science and engineering such as, weather patterns, fluid flow, motion of planets in the solar system, epidemics, changing populations of animals, birds and insects, and the motion of electrons in atoms. The complicated dynamical behavior predicted by non-linear differential equations is not limited to classical mechanics, rather it is a manifestation of the mathematical properties of the solutions of the differential equations involved, and thus is generally applicable to solutions of first or second-order non-linear differential equations. It is important to understand that the systems discussed in this chapter follow a fully deterministic evolution predicted by the laws of classical mechanics, the evolution for which is based on the prior history. This behavior is completely different from a random walk where each step is based on a random process. The complicated motion of deterministic non-linear systems stems in part from sensitivity to the initial conditions. There are many examples of turbulent and laminar flow.

The French mathematician Poincaré is credited with being the first to recognize the existence of chaos during his investigation of the gravitational three-body problem in celestial mechanics. At the end of the nineteenth century Poincaré noticed that such systems exhibit high sensitivity to initial conditions characteristic of chaotic motion, and the existence of nonlinearity which is required to produce chaos. Poincaré’s work received little notice, in part it was overshadowed by the parallel development of the Theory of Relativity and quantum mechanics at the start of the $20^{th}$ century. In addition, solving nonlinear equations of motion is difficult, which discouraged work on nonlinear mechanics and chaotic motion. The field blossomed during the $1960^{\prime }s$ when computers became sufficiently powerful to solve the nonlinear equations required to calculate the long-time histories necessary to document the evolution of chaotic behavior.

Laplace, and many other scientists, believed in the deterministic view of nature which assumes that if the position and velocities of all particles are known, then one can unambiguously predict the future motion using Newtonian mechanics. Researchers in many fields of science now realize that this “clockwork universe" is invalid. That is, knowing the laws of nature can be insufficient to predict the evolution of nonlinear systems in that the time evolution can be extremely sensitive to the initial conditions even though they follow a completely deterministic development. There are two major classifications of nonlinear systems that lead to chaos in nature. The first classification encompasses nondissipative Hamiltonian systems such as Poincaré’s three-body celestial mechanics system. The other main classification involves driven, damped, non-linear oscillatory systems.

Nonlinearity and chaos is a broad and active field and thus this chapter will focus only on a few examples that illustrate the general features of non-linear systems. Weak non-linearity is used to illustrate bifurcation and asymptotic attractor solutions for which the system evolves independent of the initial conditions. The common sinusoidally-driven linearly-damped plane pendulum illustrates several features characteristic of the evolution of a non-linear system from order to chaos. The impact of non-linearity on wavepacket propagation velocities and the existence of soliton solutions is discussed. The example of the three-body problem is discussed in chapter $11$. The transition from laminar flow to turbulent flow is illustrated by fluid mechanics discussed in chapter $16.8$. Analytic solutions of nonlinear systems usually are not available and thus one must resort to computer simulations. As a consequence the present discussion focusses on the main features of the solutions for these systems and ignores how the equations of motion are solved.

## 4.2: Weak Nonlinearity

Most physical oscillators become non-linear with increase in amplitude of the oscillations. Consequences of non-linearity include breakdown of superposition, introduction of additional harmonics, and complicated chaotic motion that has great sensitivity to the initial conditions as illustrated in this chapter. Weak non-linearity is interesting since perturbation theory can be used to solve the non-linear equations of motion.

The potential energy function for a linear oscillator has a pure parabolic shape about the minimum location, that is, $U= \frac{1}{2}k(x-x_{0})^{2}$ where $x_{0}$ is the location of the minimum. Weak non-linear systems have small amplitude oscillations $\Delta x$ about the minimum allowing use of the Taylor expansion

$$
U(\Delta x)=U(x_{0})+\Delta x\frac{dU\left( x_{0}\right) }{dx}+\frac{\Delta x^{2}}{2!}\frac{d^{2}U\left( x_{0}\right) }{dx^{2}}+\frac{\Delta x^{3}}{3!} \frac{d^{3}U\left( x_{0}\right) }{dx^{3}}+\frac{\Delta x^{4}}{4!}\frac{ d^{4}U\left( x_{0}\right) }{dx^{4}}+ \dots \tag{4.1} \label{eq-4-1}
$$

By definition, at the minimum $\frac{dU\left( x_{0}\right) }{dx}=0,$ and thus Equation [4.1](#eq-4-1) can be written as

$$
\Delta U=U(\Delta x)-U(x_{0})=\frac{\Delta x^{2}}{2!}\frac{d^{2}U\left( x_{0}\right) }{dx^{2}}+\frac{\Delta x^{3}}{3!}\frac{d^{3}U\left( x_{0}\right) }{dx^{3}}+\frac{\Delta x^{4}}{4!}\frac{d^{4}U\left( x_{0}\right) }{dx^{4}}+\dots \tag{4.2} \label{eq-4-2}
$$

For small amplitude oscillations the system is linear when only the second-order $\frac{\Delta x^{2}}{2!}\frac{d^{2}U\left( x_{0}\right) }{dx^{2} }$ term in Equation [4.2](#eq-4-2) is significant. The linearity for small amplitude oscillations greatly simplifies description of the oscillatory motion in that superposition applies, and complicated chaotic motion is avoided. For slightly larger amplitude motion, where the higher-order terms in the expansion are still much smaller than the second-order term, then perturbation theory can be used as illustrated by the simple plane pendulum which is non linear since the restoring force equals

$$
mg\sin \theta \simeq mg(\theta -\frac{\theta ^{3}}{3!}+\frac{\theta ^{5}}{5!} -\frac{\theta ^{7}}{7!}+\dots ) \tag{4.3} \label{eq-4-3}
$$

This is linear only at very small angles where the higher-order terms in the expansion can be neglected. Consider the equation of motion at small amplitudes for the harmonically-driven, linearly-damped plane pendulum

$$
\ddot{\theta}+\Gamma \dot{\theta}+\omega _{0}^{2}\sin \theta =\ddot{\theta} +\Gamma \dot{\theta}+\omega _{0}^{2}(\theta -\frac{\theta ^{3}}{6} )=F_{0}\cos \left( \omega t\right) \tag{4.4} \label{eq-4-4}
$$

where only the first two terms in the expansion [4.3](#eq-4-3) have been included. It was shown in chapter $3$ that when $\sin \theta \approx \theta$ then the steady-state solution of Equation [4.4](#eq-4-4) is of the form

$$
\theta \left( t\right) =A\cos \left( \omega t-\delta \right) \tag{4.5} \label{eq-4-5}
$$

Insert this first-order solution into Equation [4.4](#eq-4-4), then the cubic term in the expansion gives a term $\cos^{3}\omega t=\frac{1}{4}(\cos 3\omega t+3\cos \omega t)$. Thus the perturbation expansion to third order involves a solution of the form

$$
\theta \left( t\right) =A\cos \left( \omega t-\delta \right) +B\cos 3(\omega t-\delta )\tag{4.6} \label{eq-4-6}
$$

This perturbation solution shows that the non-linear term has distorted the signal by addition of the third harmonic of the driving frequency with an amplitude that depends sensitively on $\theta$. This illustrates that the superposition principle is not obeyed for this non-linear system, but, if the non-linearity is weak, perturbation theory can be used to derive the solution of a non-linear equation of motion.

[Figure 4.2.1](#fig-4-2-1) illustrates that for a potential $U(x)=2x^{2}+x^{4},$ the $x^{4}$ non-linear term are greatest at the maximum amplitude $x,$ which makes the total energy contours in state-space more rectangular than the elliptical shape for the harmonic oscillator as shown in figure (3.4.2). The solution is of the form given in Equation [4.6](#eq-4-6).

:::{figure} ../images/lt-21127-4.2.1.png
:label: fig-4-2-1
:enumerator: 4.2.1
:alt: The left side shows the potential energy for a symmetric potential U(x)=2x^2 + x^4. The right side shows the contours of constant total energy on a state-space diagram.

The left side shows the potential energy for a symmetric potential $U(x)=2x^2 + x^4$. The right side shows the contours of constant total energy on a state-space diagram.
:::

::::{admonition} Example 4.2.1: Non-linear oscillator
:class: example

*Assume that a non-linear oscillator has a potential given by*

$$
U(x)=\frac{kx^{2}}{2}-\frac{m\lambda x^{3}}{3} \nonumber
$$

*where* $\lambda$*is small. Find the solution of the equation of motion to first order in* $\lambda$*, assuming* $x=0$ *at* $t=0$*.*

**Solution**

*The equation of motion for the nonlinear oscillator is*

$$
m\ddot{x}=-\frac{dU}{dx}=-kx+m\lambda x^{2} \nonumber
$$

*If the* $m\lambda x^{2}$*term is neglected, then the second-order equation of motion reduces to a normal linear oscillator with*

$$
x_{0}=A\sin \left( \omega _{0}t+\varphi \right) \nonumber
$$

*where*

$$
\omega _{0}=\sqrt{\frac{k}{m}} \nonumber
$$

*Assume that the first-order solution has the form*

$$
x_{1}=x_{0}+\lambda x_{1} \nonumber
$$

*Substituting this into the equation of motion, and neglecting terms of higher order than* $\lambda ,$*gives*

$$
\ddot{x}_{1}+\omega _{0}^{2}x_{1}=x_{0}^{2}=\frac{A^{2}}{2}[1-\cos \left( 2\omega _{0}t\right) ] \nonumber
$$

*To solve this try a particular integral*

$$
x_{1}=B+C\cos \left( 2\omega _{0}t\right) \nonumber
$$

*and substitute into the equation of motion gives*

$$
-3\omega _{0}^{2}C\cos \left( 2\omega _{0}t\right) +\omega _{0}^{2}B=\frac{ A^{2}}{2}-\frac{A^{2}}{2}\cos \left( 2\omega _{0}t\right) \nonumber
$$

*Comparison of the coefficients gives*

$$
\begin{aligned} B &=&\frac{A^{2}}{2\omega _{0}^{2}} \\ C &=&\frac{A^{2}}{6\omega _{0}^{2}}\end{aligned} \nonumber
$$

*The homogeneous equation is*

$$
\ddot{x}_{1}+\omega _{0}^{2}x_{1}=0 \nonumber
$$

*which has a solution of the form*

$$
x_{1}=D_{1}\sin \left( \omega _{0}t\right) +D_{2}\cos \left( \omega _{0}t\right) \nonumber
$$

*Thus combining the particular and homogeneous solutions gives*

$$
x_{1}=\left( A+\lambda D_{1}\right) \sin \left( \omega _{0}t\right) +\lambda \left[ \frac{A^{2}}{2\omega _{0}^{2}}+D_{2}\cos \left( \omega _{0}t\right) + \frac{A^{2}}{6\omega _{0}^{2}}\cos \left( 2\omega _{0}t\right) \right] \nonumber
$$

*The initial condition* $x=0$*at* $t=0$*then gives*

$$
D_{2}=-\frac{2A^{2}}{3\omega ^{2}} \nonumber
$$

*and*

$$
x_{1}=\left( A+\lambda D_{1}\right) \sin \left( \omega _{0}t\right) +\frac{ \lambda A^{2}}{\omega _{0}^{2}}\left[ \frac{1}{2}-\frac{2}{3}\cos \left( \omega _{0}t\right) +\frac{1}{6}\cos \left( 2\omega _{0}t\right) \right] \nonumber
$$

*The constant* $\left( A+\lambda D_{1}\right)$*is given by the initial amplitude and velocity.*

*This system is nonlinear in that the output amplitude is not proportional to the input amplitude. Secondly, a large amplitude second harmonic component is introduced in the output waveform; that is, for a non-linear system the gain and frequency decomposition of the output differs from the input. Note that the frequency composition is amplitude dependent. This particular example of a nonlinear system does not exhibit chaos. The Laboratory for Laser Energetics uses nonlinear crystals to double the frequency of laser light.*
::::

## 4.3: Bifurcation and Point Attractors

Interesting new phenomena, such as bifurcation, and attractors, occur when the non-linearity is large. In chapter $3$ it was shown that the state-space diagram $\left( \dot{x},x\right)$ for an undamped harmonic oscillator is an ellipse with dimensions defined by the total energy of the system. As shown in figure (3.5.1), for the damped harmonic oscillator, the state-space diagram spirals inwards to the origin due to dissipation of energy. Non-linearity distorts the shape of the ellipse or spiral on the state-space diagram, and thus the state-space, or corresponding phase-space, diagrams, provide useful representations of the motion of linear and non-linear periodic systems.

The complicated motion of non-linear systems makes it necessary to distinguish between transient and asymptotic behavior. The damped harmonic oscillator executes a transient spiral motion that asymptotically approaches the origin. The transient behavior depends on the initial conditions, whereas the asymptotic limit of the steady-state solution is a specific location, that is called a **point** **attractor.** The point attractor for damped motion in the anharmonic potential well

$$
U(x)=2x^{2}+x^{4}
$$

is at the minimum, which is the origin of the state-space diagram as shown in figure (4.2.1).

The more complicated one-dimensional potential well

$$
U(x)=8-4x^{2}+0.5x^{4}
$$

shown in [Figure 4.3.1](#fig-4-3-1), has two minima that are symmetric about $x=0$ with a saddle of height $8$.

The kinetic plus potential energies of a particle with mass $m=2,$ released in this potential, will be assumed to be given by

$$
E(x,\dot{x})=\dot{x}^{2}+U(x)
$$

The state-space plot in [Figure 4.3.1](#fig-4-3-1) shows contours of constant energy with the minima at $(x,\dot{x})=(\pm 2,0)$. At slightly higher total energy the contours are closed loops around either of the two minima at $x=\pm 2$. At total energies above the saddle energy of $8$ the contours are peanut-shaped and are symmetric about the origin. Assuming that the motion is weakly damped, then a particle released with total energy $E_{total}$ which is higher than $E_{saddle}$ will follow a peanut-shaped spiral trajectory centered at $(x,\dot{x})=(0,0)$ in the state-space diagram for $E_{total}>E_{saddle}$. For $E_{total}<E_{saddle}$ there are two separate solutions for the two minimum centered at $x=\pm 2$ and $\dot{x} =0$. This is an example of *bifurcation* where the one solution for $E_{total}>E_{saddle}$ bifurcates into either of the two solutions for $E_{total}<E_{saddle}$.

:::{figure} ../images/lt-16376-bifurcationplots.jpg
:label: fig-4-3-1
:enumerator: 4.3.1
:alt: The left side shows the potential energy for a bimodal symmetric potential U(x) = 8 - 4x^2 + 0.5x^4. The right-hand figure shows contours of the sum of kinetic and potential energies on a state-space diagram. For total energies above the saddle point the particle follows peanut-shaped trajectories in statespace centered around (x, \dot{x}) = (0, 0). For total energies below the saddle point the particle will have closed trajectories about either of the two symmetric minima located at (x, \dot{x}) = (\pm 2, 0). Thus the system solution bifurcates when the total energy is below the saddle point.

The left side shows the potential energy for a bimodal symmetric potential $U(x) = 8 - 4x^2 + 0.5x^4$. The right-hand figure shows contours of the sum of kinetic and potential energies on a state-space diagram. For total energies above the saddle point the particle follows peanut-shaped trajectories in statespace centered around $(x,\dot{x}) = (0, 0)$. For total energies below the saddle point the particle will have closed trajectories about either of the two symmetric minima located at $(x, \dot{x}) = (\pm 2, 0)$. Thus the system solution bifurcates when the total energy is below the saddle point.
:::

For an initial total energy $E_{total}>E_{saddle},$ damping will result in spiral trajectories of the particle that will be trapped in one of the two minima. For $E_{total}>E_{saddle}$ the particle trajectories are centered giving the impression that they will terminate at $(x,\dot{x})=(0,0)$ when the kinetic energy is dissipated. However, for $E_{total}<E_{saddle}$ the particle will be trapped in one of the two minimum and the trajectory will terminate at the bottom of that potential energy minimum occurring at $(x, \dot{x})=(\pm 2,0)$. These two possible terminal points of the trajectory are called *point attractors.* This example appears to have a single attractor for $E_{total}>E_{saddle}$ which bifurcates leading to two attractors at $(x,\dot{x})=(\pm 2,0)$ for $E_{total}<E_{saddle}$. The determination as to which minimum traps a given particle depends on exactly where the particle starts in state space and the damping etc. That is, for this case, where there is symmetry about the $x$-axis, the particle has an initial total energy $E_{total}>E_{saddle},$ then the initial conditions with $\pi$ radians of state space will lead to trajectories that are trapped in the left minimum, and the other $\pi$ radians of state space will be trapped in the right minimum. Trajectories starting near the split between these two halves of the starting state space will be sensitive to the exact starting phase. This is an example of sensitivity to initial conditions.

## 4.4: Limit Cycles

### Poincaré-Bendixson theorem

Coupled first-order differential equations in two dimensions of the form

$$
\dot{x} = f(x,y)\hspace{0.55in}\dot{y} = g(x,y) \tag{4.10} \label{eq-4-10}
$$

occur frequently in physics. The state-space paths do not cross for such two-dimensional autonomous systems, where an autonomous system is not explicitly dependent on time.

The Poincaré-Bendixson theorem states that, state-space, and phase-space, can have three possible paths:

1. closed paths, like the elliptical paths for the undamped harmonic oscillator,

2. terminate at an equilibrium point as $t\rightarrow \infty$, like the point attractor for a damped harmonic oscillator,

3. tend to a limit cycle as $t\rightarrow \infty$.

The limit cycle is unusual in that the periodic motion tends asymptotically to the limit-cycle attractor independent of whether the initial values are inside or outside the limit cycle. The balance of dissipative forces and driving forces often leads to limit-cycle attractors, especially in biological applications. Identification of limit-cycle attractors, as well as the trajectories of the motion towards these limit-cycle attractors, is more complicated than for point attractors.

:::{figure} ../images/lt-21128-4.4.1.png
:label: fig-4-4-1
:enumerator: 4.4.1
:alt: The Poincaré-Bendixson theorem allows the following three scenarios for two-dimensional autonomous systems. (1) Closed paths as illustrated by the undamped harmonic oscillator. (2) Terminate at an equilibrium point as t\rightarrow \infty, as illustrated by the damped harmonic oscillator, and (3) …

The Poincaré-Bendixson theorem allows the following three scenarios for two-dimensional autonomous systems. (1) Closed paths as illustrated by the undamped harmonic oscillator. (2) Terminate at an equilibrium point as $t\rightarrow \infty$, as illustrated by the damped harmonic oscillator, and (3) Tend to a limit cycle as $t\rightarrow \infty$ as illustrated by the van der Pol oscillator.
:::

### van der Pol damped harmonic oscillator

The **van der Pol damped harmonic oscillator** illustrates a non-linear equation that leads to a well-studied, limit-cycle attractor that has important applications in diverse fields. The van der Pol oscillator has an equation of motion given by

$$
\frac{d^{2}x}{dt^{2}}+\mu \left( x^{2}-1\right) \frac{dx}{dt}+\omega _{0}^{2}x = 0 \tag{4.11} \label{eq-4-11}
$$

The non-linear $\mu \left( x^{2}-1\right) \frac{dx}{dt}$ damping term is unusual in that the sign changes when $x = 1$ leading to positive damping for $x>1$ and negative damping for $x<1.$ To simplify Equation [4.11](#eq-4-11), assume that the term $\omega _{0}^{2}x = x,$ that is, $\omega _{0}^{2} = 1$.

This equation was studied extensively during the 1920’s and 1930’s by the Dutch engineer, Balthazar van der Pol, for describing electronic circuits that incorporate feedback. The form of the solution can be simplified by defining a variable $y\equiv \frac{dx}{dt}.$ Then the second-order Equation [4.11](#eq-4-11) can be expressed as two coupled first-order equations.

$$
y \equiv \frac{dx}{dt} \tag{4.12} \label{eq-4-12}
$$

$$
\frac{dy}{dt} = -x-\mu \left( x^{2}-1\right) y \tag{4.13} \label{eq-4-13}
$$

It is advantageous to transform the $\left( \dot{x},x\right)$ state space to polar coordinates by setting

$$
\begin{align} x & = &r\cos \theta \tag{4.14} \label{eq-4-14}\\ y & = &r\sin \theta \nonumber \end{align}
$$

and using the fact that $\ r^{2} = x^{2}+y^{2}$. Therefore

$$
r\frac{dr}{dt} = x\frac{dx}{dt}+y\frac{dy}{dt}\tag{4.15} \label{eq-4-15}
$$

Similarly for the angle coordinate

$$
\frac{dx}{dt} = \frac{dr}{dt}\cos \theta -r\frac{d\theta }{dt}\sin \theta \tag{4.16} \label{eq-4-16}
$$

$$
\frac{dy}{dt} = \frac{dr}{dt}\sin \theta +r\frac{d\theta }{dt}\cos \theta \tag{4.17} \label{eq-4-17}
$$

:::{figure} ../images/lt-21129-4.4.2.png
:label: fig-4-4-2
:enumerator: 4.4.2
:alt: Solutions of the van der Pol system for \mu = 0.2 top row and \mu = 5 bottom row, assuming that \omega^2_0 = 1. The left column shows the time dependence x(t). The right column shows the corresponding (x,\dot{x}) state space plots. **Upper: Weak nonlinearity,** \mu = \mathbf{0.2}; At large times …

Solutions of the van der Pol system for $\mu = 0.2$ top row and $\mu = 5$ bottom row, assuming that $\omega^2_0 = 1$. The left column shows the time dependence $x(t)$. The right column shows the corresponding $(x,\dot{x})$ state space plots. **Upper: Weak nonlinearity,** $\mu = \mathbf{0.2}$; At large times the solution tends to one limit cycle for initial values inside or outside the limit cycle attractor. The amplitude $x(t)$ for two initial conditions approaches an approximately harmonic oscillation. **Lower: Strong nonlinearity,** $\mathbf{\mu} = \mathbf{5}$; Solutions approach a common limit cycle attractor for initial values inside or outside the limit cycle attractor while the amplitude $x(t)$ approaches a common approximate square-wave oscillation.
:::

Multiply Equation [4.16](#eq-4-16) by $y$ and [4.17](#eq-4-17) by $x$ and subtract gives

$$
r^{2}\frac{d\theta }{dt} = x\frac{dy}{dt}-y\frac{dx}{dt}\tag{4.18} \label{eq-4-18}
$$

Equations [4.15](#eq-4-15) and [4.18](#eq-4-18) allow the van der Pol equations of motion to be written in polar coordinates

$$
\frac{dr}{dt} = -\mu \left( r^{2}\cos ^{2}\theta -1\right) r\sin ^{2}\theta \tag{4.19} \label{eq-4-19}
$$

$$
\frac{d\theta }{dt} = -1-\mu \left( r^{2}\cos ^{2}\theta -1\right) \sin \theta \cos \theta \tag{4.20} \label{eq-4-20}
$$
 The non-linear terms on the right-hand side of equations [4.19](#eq-4-19)-[4.20](#eq-4-20) have a complicated form.

#### Weak non-linearity: $\mu <<1$

In the limit that $\mu \rightarrow 0$, equations [4.19](#eq-4-19), [4.20](#eq-4-20) correspond to a circular state-space trajectory similar to the harmonic oscillator. That is, the solution is of the form

$$
x\left( t\right) = \rho \sin \left( t-t_{0}\right)\tag{4.21} \label{eq-4-21}
$$

where $\rho$ and $t_{0}$ are arbitrary parameters. For weak non-linearity, $\mu <<1$ the angular Equation [4.20](#eq-4-20) has a rotational frequency that is unity since the $\sin \theta \cos \theta$ term changes sign twice per period, in addition to the small value of $\mu$. For $\mu <<1$ and $r<1,$ the radial Equation [4.19](#eq-4-19) has a sign of the $\left( r^{2}\cos ^{2}\theta -1\right)$ term that is positive and thus the radius increases monotonically to unity. For $r>1,$ the bracket is predominantly negative resulting in a spiral decrease in the radius. Thus, for very weak non-linearity, this radial behavior results in the amplitude spiralling to a well defined limit-cycle attractor value of $\rho = 2$ as illustrated by the state-space plots in [Figure 4.4.2](#fig-4-4-2) for cases where the initial condition is inside or external to the circular attractor. The final amplitude for different initial conditions also approach the same asymptotic behavior.

#### Dominant non-linearity: $\mu >>1$

For the case where the non-linearity is dominant, that is $\mu >>1$, then as shown in [Figure 4.4.2](#fig-4-4-2), the system approaches a well defined attractor, but in this case it has a significantly skewed shape in state-space, while the amplitude approximates a square wave. The solution remains close to $x = +2$ until $y = \dot{x}\approx +7$ and then it relaxes quickly to $x = -2$ with $y = \dot{x} \approx 0.$ This is followed by the mirror image. This behavior is called a relaxed vibration in that a tension builds up slowly then dissipates by a sudden relaxation process. The seesaw is an extreme example of a relaxation oscillator where the seesaw angle switches spontaneously from one solution to the other when the difference in their moment arms changes sign.

The study of feedback in electronic circuits was the stimulus for study of this equation by van der Pol. However, Lord Rayleigh first identified such *relaxation oscillator* behavior in $1880$ during studies of vibrations of a stringed instrument excited by a bow, or the squeaking of a brake drum. In his discussion of non-linear effects in acoustics, he derived the equation

$$
\ddot{x}-(a-b\dot{x}^{2})\dot{x}+\omega _{0}^{2}x\tag{4.22} \label{eq-4-22}
$$

Differentiation of Rayleigh’s Equation [4.22](#eq-4-22) gives

$$
\overset{\ldots}{x}-(a-3b\dot{x}^{2})\ddot{x}+\omega _{0}^{2}\dot{x} = 0\tag{4.23} \label{eq-4-23}
$$

Using the substitution of

$$
y = y_{0}\sqrt{\frac{3b}{a}}\dot{x}\tag{4.24} \label{eq-4-24}
$$

leads to the relations

$$
\dot{x} = \sqrt{\frac{a}{3b}}\frac{y}{y_{0}}\hspace{1in}\ddot{x} = \sqrt{\frac{a }{3b}}\frac{\dot{y}}{y_{0}}\hspace{1in}\overset{\ldots}{x} = \sqrt{\frac{a}{3b}}\frac{ \ddot{y}}{y_{0}} \tag{4.25} \label{eq-4-25}
$$

Substituting these relations into Equation [4.23](#eq-4-23) gives

$$
\sqrt{\frac{a}{3b}}\frac{\ddot{y}}{y_{0}}-\sqrt{\frac{a}{3b}}\left[ a-\frac{ 3ba}{b}\frac{\dot{y}^{2}}{y_{0}^{2}}\right] \frac{\dot{y}}{y_{0}}+\omega _{0}^{2}\sqrt{\frac{a}{3b}}\frac{y}{y_{0}} = 0\tag{4.26} \label{eq-4-26}
$$
 Multiplying by $y_{0}\sqrt{\frac{3b}{a}}$ and rearranging leads to the van der Pol equation 
$$
\ddot{y}-\frac{a}{y_{0}^{2}}(y_{0}^{2}-y^{2})\dot{y}-\omega _{0}^{2}y = 0 \tag{4.27} \label{eq-4-27}
$$

The rhythm of a heartbeat driven by a pacemaker is an important application where the self-stabilization of the attractor is a desirable characteristic to stabilize an irregular heartbeat; the medical term is [arrhythmia](https://med.libretexts.org/Bookshelves/Anatomy_and_Physiology/Book%3A_Anatomy_and_Physiology_(Boundless)/29%3A_APPENDIX_A%3A_Diseases_Injuries_and_Disorders_of_the_Organ_Systems/29.9%3A_Diseases_and_Disorders_of_the_Heart/29.9D%3A_Arrhythmia). The mechanism that leads to synchronization of the many pacemaker cells in the heart and human body due to the influence of an implanted pacemaker is discussed in chapter $14.12$. Another biological application of limit cycles is the time variation of animal populations.

In summary the non-linear damping of the van der Pol oscillator leads to a self-stabilized, single limit-cycle attractor that is insensitive to the initial conditions. The van der Pol oscillator has many important applications such as bowed musical instruments, electrical circuits, and human anatomy as mentioned above. The van der Pol oscillator illustrates the complicated manifestations of the motion that can be exhibited by non-linear systems.

## 4.5: Harmonically-driven, linearly-damped, plane pendulum

The harmonically-driven, linearly-damped, plane pendulum illustrates many of the phenomena exhibited by non-linear systems as they evolve from ordered to chaotic motion. It illustrates the remarkable fact that determinism does not imply either regular behavior or predictability. The well-known, harmonically-driven linearly-damped pendulum provides an ideal basis for an introduction to non-linear dynamics[^4-5-1].

Consider a harmonically-driven linearly-damped plane pendulum of moment of inertia $I$ and mass $m$ in a gravitational field that is driven by a torque due to a force $F(t)=F_{D}\cos \omega t$ acting at a moment arm $L$. The damping term is $b$ and the angular displacement of the pendulum, relative to the vertical, is $\theta$. The equation of motion of the harmonically-driven linearly-damped simple pendulum can be written as

$$
I \ddot{\theta}+b\dot{\theta}+mgL\sin \theta =LF_{D}\cos \omega t \tag{4.28} \label{eq-4-28}
$$

Note that the sinusoidal restoring force for the plane pendulum is non-linear for large angles $\theta$. The natural period of the free pendulum is

$$
\omega _{0}=\sqrt{\frac{mgL}{I}}
$$

A dimensionless parameter $\gamma$, which is called the **drive strength,** is defined by 
$$
\gamma \equiv \frac{F_{D}}{mg}
$$

The equation of motion [4.28](#eq-4-28) can be generalized by introducing dimensionless units for both time $\tilde{t}$ and relative drive frequency $\tilde{\omega}$ defined by

$$
\tilde{t}\equiv \omega _{0}t\hspace{1in}\tilde{\omega}\equiv \frac{\omega }{ \omega _{0}}
$$

In addition, define the inverse damping factor $Q$ as

$$
Q\equiv \frac{\omega _{0}I}{b}
$$

These definitions allow Equation [4.28](#eq-4-28) to be written in the dimensionless form 
$$
\frac{d^{2}\theta }{d\tilde{t}^{2}}+\frac{1}{Q}\frac{d\theta }{d\tilde{t}} +\sin \theta =\gamma \cos \tilde{\omega}\tilde{t} \tag{4.33} \label{eq-4-33}
$$

The behavior of the angle $\theta$ for the driven damped plane pendulum depends on the drive strength $\gamma$ and the damping factor $Q$. Consider the case where Equation [4.33](#eq-4-33) is evaluated assuming that the damping coefficient $Q=2$, and that the relative angular frequency $\tilde{\omega}= \frac{2}{3},$ which is close to resonance where chaotic phenomena are manifest. The Runge-Kutta method is used to solve this non-linear equation of motion.

### Close to Linearity

For drive strength $\gamma =0.2$ the amplitude is sufficiently small that $\sin \theta \simeq \theta ,$ superposition applies, and the solution is identical to that for the driven linearly-damped linear oscillator. As shown in [Figure 4.5.1](#fig-4-5-1), once the transient solution dies away, the steady-state solution asymptotically approaches one attractor that has an amplitude of $\pm 0.3$ radians and a phase shift $\delta$ with respect to the driving force. The abscissa is given in units of the dimensionless time $\tilde{t} =\omega _{0}t$. The transient solution depends on the initial conditions and dies away after about $5$ periods, whereas the steady-state solution is independent of the initial conditions and has a state-space diagram that has an elliptical shape, characteristic of the harmonic oscillator. For all initial conditions, the time dependence and state space diagram for steady-state motion approaches a unique solution, called an "**attractor**", that is, the pendulum oscillates sinusoidally with a given amplitude at the frequency of the driving force and with a constant phase shift $\delta$, i.e.

$$
\theta (t)=A\cos (\omega t-\delta ).
$$

This solution is identical to that for the harmonically-driven, linearly-damped, linear oscillator discussed in chapter $3.6.$

:::{figure} ../images/lt-21133-4.5.1.png
:label: fig-4-5-1
:enumerator: 4.5.1
:alt: Motion of the driven damped pendulum for drive strengths of \gamma = 0.2, \gamma = 0.9, \gamma = 1.05, and \gamma = 1.078. The left side shows the time dependence of the deflection angle \theta with the time axis expressed in dimensionless units \tilde t. The right side shows the corresponding st…

Motion of the driven damped pendulum for drive strengths of $\gamma = 0.2$, $\gamma = 0.9$, $\gamma = 1.05$, and $\gamma = 1.078$. The left side shows the time dependence of the deflection angle $\theta$ with the time axis expressed in dimensionless units $\tilde t$. The right side shows the corresponding state-space plots. These plots assume $\tilde \omega = \frac{\omega}{\omega_0} = \frac{2}{3}$, $Q = 2$, and the motion starts with $\theta = \omega = 0$.
:::

:::{figure} ../images/lt-21130-4.5.2.png
:label: fig-4-5-2
:enumerator: 4.5.2
:alt: The driven damped pendulum assuming that \tilde \omega = \frac{2}{3}, Q = 2, with initial conditions \theta (0) = −\frac{\pi}{2}, \omega (0) = 0. The system exhibits period-two motion for drive strengths of \gamma = 1.078 as shown by the state space diagram for cycles 10 − 20. For \gamma = 1.081 …

The driven damped pendulum assuming that $\tilde \omega = \frac{2}{3}$, $Q = 2$, with initial conditions $\theta (0) = −\frac{\pi}{2}$, $\omega (0) = 0$. The system exhibits period-two motion for drive strengths of $\gamma = 1.078$ as shown by the state space diagram for cycles $10 − 20$. For $\gamma = 1.081$ the system exhibits period-four motion shown for cycles $10 − 30$.
:::

### Weak nonlinearity

[Figure 4.5.1](#fig-4-5-1) shows that for drive strength $\gamma =0.9$, after the transient solution dies away, the steady-state solution settles down to one attractor that oscillates at the drive frequency with an amplitude of slightly more than $\frac{\pi }{2}$ radians for which the small angle approximation fails. The distortion due to the non-linearity is exhibited by the non-elliptical shape of the state-space diagram.

The observed behavior can be calculated using the successive approximation method discussed in chapter $4.2$. That is, close to small angles the sine function can be approximated by replacing

$$
\sin \theta \approx \theta -\frac{1}{6}\theta ^{3}
$$

in Equation [4.33](#eq-4-33) to give

$$
\ddot{\theta}+\frac{1}{Q}\dot{\theta}+\omega _{0}^{2}\left( \theta -\frac{1}{ 6}\theta ^{3}\right) =\gamma \cos \tilde{\omega}\tilde{t} \tag{4.35} \label{eq-4-35}
$$

As a first approximation assume that

$$
\theta (\tilde{t})\approx A\cos (\tilde{\omega}\tilde{t}-\delta )
$$

then the small $\theta^{3}$ term in Equation [4.35](#eq-4-35) contributes a term proportional to $\cos ^{3}(\tilde{\omega}\tilde{t}-\delta )$. But

$$
\cos ^{3}(\tilde{\omega}\tilde{t}-\delta )=\frac{1}{4}\left( \cos 3(\tilde{ \omega}\tilde{t}-\delta )+3\cos (\tilde{\omega}\tilde{t}-\delta )\right)
$$

That is, the nonlinearity introduces a small term proportional to $\cos 3(\omega t-\delta )$. Since the right-hand side of Equation [4.35](#eq-4-35) is a function of only $\cos \omega t,$ then the terms in $\theta ,\dot{\theta},$ and $\ddot{\theta}$ on the left hand side must contain the third harmonic $\cos 3(\omega t-\delta )$ term. Thus a better approximation to the solution is of the form

$$
\theta (\tilde{t})=A\left[ \cos (\tilde{\omega}\tilde{t}-\delta )+\varepsilon \cos 3(\tilde{\omega}\tilde{t}-\delta )\right]
$$

where the admixture coefficient $\varepsilon <1$. This successive approximation method can be repeated to add additional terms proportional to $\cos n(\omega t-\delta )$ where $n$ is an integer with $n\geq 3$. Thus the nonlinearity introduces progressively weaker $n$-fold harmonics to the solution. This successive approximation approach is viable only when the admixture coefficient $\varepsilon <1.$ Note that these harmonics are integer multiples of $\omega$, thus the steady-state response is identical for each full period even though the state space contours deviate from an elliptical shape.

### Onset of complication

[Figure 4.5.1](#fig-4-5-1) shows that for $\gamma =1.05$ the drive strength is sufficiently strong to cause the transient solution for the pendulum to rotate through two complete cycles before settling down to a single steady-state attractor solution at the drive frequency. However, this attractor solution is shifted two complete rotations relative to the initial condition. The state space diagram clearly shows the rolling motion of the transient solution for the first two periods prior to the system settling down to a single steady-state attractor. The successive approximation approach completely fails at this coupling strength since $\theta$ oscillates through large values that are multiples of $\pi .$

[Figure 4.5.1](#fig-4-5-1) shows that for drive strength $\gamma =1.078$ the motion evolves to a much more complicated periodic motion with a period that is three times the period of the driving force. Moreover the amplitude exceeds $2\pi$ corresponding to the pendulum oscillating over top dead center with the centroid of the motion offset by $3\pi$ from the initial condition. Both the state-space diagram, and the time dependence of the motion, illustrate the complexity of this motion which depends sensitively on the magnitude of the drive strength $\gamma ,$ in addition to the initial conditions, $(\theta (0),\omega (0))$ and damping factor $Q$ as is shown in [Figure 4.5.2](#fig-4-5-2)

### Period doubling and bifurcation

For drive strength $\gamma =1.078,$ with the initial condition $\left( \theta (0),\omega \left( 0\right) \right) =\left( 0,0\right) ,$ the system exhibits a regular motion with a period that is three times the drive period. In contrast, if the initial condition is $[\theta (0)=-\frac{\pi }{2} ,\omega \left( 0\right) =0]$ then, as shown in [Figure 4.5.2](#fig-4-5-2), the steady-state solution has the drive frequency with no offset in $\theta$, that is, it exhibits period-one oscillation. This appearance of two separate and very different attractors for $\gamma =1.078,$ using different initial conditions, is called **bifurcation**.

An additional feature of the system response for $\gamma =1.078$ is that changing the initial conditions to $[\theta (0)=-\frac{\pi }{2},\omega \left( 0\right) =0]$ shows that the amplitude of the even and odd periods of oscillation differ slightly in shape and amplitude, that is, the system really has period-two oscillation. This period-two motion, i.e. **period doubling**, is clearly illustrated by the state space diagram in that, although the motion still is dominated by period-one oscillations, the even and odd cycles are slightly displaced. Thus, for different initial conditions, the system for $\gamma =1.078$ bifurcates into either of two attractors that have very different waveforms, one of which exhibits period doubling.

The period doubling exhibited for $\gamma =1.078,$ is followed by a second period doubling when $\gamma =1.081$ as shown in [Figure 4.5.2](#fig-4-5-2). With increase in drive strength this period doubling keeps increasing in binary multiples to period $8$, $16$, $32$, $64$ etc. Numerically it is found that the threshold for period doubling is $\gamma _{1}=1.0663,$ from two to four occurs at $\gamma _{2}=1.0793$ etc. Feigenbaum showed that this cascade increases with increase in drive strength according to the relation that obeys

$$
(\gamma _{n+1}-\gamma _{n})\simeq \frac{1}{\delta }(\gamma _{n}-\gamma _{n-1})
$$

where $\delta =4.6692016$, $\delta$ is called a Feigenbaum number. As $n\rightarrow \infty$ this cascading sequence goes to a limit $\gamma _{c}$ where 
$$
\gamma _{c}=1.0829
$$

### Rolling motion

It was shown that for $\gamma >1.05$ the transient solution causes the pendulum to have angle excursions exceeding $2\pi$, that is, the system rolls over top dead center. For drive strengths in the range $1.3<\gamma <1.4,$ the steady-state solution for the system undergoes continuous rolling motion as illustrated in Figure 4.5.3. The time dependence for the angle exhibits a periodic oscillatory motion superimposed upon a monotonic rolling motion, whereas the time dependence of the angular frequency $\omega =\frac{ d\theta }{dt}$ is periodic. The state space plots for rolling motion corresponds to a chain of loops with a spacing of $2\pi$ between each loop. The state space diagram for rolling motion is more compactly presented if the origin is shifted by $2\pi$ per revolution to keep the plot within bounds as illustrated in Figure 4.5.3c.

:::{figure} ../images/lt-21131-4.5.3.png
:label: fig-4-5-3
:enumerator: 4.5.3
:alt: Rolling motion for the driven damped plane pendulum for \gamma = 1.4. (a) The time dependence of angle \theta (t) increases by 2\pi per drive period whereas (b) the angular velocity \omega (t) exhibits periodicity. (c) The state space plot for rolling motion is shown with the origin shifted by 2\…

Rolling motion for the driven damped plane pendulum for $\gamma = 1.4$. (a) The time dependence of angle $\theta (t)$ increases by $2\pi$ per drive period whereas (b) the angular velocity $\omega (t)$ exhibits periodicity. (c) The state space plot for rolling motion is shown with the origin shifted by $2\pi$ per revolution to keep the plot within the bounds $−\pi < \theta < +\pi$
:::

### Onset of chaos

When the drive strength is increased to $\gamma =1.105,$ then the system does not approach a unique attractor as illustrated by Figure 4.5.4 left which shows state space orbits for cycles $25-200$. Note that these orbits do not repeat implying the onset of chaos. For drive strengths greater than $\gamma _{c}=1.0829$ the driven damped plane pendulum starts to exhibit chaotic behavior. The onset of chaotic motion is illustrated by making a $3$-dimensional plot which combines the time coordinate with the state-space coordinates as illustrated in Figure 4.5.4 right. This plot shows $16$ trajectories starting at different initial values in the range $-0.15<\theta <0.15$ for $\gamma =1.168$. Some solutions are erratic in that, while trying to oscillate at the drive frequency, they never settle down to a steady periodic motion which is characteristic of chaotic motion. Figure 4.5.4 right illustrates the considerable sensitivity of the motion to the initial conditions. That is, this deterministic system can exhibit either order, or chaos, dependent on minuscule differences in initial conditions.

:::{figure} ../images/lt-16378-statespacechaos3.jpg
:label: fig-4-5-4
:enumerator: 4.5.4
:alt: Left: Space-space orbits for the driven damped pendulum with \gamma = 1.105. Note that the orbits do not repeat for cycles 25 to 200. Right: Time-state-space diagram for \gamma = 1.168. The plot shows 16 trajectories starting with different initial values in the range −0.15 < \theta < 0.15.

Left: Space-space orbits for the driven damped pendulum with $\gamma = 1.105$. Note that the orbits do not repeat for cycles 25 to 200. Right: Time-state-space diagram for $\gamma = 1.168$. The plot shows 16 trajectories starting with different initial values in the range $−0.15 < \theta < 0.15$.
:::

:::{figure} ../images/lt-16380-sketch001.jpg
:label: fig-4-5-5
:enumerator: 4.5.5
:alt: State-space plots for the harmonically-driven, linearly-damped, pendulum for driving amplitudes of F_D = 0.5 and F_D = 1.2. These calculations were performed using the Runge-Kutta method by E. Shah, (Private communication)

State-space plots for the harmonically-driven, linearly-damped, pendulum for driving amplitudes of $F_D = 0.5$ and $F_D = 1.2$. These calculations were performed using the Runge-Kutta method by E. Shah, (Private communication)
:::

[^4-5-1]: A similar approach is used by the book *"Chaotic Dynamics"* by Baker and Gollub[Bak96].

## 4.6: Differentiation Between Ordered and Chaotic Motion

Chapter $4.5$ showed that motion in non-linear systems can exhibit both order and chaos. The transition between ordered motion and chaotic motion depends sensitively on both the initial conditions and the model parameters. It is surprisingly difficult to unambiguously distinguish between complicated ordered motion and chaotic motion. Moreover, the motion can fluctuate between order and chaos in an erratic manner depending on the initial conditions. The extremely sensitivity to initial conditions of the motion for non-linear systems, makes it essential to have quantitative measures that can characterize the degree of order, and interpret the complicated dynamical motion of systems. As an illustration, consider the harmonically-driven, linearly-damped, pendulum with $Q = 2,$ and driving force $F(t) = F_{D}\sin \tilde{\omega}\tilde{t}$ where $\tilde{\omega} = \frac{2}{3}$. Figure (4.5.5) shows the state-space plots for two driving amplitudes, $F_{D} = 0.5$ which leads to ordered motion, and $F_{D} = 1.2$ which leads to possible chaotic motion. It can be seen that for $F_{D} = 0.5$ the state-space diagram converges to a single attractor once the transient solution has died away. This is in contrast to the case for $F_{D} = 1.2,$ where the state-space diagram does not converge to a single attractor, but exhibits possible chaotic motion. Three quantitative measures can be used to differentiate ordered motion from chaotic motion for this system; namely, the Lyapunov exponent, the bifurcation diagram, and the Poincaré section, as illustrated below.

### Lyapunov Exponent

The **Lyapunov exponent** provides a quantitative and useful measure of the instability of trajectories, and how quickly nearby initial conditions diverge. It compares two identical systems that start with an infinitesimally small difference in the initial conditions in order to ascertain whether they converge to the same attractor at long times, corresponding to a stable system, or whether they diverge to very different attractors, characteristic of chaotic motion. If the initial separation between the trajectories in phase space at $t = 0$ is $\left\vert \delta Z_{0}\right\vert$, then to first order the time dependence of the difference can be assumed to depend exponentially on time. That is,

$$
\left\vert \delta Z(t)\right\vert \sim e^{\lambda t}\left\vert Z_{0}\right\vert
$$

where $\lambda$ is the Lyapunov exponent. That is, the Lyapunov exponent is defined to be 
$$
\lambda = \lim_{t\rightarrow \infty }\lim_{\delta Z_{0}\rightarrow 0}\frac{1}{ t}\ln \frac{\left\vert \delta Z(t)\right\vert }{\left\vert Z_{0}\right\vert }
$$

Systems for which the Lyapunov exponent $\lambda <0$ (negative), converge exponentially to the same attractor solution at long times since $\left\vert \delta Z(t)\right\vert \rightarrow 0$ for $t\rightarrow \infty$. By contrast, systems for which $\lambda >0$ (positive) diverge to completely different long-time solutions, that is, $\left\vert \delta Z(t)\right\vert \rightarrow \infty$ for $t\rightarrow \infty$. Even for infinitesimally small differences in the initial conditions, systems having a positive Lyapunov exponent diverge to different attractors, whereas when the Lyapunov exponent $\lambda <0$ they correspond to stable solutions.

:::{figure} ../images/lt-16381-lyapunovcoeff.jpg
:label: fig-4-6-1
:enumerator: 4.6.1
:alt: Lyapunov plots of \Delta \theta versus time for two initial starting points differing by \Delta \theta_0 = 0.001 rads. The parameters are Q = 2, and F(t) = F_D \sin( \frac{2}{3}t), and \Delta t = 0.04 s. The Lyapunov exponent for F_D = 0.5 which is drawn as a dashed line, is convergent with \lamb…

Lyapunov plots of $\Delta \theta$ versus time for two initial starting points differing by $\Delta \theta_0 = 0.001$ $rads$. The parameters are $Q = 2$, and $F(t) = F_D \sin( \frac{2}{3}t)$, and $\Delta t = 0.04$ $s$. The Lyapunov exponent for $F_D = 0.5$ which is drawn as a dashed line, is convergent with $\lambda = −0.251$. For $F_D = 1.2$ the exponent is divergent as indicated by the dashed line which as a slope of $\lambda = 0.1538$. These calculations were performed using the Runge-Kutta method by E. Shah, (Private communication)
:::

Figure 4.6.1 illustrates Lyapunov plots for the harmonically-driven, linearly-damped, plane pendulum, with the same conditions discussed in chapter $4.5$. Note that for the small driving amplitude $F_{D} = 0.5,$ the Lyapunov plot converges to ordered motion with an exponent $\lambda = -0.251,$ whereas for $F_{D} = 1.2,$ the plot diverges characteristic of chaotic motion with an exponent $\lambda = 0.1538.$ The Lyapunov exponent usually fluctuates widely at the local oscillator frequency, and thus the time average of the Lyapunov exponent must be taken over many periods of the oscillation to identify the general trend with time. Some systems near an order-to-chaos transition can exhibit positive Lyapunov exponents for short times, characteristic of chaos, and then converge to negative $\lambda$ at longer time implying ordered motion. The Lyapunov exponents are used extensively to monitor the stability of the solutions for non-linear systems. For example the Lyapunov exponent is used to identify whether fluid flow is laminar or turbulent as discussed in chapter $16.8$.

A dynamical system in $n$-dimensional phase space will have a set of $n$ Lyapunov exponents $\{\lambda _{1},\lambda _{2},\dots ,\lambda _{n}\}$ associated with a set of attractors, the importance of which depend on the initial conditions. Typically one Lyapunov exponent dominates at one specific location in phase space, and thus it is usual to use the maximal Lyapunov exponent to identify chaos. The Lyapunov exponent is a very sensitive measure of the onset of chaos and provides an important test of the chaotic nature for the complicated motion exhibited by non-linear systems.

### Bifurcation Diagram

The **bifurcation diagram** simplifies the presentation of the dynamical motion by sampling the status of the system once per period, synchronized to the driving frequency, for many sets of initial conditions. The results are presented graphically as a function of one parameter of the system in the bifurcation diagram. For example, the wildly different behavior in the driven damped plane pendulum is represented on a bifurcation diagram in Figure 4.6.2, which shows the observed angular velocity $\omega$ of the pendulum sampled once per drive cycle plotted versus drive strength. The bifurcation diagram is obtained by sampling either the angle $\theta$, or angular velocity $\omega$, once per drive cycle, that is, it represents the observables of the pendulum using a stroboscopic technique that samples the motion synchronous with the drive frequency. Bifurcation plots also can be created as a function of either the time $\tilde{t}$, the damping factor $Q$, the normalized frequency $\tilde{\omega} = \frac{\omega }{\omega _{0}}$, or the driving amplitude $\gamma$.

:::{figure} ../images/lt-16382-bifurcationddpp.jpg
:label: fig-4-6-2
:enumerator: 4.6.2
:alt: Bifurcation diagram samples the angular velocity \omega once per period for the driven, linearly-damped, plane pendulum plotted as a function of the drive strength \gamma. Regions of period doubling, and chaos, as well as islands of stability all are manifest as the drive strength \gamma is changed. Note that the limited number of samples causes broadening of the lines adjacent to bifurcations.

Bifurcation diagram samples the angular velocity $\omega$ once per period for the driven, linearly-damped, plane pendulum plotted as a function of the drive strength $\gamma$. Regions of period doubling, and chaos, as well as islands of stability all are manifest as the drive strength $\gamma$ is changed. Note that the limited number of samples causes broadening of the lines adjacent to bifurcations.
:::

In the domain with drive strength $\gamma <1.0663$ there is one unique angle each drive cycle as illustrated by the bifurcation diagram. For slightly higher drive strength period-two bifurcation behavior results in two different angles per drive cycle. The Lyapunov exponent is negative for this region corresponding to ordered motion. The cascade of period doubling with increase in drive strength is readily apparent until chaos sets in at the critical drive strength $\gamma _{c}$ when there is a random distribution of sampled angular velocities and the Lyapunov exponent becomes positive. Note that at $\gamma = 1.0845$ there is a brief interval of period-$6$ motion followed by another region of chaos. Around $\gamma = 1.1$ there is a region that is primarily chaotic which is reflected by chaotic values of the angular velocity on the bifurcation plot and large positive values of the Lyapunov exponent. The region around $\gamma = 1.12$ exhibits period three motion and negative Lyapunov exponent corresponding to ordered motion. The $1.15<\gamma <1.25$ region is mainly chaotic and has a large positive Lyapunov exponent. The region with $1.3<\gamma <1.4$ is striking in that this corresponds to rolling motion with reemergence of period one and negative Lyapunov exponent. This period-1 motion is due to a continuous rolling motion of the plane pendulum as shown in figure (4.5.3) where it is seen that the average $\theta$ increases $2\pi$ per cycle, whereas the angular velocity $\omega$ exhibits a periodic motion. That is, on average the pendulum is rotating $2\pi$ per cycle. Above $\gamma = 1.4$ the system starts to exhibit period doubling followed by chaos reminiscent of the behavior seen at lower $\gamma$ values.

These results show that the bifurcation diagram nicely illustrates the order to chaos transitions for the harmonically-driven, linearly-damped, pendulum. Several transitions between order and chaos are seen to occur. The apparent ordered and chaotic regimes are confirmed by the corresponding Lyapunov exponents which alternate between negative and positive values for the ordered and chaotic regions respectively.

### Poincaré Section

State-space plots are very useful for characterizing periodic motion, but they become too dense for useful interpretation when the system approaches chaos as illustrated in Figure 4.6.2. Poincaré sections solve this difficulty by taking a stroboscopic sample once per cycle of the state-space diagram. That is, the point on the state space orbit is sampled once per drive frequency. For period-$1$ motion this corresponds to a single point $(\theta ,\omega )$. For period-$2$ motion this corresponds to two points etc. For chaotic systems the sequence of state-space sample points follow complicated trajectories. Figure 4.6.3 shows the Poincaré sections for the corresponding state space diagram shown in figure (4.5.5) for cycles $10$ to $6000$. Note the complicated curves do not cross or repeat. Enlargements of any part of this plot will show increasingly dense parallel trajectories, called **fractals**, that indicates the complexity of the chaotic cyclic motion. That is, zooming in on a small section of this Poincaré plot shows many closely parallel trajectories. The fractal attractors are surprisingly robust to large differences in initial conditions. Poincaré sections are a sensitive probe of periodic motion for systems where periodic motion is not readily apparent.

:::{figure} ../images/lt-16383-poincareplots.jpg
:label: fig-4-6-3
:enumerator: 4.6.3
:alt: Three Poincaré section plots for the harmonically-driven, linearly-damped, pendulum for various initial conditions with F_D = 1.2, \tilde\omega = \frac{2}{3}, and \Delta t = \frac{\pi}{100}. These calculations used the Runge-Kutta method and were performed for 6000 cycles by E. Shah (Private comm…

Three Poincaré section plots for the harmonically-driven, linearly-damped, pendulum for various initial conditions with $F_D = 1.2$, $\tilde\omega = \frac{2}{3}$, and $\Delta t = \frac{\pi}{100}$. These calculations used the Runge-Kutta method and were performed for 6000 cycles by E. Shah (Private communication).
:::

In summary, the behavior of the well-known, harmonically-driven, linearly-damped, plane pendulum becomes remarkably complicated at large driving amplitudes where non-linear effects dominate. That is, when the restoring force is non-linear. The system exhibits bifurcation where it can evolve to multiple attractors that depend sensitively on the initial conditions. The system exhibits both oscillatory, and rolling, solutions depending on the amplitude of the motion. The system exhibits domains of simple ordered motion separated by domains of very complicated ordered motion as well as chaotic regions. The transitions between these dramatically different modes of motion are extremely sensitive to the amplitude and phase of the driver. Eventually the motion becomes completely chaotic. The Lyapunov exponent, bifurcation diagram, and Poincaré section plots, are sensitive measures of the order of the motion. These three sensitive measures of order and chaos are used extensively in many fields in classical mechanics. Considerable computing capabilities are required to elucidate the complicated motion involved in non-linear systems. Examples include laminar and turbulent flow in fluid dynamics and weather forecasting of hurricanes, where the motion can span a wide dynamic range in dimensions from $10^{-5}$ to $10^{4}$ $m$.

## 4.7: Wave Propagation for Non-linear Systems

### Phase, group, and signal velocities

Chapter $3$ discussed the wave equation and solutions for linear systems. It was shown that, for linear systems, the wave motion obeys superposition and exhibits dispersion, that is, a frequency-dependent phase velocity, and, in some cases, attenuation. Nonlinear systems introduce intriguing new wave phenomena. For example for nonlinear systems, second, and higher terms must be included in the Taylor expansion given in equation $(4.2.2)$. These second and higher order terms result in the group velocity being a function of $\omega ,$ that is, group velocity dispersion occurs which leads to the shape of the envelope of the wave packet being time dependent. As a consequence the group velocity in the wave packet is not well defined, and does not equal the signal velocity of the wave packet or the phase velocity of the wavelets. Nonlinear optical systems have been studied experimentally where $v_{group}<<c$, which is called slow light, while other systems have $v_{group}>c$ which is called superluminal light. The ability to control the velocity of light in such optical systems is of considerable current interest since it has signal transmission applications.

The dispersion relation for a nonlinear system can be expressed as a Taylor expansion of the form

$$
k=k_{0}+\left( \frac{\partial k}{\partial \omega }\right) _{\omega =\omega _{0}}(\omega -\omega _{0})+\frac{1}{2}\left( \frac{\partial ^{2}k}{\partial \omega ^{2}} \right) _{\omega =\omega _{0}}(\omega -\omega _{0})^{2}+..
$$

where $\omega$ is used as the independent variable since it is invariant to phase transitions of the system. Note that the factor for the first derivative term is the reciprocal of the group velocity

$$
\left( \frac{\partial k}{\partial \omega }\right) _{\omega =\omega _{0}}\equiv \frac{1}{v_{group}}
$$

while the factor for the second derivative term is

$$
\left( \frac{\partial ^{2}k}{\partial \omega ^{2}}\right) _{\omega =\omega _{0}}=\frac{\partial }{\partial \omega }\left[ \frac{1}{v_{group}(\omega )} \right] _{\omega =\omega _{0}}=\left( -\frac{1}{v_{group}^{2}}\frac{\partial v_{group}}{\partial \omega }\right) _{\omega =\omega _{0}}
$$

which gives the velocity dispersion for the system.

Since

$$
k=\frac{\omega }{v_{phase}}
$$

then

$$
\frac{\partial k}{\partial \omega }\equiv \frac{1}{v_{group}}=\frac{1}{ v_{phase}}+\omega \frac{\partial \frac{1}{v_{phase}}}{\partial \omega } \tag{4.45} \label{eq-4-45}
$$

The inverse velocities for electromagnetic waves are best represented in terms of the corresponding refractive indices $n,$ where

$$
n\equiv \frac{c}{v_{phase}}
$$

and the group refractive index

$$
n_{group}\equiv \frac{c}{v_{group}}
$$

Then Equation \text{(4.45)} can be written in the more convenient form 
$$
n_{group}=n+\omega \frac{\partial n}{\partial \omega } \tag{4.48} \label{eq-4-48}
$$

:::{figure} ../images/lt-16384-5_2c17.jpg
:label: fig-4-7-1
:enumerator: 4.7.1
:alt: The real and imaginary parts of the phase refractive index n plus the real part of the group refractive index associated with an isolated atomic resonance.

The real and imaginary parts of the phase refractive index n plus the real part of the group refractive index associated with an isolated atomic resonance.
:::

Wave propagation for an optical system that is subject to a single resonance gives one example of nonlinear frequency response that has applications to optics.

Figure 4.7.1 shows that the real $n_{R}$ and imaginary $n_{I}$ parts of the phase refractive index exhibit the characteristic resonance frequency dependence of the sinusoidally-driven, linear oscillator that was discussed in chapter $3.6$ and as illustrated in figure (3.6.4). Figure 4.7.1 also shows the group refractive index $n_{group}$ computed using Equation \text{(4.48)}.

Note that at resonance, $n_{group}$ is reduced below the non-resonant value which corresponds to superluminal (fast) light, whereas in the wings of the resonance $n_{group}$ is larger than the non-resonant value corresponding to slow light. Thus the nonlinear dependence of the refractive index $n$ on angular frequency $\omega$ leads to fast or slow group velocities for isolated wave packets. Velocities of light as slow as $17$ $m/\sec$ have been observed. Experimentally the energy absorption that occurs on resonance makes it difficult to observe the superluminal electromagnetic wave at resonance.

Note that Sommerfeld and Brillouin showed that even though the group velocity may exceed $c$, the signal velocity, which marks the arrival of the leading edge of the optical pulse, does not exceed $c$, the velocity of light in vacuum, as was postulated by Einstein.

### Soliton wave propagation

The soliton is a fascinating and very special wave propagation phenomenon that occurs for certain non-linear systems. The soliton is a self-reinforcing solitary localized wave packet that maintains its shape while travelling long distances at a constant speed. Solitons are caused by a cancellation of phase modulation resulting from non-linear velocity dependence, and the group velocity dispersive effects in a medium. Solitons arise as solutions of a widespread class of weakly-nonlinear dispersive partial differential equations describing many physical systems. Figure 4.7.2 shows a soliton comprising a solitary water wave approaching the coast of Hawaii. While the soliton in Fig. 4.7.2 may appear like a normal wave, it is unique in that there are no other waves accompanying it. This wave was probably created far away from the shore when a normal wave was modulated by a geometrical change in the ocean depth, such as the rising sea floor, which forced it into the appropriate shape for a soliton. The wave then was able to travel to the coast intact, despite the apparently placid nature of the ocean near the beach. Solitons are notable in that they interact with each other in ways very different from normal waves. Normal waves are known for their complicated interference patterns that depend on the frequency and wavelength of the waves. Solitons, can pass right through each other without being a affected at all. This makes solitons very appealing to scientists because soliton waves are more sturdy than normal waves, and can therefore be used to transmit information in ways that are distinctly different than for normal wave motion. For example, optical solitons are used in optical fibers made of a dispersive, nonlinear optical medium, to transmit optical pulses with an invariant shape.

:::{figure} ../images/lt-16385-solitonwaterwavehawaii.jpg
:label: fig-4-7-2
:enumerator: 4.7.2
:alt: A solitary wave approaches the coast of Hawaii. (Image: Robert Odom/University of Washington)

A solitary wave approaches the coast of Hawaii. (Image: Robert Odom/University of Washington)
:::

Solitons were first observed in $1834$ by John Scott Russell ($1808-1882$). Russell was an engineer conducting experiments to increase the efficiency of canal boats. His experimental and theoretical investigations allowed him to recreate the phenomenon in wave tanks. Through his extensive studies, Scott Russell noticed that soliton propagation exhibited the following properties:

- The waves are stable and hold their shape for long periods of time.

- The waves can travel over long distances at uniform speed.

- The speed of propagation of the wave depends on the size of the wave, with larger waves traveling faster than smaller waves.

- The waves maintained their shape when they collided - seemingly passing right through each other.

Scott Russell’s work was met with scepticism by the scientific community. The problem with the Wave of Translation was that it was an effect that depended on nonlinear effects, whereas previously existing theories of hydrodynamics (such as those of Newton and Bernoulli) only dealt with linear systems. George Biddell Airy, and George Gabriel Stokes, published papers attacking Scott Russell’s observations because the observations could not be explained by their theories of wave propagation in water. Regardless, Scott Russell was convinced of the prime importance of the Wave of Translation, and history proved that he was correct. Scott Russell went on to develop the "wave line" system of hull construction that revolutionized nineteenth century naval architecture, along with a number of other great accomplishments leading him to fame and prominence. Despite all of the success in his career, he continued throughout his life to pursue his studies of the Wave of Translation.

In $1895$ Korteweg and de Vries developed a wave equation for surface waves for shallow water.

$$
\frac{\partial \phi }{\partial t}+\frac{\partial ^{3}\phi }{\partial x^{3}} +6\phi \frac{\partial \phi }{\partial x}=0
$$
 A solution of this equation has the characteristics of a solitary wave with fixed shape. It is given by substituting the form $\phi (x,t)=f(x-vt)$ into the Korteweg-de Vries equation which gives

$$
-v\frac{\partial f}{\partial x}+\frac{\partial ^{3}f}{\partial x^{3}}+6f \frac{\partial f}{\partial x}=0
$$
 Integrating with respect to $x$ gives

$$
3f^{2}+\frac{d^{2}f}{dx^{3}}-cf=C
$$

where $C$ is a constant of integration. This non-linear equation has a solution

$$
\phi (x,t)=\frac{1}{2}c\sec h^{2}\left[ \frac{\sqrt{v}}{2}(x-vt-a)\right] \tag{4.52} \label{eq-4-52}
$$

where $a$ is a constant. Equation \text{(4.52)} is the equation of a solitary wave moving in the $+x$ direction at a velocity $v$.

Soliton behavior is observed in phenomena such as tsunamis, tidal bores that occur for some rivers, signals in optical fibres, plasmas, atmospheric waves, vortex filaments, superconductivity, and gravitational fields having cylindrical symmetry. Much work has been done on solitons for fibre optics applications. The soliton’s inherent stability make long-distance transmission possible without the use of repeaters, and could potentially double the transmission capacity.

Before the discovery of solitons, mathematicians were under the impression that nonlinear partial differential equations could not be solved exactly. However, solitons led to the recognition that there are non-linear systems that can be solved analytically. This discovery has prompted much investigation into these so-called "integrable systems." Such systems are rare, as most non-linear differential equations admit chaotic behavior with no explicit solutions. Integrable systems nevertheless lead to very interesting mathematics ranging from differential geometry and complex analysis to quantum field theory and fluid dynamics.

Many of the fundamental equations in physics (Maxwell’s, Schrödinger’s) are linear equations. However, physicists have begun to recognize many areas of physics in which nonlinearity can result in qualitatively new phenomenon which cannot be constructed via perturbation theory starting from linearized equations. These include phenomena in magnetohydrodynamics, meteorology, oceanography, condensed matter physics, nonlinear optics, and elementary particle physics. For example, the European space mission Cluster detected a soliton-like electrical disturbances that travelled through the ionized gas surrounding the Earth starting about 50,000 kilometers from Earth and travelling towards the planet at about 8 km/s. It is thought that this soliton was generated by turbulence in the magnetosphere.

Efforts to understand the nonlinearity of solitons has led to much research in many areas of physics. In the context of solitons, their particle-like behavior (in that they are localized and preserved under collisions) leads to a number of experimental and theoretical applications. The technique known as bosonization allows viewing particles, such as electrons and positrons, as solitons in appropriate field equations. There are numerous macroscopic phenomena, such as internal waves on the ocean, spontaneous transparency, and the behavior of light in fiber optic cable, that are now understood in terms of solitons. These phenomena are being applied to modern technology.

## 4.E: Nonlinear Systems and Chaos (Exercises)

1. Consider the chaotic motion of the driven damped pendulum whose equation of motion is given by

   
$$
{\small \ }\ddot{\phi}+\Gamma \dot{\phi}+\omega _{0}^{2}\sin \phi =\gamma \omega _{0}^{2}\cos \omega t \nonumber
$$

   for which the Lyapunov exponent is $\lambda =1$ with time measured in units of the drive period.

   1. Assume that you need to predict $\phi \left( t\right)$ with accuracy of $\ 10^{-2}$ $radians$, and that the initial value $\phi \left( 0\right)$ is known to within $10^{-6}$ $radians$ . What is the maximum time horizon $t_{\max }$ for which you can predict $\phi \left( t\right)$ to within the required accuracy?

   2. Suppose that you manage to improve the accuracy of the initial value to $10^{-9}$ $radians$ (that is, a thousand-fold improvement). What is the time horizon now for achieving the accuracy of $10^{-2}$ $radians$?

   3. By what factor has $t_{\max }$ improved with the $1000-fold$ improvement in initial measurement.

   4. What does this imply regarding long-term predictions of chaotic motion?

2. A non-linear oscillator satisfies the equation $\ddot{x}+\dot{ x}^{3}+x=0.$ Find the polar equations for the motion in the state-space diagram. Show that any trajectory that starts within the circle $r<1$ encircle the origin infinitely many times in the clockwise direction. Show further that these trajectories in state space terminate at the origin.

3. Consider the system of a mass suspended between two identical springs as shown.

   :::{figure} ../images/lt-21313-4.w.1.png
   :label: fig-4-E-1
   :enumerator: 4.E.1
   :alt: Figure
   :::

   If each spring is stretched a distance $d$ to attach the mass at the equilibrium position the mass is subject to two equal and oppositely directed forces of magnitude $\kappa d$. Ignore gravity. Show that the potential in which the mass moves is approximately

   
$$
U(x)=\left\{ \frac{\kappa d}{l}\right\} x^{2}+\left\{ \frac{\kappa (l-d)}{ 4l^{3}}\right\} x^{4}
$$

   Construct a state-space diagram for this potential.

4. A non-linear oscillator satisfies the equation
   
$$
\ddot{x} + (x^{2}+\dot{x}^{2}-1) \dot{x} + x = 0 \nonumber
$$

   Find the polar equations for the motion in the state-space diagram. Show that any trajectory that starts in the domain $1<r<\sqrt{3}$ spirals clockwise and tends to the limit cycle $r=1$. [The same is true of trajectories that start in the domain $0<r<1$. ] What is the period of the limit cycle?

5. A mass $m$ moves in one direction and is subject to a constant force $+F_{0}$ when $x<0$ and to a constant force $-F_{0}$ when $x>0$. Describe the motion by constructing a state space diagram. Calculate the period of the motion in terms of $m,F_{0}$ and the amplitude $A$. Disregard damping.

6. Investigate the motion of an undamped mass subject to a force of the form 
$$
F(x)= ( \begin{array}{c} -kx\hspace{1.2in}\left\vert x\right\vert <a \\ -(k+\delta )x+\delta a\hspace{0.55in}\left\vert x\right\vert >a \end{array} \nonumber
$$

## 4.S: Nonlinear Systems and Chaos (Summary)

The study of the dynamics of non-linear systems remains a vibrant and rapidly evolving field in classical mechanics as well as many other branches of science. This chapter has discussed examples of non-linear systems in classical mechanics. It was shown that the superposition principle is broken even for weak nonlinearity. It was shown that increased nonlinearity leads to bifurcation, point attractors, limit-cycle attractors, and sensitivity to initial conditions.

### Limit-cycle attractors

The Poincaré-Bendixson theorem for limit cycle attractors states that the paths, both in state-space and phase-space, can have three possible paths:

1. closed paths, like the elliptical paths for the undamped harmonic oscillator,

2. terminate at an equilibrium point as $t\rightarrow \infty$, like the point attractor for a damped harmonic oscillator,

3. tend to a limit cycle as $t\rightarrow \infty$.

The limit cycle is unusual in that the periodic motion tends asymptotically to the limit-cycle attractor independent of whether the initial values are inside or outside the limit cycle. The balance of dissipative forces and driving forces often leads to limit-cycle attractors, especially in biological applications. Identification of limit-cycle attractors, as well as the trajectories of the motion towards these limit-cycle attractors, is more complicated than for point attractors.

The van der Pol oscillator is a common example of a limit-cycle system that has an equation of motion of the form 
$$
\frac{d^{2}x}{dt^{2}}+\mu \left( x^{2}-1\right) \frac{dx}{dt}+\omega _{0}^{2}x=0 \tag{4.11}
$$

The van der Pol oscillator has a limit-cycle attractor that includes non-linear damping and exhibits periodic solutions that asymptotically approach one attractor solution independent of the initial conditions. There are many examples in nature that exhibit similar behavior.

### Harmonically-driven, linearly-damped, plane pendulum

The non-linearity of the well-known driven linearly-damped plane pendulum was used as an example of the behavior of non-linear systems in nature. It was shown that non-linearity leads to discontinuous period bifurcation, extreme sensitivity to initial conditions, rolling motion and chaos.

### Differentiation between ordered and chaotic motion

Lyapunov exponents, bifurcation diagrams, and Poincaré sections were used to identify the transition from order to chaos. Chapter $16.8$ discusses the non-linear Navier-Stokes equations of viscous-fluid flow which leads to complicated transitions between laminar and turbulent flow. Fluid flow exhibits remarkable complexity that nicely illustrates the dominant role that non-linearity can have on the solutions of practical non-linear systems in classical mechanics.

### Wave propagation for non-linear systems

Non-linear equations can lead to unexpected behavior for wave packet propagation such as fast or slow light as well as soliton solutions. Moreover, it is notable that some non-linear systems can lead to analytic solutions.

The complicated phenomena exhibited by the above non-linear systems is not restricted to classical mechanics, rather it is a manifestation of the mathematical behavior of the solutions of the differential equations involved. That is, this behavior is a general manifestation of the behavior of solutions for second-order differential equations. Exploration of this complex motion has only become feasible with the advent of powerful computer facilities during the past three decades. The breadth of phenomena exhibited by these examples is manifest in other nonlinear systems, ranging from many-body motion, weather patterns, growth of biological species, epidemics, motion of electrons in atoms, etc. Other examples of non-linear equations of motion not discussed here, are the three-body problem, which is mentioned in chapter $11$, and turbulence in fluid flow which is discussed in chapter $16$.

It is stressed that the behavior discussed in this chapter is very different from the random walk problem which is a stochastic process where each step is purely random and not deterministic. This chapter has assumed that the motion is fully deterministic and rigorously follows the laws of classical mechanics. Even though the motion is fully deterministic, and follows the laws of classical mechanics, the motion is extremely sensitive to the initial conditions and the non-linearities can lead to chaos. Computer modelling is the only viable approach for predicting the behavior of such non-linear systems. The complexity of solving non-linear equations is the reason that this book will continue to consider only linear systems. Fortunately, in nature, non-linear systems can be approximately linear when the small-amplitude assumption is applicable.
