---
title: "3. Linear Oscillators"
short_title: "Chapter 3"
label: ch-03-linear-oscillators
---


(ch-3)=

# 3. Linear Oscillators

## 3.1: Introduction to Linear Oscillators

Oscillations are a ubiquitous feature in nature. Examples are periodic motion of planets, the rise and fall of the tides, water waves, pendulum in a clock, musical instruments, sound waves, electromagnetic waves, and wave-particle duality in quantal physics. Oscillatory systems all have the same basic mathematical form although the names of the variables and parameters are different. The classical linear theory of oscillations will be assumed in this chapter since:

1. The linear approximation is well obeyed when the amplitudes of oscillation are small, that is, the restoring force obeys Hooke’s Law.

2. The Principle of Superposition applies.

3. The linear theory allows most problems to be solved explicitly in closed form. This is in contrast to non-linear system where the motion can be complicated and even chaotic as discussed in chapter $4$.

## 3.2: Linear Restoring Forces

An oscillatory system requires that there be a stable equilibrium about which the oscillations occur. Consider a conservative system with potential energy $U$ for which the force is given by

$$
\tag{3.1} \label{eq-3-1} \mathbf{F} = - \mathbf{\nabla}U
$$

:::{figure} ../images/lt-21311-4.2.1.png
:label: fig-3-2-1
:enumerator: 3.2.1
:alt: Stability for a one-dimensional potential U(x).

Stability for a one-dimensional potential U(x).
:::

[Figure 3.2.1](#fig-3-2-1) illustrates a conservative system that has three locations at which the restoring force is zero, that is, where the gradient of the potential is zero. Stable oscillations occur only around locations 1 and 3 whereas the system is unstable at the zero gradient location 2. Point 2 is called a separatrix in that an infinitesimal displacement of the particle from this separatrix will cause the particle to diverge towards either minimum 1 or 3 depending on which side of the separatrix the particle is displaced.

The requirements for stable oscillations about any point $x_0$ are that the potential energy must have the following properties.

### Stability requirements

1. The potential has a stable position for which the restoring force is zero, i.e. $( \frac{dU}{dx} )_{x = x_0} = 0$

2. The potential $U$ must be positive and an even function of displacement $x - x_0$. That is. $\big ( \frac{d^n U}{dx_n} \big ) _{x_0} > 0$ where $n$ is even.

The requirement for the restoring force to be linear is that the restoring force for perturbation about a stable equilibrium at $x_0$ is of the form

$$
\tag{3.2} \label{eq-3-2} \mathbf{F} = -\alpha ( x - x_0) = m \ddot{x}
$$

The potential energy function for a linear oscillator has a pure parabolic shape about the minimum location, that is,

$$
\tag{3.3} \label{eq-3-3} U = \frac{1}{2} k ( x - x_0)^2
$$

where $x_0$ is the location of the minimum.

Most oscillatory systems involve small amplitude oscillations about a stable minimum. For weak non-linear systems, where the amplitude of oscillation $\Delta x$ about the minimum is small, it is useful to make a Taylor expansion of the potential energy about the minimum. That is

$$
\tag{3.4} \label{eq-3-4} U ( \Delta x ) = U ( x_0 ) + \Delta x \frac{dU ( x_0)}{dx} + \frac{\Delta x^2}{2!} \frac{d^2 U ( x _0 )}{dx^2} + \frac{\Delta x^3}{3!} \frac{d^3 U ( x_0 )}{dx^3} + \frac{\Delta x^4}{4!} \frac{d^4 U ( x_0 )}{dx^4} + \dots
$$

By definition, at the minimum $\frac{dU ( x_0 )}{dx} = 0,$ and thus Equation [3.3](#eq-3-3) can be written as

$$
\tag{3.5} \label{eq-3-5} \Delta U = U ( \Delta x ) - U ( x_0 ) = \frac{\Delta x^2}{2!} \frac{d^2 U ( x _0 )}{dx^2} + \frac{\Delta x^3}{3!} \frac{d^3 U ( x_0 )}{dx^3} + \frac{\Delta x^4}{4!} \frac{d^4 U ( x_0 )}{dx^4} + \dots
$$

For small amplitude oscillations, the system is linear if the second-order $\frac{\Delta x^2}{2!} \frac{d^2 U ( x _0 )}{dx^2}$ term in Equation [3.2](#eq-3-2) is dominant.

The linearity for small amplitude oscillations greatly simplifies description of the oscillatory motion and complicated chaotic motion is avoided. Most physical systems are approximately linear for small amplitude oscillations, and thus the motion close to equilibrium approximates a linear harmonic oscillator.

## 3.3: Linearity and Superposition

An important aspect of linear systems is that the solutions obey the *Principle of Superposition*, that is, for the superposition of different oscillatory modes, the amplitudes add linearly. The linearly-damped linear oscillator is an example of a linear system in that it involves only linear operators, that is, it can be written in the operator form (appendix $19.6.2$)

$$
\tag{3.6} \label{eq-3-6} \Big ( \frac{d^2}{dt^2} + \Gamma \frac{d}{dt} + \omega_0^2 \Big ) x (t) = A \cos \omega t
$$

The quantity in the brackets on the left hand side is a linear operator that can be designated by $\mathbb{L}$ where

$$
\tag{3.7} \label{eq-3-7} \mathbb{L} x (t) = F (t)
$$

An important feature of linear operators is that they obey the principle of superposition. This property results from the fact that linear operators are distributive, that is

$$
\tag{3.8} \label{eq-3-8} \mathbb{L} ( x_1 + x_2 ) = \mathbb{L} ( x_1 ) + \mathbb{L}(x_2)
$$

Therefore if there are two solutions $x_1 (t)$ and $x_2 (t)$ for two different forcing functions $F_1 (t)$ and $F_2 ( t)$

$$
\tag{3.9} \label{eq-3-9} \begin{align*} \mathbb{L}x_1(t) & = & F_1(t) \\ \mathbb{L}x_1(t) & = & F_2(t) \end{align*}
$$

then the addition of these two solutions, with arbitrary constants, also is a solution for linear operators.

$$
\tag{3.10} \label{eq-3-10} \mathbb{L} ( \alpha_1 x_! + \alpha _2 x_2 ) = \alpha_1 F_1 (t) + \alpha_2 F_2 (t)
$$

In general then

$$
\tag{3.11} \label{eq-3-11} \mathbb{L} \Bigg ( \sum_{n=1}^N \alpha_n x_n (t) \Bigg ) = \Bigg ( \sum_{n=1}^N \alpha_n F_n (t) \Bigg )
$$

The left hand bracket can be identified as the linear combination of solutions

$$
\tag{3.12} \label{eq-3-12} x(t) = \sum_{n=1}^N \alpha_n x_n (t)
$$

while the driving force is a linear superposition of harmonic forces

$$
\tag{3.13} \label{eq-3-13} F(t) = \sum_{n=1}^N \alpha_n F_n (t)
$$

Thus these linear combinations also satisfy the general linear equation

$$
\tag{3.14} \label{eq-3-14} \mathbb{L} x(t) = F(t)
$$

Applicability of the Principle of Superposition to a system provides a tremendous advantage for handling and solving the equations of motion of oscillatory systems.

## 3.4: Geometrical Representations of Dynamical Motion

The powerful pattern-recognition capabilities of the human brain, coupled with geometrical representations of the motion of dynamical systems, provide a sensitive probe of periodic motion. The geometry of the motion often can provide more insight into the dynamics than inspection of mathematical functions. A system with $n$ degrees of freedom is characterized by locations $q_i$, velocities $\dot q_i$, and momenta $p_i$, in addition to the time $t$ and instantaneous energy $H(t)$. Geometrical representations of the dynamical correlations are illustrated by the configuration space and phase space representations of these $2n + 2$ variables.

### Configuration space $q_i, q_j, t$

A configuration space plot shows the correlated motion of two spatial coordinates $q_i$ and $q_j$ averaged over time. An example is the two-dimensional linear oscillator with two equations of motion and solutions

$$
\tag{3.15} \label{eq-3-15} \begin{array}{lr} m \ddot{x} + k_x x = 0 & m\ddot{y} + k_y y = 0 \end {array}
$$

$$
\tag{3.16} \label{eq-3-16} \begin{array}{lr} x(t) = A \cos(\omega_x t) & y(t) = B \cos ( \omega _y t - \delta ) \end{array}
$$

where $\omega = \sqrt{\frac{k}{m}}$. For unequal restoring force constants, $k_x \neq k_y$ the trajectory executes complicated Lissajous figures that depend on the angular frequencies $\omega_x, \omega_y$ and the phase factor $\delta$. When the ratio of the angular frequencies along the two axes is rational, that is $\frac{\omega_x}{\omega_y}$ is a rational fraction, then the curve will repeat at regular intervals as shown in [Figure 3.4.1](#fig-3-4-1), and this shape depends on the phase difference. Otherwise the trajectory gradually fills the whole rectangle.

:::{figure} ../images/lt-21112-3.4.1.png
:label: fig-3-4-1
:enumerator: 3.4.1
:alt: Configuration plots of (x,y) where x = \cos(4t) and y = \cos(5t - \delta) at four different phase values \delta. The curves are called Lissajous figures

Configuration plots of $(x,y)$ where $x = \cos(4t)$ and $y = \cos(5t - \delta)$ at four different phase values $\delta$. The curves are called Lissajous figures
:::

### State space, $( q_i , \dot{q}_i, t )$

Visualization of a trajectory is enhanced by correlation of configuration $q_i$ and it’s corresponding velocity $\dot{q}_i$ which specifies the direction of the motion. The state space representation[^3-4-1] is especially valuable when discussing Lagrangian mechanics which is based on the Lagrangian $L (\mathbf{q}, {\bf \dot{q}}, t)$.

The free undamped harmonic oscillator provides a simple application of state space. Consider a mass $m$ attached to a spring with linear spring constant $k$ for which the equation of motion is

$$
\tag{3.17} \label{eq-3-17} -kx = m \ddot{x} = m \dot{x} \frac{d \dot{x}}{dx}
$$

By integration this gives

$$
\tag{3.18} \label{eq-3-18} \frac{1}{2} m \dot{x}^2 + \frac{1}{2} kx^2 = E
$$

The first term in Equation [3.18](#eq-3-18) is the kinetic energy, the second term is the potential energy, and $E$ is the total energy which is conserved for this system. This equation can be expressed in terms of the state space coordinates as

$$
\tag{3.19} \label{eq-3-19} \frac{\dot{x}^2}{ ( \frac{2E}{m} )} + \frac{ x^2}{ ( \frac{2E}{k} ) } = 1
$$

This corresponds to the equation of an ellipse for a state-space plot of $\dot{x}$ versus $x$ as shown in [Figure 3.4.2](#fig-3-4-2)-*upper*. The elliptical paths shown correspond to contours of constant total energy which is partitioned between kinetic and potential energy. For the coordinate axis shown, the motion of a representative point will be in a clockwise direction as the total oscillator energy is redistributed between potential to kinetic energy. The area of the ellipse is proportional to the total energy $E$.

### Phase space, $(q_i, p_i, t )$

:::{figure} ../images/lt-21111-3.4.2.png
:label: fig-3-4-2
:enumerator: 3.4.2
:alt: State space (upper), and phase space (lower) diagrams, for the linear harmonic oscillator.

State space (upper), and phase space (lower) diagrams, for the linear harmonic oscillator.
:::

Phase space, which was introduced by J.W. Gibbs for the field of statistical mechanics, provides a fundamental graphical representation in classical mechanics. The phase space coordinates $q_i p_i$ are the conjugate coordinates $( \mathbf{q},{\bf p} )$ and are fundamental to Hamiltonian mechanics which is based on the Hamiltonian $H ( \mathbf{q},{\bf p}, t )$. For a conservative system, only one phase-space curve passes through any point in phase space like the flow of an incompressible fluid. This makes phase space more useful than state space where many curves pass through any location. Lanczos [La49] defined an extended phase space using four-dimensional relativistic space-time as discussed in chapter $17$.

Since $p_x = m \dot{x}$ for the non-relativistic, one-dimensional, linear oscillator, then Equation [3.19](#eq-3-19) can be rewritten in the form

$$
\tag{3.20} \label{eq-3-20} \frac{p_x^2}{2mE} + \frac{x^2}{ ( \frac{2E}{k} ) } = 1
$$

This is the equation of an ellipse in the phase space diagram shown in Fig.3.4.2-*lower* which looks identical to Fig.3.4.2-*upper* since that the ordinate variable is multiplied by the constant $m$. That is, the only difference is the phase-space coordinates $( x, p_x )$ replace the state-space coordinates $( x, \dot{x} )$. State space plots are used extensively in this chapter to describe oscillatory motion. Although phase space is more fundamental, both state space and phase space plots provide useful representations for characterizing and elucidating a wide variety of motion in classical mechanics. The following discussion of the undamped simple pendulum illustrates the general features of state space.

### Plane pendulum

Consider a simple plane pendulum of mass $m$ attached to a string of length $l$ in a uniform gravitational field $g$. There is only one generalized coordinate, $\theta$. Since the moment of inertia of the simple plane-pendulum is $I = ml^2$ then the kinetic energy is

$$
\tag{3.21} \label{eq-3-21} T = \frac{1}{2} m l^2 \dot{\theta}^2
$$

and the potential energy relative to the bottom dead center is

$$
\tag{3.22} \label{eq-3-22} U = mgl ( 1 - \cos \theta)
$$

Thus the total energy equals

$$
\tag{3.33} \label{eq-3-33} E = \frac{1}{2}ml^2 \dot{\theta}^2 + mgl (1 - \cos \theta) = \frac{p_\theta^2}{2ml^2} + mgl ( 1 - \cos \theta)
$$

where $E$ is a constant of motion. Note that the angular momentum $p_\theta$ is not a constant of motion since the angular acceleration $\dot{p}_{\theta}$ explicitly depends on $\theta$.

It is interesting to look at the solutions for the equation of motion for a plane pendulum on a $\left( \theta, \dot{\theta}\right)$ state space diagram shown in [Figure 3.4.3](#fig-3-4-3). The curves shown are equally-spaced contours of constant total energy. Note that the trajectories are ellipses only at very small angles where $1− \cos \theta \approx \theta^2$, the contours are non-elliptical for higher amplitude oscillations. When the energy is in the range $0 < E < 2$ $mgl$ the motion corresponds to oscillations of the pendulum about $\theta = 0$. The center of the ellipse is at $(0, 0)$ which is a stable equilibrium point for the oscillation. However, when $|E| > 2 mgl$ there is a phase change to rotational motion about the horizontal axis, that is, the pendulum swings around and over top dead center, i.e. it rotates continuously in one direction about the horizontal axis. The phase change occurs at $E = 2$ $mgl$. and is designated by the separatrix trajectory.

:::{figure} ../images/lt-21113-3.4.3.png
:label: fig-3-4-3
:enumerator: 3.4.3
:alt: State space diagram for a plane pendulum. The \theta axis is in units of \pi radians. Note that \theta = +\pi and −\pi correspond to the same physical point, that is the phase diagram should be rolled into a cylinder connected at \theta = \pm \pi.

State space diagram for a plane pendulum. The \theta axis is in units of $\pi$ radians. Note that $\theta = +\pi$ and $−\pi$ correspond to the same physical point, that is the phase diagram should be rolled into a cylinder connected at $\theta = \pm \pi$.
:::

[Figure 3.4.3](#fig-3-4-3) shows two cycles for $\theta$ to better illustrate the cyclic nature of the phase diagram. The closed loops, shown as fine solid lines, correspond to pendulum oscillations about $\theta = 0$ or $2\pi$ for $E < 2$ $mgl$. The dashed lines show rolling motion for cases where the total energy $E > 2$ $mgl$. The broad solid line is the separatrix that separates the rolling and oscillatory motion. Note that at the separatrix the kinetic energy and $\dot{\theta}$ are zero when the pendulum is at top dead center which occurs when $\theta = \pm \pi$. The point $(\pi , 0)$ is an unstable equilibrium characterized by phase lines that are hyperbolic to this unstable equilibrium point. Note that $\theta = +\pi$ and $−\pi$ correspond to the same physical point, that is, the phase diagram is better presented on a cylindrical phase space representation since $\theta$ is a cyclic variable that cycles around the cylinder whereas $\dot{\theta}$ oscillates equally about zero having both positive and negative values. The state-space diagram can be wrapped around a cylinder, then the unstable and stable equilibrium points will be at diametrically opposite locations on the surface of the cylinder at $\dot \theta = 0$. For small oscillations about equilibrium, also called librations, the correlation between $\dot{\theta}$ and $\theta$ is given by the clockwise closed loops wrapped on the cylindrical surface, whereas for energies $|E| > 2$ $mgl$ the positive $\dot{\theta}$ corresponds to counterclockwise rotations while the negative $\dot{\theta}$ corresponds to clockwise rotations.

State-space diagrams will be used for describing oscillatory motion in chapters $3$ and $4$. Phase space is used in statistical mechanics in order to handle the equations of motion for ensembles of $\sim 10^{23}$ independent particles since momentum is more fundamental than velocity. Rather than try to account separately for the motion of each particle for an ensemble, it is best to specify the region of phase space containing the ensemble. If the number of particles is conserved, then every point in the initial phase space must transform to corresponding points in the final phase space. This will be discussed in chapters $8.3$ and $15.2.7$.

[^3-4-1]: A universal name for the $(\mathbf{q}, \mathbf{\dot{q}})$ representation has not been adopted in the literature. Therefore this book has adopted the name "state space". Lanczos [La49] uses the term "state space" to refer to the extended phase space $( \mathbf{q},{\bf p}, t)$ discussed in chapter $17$.

## 3.5: Linearly-damped Free Linear Oscillator

### General solution

All simple harmonic oscillations are damped to some degree due to energy dissipation via friction, viscous forces, or electrical resistance etc. The motion of damped systems is not conservative since energy is dissipated as heat. As was discussed in chapter $2$ the damping force can be expressed as

$$
{\bf F}_D (v) = −f(v) \hat{\mathbf{v}} \tag{3.24} \label{eq-3-24}
$$

where the velocity dependent function $f(v)$ can be complicated. Fortunately there is a very large class of problems in electricity and magnetism, classical mechanics, molecular, atomic, and nuclear physics, where the damping force depends linearly on velocity which greatly simplifies solution of the equations of motion. Therefore this chapter will discuss linear damping.

Consider the free simple harmonic oscillator, that is, assuming no oscillatory forcing function, with a linear damping term ${\bf F}_D(v) = −b{\bf v}$ where the parameter $b$ is the damping factor. Then the equation of motion is

$$
−kx − b\dot{x} = m\ddot{x}\tag{3.25} \label{eq-3-25}
$$

This can be rewritten as

$$
\ddot{x} + \ddot{x} + \Gamma \dot{x} + \omega^2_0x = 0 \tag{3.26} \label{eq-3-26}
$$

where the damping parameter

$$
\Gamma = \frac{b}{m} \tag{3.27} \label{eq-3-27}
$$

and the characteristic angular frequency

$$
\omega_0 = \sqrt{\frac{k}{m}} \tag{3.28} \label{eq-3-28}
$$

The general solution to the linearly-damped free oscillator is obtained by inserting the complex trial solution $z = z_0 e^{i\omega t}$. Then

$$
(i\omega )^2 z_0 e^{i \omega t} + i\omega \Gamma z_0 e^{i\omega t} + \omega^2_0 z_0e^{i\omega t} = 0 \tag{3.29} \label{eq-3-29}
$$

This implies that

$$
\omega^2 − i\omega \Gamma − \omega^2_0 = 0 \tag{3.30} \label{eq-3-30}
$$

The solution is

$$
\omega_{\pm} = i \frac{\Gamma}{2} \pm \sqrt{\omega^2_0 − \left( \frac{\Gamma}{2} \right)^2} \tag{3.31} \label{eq-3-31}
$$

The two solutions $\omega_{\pm}$ are complex conjugates and thus the solutions of the damped free oscillator are

$$
z = z_1 e^{i\left(i \frac{\Gamma}{2} + \sqrt{\omega^2_0 − \left( \frac{\Gamma}{2} \right)^2}\right)t} + z_2e^{i\left(i \frac{\Gamma}{2} - \sqrt{\omega^2_0 − \left( \frac{\Gamma}{2} \right)^2}\right)t} \tag{3.32} \label{eq-3-32}
$$

This can be written as

$$
z = e^{−( \frac{\Gamma}{2} )t} \left[ z_1 e^{i\omega_1 t} + z_2 e^{-i\omega_1 t}\right] \tag{3.33}
$$

where

$$
\omega_1 \equiv \sqrt{\omega^2_o − \left( \frac{\Gamma}{2} \right)^2 } \tag{3.34} \label{eq-3-34}
$$

#### Underdamped motion $\omega^2_1 \equiv \omega^2_o − \left(\frac{\Gamma}{2} \right)^2 > 0$

When $\omega^2_1 > 0$ then the square root is real so the solution can be written taking the real part of $z$ which gives that Equation [3.33](#eq-3-33) equals

$$
x(t) = Ae^{−( \frac{\Gamma}{ 2} )t} \cos (\omega_1 t − \beta ) \tag{3.35} \label{eq-3-35}
$$

Where $A$ and $\beta$ are adjustable constants fit to the initial conditions. Therefore the velocity is given by

$$
\dot{x}(t) = −Ae^{-\frac{\Gamma}{ 2}t} \left[ \omega_1 \sin (\omega_1 t − \beta ) + \frac{\Gamma}{ 2} \cos (\omega_1 t − \beta ) \right] \tag{3.36} \label{eq-3-36}
$$

This is the damped sinusoidal oscillation illustrated in [Figure 3.5.1](#fig-3-5-1)-*upper*. The solution has the following characteristics:

1. The oscillation amplitude decreases exponentially with a time constant $\tau_D = \frac{2}{\Gamma}$.

2. There is a small reduction in the frequency of the oscillation due to the damping leading to $\omega_1 = \sqrt{\omega^2_o − \left(\frac{\Gamma}{ 2}\right)^2}$

:::{figure} ../images/lt-21115-3.5.1.png
:label: fig-3-5-1
:enumerator: 3.5.1
:alt: The amplitude-time dependence and state-space diagrams for the free linearly-damped harmonic oscillator. The upper row shows the underdamped system for the case with damping \Gamma = \frac{\omega_0}{5\pi}. The lower row shows the overdamped ( \frac{\Gamma}{ 2} > \omega_0) [solid line] and critica…

The amplitude-time dependence and state-space diagrams for the free linearly-damped harmonic oscillator. The upper row shows the underdamped system for the case with damping $\Gamma = \frac{\omega_0}{5\pi}$. The lower row shows the overdamped $( \frac{\Gamma}{ 2} > \omega_0)$ [solid line] and critically damped $( \frac{\Gamma}{2} = \omega_0)$ [dashed line] in both cases assuming that initially the system is at rest.
:::

:::{figure} ../images/lt-21114-3.5.2.png
:label: fig-3-5-2
:enumerator: 3.5.2
:alt: Real and imaginary solutions \omega_{\pm} of the damped harmonic oscillator. A phase transition occurs at \Gamma = 2\omega_0. For \Gamma < 2\omega_0 (dashed) the two solutions are complex conjugates and imaginary. For \Gamma > 2\omega_0, (solid), there are two real solutions \omega_+ and \omega_−…

Real and imaginary solutions $\omega_{\pm}$ of the damped harmonic oscillator. A phase transition occurs at $\Gamma = 2\omega_0$. For $\Gamma < 2\omega_0$ (dashed) the two solutions are complex conjugates and imaginary. For $\Gamma > 2\omega_0$, (solid), there are two real solutions $\omega_+$ and $\omega_−$ with widely different decay constants where $\omega_+$ dominates the decay at long times.
:::

#### Overdamped case $\omega^2_1 \equiv \omega^2_o − \left( \frac{\Gamma}{2}\right)^2 < 0$

In this case the square root of $\omega^2_1$ is imaginary and can be expressed as $\omega^{\prime}_1 = i\sqrt{\left(\frac{\Gamma}{2}\right)^2 - \omega^2_o}$. Therefore the solution is obtained more naturally by using a real trial solution $z =z+0 e^{\omega t}$ in Equation [3.33](#eq-3-33) which leads to two roots

$$
\omega_{\pm} = − \left[ −\frac{\Gamma}{2} \pm \sqrt{ \left( \frac{\Gamma}{2}\right)^2 − \omega^2_o} \right] \nonumber
$$

Thus the exponentially damped decay has two time constants $\omega_+$ and $\omega_−$.

$$
x(t) = {A_1e^{-\omega_+ t}} + A_2e^{−\omega_− t}] \tag{3.37} \label{eq-3-37}
$$

The time constant $\frac{1}{\omega_−} < \frac{1}{\omega_+}$ thus the first term $A_1e^{-\omega_+ t}$ in the bracket decays in a shorter time than the second term $A_2e^{-\omega_- t}$. As illustrated in [Figure 3.5.2](#fig-3-5-2) the decay rate, which is imaginary when underdamped, i.e. $\frac{\Gamma}{2} < \omega_o$ bifurcates into two real values $\omega_{\pm}$ for overdamped, i.e. $\frac{\Gamma}{2} >\omega_o$. At large times the dominant term when overdamped is for $\omega_+$ which has the smallest decay rate, that is, the longest decay constant $\tau_+ = \frac{1}{\omega_+}$. There is no oscillatory motion for the overdamped case, it slowly moves monotonically to zero as shown in fig 3.5 *lower*. The amplitude decays away with a time constant that is longer than $\frac{2}{\Gamma}$.

#### Critically damped $\omega^2_1 \equiv \omega^2_o − \left( \frac{\Gamma}{2}\right)^2 = 0$

This is the limiting case where $\frac{\Gamma}{2}= \omega_o$ For this case the solution is of the form

$$
x(t) = (A +Bt) e^{-( \frac{\Gamma}{2})t} \tag{3.38} \label{eq-3-38}
$$

This motion also is non-sinusoidal and evolves monotonically to zero. As shown in [Figure 3.5.1](#fig-3-5-1) the critically-damped solution goes to zero with the shortest time constant, that is, largest $\omega$. Thus analog electric meters are built almost critically damped so the needle moves to the new equilibrium value in the shortest time without oscillation.

It is useful to graphically represent the motion of the damped linear oscillator on either a state space $(\dot{x}, x)$ diagram or phase space $(p_x, x)$ diagram as discussed in chapter $3.4$. The state space plots for the undamped, overdamped, and critically-damped solutions of the damped harmonic oscillator are shown in [Figure 3.5.1](#fig-3-5-1). For underdamped motion the state space diagram spirals inwards to the origin in contrast to critical or overdamped motion where the state and phase space diagrams move monotonically to zero.

### Energy dissipation

The instantaneous energy is the sum of the instantaneous kinetic and potential energies

$$
E = \frac{1}{2} m \dot{x}^2 + \frac{1}{2} kx^2 \tag{3.39} \label{eq-3-39}
$$

where $x$ and $\dot{x}$ are given by the solution of the equation of motion. Consider the total energy of the underdamped system

$$
E = \frac{1}{2} m \dot{x}^2 + \frac{1}{2} m\omega^2_0x^2 \tag{3.40} \label{eq-3-40}
$$

where $k = m\omega^2_0$. The average total energy is given by substitution for $x$ and $\dot{x}$ and taking the average over one cycle. Since

$$
x(t) = Ae^{−( \frac{\Gamma}{2})t} \cos (\omega_1 t − \beta ) \tag{3.41} \label{eq-3-41}
$$

Then the velocity is given by

$$
\dot{x}(t) = −Ae^{− \frac{\Gamma}{2} t} \left[ \omega_1 \sin (\omega_1t − \beta ) + \frac{\Gamma}{2} \cos (\omega_1 t − \beta ) \right] \tag{3.42} \label{eq-3-42}
$$

Inserting equations [3.41](#eq-3-41) and [3.42](#eq-3-42) into [3.40](#eq-3-40) gives a small amplitude oscillation about an exponential decay for the energy $E$. Averaging over one cycle and using the fact that $\langle \sin \theta \cos \theta \rangle = 0$, and $\left\langle [\sin \theta ]^2 \right\rangle = \left\langle [ \cos \theta ]^2 \right\rangle = \frac{1}{2}$, gives the time-averaged total energy as

$$
\langle E \rangle = e^{-\Gamma t} \left( \frac{1}{4} mA^2 \omega^2_1 + \frac{1}{4} m A^2 \left( \frac{\Gamma}{2} \right)^2 + \frac{1}{4} mA^2 \omega^2_0 \right) \tag{3.43} \label{eq-3-43}
$$

which can be written as

$$
\langle E \rangle = E_0 e^{−\Gamma t} \tag{3.44} \label{eq-3-44}
$$

Note that the *energy* of the linearly damped free oscillator decays away exponentially with a time constant $\tau = \frac{1}{\Gamma}$. That is, the *intensity* has a time constant that is half the time constant for the decay of the *amplitude* of the transient response. Note that the average kinetic and potential energies are identical, as implied by the Virial theorem, and both decay away with the same time constant. This relation between the mean life $\tau$ for decay of the damped harmonic oscillator and the damping width term $\Gamma$ occurs frequently in physics.

The damping of an oscillator usually is characterized by a single parameter $Q$ called the **Quality Factor** where

$$
Q \equiv \frac{\text{Energy stored in the oscillator}}{\text{Energy dissipated per radian}} \tag{3.45} \label{eq-3-45}
$$

The energy loss per radian is given by

$$
\Delta E = \frac{dE}{dt} \frac{1}{\omega_1} = \frac{E \Gamma}{\omega_1} = \frac{E\Gamma}{\sqrt{\omega^2_o - \left( \frac{\Gamma}{2} \right)^2 } } \tag{3.46} \label{eq-3-46}
$$

where the numerator $\omega_1 = \sqrt{\omega^2_o − \left( \frac{\Gamma}{2} \right)^2}$ is the frequency of the free damped linear oscillator.

Thus the Quality factor $Q$ equals

$$
Q = \frac{E}{\Delta E} = \frac{\omega_1}{\Gamma} \tag{3.47} \label{eq-3-47}
$$

The larger the $Q$ factor, the less damped is the system, and the greater is the number of cycles of the oscillation in the damped wave train. Chapter $3.11.3$ shows that the longer the wave train, that is the higher is the $Q$ factor, the narrower is the frequency distribution around the central value. The Mössbauer effect in nuclear physics provides a remarkably long wave train that can be used to make high precision measurements. The high-$Q$ precision of the LIGO laser interferometer was used in the recent successful search for gravity waves.

| Oscillating system | Typical Q factors |
| --- | --- |
| Earth, for earthquake wave | 250-1400 |
| Piano string | 3000 |
| Crystal in digital watch | $10^4$ |
| Microwave cavity | $10^4$ |
| Excited atom | $10^7$ |
| Neutron star | $10^{12}$ |
| LIGO laser | $10^{13}$ |
| Mössbauer effect in nucleus | $10^{14}$ |

## 3.6: Sinusoidally-driven, linearly-damped, linear oscillator

The linearly-damped linear oscillator, driven by a harmonic driving force, is of considerable importance to all branches of science and engineering. The equation of motion can be written as

$$
\ddot{x} + \Gamma \dot{x} + w^2_0 x = \frac{F (t)}{m} \tag{3.48} \label{eq-3-48}
$$

where $F(t)$ is the driving force. For mathematical simplicity the driving force is chosen to be a sinusoidal harmonic force. The solution of this second-order differential equation comprises two components, the complementary solution (*transient response*), and the particular solution (*steady-state response*).

### Transient response of a driven oscillator

The transient response of a driven oscillator is given by the complementary solution of the above second-order differential equation

$$
\ddot{x} + \Gamma \dot{x} + \omega^{2}_0 x = 0 \tag{3.49} \label{eq-3-49}
$$

which is identical to the solution of the free linearly-damped harmonic oscillator. As discussed in section $3.5$ the solution of the linearly-damped free oscillator is given by the real part of the complex variable $z$ where

$$
z = e^{− \frac{\Gamma}{2} t} [z_1 e^{i \omega_1 t} + z_2 e^{-i \omega_1 t} ] \tag{3.50} \label{eq-3-50}
$$

and

$$
\omega_1 \equiv \sqrt{\omega^2_o − \left( \frac{\Gamma}{2} \right)^2 } \tag{3.51} \label{eq-3-51}
$$

#### Underdamped motion $\omega^2_1 \equiv \omega^2_o − \frac{\Gamma}{2}^2 > 0$:

When $\omega^2_1 > 0$, then the square root is real so the transient solution can be written taking the real part of $z$ which gives

$$
x(t)_T = \frac{F_0}{m} e^{-\frac{\Gamma}{2} t} \cos (\omega_1 t) \tag{3.52} \label{eq-3-52}
$$

The solution has the following characteristics:

a) The amplitude of the transient solution decreases exponentially with a time constant $\tau_D = \frac{2}{\Gamma}$ while the energy decreases with a time constant of $\frac{1}{\Gamma}$.

b) There is a small downward frequency shift in that $\omega_1 = \sqrt{\omega^2_o − ( \frac{\Gamma}{2})^2}$.

#### Overdamped case $\omega^2_1 \equiv \omega^2_o − (\frac{\Gamma}{2})^2 < 0$:

In this case the square root is imaginary, which can be expressed as $\omega^{\prime}_1 \equiv \sqrt{(\frac{\Gamma}{2})^2 − \omega^2_o}$ which is real and the solution is just an exponentially damped one

$$
x(t)_T = \frac{F_0}{m} e^{-\frac{\Gamma}{2} t} \left[e^{\omega^{\prime}_1 t} + e^{-\omega^{\prime}_1 t} \right]\tag{3.53} \label{eq-3-53}
$$

There is no oscillatory motion for the overdamped case, it slowly moves monotonically to zero. The total energy decays away with two time constants greater than $\frac{1}{\Gamma}$.

#### Critically damped $\omega^2_1 \equiv \omega^2_o − (\frac{\Gamma}{2})^2 = 0$:

For this case, as mentioned for the damped free oscillator, the solution is of the form

$$
x(t)_T = (A + Bt) e^{− \frac{\Gamma}{2} t} \tag{3.54} \label{eq-3-54}
$$

The critically-damped system decays away the quickest.

### Steady state response of a driven oscillator

The particular solution of the differential equation gives the important steady state response, $x(t)_S$ to the forcing function. Consider that the forcing term is a single frequency sinusoidal oscillation.

$$
F(t) = F_0 \cos (\omega t) \tag{3.55} \label{eq-3-55}
$$

Thus the particular solution is the real part of the complex variable $z$ which is a solution of

$$
\ddot{z} + \Gamma \dot{z} + \omega^2_0 z = \frac{F_0}{m} e^{i\omega t} \tag{3.56} \label{eq-3-56}
$$

A trial solution is

$$
z = z_0 e^{i \omega t} \tag{3.57} \label{eq-3-57}
$$

This leads to the relation

$$
−\omega^2 z_0 + i \omega \Gamma z_0 + \omega^2_0 z_0 = \frac{F_0}{m} \tag{3.58} \label{eq-3-58}
$$

Multiplying the numerator and denominator by the factor $(\omega^2_0 − \omega^2) − i\Gamma \omega$ gives

$$
z_0 = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2) + i\Gamma \omega} = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} [( \omega^2_0 − \omega^2) − i\Gamma \omega ] \tag{3.59} \label{eq-3-59}
$$

The steady state solution $x(t)_S$ thus is given by the real part of $z$, that is

$$
x(t)_S = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} [( \omega^2_0 − \omega^2) \cos \omega t + \Gamma \omega \sin \omega t] \tag{3.60} \label{eq-3-60}
$$

This can be expressed in terms of a phase $\delta$ defined as

$$
\tan \delta \equiv \left( \frac{\Gamma \omega}{ \omega^2_0 − \omega^2}\right) \tag{3.61} \label{eq-3-61}
$$

:::{figure} ../images/lt-21116-3.6.1.png
:label: fig-3-6-1
:enumerator: 3.6.1
:alt: Phase between driving force and resultant motion.

Phase between driving force and resultant motion.
:::

As shown in [Figure 3.6.1](#fig-3-6-1) the hypotenuse of the triangle equals $\sqrt{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2}$. Thus

$$
\cos \delta = \frac{\omega^2_0 − \omega^2}{\sqrt{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2}} \tag{3.62} \label{eq-3-62}
$$

and

$$
\sin \delta = \frac{\Gamma \omega}{ \sqrt{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2}} \tag{3.63} \label{eq-3-63}
$$

The phase $\delta$ represents the phase difference between the driving force and the resultant motion. For a fixed $\omega_0$ the phase $\delta = 0$ when $\omega = 0$, and increases to $\delta = \frac{\pi}{2}$ when $\omega = \omega_0$. For $\omega > \omega_0$ the phase $\delta \rightarrow \pi$ as $\omega \rightarrow \infty$.

The steady state solution can be re-expressed in terms of the phase shift $\delta$ as

$$
x(t)_S = \frac{\frac{F_0}{m}}{\sqrt{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2}} [\cos \delta \cos \omega t + \sin \delta \sin \omega t] \\ = \frac{\frac{F_0}{m}}{\sqrt{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2}} \cos (\omega t − \delta) \tag{3.64} \label{eq-3-64}
$$

:::{figure} ../images/lt-21119-3.6.2.png
:label: fig-3-6-2
:enumerator: 3.6.2
:alt: Amplitude versus time, and state space plots of the transient solution (dashed) and total solution (solid) for two cases. The upper row shows the case where the driving frequency \omega = \frac{\omega_1}{5} while the lower row shows the same for the case where the driving frequency \omega = 5\ome…

Amplitude versus time, and state space plots of the transient solution (dashed) and total solution (solid) for two cases. The upper row shows the case where the driving frequency $\omega = \frac{\omega_1}{5}$ while the lower row shows the same for the case where the driving frequency $\omega = 5\omega_1$.
:::

### Complete solution of the driven oscillator

To summarize, the total solution of the sinusoidally forced linearly-damped harmonic oscillator is the sum of the transient and steady-state solutions of the equations of motion.

$$
x(t)_{Total} = x(t)_T + x(t)_S \tag{3.65} \label{eq-3-65}
$$

This for the underdamped case, the transient solution is the complementary solution

$$
x(t)_T = \frac{F_0}{m} e^{-\frac{\Gamma}{2} t} \cos (\omega_1 t − \beta) \tag{3.66} \label{eq-3-66}
$$

where $\omega_1 = \sqrt{\omega^2_o − (\frac{\Gamma}{2})^2}$. The steady-state solution is given by the particular solution

$$
x(t)_S = \frac{\frac{F_0}{m}}{\sqrt{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2}} \cos (\omega t − \delta) \tag{3.67} \label{eq-3-67}
$$

Note that the frequency of the transient solution is $\omega_1$ which in general differs from the driving frequency $\omega$. The phase shift $\beta − \delta$ for the transient component is set by the initial conditions. The transient response leads to a more complicated motion immediately after the driving function is switched on. [Figure 3.6.2](#fig-3-6-2) illustrates the amplitude time dependence and state space diagram for the transient component, and the total response, when the driving frequency is either $\omega = \frac{\omega_1}{5}$ or $\omega = 5\omega_1$. Note that the modulation of the steady-state response by the transient response is unimportant once the transient response has damped out leading to a constant elliptical state space trajectory. For cases where the initial conditions are $x = \dot{x} = 0$ then the transient solution has a relative phase difference $\beta −\delta = \pi$ radians at $t = 0$ and relative amplitudes such that the transient and steady-state solutions cancel at $t = 0$.

The characteristic sounds of different types of musical instruments depend very much on the admixture of transient solutions plus the number and mixture of oscillatory active modes. Percussive instruments, such as the piano, have a large transient component. The mixture of transient and steady-state solutions for forced oscillations occurs frequently in studies of *RLC* networks in electrical circuit analysis.

### Resonance

The discussion so far has discussed the role of the transient and steady-state solutions of the driven damped harmonic oscillator which occurs frequently is science, and engineering. Another important aspect is resonance that occurs when the driving frequency $\omega$ approaches the natural frequency $\omega_1$ of the damped system. Consider the case where the time is sufficient for the transient solution to have decayed to zero.

:::{figure} ../images/lt-21118-3.6.3.png
:label: fig-3-6-3
:enumerator: 3.6.3
:alt: Resonance behavior for the linearly-damped, harmonically driven, linear oscillator.

Resonance behavior for the linearly-damped, harmonically driven, linear oscillator.
:::

[Figure 3.6.3](#fig-3-6-3) shows the amplitude and phase for the *steady-state response* as $\omega$ goes through a resonance as the driving frequency is changed. The steady-states solution of the driven oscillator follows the driving force when $\omega << \omega_0$ in that the phase difference is zero and the amplitude is just $\frac{F_0}{k}$. The response of the system peaks at resonance, while for $\omega >> \omega_0$ the harmonic system is unable to follow the more rapidly oscillating driving force and thus the phase of the induced oscillation is out of phase with the driving force and the amplitude of the oscillation tends to zero.

Note that the resonance frequency for a driven damped oscillator, differs from that for the undriven damped oscillator, and differs from that for the undamped oscillator. The natural frequency for an **undamped harmonic oscillator** is given by

$$
\omega^2_0 = \frac{k}{m} \tag{3.68} \label{eq-3-68}
$$

The transient solution is the same as **damped free oscillations** of a damped oscillator and has a frequency of the system $\omega_1$ given by

$$
\omega^2_1 = \omega^2_0 − \left(\frac{\Gamma}{2}\right)^2 \tag{3.69} \label{eq-3-69}
$$

That is, damping slightly reduces the frequency.

For the **driven oscillator** the maximum value of the steady-state amplitude response is obtained by taking the maximum of the function $x(t)_s$, that is when $\frac{dx_S}{d\omega} = 0$. This occurs at the resonance angular frequency $\omega_R$ where

$$
\omega^2_R = \omega^2_0 − 2 \left(\frac{\Gamma}{2}\right)^2 \tag{3.70} \label{eq-3-70}
$$

No resonance occurs if $\omega^2_0−2 (\frac{\Gamma}{2})^2 < 0$ since then $\omega_R$ is imaginary and the amplitude decreases monotonically with increasing $\omega$. Note that the above three frequencies are identical if $\Gamma = 0$ but they differ when $\Gamma > 0$ with $\omega_R < \omega_1 < \omega_0$.

For the driven oscillator it is customary to define the **quality factor** $Q$ as

$$
Q \equiv \frac{ \omega_R}{\Gamma} \tag{3.71} \label{eq-3-71}
$$

When $Q >> 1$ then one has a narrow high resonance peak. As the damping increases the quality factor decreases leading to a wider and lower peak. The resonance disappears when $Q < 1$.

### Energy absorption

Discussion of energy stored in resonant systems is best described using the steady state solution which is dominant after the transient solution has decayed to zero. Then

$$
x(t)_S = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} [(\omega^2_0 − \omega^2) \cos \omega t + \Gamma \omega \sin \omega t] \tag{3.72} \label{eq-3-72}
$$

This can be rewritten as

$$
x(t)_S = A_{el} \cos \omega t + A_{abs} \sin \omega t \tag{3.73} \label{eq-3-73}
$$

where the **elastic amplitude**

$$
A_{el} = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} (\omega^2_0 − \omega^2) \tag{3.74} \label{eq-3-74}
$$

while the **absorptive amplitude**

$$
A_{abs} = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} \Gamma \omega \tag{3.75} \label{eq-3-75}
$$

:::{figure} ../images/lt-21117-3.6.4.png
:label: fig-3-6-4
:enumerator: 3.6.4
:alt: Elastic (solid) and absorptive (dashed) amplitudes of the steady-state solution for \Gamma = 0.10 \omega_0.

Elastic (solid) and absorptive (dashed) amplitudes of the steady-state solution for $\Gamma = 0.10$ $\omega_0$.
:::

[Figure 3.6.4](#fig-3-6-4) shows the behavior of the absorptive and elastic amplitudes as a function of angular frequency $\omega$. The absorptive amplitude is significant only near resonance whereas the elastic amplitude goes to zero at resonance. Note that the *full width at half maximum of the absorptive amplitude peak equals* $\Gamma$.

The work done by the force $F_0 \cos \omega t$ on the oscillator is

$$
W = \int F dx = \int F \dot{x} dt \tag{3.76} \label{eq-3-76}
$$

Thus the **absorbed power** $P(t)$ is given by

$$
P(t) = \frac{dW}{dt} = F \dot{x} \tag{3.77} \label{eq-3-77}
$$

The steady state response gives a velocity

$$
\dot{x}(t)_S = −\omega A_{el} \sin \omega t + \omega A_{abs} \cos \omega t \tag{3.78} \label{eq-3-78}
$$

Thus the steady-state instantaneous power input is

$$
P(t) = F_0 \cos \omega t [−\omega A_{el} \sin \omega t + \omega A_{abs} \cos \omega t] \tag{3.79} \label{eq-3-79}
$$

The absorptive term steadily absorbs energy while the elastic term oscillates as energy is alternately absorbed or emitted. The time average over one cycle is given by

$$
\langle P \rangle = F_0 \left[ −\omega A_{el} \langle \cos \omega t \sin \omega t \rangle + \omega A_{abs} \left\langle (\cos \omega t)^2 \right\rangle \right] \tag{3.80} \label{eq-3-80}
$$

where $\langle \cos \omega t \sin \omega t \rangle$ and $\langle \cos \omega t^2 \rangle$ are the time average over one cycle. The time averages over one complete cycle for the first term in the bracket is

$$
−\omega A_{el} \langle \cos \omega t \sin \omega t \rangle = 0 \tag{3.81} \label{eq-3-81}
$$

while for the second term

$$
\langle \cos \omega t^2 \rangle = \frac{1}{T} \int^{t_0 + T}_{t_o} \cos \omega t^2 dt = \frac{1}{2} \tag{3.82} \label{eq-3-82}
$$

Thus the time average power input is given by only the absorptive term

$$
\langle P \rangle = \frac{1}{2} F_0\omega A_{abs} = \frac{F^2_0}{2m} \frac{\Gamma \omega^2}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} \tag{3.83} \label{eq-3-83}
$$

This shape of the power curve is a classic Lorentzian shape. Note that the maximum of the average kinetic energy occurs at $\omega_{KE} = \omega_0$ which is different from the peak of the amplitude which occurs at $\omega^2_1 = \omega^2_0 − \left( \frac{\Gamma}{2}\right)^2$. The potential energy is proportional to the amplitude squared, i.e. $x^2_S$ which occurs at the same angular frequency as the amplitude, that is, $\omega^2_{PE} = \omega^2_R = \omega^2_0 − 2 \left(\frac{\Gamma}{2}\right)^2$. The kinetic and potential energies resonate at different angular frequencies as a result of the fact that the driven damped oscillator is not conservative because energy is continually exchanged between the oscillator and the driving force system in addition to the energy dissipation due to the damping.

When $\omega \sim \omega_0 >> \Gamma$, then the power equation simplifies since

$$
(\omega^2_0 − \omega^2) = (\omega_0 + \omega ) (\omega_0 − \omega ) \approx 2\omega_0 (\omega_0 − \omega ) \tag{3.84} \label{eq-3-84}
$$

Therefore

$$
\langle P \rangle \simeq \frac{F^2_0}{8m} \frac{\Gamma}{(\omega_0 − \omega )^2 + \left(\frac{\Gamma}{2}\right)^2} \tag{3.85} \label{eq-3-85}
$$

This is called the Lorentzian or Breit-Wigner shape. The half power points are at a frequency difference from resonance of $\pm \Delta \omega$ where

$$
\Delta \omega = |\omega_0 − \omega | = \pm \frac{\Gamma}{2} \tag{3.86} \label{eq-3-86}
$$

Thus the*full width at half maximum of the Lorentzian curve equals* $\Gamma$. Note that the Lorentzian has a narrower peak but much wider tail relative to a Gaussian shape. At the peak of the absorbed power, the absorptive amplitude can be written as

$$
A_{abs} (\omega = \omega_0) = \frac{F_0}{m} \frac{Q}{\omega^2_0} \tag{3.87} \label{eq-3-87}
$$

That is, the peak amplitude increases with increase in $Q$. This explains the classic comedy scene where the soprano shatters the crystal glass because the highest quality crystal glass has a high $Q$ which leads to a large amplitude oscillation when she sings on resonance.

The mean lifetime $\tau$ of the free linearly-damped harmonic oscillator, that is, the time for the energy of free oscillations to decay to $1/e$ was shown to be related to the damping coefficient $\Gamma$ by

$$
\tau = \frac{1}{\Gamma} \tag{3.88} \label{eq-3-88}
$$

Therefore we have the **classical uncertainty principle for the linearly-damped harmonic oscillator** that the measured full-width at half maximum of the energy resonance curve for forced oscillation and the mean life for decay of the energy of a free linearly-damped oscillator are related by

$$
\tau\Gamma = 1 \tag{3.89} \label{eq-3-89}
$$

This relation is correct only for a linearly-damped harmonic system. Comparable relations between the lifetime and damping width exist for different forms of damping.

One can demonstrate the above line width and decay time relationship using an acoustically driven electric guitar string. It also occurs for the width of the electromagnetic radiation and the lifetime for decay of atomic or nuclear electromagnetic decay. This classical uncertainty principle is exactly the same as the one encountered in quantum physics due to wave-particle duality. In nuclear physics it is difficult to measure the lifetime of states when $\tau < 10^{-13} s$. For shorter lifetimes the value of $\Gamma$ can be determined from the shape of the resonance curve which can be measured directly when the damping is large.

::::{admonition} Example 3.6.1: Harmonically-driven series RLC circuit
:class: example

The harmonically-driven, resonant, series RLC circuit, is encountered frequently in AC circuits. Kirchhoff’s Rules applied to the series RLC circuit lead to the differential equation

$$
L\ddot{q} + R\dot{q} + \frac{q}{C} = V_0 \sin \omega t \nonumber
$$

where $q$ is charge, $L$ is the inductance, $C$ is the capacitance, $R$ is the resistance, and the applied voltage across the circuit is $V (\omega ) = V_0 \sin \omega t$. The linearity of the network allows use of the phasor approach which assumes that the current $I = I_0e^{i \omega t}$, the voltage $V = V_0 e^{i(\omega t+\delta)}$, and the impedance is a complex number $Z = \frac{V_0}{I_0} e^{i \delta}$ where $\delta$ is the phase difference between the voltage and the current. For this circuit the impedance is given by

$$
Z = R + i\left( \omega L − \frac{1}{\omega C} \right) \nonumber
$$

Because of the phases involved in this RLC circuit, at resonance the maximum voltage across the resistor occurs at a frequency of $\omega_R = \omega_0$, across the capacitor the maximum voltage occurs at a frequency $\omega^2_C = \omega^2_0 − \frac{R^2}{2L^2}$, and across the inductor $L$ the maximum voltage occurs at a frequency $\omega^2_L = \frac{\omega^2_0}{1− \frac{R^2}{2L^2}}$, where $\omega^2_0 = \frac{1}{LC}$ is the resonance angular frequency when $R = 0$. Thus these resonance frequencies differ when $R > 0$.

:::{figure} ../images/lt-21120-3.6.5.png
:label: fig-3-6-5
:enumerator: 3.6.5
:alt: Figure
:::
::::

## 3.7: Wave equation

Wave motion is a ubiquitous feature in nature. Mechanical wave motion is manifest by transverse waves on fluid surfaces, longitudinal and transverse seismic waves travelling through the Earth, and vibrations of mechanical structures such as suspended cables. Acoustical wave motion occurs on the stretched strings of the violin, as well as the cavities of wind instruments. Electromagnetic wave motion includes wavelengths ranging from $10^5 \ m$ radiowaves, to $10^{-13} \ m \ \gamma$-rays. Matter waves are a prominent feature of quantum physics. All these manifestations of waves exhibit the same general features of wave motion.

Wave motion occurs for deformable bodies where elastic forces acting between the nearest-neighbor atoms of the body exert time-dependent forces on one another. Chapter $14$ will introduce the collective modes of motion, called the normal modes, of coupled, many-body, linear oscillators which act as independent modes of motion. However, it is useful to introduce wavemotion at this juncture because the equations of wave motion are simple, and wave motion features prominently in several chapters of this book.

Consider a travelling wave in one dimension for a linear system. If the wave is moving, then the wave function $\Psi$ $(x,t)$ describing the shape of the wave, is a function of both $x$ and $t$. The instantaneous amplitude of the wave $\Psi$ $(x,t)$ could correspond to the transverse displacement of a wave on a string, the longitudinal amplitude of a wave on a spring, the pressure of a longitudinal sound wave, the transverse electric or magnetic fields in an electromagnetic wave, a matter wave, etc. If the wave train maintains its shape as it moves, then one can describe the wave train by the function $f(\phi)$ where the coordinate $\phi$ is measured relative to the shape of the wave, that is, it could correspond to the phase of a crest of the wave. Consider that $f(\phi = 0)$ corresponds to a constant phase, e.g. the peak of the travelling pulse, then assuming that the wave travels at a phase velocity $v$ in the $x$ direction and the peak is at $x = 0$ for $t = 0$, then it is at $x = vt$ at time $t$. That is, a point with phase $\phi$ fixed with respect to the waveform shape of the wave profile $f(\phi)$ moves in the $+x$ direction for $\phi = x -vt$ and in $−x$ direction for $\phi = x +vt$.

General wave motion can be described by solutions of a wave equation. The wave equation can be written in terms of the spatial and temporal derivatives of the wave function $\Psi$$(xt)$. Consider the first partial derivatives of $\Psi$$(xt)$ = $f(x \mp vt) = f(\phi)$.

$$
\tag{3.90} \label{eq-3-90} \frac{\partial \Psi}{\partial x} = \frac{\partial \Psi}{\partial \phi}\frac{\partial \phi}{\partial x} = \frac{d \Psi}{d\phi}
$$

and

$$
\tag{3.91} \label{eq-3-91} \frac{\partial \Psi}{\partial t} = \frac{d \Psi}{d\phi}\frac{\partial\phi}{\partial t} = \mp v \frac{d\Psi}{d \phi}
$$

Factoring out $\frac{d \Psi}{d\phi}$ for the first derivatives gives

$$
\tag{3.92} \label{eq-3-92} \frac{\partial \Psi}{\partial t} = \mp v \frac{\partial \Psi}{\partial x}
$$

The sign in this equation depends on the sign of the wave velocity making it not a generally useful formula.

Consider the second derivatives

$$
\tag{3.93} \label{eq-3-93} \frac{\partial^2 \Psi}{\partial x^2} = \frac{d^2 \Psi}{d \phi^2}\frac{\partial \phi}{\partial x} = \frac{d^2 \Psi}{d\phi^2}
$$

and

$$
\tag{3.94} \label{eq-3-94} \frac{\partial^2 \Psi}{\partial t^2} = \frac{d^2 \Psi}{d \phi^2} \frac{\partial \phi}{\partial t} = +v^2 \frac{d^2 \Psi}{d \phi^2}
$$

Factoring out $\frac{d^2 \Psi}{d \phi^2}$ gives

$$
\tag{3.95} \label{eq-3-95} \frac{\partial^2 \Psi}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 \Psi}{\partial t^2}
$$

This *wave equation in one dimension for a linear system* is independent of the sign of the velocity. There are an infinite number of possible shapes of waves both travelling and standing in one dimension, all of these must satisfy this one-dimensional wave equation. The converse is that any function that satisfies this one dimensional wave equation must be a wave in this one dimension.

The *Wave Equation in three dimensions* is

$$
\tag{3.96} \label{eq-3-96} \nabla^2 \Psi \equiv \frac{\partial^2 \Psi}{\partial x^2} + \frac{\partial^2 \Psi}{\partial y^2} + \frac{\partial^2 \Psi}{\partial z^2} = \frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2}
$$

There are an infinite number of possible solutions $\Psi$ to this wave equation, any one of which corresponds to a wave motion with velocity $v$.

The Wave Equation is applicable to all manifestations of wave motion, both transverse and longitudinal, for linear systems. That is, it applies to waves on a string, water waves, seismic waves, sound waves, electromagnetic waves, matter waves, etc. If it can be shown that a wave equation can be derived for any system, discrete or continuous, then this is equivalent to proving the existence of waves of any waveform, frequency, or wavelength travelling with the phase velocity given by the wave equation.[Cra65]

## 3.8: Travelling and standing wave solutions of the wave equation

The wave equation can have both travelling and standing-wave solutions. Consider a one-dimensional travelling wave with velocity $v$ having a specific wavenumber $k \equiv \frac{2\pi}{\lambda}$. Then the travelling wave is best written in terms of the phase of the wave as

$$
\tag{3.97} \label{eq-3-97} \Psi(x,t) = A(k)e^{i\frac{2\pi}{\lambda}(x \mp vt)} = A(k)e^{i(kx \mp \omega t)}
$$

where the wave number $k \equiv \frac{2\pi}{\lambda}$, with $\lambda$ being the wave length, and angular frequency $\omega \equiv kv$. This particular solution satisfies the wave equation and corresponds to a travelling wave with phase velocity $v = \frac{\omega_n}{k_n}$ in the positive or negative direction $x$ depending on whether the sign is negative or positive. Assuming that the superposition principle applies, then the superposition of these two particular solutions of the wave equation can be written as

$$
\tag{3.98} \label{eq-3-98} \Psi(x,t) = A(k)(e^{i (kx - \omega t)} + e^{i(kx + \omega t)}) = A(k)e^{ikx}(e^{- i \omega t} + e^{i \omega t}) = 2A(k)e^{ikx} \cos \omega t
$$

Thus the superposition of two identical single wavelength travelling waves propagating in opposite directions can correspond to a standing wave solution. Note that a standing wave is identical to a stationary normal mode of the system discussed in chapter $14$. This transformation between standing and travelling waves can be reversed, that is, the superposition of two standing waves, i.e. normal modes, can lead to a travelling wave solution of the wave equation. Discussion of waveforms is simplified when using either of the following two limits.

1) The time dependence of the waveform at a given location $x = x_0$ which can be expressed using a Fourier decomposition, appendix $19.9.2$, of the time dependence as a function of angular frequency $\omega = n\omega_0$.

$$
\tag{3.99} \label{eq-3-99}\Psi(x_0,t) = \sum_{n= - \infty}^\infty A_n e^{in(k_0x_0-\omega_0t)} = \sum_{n= - \infty}^\infty B_n (x_0)e^{-in\omega_0t}
$$

2) The spatial dependence of the waveform at a given instant $t = t_0$ which can be expressed using a Fourier decomposition of the spatial dependence as a function of wavenumber $k = nk_0$

$$
\tag{3.100} \label{eq-3-100}\Psi(x,t_0) = \sum_{n= - \infty}^\infty A_n e^{in(k_0x-\omega_1t_0)} = \sum_{n= - \infty}^\infty C_n (t_0)e^{ink_0x}
$$

The above is applicable both to discrete, or continuous linear oscillator systems, e.g. waves on a string. In summary, stationary normal modes of a system are obtained by a superposition of travelling waves travelling in opposite directions, or equivalently, travelling waves can result from a superposition of stationary normal modes.

## 3.9: Waveform Analysis

### Harmonic decomposition

As described in appendix $19.9$, when superposition applies, then a Fourier series decomposition of the form [3.101](#eq-3-101) can be made of any periodic function where

$$
\tag{3.101} \label{eq-3-101} F(t) = \sum_{n=1}^{N} \alpha_n \cos(n\omega_0t + \phi_n )
$$

or the more general Fourier Transform can be made for an aperiodic function where

$$
\tag{3.102} \label{eq-3-102} F(t) = \int \alpha (\omega) \cos(\omega t + \phi(\omega)) dt
$$

Any linear system that is subject to the forcing function $F(t)$ has an output that can be expressed as a linear superposition of the solutions of the individual harmonic components of the forcing function. Fourier analysis of periodic waveforms in terms of harmonic trigonometric functions plays a key role in describing oscillatory motion in classical mechanics and signal processing for linear systems. Fourier’s theorem states that any arbitrary forcing function $F(t)$ can be decomposed into a sum of harmonic terms. As a consequence two equivalent representations can be used to describe signals and waves; the first is in the time domain which describes the time dependence of the signal. The second is in the frequency domain which describes the frequency decomposition of the signal. Fourier analysis relates these equivalent representations.

:::{figure} ../images/lt-21121-3.9.1.png
:label: fig-3-9-1
:enumerator: 3.9.1
:alt: The time and frequency representations of a system exhibiting beats.

The time and frequency representations of a system exhibiting beats.
:::

For example, the superposition of two equal intensity harmonic oscillators in the time domain is given by

$$
\tag{3.103} \label{eq-3-103} y(t) = A\cos(\omega_1t) + A\cos(\omega_2t) \\ = 2A\cos \Bigg [ \Bigg ( \frac{\omega_1 + \omega_2}{2} \Bigg ) t \Bigg] \cos \Bigg [ \Bigg (\frac{\omega_1 - \omega_2}{2} \Bigg ) t \Bigg ]
$$

### The free linearly-damped linear oscillator

The response of the free, linearly-damped, linear oscillator is one of the most frequently encountered waveforms in science and thus it is useful to investigate the Fourier transform of this waveform. The damped waveform for the underdamped case, shown in figure (3.5.1) is given by equation (3.5.12), that is

$$
\begin{align} \tag{3.104} \label{eq-3-104} f(t) & = & Ae^{-\frac{\Gamma}{2}t}\cos(\omega_1t-\delta) && t \geq 0 \\ \tag{3.105} f(t) & = & 0 && t < 0 \end{align}
$$

where $\omega_1^2 = \omega_0^2 - \big ( \frac{\Gamma}{2} \big )^2$ and where $\omega_0$ is the angular frequency of the underdamped system. The Fourier transform is given by

$$
\tag{3.106} \label{eq-3-106} G(\omega) = \frac{\omega_0}{(\omega^2 - \omega_1^2)^2 + (\Gamma \omega)^2} [ (\omega^2 - \omega_1^2) - i \Gamma \omega ]
$$

which is complex and has the famous Lorentz form.

:::{figure} ../images/lt-21122-3.9.2.png
:label: fig-3-9-2
:enumerator: 3.9.2
:alt: The intensity f(t)^2 and Fourier transform |G(w)|^2 of the free linearly-underdamped harmonic oscillator with \omega_0 = 10 and damping \Gamma = 1.

The intensity $f(t)^2$ and Fourier transform $|G(w)|^2$ of the free linearly-underdamped harmonic oscillator with $\omega_0 = 10$ and damping $\Gamma = 1$.
:::

The intensity of the wave gives

$$
|f(t)|^2 = A^2 e^{-\Gamma t} \cos^2 (\omega_1 t - \delta) \tag{3.107} \label{eq-3-107}
$$

$$
|G ( \omega)|^2 = \frac{\omega^2_0}{(\omega^2 - \omega^2_1)^2 + ( \Gamma \omega )^2} \tag{3.108} \label{eq-3-108}
$$

Note that since the average over $2\pi$ of $\cos^2 = \frac{1}{2}$, then the average over the $\cos^2 (\omega_1 t − \delta)$ term gives the intensity $I(t) = \frac{A^2}{2} e^{−\Gamma t}$ which has a mean lifetime for the decay of $\tau = \frac{1}{\Gamma}$. The $|G (\omega )|^2$ distribution has the classic Lorentzian shape, shown in [Figure 3.9.2](#fig-3-9-2), which has a full width at half-maximum, FWHM, equal to $\Gamma$. Note that $G (\omega )$ is complex and thus one also can determine the phase shift $\delta$ which is given by the ratio of the imaginary to real parts of Equation [3.105](#eq-3-104), i.e. $\tan \delta = \frac{\Gamma\omega}{ (\omega^2−\omega^2_1)}$.

The mean lifetime of the exponential decay of the intensity can be determined either by measuring $\tau$ from the time dependence, or measuring the FWHM $\Gamma = \frac{1}{\tau}$ of the Fourier transform $|G (\omega )|^2$. In nuclear and atomic physics excited levels decay by photon emission with the wave form of the free linearly-damped, linear oscillator. Typically the mean lifetime $\tau$ usually can be measured when $\tau \gtrsim 10^{−12} s$ whereas for shorter lifetimes the radiation width $\Gamma$ becomes sufficiently large to be measured. Thus the two experimental approaches are complementary.

### Damped linear oscillator subject to an arbitrary periodic force

Fourier’s theorem states that any arbitrary forcing function $F(t)$ can be decomposed into a sum of harmonic terms. Consider the response of a damped linear oscillator to an arbitrary periodic force.

$$
F(t) = \sum^{N}_{n=0} \alpha_n F_0 ( \omega_n) \cos (\omega_n t + \delta_n) \tag{3.109} \label{eq-3-109}
$$

For each harmonic term $\omega_n$ the response of a linearly-damped linear oscillator to the forcing function $F(t) = F_0 (\omega) \cos ( \omega_n t)$ is given by equation (3.6.18-3.6.20) to be

$$
\begin{align} x(t)_{Total} & = & x(t)_T + x(t)_S \nonumber \\ & = & \frac{F_0 (\omega_n)}{m} \left[ e^{-\frac{\Gamma}{2}t} \cos (\omega_1 t - \delta_n) + \frac{1}{\sqrt{ (\omega^2_0 - \omega^2_n)^2 + (\Gamma \omega_n)^2}} \cos (\omega_n t - \delta_n) \right] \tag{3.110} \label{eq-3-110} \end{align}
$$

The amplitude is obtained by substituting into Equation [3.110](#eq-3-110) the derived values $\frac{F_0 (\omega_n)}{m}$ from the Fourier analysis.

::::{admonition} Example 3.9.1: Vibration isolation
:class: example

Frequently it is desired to isolate instrumentation from the influence of horizontal and vertical external vibrations that exist in its environment. One arrangement to achieve this isolation is to mount a heavy base of mass $m$ on weak springs of spring constant $k$ plus weak damping. The response of this system is given by Equation [3.109](#eq-3-109) which exhibits a resonance at the angular frequency $\omega^2_R = \omega^2_0 − 2 ( \frac{\Gamma}{2})^2$ associated with each resonant frequency $\omega_0$ of the system. For each resonant frequency the system amplifies the vibrational amplitude for angular frequencies close to resonance that is, below $\sqrt{2} \omega_0$, while it attenuates the vibration roughly by a factor of $(\frac{\omega_0}{\omega})^2$ at higher frequencies. To avoid the amplification near the resonance it is necessary to make $\omega_0$ very much smaller than the frequency range of the vibrational spectrum and have a moderately high $Q$ value. This is achieved by use a very heavy base and weak spring constant so that $\omega_0$ is very small. A typical table may have the resonance frequency at 0.5 $Hz$ which is well below typical perturbing vibrational frequencies, and thus the table attenuates the vibration by 99% at 5 $Hz$ and even more attenuation for higher frequency perturbations. This principle is used extensively in design of vibration-isolation tables for optics or microbalance equipment.

:::{figure} ../images/lt-21123-3.9.3.png
:label: fig-3-9-3
:enumerator: 3.9.3
:alt: Seismic isolation of an optical bench.

Seismic isolation of an optical bench.
:::
::::

## 3.10: Signal Processing

It has been shown that the response of the linearly-damped linear oscillator, subject to any arbitrary periodic force, can be calculated using a frequency decomposition, (Fourier analysis), of the force, appendix $19.9$. The response can equally well can be calculated using a time-ordered discrete-time sampling of the pulse shape; that is, the Green’s function approach, appendix $19.9$. The linearly-damped, linear oscillator is the simplest example of a linear system that exhibits both resonance and frequency-dependent response. Typical physical linear systems exhibit far more complicated response functions with multiple resonances and corresponding frequency response. For example, an automobile suspension system involves four wheels and associated springs plus dampers allowing the car to rock sideways, or forward and backward, in addition to the updown motion, when subject to the forces produced by a rough road. Similarly a suspension bridge or aircraft wing can twist as well as bend due to air turbulence, or a building can undergo complicated oscillations due to seismic waves. An acoustic system exhibits similar complexity. Signal analysis and signal processing is of pivotal importance to elucidating the response of complicated linear systems to complicated periodic forcing functions. This is used extensively in engineering, acoustics, and science.

The response of a low-pass filter, such as an R-C circuit or a coaxial cable, to a input square wave, shown in [Figure 3.10.1](#fig-3-10-1), provides a simple example of the relative advantages of using the complementary Fourier analysis in the frequency domain, or the Green’s discrete-function analysis in the time domain. The response of a repetitive square-wave input signal is shown in the time domain and the Fourier transform to the frequency domain. The middle curves show the time dependence for the response of the low-pass filter to an impulse $I(t)$ and the Fourier transform $H(\omega)$. The output of the low-pass filter can be calculated by folding the input square wave and impulse time dependence in the time domain as shown on the left or by folding of their Fourier transforms shown on the right. Working in the frequency domain the response of linear mechanical systems, such as an automobile suspension or a musical instrument, as well as linear electronic signal processing systems such as amplifiers, loudspeakers and microphones, can be treated as black boxes having a certain **transfer function** $H(\omega, \phi)$ describing the gain and phase shift versus frequency. That is, the output wave frequency decomposition is

$$
G(\omega)_{output} = H(\omega , \phi) \cdot G(\omega)_{input} \tag{3.111} \label{eq-3-111}
$$

Working in the time domain, the low-pass system has an **impulse response** $I(t) = e^{-\frac{t}{\tau}}$, which is the Fourier transform of the transfer function $H(\omega , \phi )$. In the time domain

$$
y(t)_{output} = \int^{\infty}_{-\infty} x(\tau ) \cdot I(t - \tau) d \tau \tag{3.112} \label{eq-3-112}
$$

This is shown schematically in [Figure 3.10.1](#fig-3-10-1). The Fourier transformation connects the three quantities in the time domain with the corresponding three in the frequency domain. For example, the impulse response of the low-pass filter has a fall time of $\tau$ which is related by a Fourier transform to the width of the transfer function. Thus the time and frequency domain approaches are closely related and give the same result for the output signal for the low-pass filter to the applied square-wave input signal. The result is that the higher-frequency components are attenuated leading to slow rise and fall times in the time domain.

Analog signal processing and Fourier analysis were the primary tools to analyze and process all forms of periodic motion during the 20$^{th}$ century. For example, musical instruments, mechanical systems, electronic circuits, all employed resonant systems to enhance the desired frequencies and suppress the undesirable frequencies and the signals were observed using analog oscilloscopes. The remarkable development of computing has enabled use of digital signal processing leading to a revolution in signal processing that has had a profound impact on both science and engineering. For example, the digital oscilloscope, which can sample at frequencies above $10^9$ $Hz$ has replaced the analog oscilloscope because it allows sophisticated analysis of each individual signal that was not possible using analog signal processing. For example, the analog approach in nuclear physics involved tiny analog electric signals, produced by many individual radiation detectors, that were transmitted hundreds of meters via carefully shielded and expensive coaxial cables to the data room where the signals were amplified and signal processed using analog filters to maximize the signal to noise in order to separate the signal from the background noise. Stray electromagnetic radiation picked up via the cables significantly degraded the signals. The performance and limitations of the analog electronics severely restricted the pulse processing capabilities. Digital signal processing has rapidly replaced analog signal processing. Analog to digital detector circuits are built directly into the electronics for each individual detector so that only digital information needs to be transmitted from each detector to the analysis computers. Computer processing provides unlimited and flexible processing capabilities for the digital signals greatly enhancing the response and sensitivity of our detector systems. Common examples of digital signal processing are digital CD and DVD disks.

:::{figure} ../images/lt-21124-3.10.1.png
:label: fig-3-10-1
:enumerator: 3.10.1
:alt: Response of an *RC* electrical circuit to an input square wave. The upper row shows the time and the exponential-form frequency representations of the square-wave input signal. The middle row gives the impulse response, and corresponding transfer function for the *RC* circuit. The bottom row show…

Response of an *RC* electrical circuit to an input square wave. The upper row shows the time and the exponential-form frequency representations of the square-wave input signal. The middle row gives the impulse response, and corresponding transfer function for the *RC* circuit. The bottom row shows the corresponding output properties in both the time and frequency domains
:::

## 3.11: Wave Propagation

Wave motion typically involves a packet of waves encompassing a finite number of wave cycles. Information in a wave only can be transmitted by starting, stopping, or modulating the amplitude of a wave train, which is equivalent to forming a wave packet. For example, a musician will play a note for a finite time, and this wave train propagates out as a wave packet of finite length. You have no information as to the frequency and amplitude of the sound prior to the wave packet reaching you, or after the wave packet has passed you. The velocity of the wavelets contained within the wave packet is called the **phase velocity**. For a dispersive system the phase velocity of the wavelets contained within the wave packet is frequency dependent and the shape of the wave packet travels at the **group velocity** which usually differs from the phase velocity. If the shape of the wave packet is time dependent, then neither the phase velocity, which is the velocity of the wavelets, nor the group velocity, which is the velocity of an instantaneous point fixed to the shape of the wave packet envelope, represent the actual velocity of the overall wavepacket.

A third wavepacket velocity, the **signal velocity**, is defined to be the velocity of the leading edge of the energy distribution, and corresponding information content, of the wave packet. For most linear systems the shape of the wave packet is not time dependent and then the group and signal velocities are identical. However, the group and signal velocities can be very different for non-linear systems as discussed in chapter $4.7$. Note that even when the phase velocity of the waves within the wave packet travels faster than the group velocity of the shape, or the signal velocity of the energy content of the envelope of the wave packet, the information contained in a wave packet is only manifest when the wave packet envelope reaches the detector and this energy and information travel at the signal velocity.

The modern ideas of wave propagation, including Hamilton’s concept of group velocity, were developed by Lord Rayleigh when applied to the theory of sound[Ray1887]. The concept of phase, group, and signal velocities played a major role in discussion of electromagnetic waves as well as de Broglie’s development of the concept of wave-particle duality and the development of wave mechanics by Schrödinger.

### Phase, group, and signal velocities of wave packets

The concepts of wave packets, as well as their phase, group, and signal velocities, are of considerable importance for propagation of information and other manifestations of wave motion in science and engineering which warrants further discussion at this juncture.

Consider a particular $k, \omega$, component of a one-dimensional wave,

$$
q(x,t) = Ee^{i(kx\pm \omega t)} \tag{3.113} \label{eq-3-113}
$$

The argument of the exponential is called the **phase** $\phi$ of the wave where

$$
\phi \equiv kx - \omega t \tag{3.114} \label{eq-3-114}
$$

If we move along the $x$ axis at a velocity such that the phase is constant then we perceive a stationary wave. The velocity of this wave is called the **phase velocity**. To ensure constant phase we require that $\phi$ is constant or, assuming real $k$ and $\omega$

$$
\omega dt = k dx \tag{3.115} \label{eq-3-115}
$$

Therefore the **phase velocity** is defined to be

$$
v_{phase} = \frac{\omega}{k} \tag{3.116} \label{eq-3-116}
$$

The velocity we have used so far is just the phase velocity of the individual wavelets at the carrier frequency. If $k$ or $\omega$ are complex then one must take the real parts to ensure that the velocity is real.

If the phase velocity of a wave is dependent on the wavelength, that is, $v_{phase} (k)$, then the system is said to be dispersive in that the wave is dispersed according the wavelength. The simplest illustration of dispersion is the refraction of light in glass prism which leads to dispersion of the light into the spectrum of wavelengths. Dispersion leads to development of wave packets that travel at group and signal velocities that usually differ from the phase velocity. To illustrate this consider two equal amplitude travelling waves having slightly different wave number $k$ and angular frequency $\omega$. Superposition of these waves gives

$$
\begin{align} q(x, t) & = A ( e^{i[k x-\omega t]} + e^{i[(k+\Delta k) x-(\omega+\Delta \omega) t]} ) \nonumber \\ & = A e^{i [ ( k+\frac{\Delta k}{2} ) x- ( \omega+\frac{\Delta w}{2} ) t ]} \cdot \{e^{-i [\frac{\Delta k}{2} x-\frac{\Delta \omega}{2} t ]} + e^{i [\frac{\Delta k}{2} x-\frac{\Delta \omega}{2} t ]} \} \nonumber \\ & = 2 A e^{i [ ( k+\frac{\Delta k}{2} ) x- ( \omega+\frac{\Delta \omega}{2} ) t ]} \cos [\frac{\Delta k}{2} x-\frac{\Delta \omega}{2} t ] \end{align} \tag{3.117} \label{eq-3-117}
$$

This corresponds to a wave with the average carrier frequency modulated by the cosine term which has a wavenumber of $\frac{\Delta k}{2}$ and angular frequency $\frac{\Delta \omega}{2}$, that is, this is the usual example of beats. The cosine term modulates the average wave producing wave packets as shown in figure (3.9.1). The velocity of these wave packets is called the **group velocity** given by requiring that the phase of the modulating term is constant, that is

$$
\frac{\Delta k}{2} dx = \frac{\Delta \omega}{2} dt \tag{3.118} \label{eq-3-118}
$$

Thus the **group velocity** is given by

$$
v_{group} = \frac{dx}{dt} = \frac{\Delta \omega}{ \Delta k} \tag{3.119} \label{eq-3-119}
$$

If dispersion is present then the group velocity $v_{group} = \frac{\Delta \omega}{\Delta k}$ does not equal the phase velocity $v_{phase} = \frac{ \omega}{k}$.

Expanding the above example to superposition of $n$ waves gives

$$
q(x,t) = \sum^{n}_{r = 1} A_r e^{i ( k_r x \pm \omega_r t)} \tag{3.120} \label{eq-3-120}
$$

In the event that $n \rightarrow \infty$ and the frequencies are continuously distributed, then the summation is replaced by an integral

$$
q(x,t) = \int^{\infty}_{-\infty} A(k) e^{i(kx \pm \omega t)} dk \tag{3.121} \label{eq-3-121}
$$

where the factor $A (k)$ represents the distribution amplitudes of the component waves, that is the spectral decomposition of the wave. This is the usual Fourier decomposition of the spatial distribution of the wave.

Consider an extension of the linear superposition of two waves to a well defined wave packet where the amplitude is nonzero only for a small range of wavenumbers $k_0 \pm \Delta k$.

$$
q(x,t) = \int^{k_0 + \Delta k}_{k_0−\Delta k} A(k) e^{i(kx - \omega t)} dk \tag{3.122} \label{eq-3-122}
$$

This functional shape is called a wave packet which only has meaning if $\Delta k << k_0$. The angular frequency can be expressed by making a Taylor expansion around $k_0$

$$
\omega (k) = \omega (k_0) + \left(\frac{d \omega}{dk} \right)_{k_0} (k − k_0) + \dots \tag{3.123} \label{eq-3-123}
$$

For a linear system the phase then reduces to

$$
kx − \omega t = (k_0 x − \omega_0 t) + (k − k_0) x − \left( \frac{d\omega}{dk}\right)_{k_0} (k - k_0) t \tag{3.124} \label{eq-3-124}
$$

The summation of terms in the exponent given by [3.125](#eq-3-125) leads to the amplitude [3.123](#eq-3-123) having the form of a product where the integral becomes

$$
q(x,t) = e^{i(k_0 x - \omega_0 t)} \int^{k_0+\Delta k}_{k_0 − \Delta k} A(k) e^{i(k - k_0)[x-(\frac{d\omega}{dk})_{k_0} t]} dk \tag{3.125} \label{eq-3-125}
$$

The integral term modulates the $e^{i(k_0 x - \omega_0 t)}$ first term.

The group velocity is defined to be that for which the phase of the exponential term in the integral is constant. Thus

$$
v_{group} = \left(\frac{d\omega}{dk}\right)_{k_0} \tag{3.126} \label{eq-3-126}
$$

Since $\omega = kv_{phase}$ then

$$
v_{group} = v_{phase} + k\frac{\partial v_{phase}}{\partial k} \tag{3.127} \label{eq-3-127}
$$

For non-dispersive systems the phase velocity is independent of the wave number $k$ or angular frequency $\omega$ and thus $v_{group} = v_{phase}$. The case discussed earlier, equation (3.9.3), for beating of two waves gives the same relation in the limit that $\Delta \omega$ and $\Delta k$ are infinitesimal.

The group velocity of a wave packet is of physical significance for dispersive media where $v_{group} = (\frac{d\omega}{dk})_{k_0} \neq \frac{\omega}{k} = v_{phase}$. Every wave train has a finite extent and thus we usually observe the motion of a group of waves rather than the wavelets moving within the wave packet. In general, for non-linear dispersive systems the derivative $\frac{\partial v_{phase}}{\partial k}$ can be either positive or negative and thus in principle the group velocity can either be greater than, or less than, the phase velocity. Moreover, if the group velocity is frequency dependent, that is, when group velocity dispersion occurs, then the overall shape of the wave packet is time dependent and thus the speed of a specific relative location defined by the shape of the envelope of the wave packet does not represent the signal velocity of the wave packet. Brillouin showed that the distribution of the energy, and corresponding information content, in any wave packet travels at the signal velocity which can be different from the group velocity if the shape of the envelope of the wave packet is time dependent. For electromagnetic waves one has the possibility that the group velocity $v_{group} > v_{phase} = c$. In 1914 Brillouin[Bri14][Bri60] showed that the signal velocity of electromagnetic waves, defined by the leading edge of the time-dependent envelope of the wave packet, never exceeds $c$ even though the group velocity corresponding to the velocity of the instantaneous shape of the wave packet may exceed $c$. Thus, there is no violation of Einstein’s fundamental principle of relativity that the velocity of an electromagnetic wave cannot exceed $c$.

::::{admonition} Example 3.11.1: Water waves breaking on a beach
:class: example

The concepts of phase and group velocity are illustrated by the example of water waves moving at velocity $v$ incident upon a straight beach at an angle $\alpha$ to the shoreline. Consider that the wavepacket comprises many wavelengths of wavelength $\lambda$. During the time it takes the wave to travel a distance $\lambda$, the point where the crest of one wave breaks on the beach travels a distance $\frac{\lambda}{\cos \alpha}$ along beach. Thus the phase velocity of the crest of the one wavelet in the wave packet is

$$
v_{phase} = \frac{v}{\cos \alpha} \nonumber
$$

The velocity of the wave packet along the beach equals

$$
v_{group} = v \cos \alpha \nonumber
$$

Note that for the wave moving parallel to the beach $\alpha = 0$ and $v_{phase} = v_{group} = v$. However, for $\alpha = \frac{\pi}{2} v_{phase} \rightarrow \infty$ and $v_{group} \rightarrow 0$. In general for waves breaking on the beach

$$
v_{phase}v_{group} = v^2 \nonumber
$$

The same behavior is exhibited by surface waves bouncing off the sides of the Erie canal, sound waves in a trombone, and electromagnetic waves transmitted down a rectangular wave guide. In the latter case the phase velocity exceeds the velocity of light $c$ in apparent violation of Einstein’s theory of relativity. However, the information travels at the signal velocity which is less than $c$.
::::

::::{admonition} Example 3.11.2: Surface waves for deep water
:class: example

In the "Theory of Sound" Rayleigh discusses the example of surface waves for water where he derives a dispersion relation for the phase velocity $v_{phase}$ and wavenumber $k$ which are related to the density $\rho$, depth $l$, gravity $g$, and surface tension $T$, by

$$
\omega^2 = gk + \frac{Tk^3}{\rho} \tanh (kl) \nonumber
$$

For deep water where the wavelength is short compared with the depth, that is $kl >> 1$, then $\tanh (kl) \rightarrow 1$ and the dispersion relation is given approximately by

$$
\omega^2 = gk + \frac{Tk^3}{\rho} \nonumber
$$

For long surface waves for deep water, that is, small $k$, then the gravitational first term in the dispersion relation dominates and the group velocity is given by

$$
v_{group} = \left( \frac{d\omega}{dk} \right) = \frac{1}{2} \sqrt{\frac{g}{k}} = \frac{1}{2} \frac{\omega}{k} = \frac{ v_{phase}}{2} \nonumber
$$

That is, the group velocity is half of the phase velocity. Here the wavelets are building at the back of the wave packet, progress through the wave packet and dissipate at the front. This can be demonstrated by dropping a pebble into a calm lake. It will be seen that the surface disturbance comprises a wave packet moving outwards at the group velocity with the individual waves within the wave packet expanding at twice the group velocity of the wavepacket, that is, they appear at the inner radius of the wave packet and disappear at the outer radius of the wave packet.

For small wavelength ripples, where $k$ is large, then the surface tension term dominates and the dispersion relation is approximately given by

$$
\omega^2 \simeq \frac{Tk^3}{\rho} \nonumber
$$

leading to a group velocity of

$$
v_{group} = \left( \frac{d\omega}{dk}\right) = \frac{3}{2} v_{phase} \nonumber
$$

Here the group velocity exceeds the phase velocity and wavelets are building at the front of the wave packet and dissipate at the back. Note that for this linear system the Brillouin signal velocity equals the group velocity for both gravity and surface tension waves for deep water.
::::

::::{admonition} Example 3.11.3: Electromagnetic waves in ionosphere
:class: example

The response to radio waves of the free electron plasma in the ionosphere provides an excellent example that involves cut-off frequency, complex wavenumber $k$, as well as the phase, group, and signal velocities.

Maxwell’s equations give the most general wave equation for electromagnetic waves to be

$$
\nabla^2 \mathbf{E} − \varepsilon \mu \frac{ \partial^2\mathbf{E}}{\partial t^2} = \mu \frac{ \partial \mathbf{j}_{free}}{\partial t} + \nabla \cdot \left(\frac{\rho_{free}}{\varepsilon} \right) \nonumber
$$

$$
\nabla^2\mathbf{H} − \mu \varepsilon \frac{ \partial^2 \mathbf{H}}{\partial t^2} = −\nabla \times \mathbf{j}_{free} \nonumber
$$

where $\rho_{free}$ and $\mathbf{j}_{free}$ are the unbound charge and current densities. The effect of the bound charges and currents are absorbed into $\varepsilon$ and $\mu$. Ohm’s Law can be written in terms of the electrical conductivity $\sigma$ which is a constant

$$
\mathbf{j} = \sigma \mathbf{E} \nonumber
$$

Assuming Ohm’s Law plus assuming $\rho_{free} = 0$, in the plasma gives the relations

$$
\nabla^2 \mathbf{E} − \varepsilon \mu \frac{\partial^2\mathbf{E}}{\partial t^2} − \sigma \mu \frac{\partial \mathbf{E}}{\partial t} = 0 \nonumber
$$

$$
\nabla^2 \mathbf{H} − \mu \varepsilon \frac{\partial^2 \mathbf{H}}{\partial t^2} − \sigma \mu \frac{\partial \mathbf{H}}{\partial t} = 0 \nonumber
$$

The third term in both of these wave equations is a damping term that leads to a damped solution of an electromagnetic wave in a good conductor.

The solution of these damped wave equations can be solved by considering an incident wave

$$
\mathbf{E} = E_o \mathbf{\hat{x}}e^{i(\omega t− kz)} \nonumber
$$

Substituting for $\mathbf{E}$ in the first damped wave equation gives

$$
−k^2 + \omega^2 \varepsilon \mu − i \omega \sigma \mu = 0 \nonumber
$$

That is

$$
k^2 = \omega^2 \varepsilon \mu \left[ 1 − \frac{i\sigma}{\omega \varepsilon} \right] \nonumber
$$

In general $k$ is complex, that is, it has real $k_R$ and imaginary $k_1$ parts that lead to a solution of the form

$$
\mathbf{E} = E_o e^{-k_I z} e^{i(\omega t - k_R z)} \nonumber
$$

The first exponential term is an exponential damping term while the second exponential term is the oscillating term.

Consider that the plasma involves the motion of a bound damped electron, of charge $q$ of mass $m$, bound in a one dimensional atom or lattice subject to an oscillatory electric field of frequency $\omega$. Assume that the electromagnetic wave is travelling in the $\hat{z}$ direction with the transverse electric field in the $\hat{x}$ direction. The equation of motion of an electron can be written as

$$
\mathbf{\ddot{x}} + \Gamma \mathbf{\dot{x}} + \omega^2_0 x = \mathbf{\hat{x}} q E_0 e^{i(\omega t − kz)} \nonumber
$$

where $\Gamma$ is the damping factor. The instantaneous displacement of the oscillating charge equals

$$
\mathbf{x} = \frac{q}{m} \frac{1}{(\omega^2_0 − \omega^2) + i\Gamma \omega} \mathbf{\hat{x}} E_0 e^{i(\omega t − kz)} \nonumber
$$

and the velocity is

$$
\mathbf{\dot{x}} = \frac{q}{m} \frac{i \omega}{(\omega^2_0 − \omega^2) + i\Gamma \omega} \mathbf{\hat{x}} E_0 e^{i(\omega t − kz)} \nonumber
$$

Thus the instantaneous current density is given by

$$
\mathbf{j} = Nq\mathbf{\dot{x}} = \frac{Nq^2}{m} \frac{i \omega}{(\omega^2_0 − \omega^2) + i\Gamma \omega} \mathbf{\hat{x}} E_0 e^{i(\omega t − kz)} \nonumber
$$

therefore the electrical conductivity is given by

$$
\sigma = \frac{Nq^2}{m} \frac{i \omega}{(\omega^2_0 − \omega^2) + i\Gamma \omega} \nonumber
$$

Let us consider only unbound charges in the plasma, that is let $\omega_0 = 0$. Then the conductivity is given by

$$
\sigma = \frac{Nq^2}{m} \frac{i\omega}{i\Gamma \omega - \omega^2} \nonumber
$$

For a low density ionized plasma $\omega >> \Gamma$ thus the conductivity is given approximately by

$$
\sigma \approx −i \frac{Nq^2}{m\omega} \nonumber
$$

Since $\sigma$ is pure imaginary, then $\mathbf{j}$ and $\mathbf{E}$ have a phase difference of $\frac{\pi}{2}$ which implies that the average of the Joule heating over a complete period is $\langle \mathbf{j} \cdot \mathbf{E} \rangle = 0$. Thus there is no energy loss due to Joule heating implying that the electromagnetic energy is conserved.

Substitution of $\sigma$ into the relation for $k^2$

$$
k^2 = \omega^2 \varepsilon \mu \left[ 1 − \frac{i\sigma}{\omega \varepsilon} \right] = \omega^2 \varepsilon \mu \left[ 1 − \frac{Nq^2}{ \varepsilon m\omega^2} \right] \nonumber
$$

Define the Plasma oscillation frequency $\omega_P$ to be

$$
\omega_P \equiv \sqrt{\frac{Nq^2}{\varepsilon m}} \nonumber
$$

then $k^2$ can be written as

$$
k^2 = \omega^2 \varepsilon \mu \left[ 1 − \left(\frac{\omega_P}{\omega}\right)^2 \right] \tag{$\alpha$}
$$

For a low density plasma the dielectric constant $\kappa_E \simeq 1$ and the relative permeability $\kappa_B \simeq 1$ and thus $\varepsilon = \kappa_E \varepsilon_0 \simeq \varepsilon_0$ and $\mu = \kappa_B \mu_0 \simeq \mu_0$. The velocity of light in vacuum $c = \frac{1}{\sqrt{\varepsilon_0\mu_0}}$. Thus for low density equation $\alpha$ can be written as

$$
\omega^2 = \omega^2_p + c^2k^2 \tag{$\beta$}
$$

Differentiation of equation $\beta$ with respect to $k$ gives $2\omega \frac{d\omega}{dk} = 2c^2 k$. That is, $v_{phase}v_{group} = c^2$ and the phase velocity is

$$
v_{phase} = \sqrt{c^2 + \frac{\omega^2_p}{k^2}} \nonumber
$$

There are three cases to consider.

1) $\omega > \omega_P$: For this case $\left[ 1 − ( \frac{\omega_P}{\omega})^2\right] > 1$ and thus $k$ is a pure real number. Therefore the electromagnetic wave is transmitted with a phase velocity that exceeds $c$ while the group velocity is less than $c$.

2) $\omega < \omega_P$: For this case $\left[ 1 − ( \frac{\omega_P}{\omega})^2\right] < 1$ and thus $k$ is a pure imaginary number. Therefore the electromagnetic wave is not transmitted and in the ionosphere it is attenuated rapidly as $e^{−( \frac{\omega_P}{c})z}$. However, since there are no Joule heating losses then the electromagnetic wave must be complete reflected. Thus the Plasma oscillation frequency serves as a cut-off frequency. For this example the signal and group velocities are identical.

For the ionosphere $N = 10^{−11}$ electrons/$m^3$, which corresponds to a Plasma oscillation frequency of $v = \omega_P / 2\pi = 3$ $MHz$. Thus electromagnetic waves in the AM waveband ( < 1.6 $MHz$) are totally reflected by the ionosphere and bounce repeatedly around the Earth, whereas for VHF frequencies above 3 $MHz$, the waves are transmitted and refracted passing through the atmosphere. Thus light is transmitted by the ionosphere. By contrast, for a good conductor like silver, the Plasma oscillation frequency is around $10^{16}$ $Hz$ which is in the far ultraviolet part of the spectrum. Thus, all lower frequencies, such as light, are totally reflected by such a good conductor, whereas X-rays have frequencies above the Plasma oscillation frequency and are transmitted.
::::

### Fourier transform of wave packets

The relation between the time distribution and the corresponding frequency distribution, or equivalently, the spatial distribution and the corresponding wave-number distribution, are of considerable importance in discussion of wave packets and signal processing. It directly relates to the uncertainty principle that is a characteristic of all forms of wave motion. The relation between the time and corresponding frequency distribution is given via the Fourier transform discussed in appendix $19.9$. The following are two examples of the Fourier transforms of typical but rather different wavepacket shapes that are encountered frequently in science and engineering.

::::{admonition} Example 3.11.4: Fourier transform of a Gaussian wave packet
:class: example

Assuming that the amplitude of the wave is a Gaussian wave packet shown in the adjacent figure where

$$
G (\omega ) = ce^{− \frac{(\omega −\omega_0)^2}{ 2\sigma^2_{\omega}} }\nonumber
$$

This leads to the Fourier transform

$$
f(t) = c \sqrt{2\pi} \sigma_{\omega} e^{− \frac{\sigma^2_{\omega} t^2}{2}} \cos (\omega_0 t) \nonumber
$$

Note that the wavepacket has a standard deviation for the amplitude of the wavepacket of $\sigma_t = \frac{1}{\sigma_{\omega}}$, that is $\sigma_t \cdot \sigma_{\omega} = 1$. The Gaussian wavepacket results in the minimum product of the standard deviations of the frequency and time representations for a wavepacket. This has profound importance for all wave phenomena, and especially to quantum mechanics. Because matter exhibits wave-like behavior, the above property of wave packet leads to Heisenberg’s Uncertainty Principle. For signal processing, it shows that if you truncate a wavepacket you will broaden the frequency distribution.

:::{figure} ../images/lt-21125-3.11.1.png
:label: fig-3-11-1
:enumerator: 3.11.1
:alt: Fourier transform of a Gaussian frequency distribution.

Fourier transform of a Gaussian frequency distribution.
:::
::::

::::{admonition} Example 3.11.5: Fourier transform of a rectangular wave packet
:class: example

Assume unity amplitude of the frequency distribution between $\omega_0 − \Delta \omega \leq \omega \leq \omega_0 + \Delta \omega$, that is, a single isolated square pulse of width $\tau$ that is described by the rectangular function $\prod$ defined as

$$
\prod (\omega ) = \begin{cases} 1 && |\omega − \omega_0| < \Delta \omega \\ 0 && |\omega − \omega_0| > \Delta \omega \end{cases} \nonumber
$$

Then the Fourier transform us given by

$$
f(t) = \left[\frac{\sin \Delta \omega t}{\Delta \omega t} \right] \cos \omega_0 t \nonumber
$$

That is, the transform of a rectangular wavepacket gives a cosine wave modulated by an unnormalized sinc function which is a nice example of a simple wave packet. That is, on the right hand side we have a wavepacket $\Delta t = \pm \frac{2\pi}{\Delta \omega}$ wide. Note that the product of the two measures of the widths $\Delta \omega \cdot \Delta t = \pm \pi$. Example $I.2$ considers a rectangular pulse of unity amplitude between $−\frac{\pi}{2} \leq t \leq \frac{\pi}{2}$ which resulted in a Fourier transform $G (\omega ) = \tau \left( \frac{\sin \frac{\omega \tau}{2}}{\frac{\omega \tau}{2}}\right)$. That is, for a pulse of width $\Delta t = \pm \frac{\tau}{2}$ the frequency envelope has the first zero at $\Delta \omega = \pm \frac{\pi}{\tau}$. Note that this is the complementary system to the one considered here which has $\Delta \omega \cdot \Delta t = \pm \pi$ illustrating the symmetry of the Fourier transform and its inverse.
::::

### Wave-packet Uncertainty Principle

The Uncertainty Principle states that for all types of wave motion there is a minimum product of the uncertainty in the width of a wave packet and the distribution width of the frequency decomposition of the wave packet. This was illustrated by the Fourier transforms of wave packets discussed above where it was shown the product of the widths is minimized for a Gaussian-shaped wave packet. The Uncertainty Principle implies that to make a precise measurement of the frequency of a sinusoidal wave requires that the wave packet be infinitely long. If the length of the wave packet is reduced then the frequency distribution broadens. Then the crucial aspect needed for this discussion, is that, for the *amplitudes* of any wavepacket, the *standard deviations* $\sigma (t) = \sqrt{ \langle t^2 \rangle - \langle t \rangle^2}$ characterizing the width of the spectral distribution in the angular frequency domain, $\sigma_A (\omega )$, and the width in time $\sigma_A (t)$ are related:

$$
\sigma_A (t) \cdot \sigma_A (\omega ) \geqslant 1 \tag{Relation between amplitude uncertainties.}
$$

This product of the *standard deviations equals unity only for the special case of Gaussian-shaped spectral distributions, and is greater than unity for all other shaped spectral distributions.*

The *intensity* of the wave is the square of the amplitude leading to standard deviation widths for a Gaussian distribution where $\sigma_I (t)^2 = \frac{1}{2} \sigma_A (t)^2$, that is, $\sigma_I (t) = \frac{\sigma_A (t)}{\sqrt{2}}$. Thus the standard deviations for the spectral distribution and width of the intensity of the wavepacket are related by:

$$
\sigma_I (t) \cdot \sigma_I (\omega ) \geqslant \frac{1}{2} \tag{Uncertainty principle for frequency-time intensities}
$$

This states that the uncertainties with which you can simultaneously measure the time and frequency for the intensity of a given wavepacket are related. If you try to measure the frequency within a short time interval $\sigma_I (t)$ then the uncertainty in the frequency measurement $\sigma_I (\omega ) \geqslant \frac{1}{2\sigma_I (t)}$. Accurate measurement of the frequency requires measurement times that encompass many cycles of oscillation, that is, a long wavepacket.

Exactly the same relations exist between the spectral distribution as a function of wavenumber $k_x$ and the spatial dependence of a wave $x$ which are conjugate representations. Thus the spectral distribution plotted versus $k_x$ is directly related to the amplitude as a function of position $x$; the spectral distribution versus $k_y$ is related to the amplitude as a function of $y$; and the $k_z$ spectral distribution is related to the spatial dependence on $z$. Following the same arguments discussed above, the standard deviation, $\sigma_I (k_x)$ characterizing the width of the *spectral intensity* distribution of $k_x$, and the standard deviation $\sigma_I (x)$, characterizing the spatial width of the wave packet intensity as a function of $x$, are related by the Uncertainty Principle for position-wavenumber. Thus in summary the uncertainty principle for the intensity of wave motion is,

$$
\sigma_I (t) \cdot \sigma_I (\omega ) \geqslant \frac{1}{2} \tag{3.128} \label{eq-3-128} \\ \sigma_I (x) \cdot \sigma_I (k_x) \geqslant \frac{1}{2} \quad \sigma_I (y) \cdot \sigma_I (k_y) \geqslant \frac{1}{2} \quad \sigma_I (z) \cdot \sigma_I (k_z) \geqslant \frac{1}{2}
$$

This *applies to all forms of wave motion*, be they, sound waves, water waves, electromagnetic waves, or matter waves.

As discussed in chapter $18$, the transition to quantum mechanics involves relating the matter-wave properties to the energy and momentum of the corresponding particle. That is, in the case of matter waves, multiplying both sides of Equation [3.128](#eq-3-128) by $\hbar$ and using the de Broglie relations gives that the particle energy is related to the angular frequency by $E = \hbar \omega$ and the particle momentum is related to the wavenumber, that is $\mathbf{p} = \hbar \mathbf{k}$. These lead to the **Heisenberg Uncertainty Principle**:

$$
\sigma_I (t) \cdot \sigma_I (E) \geqslant \frac{\hbar}{2} \tag{3.129} \label{eq-3-129} \\ \sigma_I (x) \cdot \sigma_I (p_x) \geqslant \frac{\hbar}{2} \quad \sigma_I (y) \cdot \sigma_I (p_y) \geqslant \frac{\hbar}{2} \quad \sigma_I (z) \cdot \sigma_I (p_z) \geqslant \frac{\hbar}{2}
$$

This uncertainty principle applies equally to the wavefunction of the electron in the hydrogen atom, proton in a nucleus, as well as to a wavepacket describing a particle wave moving along some trajectory. Thus, this implies that, for a particle of given momentum, the wavefunction is spread out spatially. Planck’s constant $\hbar = 1.05410^{−34} J \cdot s = 6.58210^{−16} eV \cdot s$ is extremely small compared with energies and times encountered in normal life, and thus the effects due to the Uncertainty Principle are not manifest for macroscopic dimensions.

Confinement of a particle, of mass $m$, within $\pm \sigma (x)$ of a fixed location implies that there is a corresponding uncertainty in the momentum

$$
\sigma (p_x) \geq \frac{\hbar}{2\sigma (x)} \tag{3.130} \label{eq-3-130}
$$

Now the variance in momentum $\mathbf{p}$ is given by the difference in the average of the square $\left\langle( \mathbf{p} \cdot \mathbf{p})^2 \right\rangle$, and the square of the average of $\langle \mathbf{p} \rangle^2$. That is

$$
\sigma (\mathbf{p})^2 = \left\langle (\mathbf{p} \cdot \mathbf{p})^2 \right\rangle − \langle \mathbf{p} \rangle^2 \tag{3.131} \label{eq-3-131}
$$

Assuming a fixed average location implies that $\langle \mathbf{p} \rangle = 0$, then

$$
\left\langle ( \mathbf{p} \cdot \mathbf{p})^2 \right\rangle = \sigma (p)^2 \geq \left( \frac{\hbar}{2\sigma (r)} \right)^2 \tag{3.132} \label{eq-3-132}
$$

Since the kinetic energy is given by:

$$
\text{Kinetic energy } = \frac{p^2}{2m} \geq \frac{\hbar^2}{8m\sigma (r)^2} \tag{Zero-point energy}
$$

This zero-point energy is the minimum kinetic energy that a particle of mass $m$ can have if confined within a distance $\pm \sigma (r)$. This zero-point energy is a consequence of wave-particle duality and the uncertainty between the size and wavenumber for any wave packet. It is a quantal effect in that the classical limit has $\hbar \rightarrow 0$ for which the zero-point energy $\rightarrow 0$.

Inserting numbers for the zero-point energy gives that an electron confined to the radius of the atom, that is $\sigma (x) = 10^{−10}m$, has a zero-point kinetic energy of $\sim 1 \ eV$. Confining this electron to $3 \times 10^{−15}m$, the size of a nucleus, gives a zero-point energy of $10^9 \ eV (1 \ GeV )$. Confining a proton to the size of the nucleus gives a zero-point energy of 0.5 $MeV$. These values are typical of the level spacing observed in atomic and nuclear physics. If $\hbar$ was a large number, then a billiard ball confined to a billiard table would be a blur as it oscillated with the minimum zero-point kinetic energy. The smaller the spatial region that the ball was confined, the larger would be its zero-point energy and momentum causing it to rattle back and forth between the boundaries of the confined region. Life would be dramatically different if $\hbar$ was a large number.

In summary, Heisenberg’s Uncertainty Principle is a well-known and crucially important aspect of quantum physics. What is less well known, is that the Uncertainty Principle exists for all forms of wave motion, that is, it is not restricted to matter waves. The following three examples illustrate application of the Uncertainty Principle to acoustics, the nuclear Mössbauer effect, and quantum mechanics.

::::{admonition} Example 3.11.6: Acoustic Wave Packet
:class: example

A violinist plays the note middle C (261.625 $Hz$) with constant intensity for precisely 2 seconds. Using the fact that the velocity of sound in air is 343.2 $m/s$ calculate the following:

1. The wavelength of the sound wave in air: $\lambda$ = 343.2/261.625 = 1.312 $m$.

2. The length of the wavepacket in air: Wavepacket length = 343.2 $\times$ 2 = 686.4 $m$

3. The fractional frequency width of the note: Since the wave packet has a square pulse shape of length $\tau = 2s$, then the Fourier transform is a sinc function having the first zeros when $\sin \frac{\omega \tau}{2} = 0$, that is, $\Delta \nu = \frac{1}{\tau}$.

Therefore the fractional width is $\frac{\Delta \nu}{\nu} = \frac{1}{\nu \tau}$ = 0.0019. Note that to achieve a purity of $\frac{\Delta \nu}{\nu} = 10^{−6}$ the violinist would have to play the note for 1.06 hours.
::::

::::{admonition} Example 3.11.7: Gravitational Red Shift
:class: example

The Mössbauer effect in nuclear physics provides a wave packet that has an exceptionally small fractional width in frequency. For example, the $^{57}$Fe nucleus emits a 14.4 $keV$ deexcitation-energy photon which corresponds to $\omega \approx 2 \times 10^{25}$ $rad/s$ that has a decay time of $\tau \approx 10^{−7}$ $s$. Thus the fractional width is $\frac{\Delta \omega}{\omega} \approx 3 \times 10^{−18}$. In 1959 Pound and Rebka used this to test Einstein’s general theory of relativity by measurement of the gravitational red shift between the attic and basement of the 22.5 $m$ high physics building at Harvard. The magnitude of the predicted relativistic red shift is $\frac{\Delta E}{E} = 2.5\times 10^{−15}$ which is what was observed with a fractional precision of about 1%.
::::

::::{admonition} Example 3.11.8: Quantum Baseball
:class: example

George Gamow, in his book ”Mr. Tompkins in Wonderland”, describes the strange world that would exist if $\hbar$ was a large number. As an example, consider you play baseball in a universe where $\hbar$ is a large number. The pitcher throws a 150 $g$ ball 20 $m$ to the batter at a speed of 40 $m/s$. For a strike to be thrown, the ball’s position must be pitched within the 30 $cm$ radius of the strike zone, that is, it is required that $\Delta x \leq 0.3$ $m$. The uncertainty relation tells us that the transverse velocity of the ball cannot be less than $\Delta v = \frac{\hbar}{2 m \Delta x}$. The time of flight of the ball from the mound to batter is $t = 0.5 \ s$. Because of the transverse velocity uncertainty, $\Delta v$, the ball will deviate $t \Delta v$ transversely from the strike zone. This also must not exceed the size of the strike zone, that is;

$$
t \Delta v = \frac{\hbar t}{2 m \Delta x} \leq 0.3 m \tag{Due to transverse velocity uncertainty}
$$

Combining both of these requirements gives

$$
\hbar \leq \frac{2m \Delta x^2}{t} = 5.4 \ 10^{−2} J \cdot s. \nonumber
$$

This is 32 orders of magnitude larger than $\hbar$ so quantal effects are negligible. However, if $\hbar$ exceeded the above value, then the pitcher would have difficulty throwing a reliable strike.
::::

## 3.E: Linear Oscillators (Exercises)

1. Consider a simple harmonic oscillator consisting of a mass $m$ attached to a spring of spring constant $k$. For this oscillator $x(t) = A \sin(\omega_0 t − \delta )$.

1. Find an expression for $\dot{x}(t)$.

2. Eliminate $t$ between $x(t)$ and $\dot{x}(t)$ to arrive at one equation similar to that for an ellipse.

3. Rewrite the equation in part (b) in terms of $x, \dot{x}, k, m$, and the total energy $E$.

4. Give a rough sketch of the phase space diagram ($\dot{x}$ versus $x$) for this oscillator. Also, on the same set of axes, sketch the phase space diagram for a similar oscillator with a total energy that is larger than the first oscillator.

5. What direction are the paths that you have sketched? Explain your answer.

6. Would different trajectories for the same oscillator ever cross paths? Why or why not?

2. Consider a damped, driven oscillator consisting of a mass $m$ attached to a spring of spring constant $k$.

1. What is the equation of motion for this system?

2. Solve the equation in part (a). The solution consists of two parts, the complementary solution and the particular solution. When might it be possible to safely neglect one part of the solution?

3. What is the difference between amplitude resonance and kinetic energy resonance?

4. How might phase space diagrams look for this type of oscillator? What variables would affect the diagram?

3. A particle of mass $m$ is subject to the following force 
$$
\mathbf{F} = A(x^3 − 4x^2 + 3x)\mathbf{\hat{x}}\nonumber
$$
 where $A$ is a constant.

1. Determine the points when the particle is in equilibrium.

2. Which of these points is stable and which are unstable?

3. Is the motion bounded or unbounded?

4. A very long cylindrical shell has a mass density that depends upon the radial distance such that $\rho (r) = \frac{k}{r}$, where $k$ is a constant. The inner radius of the shell is $a$ and the outer radius is $b$.

1. Determine the direction and the magnitude of the gravitational field for all regions of space.

2. If the gravitational potential is zero at the origin, what is the difference between the gravitational potential at $r = b$ and $r = a$?

5. A mass $m$ is constrained to move along one dimension. Two identical springs are attached to the mass, one on each side, and each spring is in turn attached to a wall. Both springs have the same spring constant $k$.

1. Determine the frequency of the oscillation, assuming no damping.

2. Now consider damping. It is observed that after $n$ oscillations, the amplitude of the oscillation has dropped to one-half of its initial value. Find an expression for the damping constant.

3. How long does it take for the amplitude to decrease to one-quarter of its initial value?

6. Discuss the motion of a continuous string when plucked at one third of the length of the string. That is, the initial condition is $\ddot{q} (x,0) = 0$, and $q(x,0) = \left. \begin{cases} \frac{3A}{L} x, & 0 \leq x \leq \frac{L}{3} \\ \frac{3A}{2L} (L-x), & \frac{L}{3} \leq x \leq L \end{cases} \right\}$

7. When a particular driving force is applied to a stretched string it is observed that the string vibration in purely of the $n^{th}$ harmonic. Find the driving force.

8. Consider the two-mass system pivoted at its vertex where $M \neq m$. It undergoes oscillations of the angle $\theta$ with respect to the vertical in the plane of the triangle.

:::{figure} ../images/lt-21312-3.w.1.png
:label: fig-3-E-1
:enumerator: 3.E.1
:alt: Figure
:::

1. Determine the angular frequency of small oscillations.

2. Use your result from part (a) to show $\omega 2 \approx \frac{g}{l}$ for $M \gg m$.

3. Show that your result from part (a) agrees with $\omega^2 = \frac{U^{\prime \prime} (\theta_e)}{I}$ where $\theta_e$ is the equilibrium angle and $I$ is the moment of inertia.

4. Assume the system has energy $E$. Setup an integral that determines the period of oscillation.

9. An unusual pendulum is made by fixing a string to a horizontal cylinder of radius $R$, wrapping the string several times around the cylinder, and then tying a mass $m$ to the loose end. In equilibrium the mass hangs a distance $l_0$ vertically below the edge of the cylinder. Find the potential energy if the pendulum has swung to an angle $\phi$ from the vertical. Show that for small angles, it can be written in the Hooke’s Law form $U = \frac{1}{2} k\phi^2$. Comment of the value of $k$.

10. Consider the two-dimensional anisotropic oscillator with motion with $\omega_x = p\omega$ and $\omega_y = q\omega$.

1. Prove that if the ratio of the frequencies is rational (that is, $\frac{\omega_x}{\omega_y} = \frac{p}{q}$ where $p$ and $q$ are integers) then the motion is periodic. What is the period?

2. Prove that if the same ratio is irrational, the motion never repeats itself.

11. A simple pendulum consists of a mass $m$ suspended from a fixed point by a weight-less, extensionless rod of length $l$.

1. Obtain the equation of motion, and in the approximation $\sin \theta \approx \theta$, show that the natural frequency is $\omega_0 = \sqrt{\frac{q}{l}}$, where $g$ is the gravitational field strength.

2. Discuss the motion in the event that the motion takes place in a viscous medium with retarding force $2m \sqrt{gl} \dot{\theta}$.

12. Derive the expression for the State Space paths of the plane pendulum if the total energy is $E > 2$ $mgl$. Note that this is just the case of a particle moving in a periodic potential $U(\theta ) = mgl (1− \cos\theta )$. Sketch the State Space diagram for both $E> 2$ $mgl$ and $E< 2$ $mgl$.

13. Consider the motion of a driven linearly-damped harmonic oscillator after the transient solution has died out, and suppose that it is being driven close to resonance, $\omega = \omega_o$.

1. Show that the oscillator’s total energy is $E = \frac{1}{2} m\omega^2 A^2$.

2. Show that the energy $\Delta E_{dis}$ dissipated during one cycle by the damping force $\Gamma \dot{x}$ is $\pi \Gamma m \omega A^2$

14. Two masses $\text{m}_1$ and $\text{m}_2$ slide freely on a horizontal frictionless rail and are connected by a spring whose force constant is k. Find the frequency of oscillatory motion for this system.

15. A particle of mass $m$ moves under the influence of a resistive force proportional to velocity and a potential $U$, that is $l$. 
$$
F (x, \dot{x}) = -b\dot{x} - \frac{\partial U}{\partial x} \nonumber
$$
 where $b > 0$ and $U(x) = (x^2 - a^2)^2$

1. Find the points of stable and unstable equilibrium.

2. Find the solution of the equations of motion for small oscillations around the stable equilibrium points

3. Show that as $t \rightarrow \infty$ the particle approaches one of the stable equilibrium points for most choices of initial conditions. What are the exceptions? (Hint: You can prove this without finding the solutions explicitly.)

## 3.S: Linear Oscillators (Summary)

Linear systems have the feature that the solutions obey the *Principle of Superposition*, that is, the amplitudes add linearly for the superposition of different oscillatory modes. Applicability of the Principle of Superposition to a system provides a tremendous advantage for handling and solving the equations of motion of oscillatory systems.

Geometric representations of the motion of dynamical systems provide sensitive probes of periodic motion. Configuration space $(\mathbf{q}, \mathbf{q}, t)$, state space $(\mathbf{q}, \mathbf{\dot{q}}, t)$ and phase space $(\mathbf{q}, \mathbf{p}, t)$, are powerful geometric representations that are used extensively for recognizing periodic motion where $\mathbf{q}$, $\mathbf{\dot{q}}$, and $\mathbf{p}$ are vectors in $n$-dimensional space.

### Linearly-damped free linear oscillator

The free linearly-damped linear oscillator is characterized by the equation

$$
\ddot{x} + \Gamma \dot{x} + \omega^2_0 x = 0 \tag{3.26}
$$

The solutions of the linearly-damped free linear oscillator are of the form

$$
\begin{array}{lcl} z = e^{−\left( \frac{\Gamma}{2} \right)t} \left[ z_1 e^{i\omega_1 t} + z_2 e^{−i \omega_1 t} \right] && \omega_1 \equiv \sqrt{\omega^2_o − \left( \frac{\Gamma}{2} \right)^2} \end{array} \tag{3.33}
$$

The solutions fall into three categories

::::{list-table}
* - $x(t) = Ae^{−\left( \frac{\Gamma}{2} \right)t} \cos (\omega_1 t − \beta )$
  - underdamped
  - $\omega_1 = \sqrt{\omega^2_o − \left( \frac{\Gamma}{2} \right)^2} > 0$
* - $x(t) = [A_1e^{−\omega_+ t} + A_2e^{−\omega_−t} ]$
  - overdamped
  - $\omega_{\pm} = − \left[ −\frac{\Gamma}{2} \pm \sqrt{ \left(\frac{\Gamma}{2} \right)^2 − \omega^2_o } \right]$
* - $x(t) = (A + Bt) e^{−\left( \frac{\Gamma}{2} \right)t}$
  - critically damped
  - $\omega_1 = \sqrt{\omega^2_o − \left( \frac{\Gamma}{2} \right)^2} = 0$
::::

The energy dissipation for the linearly-damped free linear oscillator time averaged over one period is given by

$$
\langle E \rangle = E_0 e^{−\Gamma t} \tag{3.44}
$$

The quality factor $Q$ characterizing the damping of the free oscillator is define to be

$$
Q = \frac{E}{\Delta E} = \frac{\omega_1}{\Gamma} \tag{3.47}
$$

where $\Delta E$ is the energy dissipated per radian.

### Sinusoidally-driven, linearly-damped, linear oscillator

The linearly-damped linear oscillator, driven by a harmonic driving force, is of considerable importance to all branches of physics, and engineering. The equation of motion can be written as

$$
\ddot{x} + \Gamma \dot{x} + \omega^2_0 x = \frac{F (t)}{m} \tag{3.49}
$$

where $F(t)$ is the driving force. The complete solution of this second-order differential equation comprises two components, the complementary solution (*transient response*), and the particular solution (*steady-state response*). That is,

$$
x(t)_{Total} = x(t)_T + x(t)_S \tag{3.65}
$$

For the underdamped case, the transient solution is the complementary solution

$$
x(t)_T = \frac{F_0}{m} e^{− \frac{\Gamma}{2} t} \cos (\omega_1t − \delta ) \tag{3.66}
$$

and the steady-state solution is given by the particular solution

$$
x(t)_S = \frac{\frac{F_0}{m}}{\sqrt{ (\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2}} \cos (\omega t − \delta ) \tag{3.67}
$$

### Resonance

A detailed discussion of resonance and energy absorption for the driven linearly-damped linear oscillator was given. For resonance the maximum amplitudes occur at frequencies

::::{list-table}
* - Resonant system
  - Resonant frequency
* - undamped free linear oscillator
  - $\omega_0 = \sqrt{\frac{k}{m}}$
* - linearly-damped free linear oscillator
  - $\omega_1 = \sqrt{\omega^2_0 − \left(\frac{\Gamma}{2}\right)^2}$
* - driven linearly-damped linear oscillator
  - $\omega_R = \sqrt{\omega^2_0 − 2 \left( \frac{\Gamma}{2} \right)^2}$
::::

The energy absorption for the steady-state solution for resonance is given by

$$
x(t)_S = A_{el} \cos \omega t + A_{abs} \sin \omega t \tag{3.73}
$$

where the **elastic amplitude**

$$
A_{el} = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} (\omega^2_0 − \omega^2) \tag{3.74}
$$

while the **absorptive amplitude**

$$
A_{abs} = \frac{\frac{F_0}{m}}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} \Gamma \omega \tag{3.75}
$$

The time average power input is given by only the absorptive term

$$
\langle P \rangle = \frac{1}{2} F_0 \omega A_{abs} = \frac{F_0^2}{2m} \frac{\Gamma \omega^2}{(\omega^2_0 − \omega^2)^2 + (\Gamma \omega )^2} \tag{3.133} \label{eq-3-133}
$$

This power curve has the classic Lorentzian shape.

### Wave propagation

The wave equation was introduced and both travelling and standing wave solutions of the wave equation were discussed. Harmonic wave-form analysis, and the complementary time-sampled wave form analysis techniques, were introduced in this chapter and in appendix $19.9$. The relative merits of Fourier analysis and the digital Green’s function waveform analysis were illustrated for signal processing.

The concepts of phase velocity, group velocity, and signal velocity were introduced. The phase velocity is given by

$$
v_{phase} = \frac{\omega}{k} \tag{3.117}
$$

and group velocity

$$
v_{group} = \left( \frac{d\omega}{dk} \right)_{k_0} = v_{phase} + k \frac{\partial v_{phase}}{\partial k} \tag{3.128}
$$

If the group velocity is frequency dependent then the information content of a wave packet travels at the signal velocity which can differ from the group velocity.

The Wave-packet Uncertainty Principle implies that making a precise measurement of the frequency of a sinusoidal wave requires that the wave packet be infinitely long. The *standard deviation* $\sigma (t) = \sqrt{\langle t^2 \rangle − \langle t \rangle^2}$ characterizing the width of the *amplitude* of the wavepacket spectral distribution in the angular frequency domain, $\sigma_A(\omega )$, and the corresponding width in time $\sigma_A(t)$, are related by :

$$
\sigma_A(t) \cdot \sigma_A (\omega ) \geqslant 1 \tag{Relation between amplitude uncertainties.}
$$

The standard deviations for the spectral distribution and width of the *intensity* of the wave packet are related by:

$$
\sigma_I (t) \cdot \sigma_I (\omega) \geqslant \frac{1}{2} \tag{3.134} \label{eq-3-134} \\ \sigma_I (x) \cdot \sigma_I (k_x) \geqslant \frac{1}{2} \quad \sigma_I (y) \cdot \sigma_I (k_y) \geqslant \frac{1}{2} \quad \sigma_I (z) \cdot \sigma_I (k_z) \geqslant \frac{1}{2}
$$

This applies to all forms of wave motion, including sound waves, water waves, electromagnetic waves, or matter waves.
