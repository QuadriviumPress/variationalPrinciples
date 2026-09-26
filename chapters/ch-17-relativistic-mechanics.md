---
title: "17. Relativistic Mechanics"
short_title: "Chapter 17"
label: ch-17-relativistic-mechanics
---


(ch-17)=

# 17. Relativistic Mechanics

## 17.1: Introduction to Relativistic Mechanics

Newtonian mechanics incorporates the Newtonian concept of the complete separation of space and time. This theory reigned supreme from inception, in 1687, until November 1905 when Einstein pioneered the Special Theory of Relativity. Relativistic mechanics undermines the Newtonian concepts of absoluteness of time that is inherent to Newton’s formulation, as well as when recast in the Lagrangian and Hamiltonian formulations of classical mechanics. Relativistic mechanics has had a profound impact on twentieth-century physics and the philosophy of science. Classical mechanics is an approximation of relativistic mechanics that is valid for velocities much less than the velocity of light in vacuum. The term “relativity” refers to the fact that physical measurements are always made relative to some chosen reference frame. Naively one may think that the transformation between different reference frames is trivial and contains little underlying physics. However, Einstein showed that the results of measurements depend on the choice of coordinate system, which revolutionized our concept of space and time.

Einstein’s work on relativistic mechanics comprised two major advances. The first advance is the 1905 **Special Theory of Relativity**which refers to nonaccelerating frames of reference. The second major advance was the 1916 **General Theory of Relativity** which considers accelerating frames of reference and their relation to gravity. The Special Theory is a limiting case of the General Theory of Relativity. The mathematically complex General Theory of Relativity is required for describing accelerating frames, gravity, plus related topics like Black Holes, or extremely accurate time measurements inherent to the Global Positioning System. The present discussion will focus primarily on the mathematically simple Special Theory of Relativity since it encompasses most of the physics encountered in atomic, nuclear and high energy physics. This chapter uses the basic concepts of the Special Theory of Relativity to investigate the implications of extending Newtonian, Lagrangian and Hamiltonian formulations of classical mechanics into the relativistic domain. The Lorentz-invariant extended Hamiltonian and Lagrangian formalisms are introduced since they are applicable to the Special Theory of Relativity. The General Theory of Relativity incorporates the gravitational force as a geodesic phenomena in a four-dimensional Riemannian structure based on space, time, and matter. A superficial outline is given to the fundamental concepts and evidence that underlie the General Theory of Relativity.

## 17.2: Galilean Invariance

As discussed in chapter $2.3$, an inertial frame is one in which Newton’s Laws of motion apply. Inertial frames are non-accelerating frames so that pseudo forces are not induced. All reference frames moving at constant velocity relative to an inertial reference, are inertial frames. Newton’s Laws of nature are the same in all inertial frames of reference and therefore there is no way of determining absolute motion because no inertial frame is preferred over any other. This is called Galilean-Newtonian invariance. Galilean invariance assumes that the concepts of space and time are completely separable. Time is assumed to be an absolute quantity that is invariant to transformations between coordinate systems in relative motion. Also the element of length is the same in different Galilean frames of reference.

:::{figure} ../images/lt-21263-16.2.1.png
:label: fig-17-2-1
:enumerator: 17.2.1
:alt: Motion of the primed frame along the x_1 axis with velocity v relative to the parallel unprimed frame.

Motion of the primed frame along the $x_1$ axis with velocity $v$ relative to the parallel unprimed frame.
:::

Consider two coordinate systems shown in [Figure 17.2.1](#fig-17-2-1), where the primed frame is moving along the $x$ axis of the fixed unprimed frame. A **Galilean transformation** implies that the following relations apply;

$$
x^{\prime}_1 = x_1 − vt \\ x^{\prime}_2 = x_2 \\ x^{\prime}_3 = x_3 \\ t^{\prime} = t
$$

Note that at any instant $t$, the infinitesimal units of length in the two systems are identical since

$$
ds^2 = \sum^2_{i=1} dx^2_i = \sum^3_{i=1} dx^{\prime 2}_i = ds^{\prime 2}
$$

These are the mathematical expression of the Newtonian idea of space and time. An immediate consequence of the Galilean transformation is that the velocity of light must differ in different inertial reference frames.

At the end of the 19$^{th}$ century physicists thought they had discovered a way of identifying an absolute inertial frame of reference, that is, it must be the frame of the medium that transmits light in vacuum. Maxwell’s laws of electromagnetism predict that electromagnetic radiation in vacuum travels at $c = \frac{1}{\sqrt{\mu_o \varepsilon_o}} = 2.998 \times 10^8$ $m/s$. Maxwell did not address in what frame of reference that this speed applied. In the nineteenth century all wave phenomena were transmitted by some medium, such as waves on a string, water waves, sound waves in air. Physicists thus envisioned that light was transmitted by some unobserved medium which they called the *ether*. This ether had mystical properties, it existed everywhere, even in outer space, and yet had no other observed consequences. The ether obviously should be the absolute frame of reference.

In the 1880's, Michelson and Morley performed an experiment in Cleveland to try to detect this ether. They transmitted light back and forth along two perpendicular paths in an interferometer, shown in [Figure 17.2.2](#fig-17-2-2), and assumed that the earth’s motion about the sun led to movement through the ether.

:::{figure} ../images/lt-21264-16.2.2.png
:label: fig-17-2-2
:enumerator: 17.2.2
:alt: The Michelson interferometer used for the Michelson-Morley experiment. Interference of the two beams of coherent light leads to fringes that depends on the differences in phase along the two paths.

The Michelson interferometer used for the Michelson-Morley experiment. Interference of the two beams of coherent light leads to fringes that depends on the differences in phase along the two paths.
:::

The time taken to travel a return trip takes longer in a moving medium, if the medium moves in the direction of the motion, compared to travel in a stationary medium. For example, you lose more time moving against a headwind than you gain travelling back with the wind. The time difference $\Delta t$, for a round trip to a distance $L$, between travelling in the direction of motion in the ether, versus travelling the same distance perpendicular to the movement in the ether, is given by $\Delta t \approx \frac{L}{c} \left(\frac{v}{c}\right)^2$ where $v$ is the relative velocity of the ether and $c$ is the velocity of light.

Interference fringes between perpendicular light beams in an optical interferometer provides an extremely sensitive measure of this time difference. Michelson and Morley observed no measurable time difference at any time during the year, that is, the relative motion of the earth within the ether is less than $1/6$ the velocity of the earth around the sun. Their conclusion was either, that the ether was dragged along with the earth, or the velocity of light was dependent on the velocity of the source, but these did not jibe with other observations. Their disappointment at the failure of this experiment to detect evidence for an absolute inertial frame is important and confounded physicists for two decades until Einstein’s Special Theory of Relativity explained the result.

## 17.3: Special Theory of Relativity

### Einstein Postulates

In November 1905, at the age of 26, Einstein published a seminal paper entitled ”On the electrodynamics of moving bodies”. He considered the relation between space and time in inertial frames of reference that are in relative motion. In this paper he made the following postulates.

1. The laws of nature are the same in all inertial frames of reference.

2. The velocity of light in vacuum is the same in all inertial frames of reference.

Note that Einstein’s first postulate, coupled with Maxwell’s equations, leads to the statement that the velocity of light in vacuum is a universal constant. Thus the second postulate is unnecessary since it is an obvious consequence of the first postulate plus Maxwell’s equations which are basic laws of physics. This second postulate explained the null result of the Michelson-Morley experiment. However, it was not this experimental result that led Einstein to the theory of special relativity; he deduced the Special Theory of Relativity from consideration of Maxwell’s equations of electromagnetism. Although Einstein’s postulates appear reasonable, they lead to the following surprising implications.

### Lorentz transformation

Galilean invariance leads to violation of the Einstein postulate that the velocity of light is a universal constant in all frames of reference. It is necessary to assume a new transformation law that renders physical laws relativistically invariant. Maxwell’s equations are relativistically invariant, which led to some electromagnetic phenomena that could not be explained using Galilean invariance. In 1904 Lorentz proposed a new transformation to replace the Galilean transformation in order to explain such electromagnetic phenomena. Einstein’s genius was that he derived the transformation, that had been proposed by Lorentz, directly from the postulates of the Special Theory of Relativity. The Lorentz transformation satisfies Einstein’s theory of relativity, and has been confirmed to be correct by many experiments.

For the geometry shown in Figure $17.2.1$, the **Lorentz transformations** are:

$$
x^{\prime}_= \gamma (x − vt) \tag{17.3} \label{eq-17-3} \\ y^{\prime} = y \\ z^{\prime} = z \\ t^{\prime} = \gamma \left( t − \frac{vx}{ c^2} \right)
$$

where the Lorentz $\gamma$ factor

$$
\gamma \equiv \frac{1}{\sqrt{ 1 − ( \frac{v}{c} )^2}} \tag{17.4} \label{eq-17-4}
$$

The inverse transformations are

$$
x = \gamma (x^{\prime}_+ vt^{\prime}) \tag{17.5} \label{eq-17-5} \\ y = y^{\prime} \\ z = z^{\prime} \\ t = \gamma \left( t^{\prime} + \frac{vx^{\prime}}{c^2} \right)
$$

:::{figure} ../images/lt-21265-16.3.1.png
:label: fig-17-3-1
:enumerator: 17.3.1
:alt: The dependence of the Lorentz \gamma factor on \frac{v}{c}.

The dependence of the Lorentz $\gamma$ factor on $\frac{v}{c}$.
:::

The Lorentz $\gamma$ factor, defined above, is the key feature differentiating the Lorentz transformations from the Galilean transformation. Note that $\gamma \geq 1$; also $\gamma \rightarrow 1.0$ as $v \rightarrow 0$ and increases to infinity as $\frac{v}{c} \rightarrow 1$ as illustrated in [Figure 17.3.1](#fig-17-3-1). A useful fact that will be used later is that for $\frac{v}{c} << 1$;

$$
\gamma \rightarrow 1 + \frac{1}{ 2} \left(\frac{v}{c} \right)^2 \tag{Limit for v << c}
$$

Note that for $v << c$ then $\gamma = 1$ and the Lorentz transformation is identical to the Galilean transformation.

:::{figure} ../images/lt-21268-16.3.2.png
:label: fig-17-3-2
:enumerator: 17.3.2
:alt: The observer and mirror are at rest in the left-hand frame (a). The light beam takes a time \Delta t = \frac{d}{c} to travel to the mirror. In the right-hand frame (b) the source and mirror are travelling at a velocity v relative to the observer. The light travels further in the right-hand frame …

The observer and mirror are at rest in the left-hand frame (a). The light beam takes a time $\Delta t = \frac{d}{c}$ to travel to the mirror. In the right-hand frame (b) the source and mirror are travelling at a velocity $v$ relative to the observer. The light travels further in the right-hand frame of reference (b) than is the stationary frame (a). Since Einstein states that the velocity of light is the same in both frames of reference then the time interval must by larger in frame (b) since the light travels further than in (a).
:::

### Time Dilation

Consider that a clock is *fixed at* $x^{\prime}_o$ *in a moving frame* and measures the time interval between two events in the moving frame, i.e. $\Delta t^{\prime}_p = t^{\prime}_1 − t^{\prime}_2$. According to the Lorentz transformation, the times in the fixed frame are given by:

$$
t_1 = \gamma \left( t^{\prime}_1 + \frac{vx^{\prime}_0 }{c^2} \right) \tag{17.6} \label{eq-17-6} \\ t_2 = \gamma \left( t^{\prime}_2 + \frac{vx^{\prime}_0}{ c^2} \right)
$$

Thus the time interval is given by:

$$
t_2 − t_1 = \gamma (t^{\prime}_2 − t^{\prime}_1) \tag{17.7} \label{eq-17-7}
$$

The time between events in the rest frame of the clock, $\Delta \tau \equiv \Delta t^{\prime}_p$ is called the *proper time* which always is the shortest time measured for a given event and is represented by the symbol $\tau$. That is

$$
\Delta t = \gamma\Delta t^{\prime}_p = \gamma\Delta \tau \tag{17.8} \label{eq-17-8}
$$

Note that the time interval for any other frame of reference, moving with respect to the clock frame, will show larger time intervals because $\gamma \geq 1.0$ which implies that the fixed frame perceives that the moving clock is slow by the factor $\gamma$.

The plausibility of this *time dilation* can be understood by looking at the simple geometry of the space ship example shown in [Figure 17.3.2](#fig-17-3-2). Pretend that the clock in the proper frame of the space ship is based on the time for the light to travel to and from the mirror in the space ship. In this proper frame the light has the shortest distance to travel, and the proper transit time is

$$
\Delta \tau = \frac{2d}{ c} \tag{17.9} \label{eq-17-9}
$$

In the fixed frame, $b$, the component of velocity in the direction of the mirror is $\sqrt{c^2 − v^2}$ using the Pythagorean theorem, assuming that the light cannot travel faster than $c$. Thus the transit time towards and back from the mirror must be

$$
\Delta t = \frac{2d}{ c \sqrt{1 − ( \frac{v}{c} )^2}} = \gamma\Delta \tau \tag{17.10} \label{eq-17-10}
$$

which is the predicted time dilation.

There are many experimental verifications of time dilation in physics. For example, a stationary muon has a mean lifetime of $\tau_p = 2$ $\mu s$, whereas the lifetime of a fast moving muon, produced in the upper atmosphere by high-energy cosmic rays, was observed in 1941 to be longer and given by $\gamma\tau_p$ as described in example 17.3.1. In 1972 Hafele and Keating used four accurate cesium atomic clocks to confirm time dilation. Two clocks were flown on regularly scheduled airlines travelling around the World, one westward and the other eastward. The other two clocks were used for reference. The westward moving clock was slow by $(273 \pm 7)$ $n s$ compared to the predicted value of $(275 \pm 10)$ $n s$. The Global Positioning System of 24 geosynchronous satellites is used for locating positions to within a few meters. It has an accuracy of a few nanoseconds which requires allowance for time dilation and is a daily tribute to the correctness of Einstein’s Theory of Relativity.

### Length Contraction

The Lorentz transformation leads to a contraction of the apparent length of an object in a moving frame as seen from a fixed frame. The length of a ruler in its own frame of reference is called the *proper length*. Consider an accurately measured rod of known proper length $L_p = x^{\prime}_2 − x^{\prime}_1$ that is, at rest in the moving primed frame. The locations of both ends of this rod are measured at a *given time in the stationary frame*, $t_1 = t_2$, by taking a photograph of the moving rod. The corresponding locations in the moving frame are:

$$
x^{\prime}_2 = \gamma (x_2 − vt_2) \tag{17.11} \label{eq-17-11} \\ x^{\prime}_1 = \gamma (x_1 − vt_1)
$$

Since $t_2 = t_1$, the measured lengths in the two frames are related by:

$$
x^{\prime}_2 − x^{\prime}_1 = \gamma (x_2 − x_1) \tag{17.12} \label{eq-17-12}
$$

That is, the lengths are related by:

$$
L = \frac{1 }{\gamma} L_p \tag{17.13} \label{eq-17-13}
$$

Note that the moving rod appears shorter in the direction of motion. As $v \rightarrow c$ the apparent length shrinks to zero in the direction of motion while the dimensions perpendicular to the direction of motion are unchanged. This is called the *Lorentz contraction*. If you could ride your bicycle at close to the speed of light, you would observe that stationary cars, buildings, people, all would appear to be squeezed thin along the direction that you are travelling. Also objects that are further away down any side street would be distorted in the direction of travel. A photograph taken by a stationary observer would show the moving bicycle to be Lorentz contracted along the direction of travel and the stationary objects would be normal.

### Simultaneity

The Lorentz transformations imply a new philosophy of space and time. A surprising consequence is that the concept of simultaneity is frame dependent in contrast to the prediction of Newtonian mechanics.

Consider that two events occur in frame $S$ at $(x_1, t_1)$ and $(x_2, t_2)$. In frame $S^{\prime}$ these two events occur at $(x^{\prime}_1, t^{\prime}_1)$ and $(x^{\prime}_2, t^{\prime}_2)$. From the Lorentz transformation the time difference is

$$
t^{\prime}_2 − t^{\prime}_1 = \gamma \left[ (t_2 − t_1) − \frac{v (x_2 − x_1) }{c^2} \right] \tag{17.14} \label{eq-17-14}
$$

If an event is simultaneous in frame $S$, that is $(t_2 − t_1)=0$ then

$$
t^{\prime}_2 − t^{\prime}_1 = \gamma \left[ \frac{v (x_1 − x_2) }{c^2} \right] \tag{17.15} \label{eq-17-15}
$$

Thus the event is not simultaneous in frame $S^{\prime}$ if $(x_2 − x_1) = L_p \neq 0$. That is, an event that is simultaneous in one frame is not simultaneous in the other frame if the events are spatially separated. The equivalent statement is that for two clocks, spatially separated by a distance $L_p$, which are synchronized in their rest frame, then in a moving frame they are not simultaneous.

Einstein discussed the problem of lightning striking both ends of a railway carriage that is moving at a velocity $v$. Assume that the lightning strikes both the front and rear of the carriage simultaneously, according to a stationary observer. A woman riding in the center of the train will se the lightning flash arrive from the front of the carriage before the wavefront from the rear of the carriage arrives since the carriage is moving towards the approaching wavefront and away from the wavefront from the rear of the train. If the length of the carriage is $L$, then the time difference between the light flash from front and rear of the carriage will be $\Delta t = \gamma L_p \frac{v}{c^2}$. As a consequence she observes that the two signals are not simultaneous. Thus a photograph of a rapidly moving body will appear to have a shorter distance. The relativistic snake discussed in chapter $17$, exercise 1 is a similar example of the role of simultaneity in relativistic mechanics.

::::{admonition} Example 17.3.1: Muon lifetime
:class: example

Many people had trouble comprehending time dilation and Lorentz contraction predicted by the Special Theory of Relativity. The predictions appear to be crazy, but there are many examples where time dilation and Lorentz contraction are observed experimentally such as the decay in flight of the muon. At rest, the muon decays with a mean lifetime of $2$ $\mu s$. Muons are created high in the atmosphere due to cosmic ray bombardment. A typical muon travels at $v = 0.998c$ which corresponds to $\gamma = 15$. Time dilation implies that the lifetime of the moving muon in the earth’s frame of reference is $30$ $\mu s$. The speed of the muon is essentially $c$ in both frames of reference, and it would travel $600$ $m$ in $2$ $\mu s$ and $9000$ $m$ in $30$ $\mu s$. In fact, it is observed that the muon does travel, on average, $9000$ $m$ in the earth frame of reference before decaying. Is this inconsistent with the view of someone travelling with the muon? In the muon’s moving frame, the lifetime is only $2$ $\mu s$, but the Lorentz contraction of distance means that $9000$ $m$ in the earth frame appears to be only $600$ $m$ in the muon moving frame; a distance it travels is $2$ $\mu s$. Thus in both frames of reference we have consistent explanations, that is, the muon travels the height of the mountain in one lifetime.
::::

::::{admonition} Example 17.3.2: Relativistic Doppler Effect
:class: example

The relativistic Doppler effect is encountered frequently in physics and astronomy. Consider monochromatic electromagnetic radiation from a source, such as a star, that is moving towards the detector at a velocity $v$. During the time $\Delta t$ in the frame of the receiver, the source emits $n$ cycles of the sinusoidal waveform. Thus the length of this waveform, as seen by the receiver, is $n\lambda$ which equals

$$
n\lambda = (c − v)\Delta t \nonumber
$$

The frequency as measured by the receiver is

$$
\nu = \frac{c}{ \lambda } = \frac{cn}{ (c − v)\Delta t} \nonumber
$$

According to the source, it emits $n$ waves of frequency $\nu_0$ during the proper time interval $\Delta t^{\prime}$, that is

$$
n = \nu_0\Delta t^{\prime} \nonumber
$$

This proper time interval $\Delta t^{\prime}$, in the source frame, corresponds to a time interval $\Delta t$ in the receiver frame where

$$
\Delta t = \gamma\Delta t^{\prime} \nonumber
$$

Thus the frequency measured by the receiver is

$$
\nu = \frac{1}{ (1 − \frac{v}{c} )} \frac{\nu_0}{ \gamma} = \frac{\sqrt{1 − ( \frac{v}{c} )^2}}{ (1 − \frac{v}{c} )} \nu_0 = \sqrt{\frac{ 1 + \beta}{ 1 − \beta}} \nu_0 \nonumber
$$

where $\beta \equiv \frac{v}{c}$. This formula for source and receiver approaching each other also gives the correct answer for source and receiver receding if the sign of $\beta$ is changed.

This relativistic Doppler Effect accounts for the red shift observed for light emitted by receding stars and galaxies, as well as many examples in atomic and nuclear physics involving moving sources of electromagnetic radiation.
::::

::::{admonition} Example 17.3.3: Twin paradox
:class: example

A problem that troubled physicists for many years is called the twin paradox. Consider two identical twins, Jack and Jill. Assume that Jill travels in a space ship at a speed of $\gamma = 4$ for 20 years, as measured by Jack’s clock, and then returns taking another 20 years, according to Jack. Thus, Jack has aged 40 years by the time his twin sister returns home. However, Jill’s clock measures $20/4=5$ years for each half of the trip so that she thinks she travelled for 10 years total time according to her clock. Thus she has aged only 10 years on the trip, that is, now she is 30 years younger that her twin brother. Note that, according to Jill, the distance she travelled out and back was $1/4$ the distance according to Jack, so she perceives no inconsistency in her clock, and the speed of the space ship. This was called a paradox because some people claimed that Jill will perceive that the earth and Jack moved away at the same relative speed in the opposite direction and thus according to Jill, Jack should be 30 years younger, not her. Moreover, some claimed that this problem is symmetric and therefore both twins must still be the same age since there is no way of telling who was moving away from whom. This argument is incorrect because Jill was able to sense that she accelerated to $\gamma = 4$ which destroys the symmetry argument. The effect is observed with accelerated beams of unstable nuclei such as the muon and was confirmed by the results of the experiment where cesium atomic clocks were flown around the Earth. Thus the Twin paradox is not a paradox; the fact is that Jill will be younger than her twin brother.
::::

## 17.4: Relativistic Kinematics

### Velocity Transformations

Consider the two parallel coordinate frames with the primed frame moving at a velocity $v$ along the $x^{\prime}_1$ axis as shown in Figure $17.2.1$. Velocities of an object measured in both frames are defined to be

$$
u_i = \dfrac{dx_i}{ dt} \tag{17.16} \label{eq-17-16} \\ u^{\prime}_i = \dfrac{dx^{\prime}_i}{ dt^{\prime}}
$$

Using the Lorentz transformations $(17.3.1)$, $(17.3.3)$ between the two frames moving with relative velocity $v$ along the $x_1$ axis, gives that the velocity along the $x^{\prime}_1$ axis is

$$
u^{\prime}_1 = \dfrac{dx^{\prime}_1}{ dt^{\prime} } = \dfrac{dx_1 − vdt}{ dt − \dfrac{v}{ c^2} dx_1} = \dfrac{u_1 − v}{ 1 − \dfrac{u_1v}{ c^2} } \tag{17.17} \label{eq-17-17}
$$

Similarly we get the velocities along the perpendicular $x^{\prime}_2$ and $x^{\prime}_3$ axes to be

$$
u^{\prime}_2 = \dfrac{dx^{\prime}_2 }{dt^{\prime}} = \dfrac{u_2}{ 1 − \dfrac{u_1v}{ c^2}} \tag{17.18} \label{eq-17-18} \\ u^{\prime}_3 = \dfrac{dx^{\prime}_3 }{dt^{\prime}} = \dfrac{u_3}{ 1 − \dfrac{u_1v}{ c^2}}
$$

When $\dfrac{u_1v}{ c^2} \rightarrow 0$ these velocity transformations become the usual Galilean relations for velocity addition. Do not confuse $\mathbf{u}$ and $\mathbf{u}^{\prime}$ with $\mathbf{v}$; that is, $\mathbf{u}$ and $\mathbf{u}^{\prime}$ are the velocities of some object measured in the unprimed and primed frames of reference respectively, whereas $\mathbf{v}$ is the relative velocity of the origin of one frame with respect to the origin of the other frame.

### Momentum

Using the classical definition of momentum, that is $\mathbf{p} = m\mathbf{u}$, the linear momentum is not conserved using the above relativistic velocity transformations if the mass $m$ is a scalar quantity. This problem originates from the fact that both $\mathbf{x}$ and $t$ have non-trivial transformations and thus $\mathbf{u} = \dfrac{d\mathbf{x}}{dt}$ is frame dependent.

Linear momentum conservation can be retained by redefining momentum in a form that is identical in all frames of reference, that is by referring to the *proper time* $\tau$ as measured in the rest frame of the moving object. Therefore we define relativistic linear momentum as

$$
\mathbf{p} \equiv m \dfrac{d\mathbf{x}}{ d\tau} = m \dfrac{d\mathbf{x}}{ dt} \dfrac{dt}{ d\tau} \tag{17.19} \label{eq-17-19}
$$

But we know the time dilation relation

$$
dt = \dfrac{d\tau }{\sqrt{ (1 − \dfrac{u^2}{ c^2} )}} = \gamma_u d\tau \tag{17.20} \label{eq-17-20}
$$

Note that the $\gamma_u$ in this relation refers to the velocity $u$ between the moving object and the frame; *this is quite different* from the $\gamma = \dfrac{ 1}{\sqrt{ (1− \dfrac{v^2}{ c^2} )}}$ which refers to the transformation between the two frames of reference. Thus the new relativistic definition of momentum is

$$
\begin{align} \mathbf{p} &\equiv m \dfrac{d\mathbf{x}}{ d\tau} \\[4pt] &= m\gamma_u \dfrac{d\mathbf{x}}{ dt} \\[4pt] &= \gamma_u m\mathbf{u} \tag{17.21} \label{eq-17-21} \end{align}
$$

The relativistic definition of linear momentum is the same as the classical definition with the rest mass $m$ replaced by the relativistic mass $\gamma m$.[^17-4-1]

### Center of momentum coordinate system

The classical relations for handling the kinematics of colliding objects, carry over to special relativity when the relativistic definition of linear momentum, Equation [17.21](#eq-17-21), is assumed. That is, one can continue to apply conservation of linear momentum. However, there is one important conceptual difference for relativistic dynamics in that the center of mass no longer is a meaningful concept due to the interrelation of mass and energy. However, this problem is eliminated by considering the center of momentum coordinate system which, as in the non-relativistic case, is the frame where the total linear momentum of the system is zero. Using the concept of center of momentum incorporates the formalism of classical non-relativistic kinematics.

### Force

Newton’s second law $\mathbf{F} = \dfrac{d\mathbf{p}}{ dt}$ is covariant under a Galilean transformation. In special relativity this definition also applies using the relativistic definition of momentum $\mathbf{p}$. The fact that the **relativistic momentum** $\mathbf{p}$ is conserved in the force-free situation, leads naturally to using the definition of force to be

$$
\mathbf{F} = \dfrac{d\mathbf{p}}{ dt} \tag{17.22} \label{eq-17-22}
$$

Then the relativistic momentum is conserved if $\mathbf{F} = 0$.

### Energy

The classical definition of work done is defined by

$$
W_{12} = \int^2_1 \mathbf{F}\cdot d\mathbf{r} = T_2 − T_1 \tag{17.23} \label{eq-17-23}
$$

Assume $T_1 = 0$, let $d\mathbf{r} = \mathbf{u}dt$ and insert the relativistic force relation in Equation [17.23](#eq-17-23), gives

$$
W = T = \int^t_0 \dfrac{d}{dt} (\gamma_u m\mathbf{u}) \cdot \mathbf{u}dt = m \int^u_0 ud (\gamma_u u) \tag{17.24} \label{eq-17-24}
$$

Integrate by parts, followed by algebraic manipulation, gives

$$
\begin{align} T &= \gamma_{u} m u^{2}-m \int_{0}^{u} \dfrac{u d u}{\sqrt{1-\dfrac{u^{2}}{c^{2}}}} \\[4pt] &= \gamma_{u} m u^{2} + m c^{2} \sqrt{1-\dfrac{u^{2}}{c^{2}}} - m c^{2} \\ &= \dfrac{m u^{2}}{\sqrt{1-\dfrac{u^{2}}{c^{2}}}} + \dfrac{m c^{2}}{\sqrt{1-\dfrac{u^{2}}{c^{2}}}} \left( 1 - \dfrac{u^{2}}{c^{2}} \right) - m c^{2} \\[4pt] &= m c^{2} \left( \gamma_{u} -1 \right) \tag{17.25} \label{eq-17-25} \end{align}
$$

Define the **rest energy** $E_0$

$$
E_0 \equiv mc^2 \tag{17.26} \label{eq-17-26}
$$

and **total relativistic energy** $E$

$$
E \equiv \gamma_u mc^2 \tag{17.27} \label{eq-17-27}
$$

then Equation [17.25](#eq-17-25) can be written as

$$
\begin{align} E &= T + E_0 \\[4pt] &= \gamma_u mc^2 \tag{17.28} \label{eq-17-28} \end{align}
$$

This is the famous Einstein relativistic energy that relates the equivalence of mass and energy. The total relativistic energy $E$ is a conserved quantity in nature. It is an extension of the conservation of energy and manifestations of the equivalence of energy and mass occur extensively in the real world.

In nuclear physics we often convert mass to energy and back again to mass. For example, gamma rays with energies greater than $1.022$ $MeV$, which are pure electromagnetic energy, can be converted to an electron plus positron both of which have rest mass. The positron can then annihilate a different electron in another atom resulting in emission of two $511$ $keV$ gamma rays in back to back directions to conserve linear momentum. A dramatic example of Einstein’s equation is a nuclear reactor. One gram of material, the mass of a paper clip, provides $E = 9 \times 10^{13}$ joules. This is the daily output of a $1$ ${GWatt}$ nuclear power station or the explosive power of the Nagasaki or Hiroshima bombs.

As the velocity of a particle $v$ approaches $c$, then $\gamma$ and the relativistic mass $\gamma m$ both approach infinity. This means that the force needed to accelerate the mass also approaches infinity, and thus no particle can exceed the velocity of light. The energy continues to increase not by increasing the velocity but by increase of the relativistic mass. Although the relativistic relation for kinetic energy is quite different from the Newtonian relation, the Newtonian form is obtained for the case of $u \ll c$ in that

$$
\begin{align} T &= \dfrac{mc^2}{\sqrt{1 − \dfrac{u^2}{ c^2}}} − mc^2 \\[4pt] &= mc^2(1 + \dfrac{1}{ 2} \dfrac{u^2}{ c^2} + \cdots ) − mc^2 \\[4pt] &= \dfrac{1}{ 2} mu^2 \tag{17.29} \label{eq-17-29} \end{align}
$$

An especially useful relativistic relation that can be derived from the above is

$$
E^2 = p^2c^2 + E^2_0 \tag{17.30} \label{eq-17-30}
$$

This is useful because it provides a simple relation between total energy of a particle and its relativistic linear momentum plus rest energy.

::::{admonition} Example 17.4.1: Rocket Propulsion
:class: example

Consider a rocket, having initial mass $M$, is accelerated in a straight line in free space by exhausting propellant at a constant speed $v_p$ relative to the rocket. Let $u$ be the speed of the rocket relative to it’s initial rest frame $S$, when its rest mass has decreased to $m$. At this instant the rocket is at rest in the inertial frame $S^{\prime}$. At a proper time $\tau + d\tau$ the rest mass is $m − dm$ and it has acquired a velocity increment $du$ relative to $S^{\prime}$ and propellant of rest mass $dm_p$ has been expelled with velocity $v_p$ relative to $S^{\prime}$. At proper time $\tau$ in $S^{\prime}$ the rest mass is $mc^2$. At the time $\tau + d\tau$, energy conservation requires that

$$
\gamma_{u^{\prime}} (m − dm) c^2 + \gamma_{v_p} m_p c^2 = mc^2 \nonumber
$$

At the same instant, conservation of linear momentum requires

$$
\gamma_{u^{\prime}} (m − dm) du^{\prime} − \gamma_p v_p dm_p = 0 \nonumber
$$

To first order these two equations simplify to

$$
dm_p = \sqrt{ 1 − \left(\dfrac{v_p }{c} \right)^2 } dm \nonumber
$$

$$
mdu^{\prime} = dm_p\gamma_{v_p} v_p \nonumber
$$

Therefore

$$
mdu^{\prime} = v_pdm \label{eq-17-a}\tag{a}
$$

The velocity increment $du^{\prime}$ in frame $S^{\prime}$ can be transformed back to frame $S$ using equation $(17.3.3)$, that is

$$
d + du = \dfrac{u + du^{\prime}}{ 1 + \dfrac{ udu^{\prime}}{ c^2}} \approx u + \left( 1 − \left(\dfrac{u}{c} \right)^2 \right) du^{\prime} \label{eq-17-b}\tag{b}
$$

Equations [a](#eq-17-a) and [b](#eq-17-b) yield a differential equation for $u(m)$ of

$$
\dfrac{du}{ 1 − (\dfrac{u}{c} )^2} = v_p \dfrac{dm}{m} \nonumber
$$

Integrate the left-hand side between $0$ and $u$ and the right-hand side between $M$ and $m$ gives

$$
\dfrac{1}{ 2} c \ln \left(\dfrac{1 + \dfrac{u}{c} }{1 − \dfrac{u}{c}} \right) = −v_p \ln \left( \dfrac{m}{M} \right) \nonumber
$$

This reduces to

$$
\dfrac{u}{c} = \dfrac{1 − ( \dfrac{m}{M} )^{2v_p/c}}{ 1 + ( \dfrac{m}{M} )^{2v_p/c}} \nonumber
$$

When $\dfrac{u}{c} \rightarrow 0$ this equation reduces to the non-relativistic answer given in equation $(2.12.34)$.
::::

[^17-4-1]: Note that, until recently, the rest mass was denoted by $m_0$ and the relativistic mass was referred to as $m$. Modern texts denote the rest mass by $m$ and the relativistic mass by $\gamma m$. This book follows the modern nomenclature for rest mass to avoid confusion.

## 17.5: Geometry of Space-time

### Four-Dimensional Space-Time

In 1906 Poincaré showed that the Lorentz transformation can be regarded as a rotation in a 4-dimensional Euclidean space-time introduced by adding an imaginary fourth space-time coordinate $ict$ to the three real spatial coordinates. In 1908 Minkowski reformulated Einstein’s Special Theory of Relativity in this 4-dimensional Euclidean space-time vector space and concluded that the spatial variables $q_i$, where $(i = 1, 2, 3)$, plus the time $q_0 = ict$ are equivalent variables and should be treated equally using a covariant representation of both space and time. The idea of using an imaginary time axis $ict$ to make space-time Euclidean was elegant, but it obscured the non-Euclidean nature of space-time as well as causing difficulties when generalized to non-inertial accelerating frames in the General Theory of Relativity. As a consequence, the use of the imaginary $ict$ has been abandoned in modern work. Minkowski developed an alternative non-Euclidean metric that treats all four coordinates $(ct, x, y, z)$ as a four-dimensional Minkowski metric with all coordinates being real, and introduces the required minus sign explicitly.

Analogous to the usual 3-dimensional cartesian coordinates, the displacement four vector $d\mathbf{s}$ is defined using the four components along the **four unit vectors** in either the unprimed or primed coordinate frames.

$$
\begin{align} d\mathbf{s} &= dx^0\mathbf{\hat{e}}_0 + dx^1\mathbf{\hat{e}}_1 + dx^2\mathbf{\hat{e}}_2 + dx^3\mathbf{\hat{e}}_3 \nonumber \\[4pt] &= dx^{\prime 0}\mathbf{\hat{e}}^{\prime}_0 + dx^{\prime 1}\mathbf{\hat{e}}^{\prime}_1 + dx^{\prime 2}\mathbf{\hat{e}}^{\prime}_2 + dx^{\prime 3}\mathbf{\hat{e}}^{\prime}_3 \tag{17.31} \label{eq-17-31} \end{align}
$$

The convention used is that greek subscripts (covariant) or superscripts (contravariant) designate a four vector with $0 \leq \mu \leq 3$. The covariant unit vectors $\mathbf{\hat{e}}_{\mu}$ are written with the subscript $\mu$ which has 4 values $0 \leq \mu \leq 3$. As described in appendix $19.5.3$, using the Einstein convention the components are written with the contravariant superscript $dx^{\mu}$ where the time axis $x^0 = ct$, while the spatial coordinates, expressed in cartesian coordinates, are $x^1 = x$, $x^2 = y$, and $x^3 = z$. With respect to a different (primed) unit vector basis $\mathbf{\hat{e}}^{\prime}_{\mu}$, the displacement must be unchanged as given by Equation [17.31](#eq-17-31). In addition, Equation [17.43](#eq-17-43) shows that the magnitude $|ds|^2$ of the displacement four vector is invariant to a Lorentz transformation.

The most general Lorentz transformation between inertial coordinate systems $S$ and $S^{\prime}$, in relative motion with velocity $\mathbf{v}$, assuming that the two sets of axes are aligned, and that their origins overlap when $t = t^{\prime} = 0$, is given by the symmetric matrix $\lambda$ where

$$
x^{\prime \mu} = \sum_{\nu} \lambda_{\mu\nu} x^{\nu} \tag{17.32} \label{eq-17-32}
$$

This Lorentz transformation of the *four vector* $\mathbb{X}$ components can be written in matrix form as

$$
\mathbb{X}^{\prime} = \boldsymbol{\lambda}\mathbb{X} \tag{17.33} \label{eq-17-33}
$$

Assuming that the two sets of axes are aligned, then the elements of the Lorentz transformation $\lambda_{ \mu \nu }$ are given by

$$
\mathbb{X}^{\prime} = \begin{pmatrix} ct^{\prime} \\ x^{\prime 1} \\ x^{\prime 2} \\ x^{\prime 3} \end{pmatrix} = \begin{pmatrix} \gamma & −\gamma \beta_1 & −\gamma \beta_2 & −\gamma \beta_3 \\ −\gamma \beta_1 & 1+(\gamma − 1) \frac{\beta^2_1}{ \beta^2} & (\gamma − 1) \frac{\beta_1\beta_2}{ \beta^2} & (\gamma − 1) \frac{\beta_1\beta_3}{ \beta^2} \\ −\gamma \beta_2 & (\gamma − 1) \frac{\beta_1\beta_2}{ \beta^2} & 1+(\gamma − 1) \frac{\beta^2_2}{ \beta^2} & (\gamma − 1) \frac{\beta_2\beta_3}{ \beta^2} \\ −\gamma \beta_3 & (\gamma − 1) \frac{\beta_1\beta_3}{ \beta^2} & (\gamma − 1) \frac{\beta_2\beta_3}{ \beta^2} & 1+(\gamma − 1) \frac{\beta^2_3}{ \beta^2} \end{pmatrix} \cdot \begin{pmatrix} ct \\ x^1 \\ x^2 \\ x^3 \end{pmatrix} \tag{17.34} \label{eq-17-34}
$$

where $\beta = \frac{v}{ c}$ and $\gamma = \frac{1}{\sqrt{ 1−\beta^2}}$ and assuming that the origin of $S$ transforms to the origin of $S^{\prime}$ at $(0, 0, 0, 0)$.

For the case illustrated in Figure $17.2.1$, where the corresponding axes of the two frames are parallel and in relative motion with velocity $v$ in the $x_1$ direction, then the Lorentz transformation matrix [17.34](#eq-17-34) reduces to

$$
\begin{pmatrix} ct^{\prime} \\ x^{\prime 1} \\ x^{\prime 2} \\ x^{\prime 3} \end{pmatrix} = \begin{pmatrix} \gamma & −\beta\gamma & 0 & 0 \\ −\beta\gamma & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} ct \\ x^1 \\ x^2 \\ x^3 \end{pmatrix} \tag{17.35} \label{eq-17-35}
$$

This Lorentz transformation matrix is called a *standard boost* since it only boosts from one frame to another parallel frame. In general a rotation matrix also is incorporated into the transformation matrix $\lambda$ for the spatial variables.

### Four-vector scalar products

Scalar products of vectors and tensors usually are invariant to rotations in three-dimensional space providing an easy way to solve problems. The scalar, or inner, product of two four vectors is defined by

$$
\begin{align} \mathbb{X} \cdot \mathbb{Y} &= g_{\mu\nu} X^{\mu} Y^{\nu} \\[4pt] &= ( X^0 X^1 X^2 X^3 ) \cdot \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & −1 & 0 & 0 \\ 0 & 0 & −1 & 0 \\ 0 & 0 & 0 & −1 \end{pmatrix} \cdot \begin{pmatrix} Y^0 \\ Y^1 \\ Y^2 \\ Y^3 \end{pmatrix} \\[4pt] \tag{17.36} \label{eq-17-36} &= X^0Y^0 − X^1Y^1 − X^2Y^2 − X^3Y^3 \end{align}
$$

The correct sign of the inner product is obtained by inclusion of the *Minkowski metric* $g$ defined by

$$
g_{\mu\nu} \equiv \mathbf{\hat{e}}_{\mu} \cdot \mathbf{\hat{e}}_{\nu} \tag{17.37} \label{eq-17-37}
$$

that is, it can be represented by the matrix

$$
g \equiv \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & −1 & 0 & 0 \\ 0 & 0 & −1 & 0 \\ 0 & 0 & 0 & −1 \end{pmatrix} \tag{17.38} \label{eq-17-38}
$$

The sign convention used in the Minkowski metric, Equation [17.38](#eq-17-38), has been chosen with the time coordinate $(ct)^2$ positive which makes $(ds)^2 > 0$ for objects moving at less than the speed of light and corresponds to $ds$ being real.[^17-5-1]

The presence of the Minkowski metric matrix, in the inner product of four vectors, complicates General Relativity and thus the Einstein convention has been adopted where the components of the *contravariant four-vector* $\mathbb{X}$ are written with superscripts $X^{\mu}$. See also appendix $19.6$. The corresponding *covariant four-vector* components are written with the subscript $X_{\mu}$ which is related to the contravariant four-vector components $X^{\nu}$ using the $\mu\nu$ component of the covariant Minkowski metric matrix $\mathbf{g}$. That is

$$
X_{\mu} = \sum^3_{\nu =0} g_{\mu\nu} X^{\nu} \tag{17.39} \label{eq-17-39}
$$

The contravariant metric component $g^{\mu\nu}$ is defined as the $\mu\nu$ component of the inverse metric matrix $\mathbf{g}^{−1}$ where

$$
\mathbf{gg}^{−1} = \mathbf{I} = \mathbf{g}^{−1} \mathbf{g} \tag{17.40} \label{eq-17-40}
$$

where $\mathbf{I}$ is the four-vector identity matrix. The contravariant components of the four vector can be expressed in terms of the covariant components as

$$
X^{\mu} = \sum^3_{\nu =0} g^{\mu\nu} X_{\nu} \tag{17.41} \label{eq-17-41}
$$

Thus equations [17.39](#eq-17-39) and [17.41](#eq-17-41) can be used to transform between covariant and contravariant four vectors, that is, to raise or lower the index $\mu$.

The scalar inner product of two four vectors can be written compactly as the scalar product of a covariant four vector and a contravariant four vector. The Minkowski metric matrix can be absorbed into either $\mathbb{X}$ or $\mathbb{Y}$ thus

$$
\begin{align} \mathbb{X} \cdot \mathbb{Y} &= \sum^3_{\mu=0} \sum^3_{\nu =0} g_{\mu v} X^{\mu}Y^{\nu} \\[4pt] &= \sum^3_{\nu =0} X_{\nu} Y^{\nu} \\[4pt] &= \sum^3_{\mu=0} X^{\mu} Y_{\mu} \tag{17.42} \label{eq-17-42} \end{align}
$$

If this covariant expression is Lorentz invariant in one coordinate system, then it is Lorentz invariant in all coordinate systems obtained by proper Lorentz transformations.

The scalar inner product of the invariant space-time interval is an especially important example.

$$
\begin{align} (ds)^2 \equiv \mathbb{X}\cdot\mathbb{X} &= c^2 (dt)^{\mathbf{2}} − (d\mathbf{r})^2 \\[4pt] &= (cdt)^2 −\sum^3_{i=1} dx^2_i = (cd\tau)^2 \tag{17.43} \label{eq-17-43} \end{align}
$$

This is invariant to a Lorentz transformation as can be shown by applying the Lorentz standard boost transformation given above. In particular, if $S^{\prime}$ is the rest frame of the clock, then the invariant space-time interval $ds$ is simply given by the proper time interval $d\tau$.

### Minkowski Space-Time

[Figure 17.5.1](#fig-17-5-1) illustrates a three-dimensional $( ct, x^1, x^2)$ representation of the 4−dimensional space-time diagram where it is assumed that $x^3 = 0$. The fact that the velocity of light has a fixed velocity leads to the concept of the light cone defined by the locus of $|x| = ct$.

:::{figure} ../images/lt-21262-16.5.1.png
:label: fig-17-5-1
:enumerator: 17.5.1
:alt: The light cone in the ct, x_1, x_2 space is defined by the condition \mathbb{X} \cdot \mathbb{X} = c^2t^2 − r^2 = 0 and divides space-time into the forward and backward light cones, with t > 0 and t < 0 respectively; the interiors of the forward and backward light cones are called absolute future…

The light cone in the $ct$, $x_1$, $x_2$ space is defined by the condition $\mathbb{X} \cdot \mathbb{X} = c^2t^2 − r^2 = 0$ and divides space-time into the forward and backward light cones, with $t > 0$ and $t < 0$ respectively; the interiors of the forward and backward light cones are called absolute future and absolute past.
:::

#### Inside the light cone

The vertex of the cones represent the present. Locations inside the upper cone represent the future while the past is represented by locations inside the lower cone. Note that $(ds)^2 = c^2 (dt)^{\mathbf{2}} − (d\mathbf{r})^2 > 0$ inside both the future and past light cones. Thus the space-time interval $c\Delta t$ is real and positive for the future, whereas it is real and negative for the past relative to the vertex of the light cone. A **world line** is the trajectory a particle follows is a function of time in Minkowski space. In the interior of the future light cone $\Delta t > 0$ and, since it is real, it can be asserted unambiguously that any point inside this forward cone must occur later than at the vertex of the cone, that is, it is the absolute future. A Lorentz transformation can rotate Minkowski space such that the axis $x_0$ goes through any point within this light cone and then the “world line” is pure **time like**. Similarly, any point inside the backward light cone unambiguously occurred before the vertex, i.e. it is absolute past.

#### Outside the Light Cone

Outside of the light cone, has

$$
(ds)^2 = c^2 (dt)^{\mathbf{2}} − (d\mathbf{r})^2 < 0 \nonumber
$$

and thus $\Delta s$ is imaginary and is called **space like**. A spacelike plane hypersurface in spatial coordinates is shown for the present time in the unprimed frame. A rotation in Minkowski space can be made to $s^{\prime}$ such that the space-like hypersurface now is tilted relative to the hypersurface shown and thus any point $P$ outside the light cone can be made to occur later, simultaneous, or earlier than at the vertex depending on the orientation of the space-like hypersurface. This startling situation implies that the time ordering of two points, each outside the others light cone, can be reversed which has profound implications related to the concept of simultaneity and the notion of causality.

For the special case of two events lying on the light cone:

$$
\sum^4_{\mu} x^2_{\mu} = c^2t^2 − ( x^2_1 + x^2_2 + x^2_3 ) = 0 \nonumber
$$

and thus these events are separated by a light ray travelling at velocity $c$. Only events separated by time-like intervals can be connected causally. The world line of a particle must lie within its light cone. The division of intervals into space-like and time-like, because of their invariance, is an absolute concept. That is, it is independent of the frame of reference.

The concept of proper time can be expanded by considering a clock at rest in frame $S^{\prime}$ which is moving with uniform velocity $v$ with respect to a rest frame $S$. The clock at rest in the $S^{\prime}$ frame measures the **proper time**$\tau$, then the time observed in the fixed frame can be obtained by looking at the interval $ds$. Because of the invariance of the interval, $ds^2$ then

$$
\begin{align} ds^2 &= c^2d\tau^2 \\[4pt] &= c^2dt^2 − [ dx^2_1 + dx^2_2 + dx^2_3 ] \tag{17.44} \label{eq-17-44} \end{align}
$$

That is,

$$
\begin{align} d\tau &= dt \sqrt{ 1 − \frac{ dx^2_1 + dx^2_2 + dx^2_3 }{ c^2dt^2} } \\[4pt] &= dt \sqrt { 1 − \frac{v^2}{ c^2} } = \frac{dt}{ \gamma} \tag{17.45} \label{eq-17-45} \end{align}
$$

that is $dt = \gamma d\tau$ which satisfies the normal expression for time dilation, $(17.3.5)$.

### Momentum-energy four vector

The previous four-vector discussion can be elegantly exploited using the covariant Minkowski space-time representation. Separating the spatial and time of the differential four vector gives

$$
d\mathbb{X} = (cdt, d\mathbf{x}) \tag{17.46} \label{eq-17-46}
$$

Remember that the square of the four-dimensional space-time element of length $(ds)^2$ is invariant [17.43](#eq-17-43), and is simply related to the proper time element $d\tau$. Thus the scalar product

$$
d\mathbb{X}\cdot d\mathbb{X} = ds^2 = c^2d\tau^2 = c^2dt^2 − [ dx^2_1 + dx^2_2 + dx^2_3 ] \tag{17.47} \label{eq-17-47}
$$

Thus the proper time is an invariant.

The ratio of the four-vector element $d\mathbb{X}$ and the invariant proper time interval $d\tau$, is a four-vector called the *four-vector velocity* $\mathbb{U}$ where

$$
\mathbb{U} = \frac{d\mathbb{X}}{ d\tau} = \left( c \frac{dt}{ d\tau }, \frac{dx}{ d\tau} \right) = \gamma_u \left( c, \frac{d\mathbf{x}}{ dt} \right) = \gamma_u (c, \mathbf{u}) \tag{17.48} \label{eq-17-48}
$$

where $\mathbf{u}$ is the particle velocity, and $\gamma_u = \frac{1}{\sqrt{(1 - \frac{u^2}{c^2})}}$.

The four-vector momentum $\mathbb{P}$ can be obtained from the four-vector velocity by multiplying it by the scalar rest mass $m$

$$
\mathbb{P} = m\mathbb{U} = (\gamma_u mc, \gamma_u m\mathbf{u}) \tag{17.49} \label{eq-17-49}
$$

However,

$$
\gamma_u mc = \frac{E}{c} \tag{17.50} \label{eq-17-50}
$$

thus the momentum four vector can be written as

$$
\mathbb{P} = \left(\frac{E}{c} , \mathbf{p} \right) \tag{17.51} \label{eq-17-51}
$$

where the vector $\mathbf{p}$ represents the three spatial components of the relativistic momentum. It is interesting to realize that the Theory of Relativity couples not only the spatial and time coordinates, but also, it couples their conjugate variables linear momentum $\mathbf{p}$ and total energy, $\frac{E}{c}$.

An additional feature of this momentum-energy four vector $\mathbb{P}$, is that the scalar inner product $\mathbb{P} \cdot \mathbb{P}$ is invariant to Lorentz transformations and equals $(mc)^2$ in the rest frame

$$
\begin{align} \mathbb{P} \cdot \mathbb{P} &= \sum^3_{\mu=0} \sum^3_{\nu =0} g_{\mu\nu} P^{ \mu} P^{\nu} \\[4pt] &= \sum^3_{\mu=0} \sum^3_{\nu =0} P_{\mu}P^{\nu} \\[4pt] &= \left(\frac{E}{c} \right)^2 − |\mathbf{p}|^2 \\[4pt] &= m^2c^2 \tag{17.52} \label{eq-17-52} \end{align}
$$

which leads to the well-known equation

$$
E^2 = p^2c^2 + E^2_0 \tag{17.53} \label{eq-17-53}
$$

The Lorentz transformation matrix $\lambda$ can be applied to $\mathbb{P}$

$$
\mathbb{P} = \boldsymbol{\lambda}\mathbb{P} \tag{17.54} \label{eq-17-54}
$$

The Lorentz invariant four-vector representation is illustrated by applying the Lorentz transformation shown in Figure $17.2.1$, which gives, $p^{\prime}_1 = \gamma \left(p_1 - (\frac{v}{c})^2 E \right)$, $p^{\prime}_2 = p_2$, $p^{\prime}_3 = p_3$, and $E^{\prime} = \gamma (E − vp_1)$.

[^17-5-1]: Older textbooks, such as all editions of Marion, and the first two editions of Goldstein, use the Euclidean Poincaré 4-dimensional space-time with the imaginary time axis $ict$. About half the scientific community, and modern physics textbooks including this textbook, and the 3$^{rd}$ edition of Goldstein, use the Bjorken - Drell $+, −, −, −$, sign convention given in Equation [17.38](#eq-17-38) where $x_0 \equiv ct$, and $x_1, x_2, x_3$ are the spatial coordinates. The other half of the community, including mathematicians and gravitation physicists, use the opposite $−, +, +, +$, sign convention. Further confusion is caused by a few books that assign the time axis $ct$ to be $x_4$ rather than $x_0$.

## 17.6: Lorentz-Invariant Formulation of Lagrangian Mechanics

### Parametric Formulation

The Lagrangian and Hamiltonian formalisms in classical mechanics are based on the Newtonian concept of absolute time $t$ which serves as the system evolution parameter in Hamilton’s Principle. This approach violates the Special Theory of Relativity. The extended Lagrangian and Hamiltonian formalism is a parametric approach, pioneered by Lanczos[La49], that introduces a system evolution parameter $s$ that serves as the independent variable in the action integral, and all the space-time variables $q_i (s), t(s)$ are dependent on the evolution parameter $s$. This extended Lagrangian and Hamiltonian formalism renders it to a form that is compatible with the Special Theory of Relativity. The importance of the Lorentz-invariant extended formulation of Lagrangian and Hamiltonian mechanics has been recognized for decades.[La49, Go50, Sy60] Recently there has been a resurgence of interest in the extended Lagrangian and Hamiltonian formalism stimulated by the papers of Struckmeier[Str05, Str08] and this formalism has featured prominently in recent textbooks by Johns[Jo05] and Greiner[Gr10]. This parametric approach develops manifestly-covariant Lagrangian and Hamiltonian formalisms that treat equally all $2n+1$ space-time canonical variables. It provides a plausible manifestly-covariant Lagrangian for the one-body system, but serious problems exist extending this to the $N$-body system when $N > 1$. Generalizing the Lagrangian and Hamiltonian formalisms into the domain of the Special Theory of Relativity is of fundamental importance to physics, while the parametric approach gives insight into the philosophy underlying use of variational methods in classical mechanics.[^17-6-1]

In conventional Lagrangian mechanics, the equations of motion for the $n$ generalized coordinates are derived by minimizing the action integral, that is, Hamilton’s Principle.

$$
\delta S (\mathbf{q}, \mathbf{\dot{q}},t) = \delta \int^b_a L(\mathbf{q}(t), \mathbf{\dot{q}}(t),t) dt = 0 \tag{17.55} \label{eq-17-55}
$$

where $L(\mathbf{q}(t), \mathbf{\dot{q}}(t),t)$ denotes the conventional Lagrangian. This approach implicitly assumes the Newtonian concept of absolute time $t$ which is chosen to be the independent variable that characterizes the evolution parameter of the system. The actual path $[\mathbf{q}(t), \mathbf{\dot{q}}(t)]$ the system follows is defined by the extremum of the action integral $S(\mathbf{q}, \mathbf{\dot{q}},t)$ which leads to the corresponding Euler-Lagrange equations. This assumption is contrary to the Theory of Relativity which requires that the space and time variables be treated equally, that is, the Lagrangian formalism must be covariant.

### Extended Lagrangian

Lanczos[La49] proposed making the Lagrangian covariant by introducing a general evolution parameter $s$, and treating the time as a dependent variable $t(s)$ on an equal footing with the configuration space variables $q^i (s)$. That is, the time becomes a dependent variable $q_0(s) = ct(s)$ similar to the spatial variables $q_{\mu} (s)$ where $1 \leq \mu \leq n$. The dynamical system then is described as motion confined to a hypersurface within an extended space where the value of the extended Hamiltonian and the evolution parameter $s$ constitute an additional pair of canonically conjugate variables in the extended space. That is, the canonical momentum $p_0$, corresponding to $q_0 = ct$, is $p_0 = \frac{E}{c}$ similar to the momentum-energy four vector, equation $(17.5.21)$.

An *extended Lagrangian* $\mathbb{L}(\mathbf{q}(s), \frac{d\mathbf{q}(s) }{ds },t(s), \frac{dt(s)}{ ds} )$ can be defined which can be written compactly as $\mathbb{L}(q^{\mu} (s), \frac{dq^{\mu }(s)}{ ds} )$ where the index $0 \leq \mu \leq n$ denotes the entire range of space-time variables.

This extended Lagrangian can be used in an extended action functional $\mathbb{S}(\mathbf{q}, \frac{d\mathbf{q} }{ds} ,t, \frac{dt}{ ds} )$ to give an extended version of Hamilton’s Principle[^17-6-2]

$$
\delta \mathbb{S}(\mathbf{q}, \frac{d\mathbf{q} }{ds} ,t, \frac{dt }{ds} ) = \delta \int^b_a \mathbb{L}(q^{\mu }(s), \frac{dq^{\mu} (s)}{ ds })ds = 0 \tag{17.56} \label{eq-17-56}
$$

The conventional action $S$, and extended action $\mathbb{S}$, address alternate characterizations of the same underlying physical system, and thus the action principle implies that $\delta S = \delta \mathbb{S} = 0$ must hold simultaneously. That is,

$$
\delta \int^b_a L(\mathbf{q}, \frac{d\mathbf{q}}{ dt} ,t) \frac{dt}{ ds} ds = \delta \int^b_a \mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ ds} ,t, \frac{dt}{ds})ds \tag{17.57} \label{eq-17-57}
$$

As discussed in chapter $9.3$, there is a continuous spectrum of equivalent gauge-invariant Lagrangians for which the Euler-Lagrange equations lead to identical equations of motion. Equation [17.57](#eq-17-57) is satisfied if the conventional and extended Lagrangians are related by

$$
\mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds},t, \frac{dt}{ds} ) = L(\mathbf{q}, \frac{d\mathbf{q}}{ dt },t) \frac{dt}{ ds} + \frac{d\Lambda (\mathbf{q},t)}{ ds} \tag{17.58} \label{eq-17-58}
$$

where $\Lambda (\mathbf{q},t)$ is a continuous function of $\mathbf{q}$ and $t$ that has continuous second derivatives. It is acceptable to assume that $\frac{d\Lambda (\mathbf{q},t)}{ ds} = 0$, then the extended and conventional Lagrangians have a unique relation requiring no simultaneous transformation of the dynamical variables. That is, assume

$$
\mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds},t, \frac{dt}{ds}) = L(\mathbf{q}, \frac{d\mathbf{q}}{ dt },t) \frac{dt}{ ds} \tag{17.59} \label{eq-17-59}
$$

Note that the time derivative of $\mathbf{q}$ can be expressed in terms of the $s$ derivatives by

$$
\frac{d\mathbf{q}}{ dt} = \frac{d\mathbf{q}/ds}{ dt/ds} \tag{17.60} \label{eq-17-60}
$$

Thus, for a conventional Lagrangian with $n$ variables, the corresponding extended Lagrangian is a function of $n + 1$ variables while the conventional and extended Lagrangians are related using equations [17.59](#eq-17-59), and [17.60](#eq-17-60).

The derivatives of the relation between the extended and conventional Lagrangians lead to

$$
\frac{\partial \mathbb{L}}{ \partial q^{\mu}} = \frac{\partial L}{ \partial q^{\mu}} \frac{dt}{ds} \tag{17.61} \label{eq-17-61}
$$

$$
\frac{\partial \mathbb{L}}{ \partial t} = \frac{\partial L}{ \partial t} \frac{dt}{ds} \tag{17.62} \label{eq-17-62}
$$

$$
\frac{\partial \mathbb{L}}{ \partial \left(\frac{dq^{\mu} }{ ds} \right)} = \frac{\partial L}{ \partial \left(\frac{dq^{\mu}}{ dt} \right)} \tag{17.63} \label{eq-17-63}
$$

$$
\frac{\partial \mathbb{L} }{\partial \left( \frac{dt}{ds} \right)} = L −\sum^n_{ \mu =1} \frac{\partial L}{ \partial \left(\frac{dq^{\mu}}{ dt} \right)} \frac{dq^{\mu}}{ dt} \tag{17.64} \label{eq-17-64}
$$

where $1 \leq \mu \leq n$ since the $\mu = 0$ time derivatives are written explicitly in equations [17.62](#eq-17-62), [17.64](#eq-17-64).

Equations [17.63](#eq-17-63) — [17.64](#eq-17-64), summed over the extended range $0 \leq \mu \leq n$ of time and spatial dynamical variables, imply

$$
\sum^n_{\mu = 0} \frac{\partial \mathbb{L}}{ \partial \left(\frac{dq^{\mu}}{ ds } \right)} \left(\frac{dq^{\mu}}{ds} \right) = L\frac{dt}{ds} −\sum^n_{\mu =1} \frac{\partial L}{ \partial \left(\frac{dq^{\mu}}{dt} \right)} \frac{dq^{\mu}}{dt} \frac{dt}{ds} + \sum^n_{ i=1} \frac{\partial L}{ \partial \left(\frac{dq^{\mu}}{dt} \right)} \frac{dq^{\mu}}{ds} = \mathbb{L} \tag{17.65} \label{eq-17-65}
$$

Equation [17.65](#eq-17-65) can be written in the form

$$
\mathbb{L}−\sum^n_{\mu = 0} \frac{\partial \mathbb{L}}{ \partial \left(\frac{dq^{\mu}}{ds} \right)} \frac{dq^{\mu}}{ds} = \begin{cases} \underset{=}{\not\equiv} 0 \text{ if } \mathbb{L} \text{ is not homogeneous in } \frac{dq^{\mu}}{ds} \\ \equiv 0 \text{ if } \mathbb{L} \text{ is homogeneous in } \frac{dq^{\mu}}{ds} \end{cases} \tag{17.66} \label{eq-17-66}
$$

If the extended Lagrangian $\mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds},t, \frac{dt}{ds} )$ is homogeneous to first order in the $n+1$ variables $\frac{dq^{\mu}}{ds}$, then Euler’s theorem on homogeneous functions trivially implies the relation given in Equation [17.66](#eq-17-66). Struckmeier[Str08] identified a subtle but important point that if $\mathbb{L}$ is not homogeneous in $\frac{dq^{\mu}}{ds}$, then Equation [17.66](#eq-17-66) is not an identity but is an implicit equation that is always satisfied as the system evolves according to the solution of the extended Euler-Lagrange equations. Then Equation [17.59](#eq-17-59) is satisfied without it being a homogeneous form in the $n+1$ velocities $\frac{dq^{\mu}}{ds}$. This introduces a new class of non-homogeneous Lagrangians. The relativistic free particle, discussed in example 17.6.1, is a case of a non-homogeneous extended Lagrangian.

### Extended generalized momenta

The generalized momentum is defined by

$$
p_{\mu} = \frac{\partial L}{ \partial \left( \frac{\partial q^{\mu} }{\partial t} \right)} \tag{17.67} \label{eq-17-67}
$$

Assume that the definitions of the extended Lagrangian $\mathbb{L}$, and the extended Hamiltonian $\mathbb{H}$, are related by a Legendre transformation, and are based on variational principles, analogous to the relation that exists between the conventional Lagrangian $L$ and Hamiltonian $H$. The Legendre transformation requires defining the extended generalized (canonical) momentum-energy four vector $\mathbb{P}(s)= ( \frac{\mathbb{E}(s)}{ c} ,\mathbf{p}(s))$. The momentum components of the momentum-energy four vector $\mathbb{P}(s)= ( \frac{\mathbb{E}(s)}{ c} , \mathbf{p}(s))$ are given by the $1 \leq \mu \leq n$ components using Equation [17.63](#eq-17-63).

$$
p_{\mu} (s) = \frac{\partial \mathbb{L}}{ \partial \left(\frac{dq^{\mu}}{ds} \right)} = \frac{\partial L}{ \partial \left(\frac{dq^{\mu}}{dt} \right)} \tag{17.68} \label{eq-17-68}
$$

The $\mu = 0$ component of the momentum-energy four vector can be derived by recognizing that the right-hand side of Equation [17.64](#eq-17-64) is equal to $−H(p_{\mu }, q^{\mu }, t)$. That is, the corresponding generalized momentum $p_0$, that is conjugate to $q_0 = ct$, is given by

$$
p_0 = \frac{\partial \mathbb{L}}{ \partial \left(\frac{dq^0}{ ds} \right)} = \frac{1}{ c} \left( \frac{\partial \mathbb{L}}{ \partial \left( \frac{dt}{ds} \right) } \right) = \frac{1}{ c} \left(L − \sum^n_{\mu =1} \frac{\partial L}{ \partial \left(\frac{dq^{\mu}}{dt} \right)} \frac{dq^{\mu}}{dt} \right) = −\frac{H(p_{\mu} , q^{\mu} , t)}{ c} \tag{17.69} \label{eq-17-69}
$$

### Extended Lagrange equations of motion

By direct analogy with the non-relativistic action integral [17.55](#eq-17-55), the extremum for the relativistic action integral $S(\mathbf{q}, \frac{d\mathbf{q}}{ds},t, \frac{dt}{ds} )$ is obtained using the Euler-Lagrange equations derived from Equation [17.56](#eq-17-56) where the independent variable is $s$. This implies that for $0 \leq \mu \leq n$

$$
\frac{d}{ ds} \left( \frac{\partial \mathbb{L}}{ \partial \left(\frac{dq^{\mu}}{ds} \right)} \right) − \frac{\partial \mathbb{L}}{ \partial q^{\mu}} = \mathbb{Q}^{EX}_{\mu} = \sum^m_{ k=1} \frac{dt}{ds}\lambda_k \frac{\partial g_k}{ \partial q^{\mu} } + Q^{EXC}_{\mu} \frac{dt}{ds} \tag{17.70} \label{eq-17-70}
$$

where the extended generalized force $\mathbb{Q}^{EX}_{\mu}$ shown on the right-hand side of Equation [17.70](#eq-17-70), accounts for all forces not included in the potential energy term in the Lagrangian. The extended generalized force $\mathbb{Q}^{EX}_{\mu}$ can be factored into two terms as discussed in chapter $6$, equation $(6.5.12)$. The Lagrange multiplier term includes $1 \leq k \leq m$ holonomic constraint forces where the $m$ holonomic constraints, which do no work, are expressed in terms of the $m$ algebraic equations of holonomic constraint $g_k$. The $Q^{EXC}_{\mu}$ term includes the remaining constraint forces and generalized forces that are not included in the Lagrange multiplier term or the potential energy term of the Lagrangian.

For the case where $\mu = 0$, since $q_0 = ct$, then Equation [17.70](#eq-17-70) reduces to

$$
\frac{d}{ds} \left( \frac{\partial \mathbb{L}}{ \partial \left( \frac{dt}{ds} \right)} \right) − \frac{\partial \mathbb{L}}{ \partial t} = \sum^m_{k=1} \frac{dt}{ds}\lambda_k \frac{\partial g_k}{ \partial t} −\sum^n_{\nu =1} Q^{EXC}_{\nu} \frac{dq^{\nu}}{ ds} \tag{17.71} \label{eq-17-71}
$$

These Euler-Lagrange equations of motion [17.70](#eq-17-70), [17.71](#eq-17-71) determine the $1 \leq \mu \leq n$ generalized coordinates $q^{\mu} (s)$, plus $q^0 = ct(s)$ in terms of the independent variable $s$.

If the holonomic equations of constraint are time independent, that is $\frac{\partial g_k }{\partial t} = 0$ and if $\mathbb{Q}^{EXC}_0 = 0$, then the $\mu = 0$ term of the Euler-Lagrange equations simplifies to

$$
\frac{d}{ds} \left( \frac{\partial \mathbb{L}}{ \partial \left( \frac{dt}{ds} \right) } \right) − \frac{\partial \mathbb{L}}{ \partial t} = 0 \tag{17.72} \label{eq-17-72}
$$

One interpretation is to select $L$ to be primary. Then $\mathbb{L}$ is derived from $L$ using Equation [17.59](#eq-17-59) and $\mathbb{L}$ must satisfy the identity given by Equation [17.66](#eq-17-66) while the Euler-Lagrange equations containing $\frac{dt}{ds}$ yield an identity which implies that $L$ does not provide an equation of motion in terms of $t(s)$. Conversely, if $\mathbb{L}$ is chosen to be primary, then $\mathbb{L}$ is no longer a homogeneous function and Equation [17.66](#eq-17-66) serves as a constraint on the motion that can be used to deduce $L$, while $\frac{dt}{ds}$ yields a non-trivial equation of motion in terms of $t(s)$. In both cases the occurrence of a constraint surface results from the fact that the extended space has $2n + 2$ variables to describe $2n + 1$ degrees of freedom, that is, one more degree of freedom than required for the actual system.

::::{admonition} Example 17.6.1: Lagrangian for a relativistic free particle
:class: example

The standard Lagrangian $L = T − U$ is not Lorentz invariant. The extended Lagrangian $L(\mathbf{q}, \frac{d\mathbf{q}}{ds}, t, \frac{dt}{ds} )$ introduces the independent variable $s$ which treats both the space variables $q(s)$ and time variable $q_0 = ct(s)$ equally. This can be achieved by defining the non-standard Lagrangian

$$
\mathbb{L} \left(\mathbf{q}, \frac{d\mathbf{q}}{ds},t, \frac{dt}{ds} \right) = \frac{1}{ 2} mc^2 \left[ \frac{1}{ c^2} \left(\frac{d\mathbf{q}}{ ds} \right)^2 − \left( \frac{dt}{ds} \right)^2 − 1 \right] \tag{$\alpha$}\label{eq-17-alpha}
$$

The constant third term in the bracket is included to ensure that the extended Lagrangian converges to the standard Lagrangian in the limit $\frac{dt}{ds} \rightarrow 1$.

Note that the extended Lagrangian [$\alpha$](#eq-17-alpha) is not homogeneous to first order in the velocities $\frac{d\mathbf{q}}{ ds}$ as is required. Equation [17.66](#eq-17-66) must be used to ensure that Equation [$\alpha$](#eq-17-alpha) is homogeneous. That is, it must satisfy the constraint relation

$$
\left( \frac{dt}{ds}\right)^2 − \frac{1}{ c^2} \left(\frac{d\mathbf{q}}{ ds} \right)^2 − 1=0 \label{eq-17-beta}\tag{$\beta$}
$$

Inserting [$\beta$](#eq-17-beta) into the extended Lagrangian [$\alpha$](#eq-17-alpha) yields that the square bracket in Equation [$\alpha$](#eq-17-alpha) must equal 2. Thus

$$
|\mathbb{L}| = \frac{1}{ 2} mc^2 [−2] = −mc^2 \label{eq-17-gamma}\tag{$\gamma$}
$$

The constraint Equation [$\beta$](#eq-17-beta) implies that

$$
\frac{ds}{ dt} = \sqrt{1 − \frac{1}{ c^2} \left(\frac{d\mathbf{q}}{ dt} \right)^2} = \frac{1}{ \gamma} \tag{$\delta$}\label{eq-17-delta}
$$

Using Equation [$\delta$](#eq-17-delta) gives that the relativistic Lagrangian is

$$
L = \frac{\mathbb{L}}{ \gamma} = −\frac{mc^2}{ \gamma} = −mc^2 \sqrt{ 1 − \beta^2} \label{eq-17-epsilon}\tag{$\epsilon$}
$$

Equation [$\epsilon$](#eq-17-epsilon) is the conventional relativistic Lagrangian derived by assuming that the system evolution parameter $s$ is transformed to be along the world line $ds$, where the invariant length $ds$ replaces the proper time interval

$$
ds = cd\tau = \frac{cdt}{ \gamma} \label{eq-17-varepsilon}\tag{$\varepsilon$}
$$

The definition of the generalized (canonical) momentum

$$
p_i = \frac{\partial L}{ d\dot{q}_i} = \gamma m\dot{q}_i \label{eq-17-varsigma}\tag{$\varsigma$}
$$

leads to the relativistic expression for momentum given in equation $(17.4.6)$.

The relativistic Lagrangian is an important example of a non-standard Lagrangian. Equation [$\alpha$](#eq-17-alpha) does not equal the difference between the kinetic and potential energies, that is, the relativistic expression for kinetic energy is given by $(17.4.13)$ to be

$$
T = (\gamma − 1) mc^2 \label{eq-17-eta}\tag{$\eta$}
$$

The non-standard relativistic Lagrangian [$\epsilon$](#eq-17-epsilon) can be used with the Euler-Lagrange equations to derive the second-order equations of motion for both relativistic and non-relativistic problems within the Special Theory of Relativity.
::::

::::{admonition} Example 17.6.2: Relativistic particle in an external electromagnetic field
:class: example

A charged particle moving at relativistic speed in an external electromagnetic field provides an example of the use of the relativistic Lagrangian.

In the discussion of classical mechanics it was shown that the velocity-dependent Lorentz force can be absorbed into the scalar electric potential $\Phi$ plus the vector magnetic potential $\mathbf{A}$. That is, the potential energy is given by equation $(17.3.4)$ to be $U = q(\Phi − \mathbf{A} \cdot \mathbf{v})$. Including this in the Lagrangian, [17.71](#eq-17-71), gives

$$
L = −\frac{mc^2}{ \gamma} − U = −mc^2 \sqrt{1 − \beta^2} − q\Phi + q\mathbf{A} \cdot \mathbf{v} \nonumber
$$

The three spatial partial derivatives can be written in vector notation as

$$
\frac{\partial L}{ \partial \mathbf{r}} = −q\boldsymbol{\nabla}\Phi + \frac{q}{ c} \boldsymbol{\nabla}(\mathbf{v} \cdot \mathbf{A}) \label{eq-17-a-2}\tag{a}
$$

and the generalized momentum is given by

$$
\mathbf{p} = \frac{\partial L}{ d\mathbf{v}} = \gamma m \mathbf{v} + q\mathbf{A} \nonumber
$$

which is identical to the non-relativistic answer given by equation 7.6. That is, it includes the momentum of the electromagnetic field plus the classical linear momentum of the moving particle.

The total time derivative of the generalized momentum is

$$
\frac{d\mathbf{p}}{ dt} = \frac{d}{dt} \left(\frac{\partial L}{ d\mathbf{v}} \right) = \frac{d}{dt}(\gamma m \mathbf{v}) + q \frac{d\mathbf{A}}{ dt} \label{eq-17-b-2}\tag{b}
$$

where the last term is given by the chain rule

$$
\frac{d\mathbf{A}}{ dt} = \frac{\partial \mathbf{A}}{\partial t} + (\mathbf{v} \cdot \boldsymbol{\nabla})\mathbf{A} \label{eq-17-c}\tag{c}
$$

Using equations [a](#eq-17-a), [b](#eq-17-b), [c](#eq-17-c) in the Euler-Lagrange equation gives

$$
\frac{d}{dt} \left(\frac{\partial L}{ d\mathbf{v}} \right) = \frac{\partial L}{ \partial \mathbf{r}} \nonumber
$$

$$
\frac{d}{dt}(\gamma m \mathbf{v}) + q \frac{d\mathbf{A}}{ dt} = −q\boldsymbol{\nabla}\Phi + q\boldsymbol{\nabla}(\mathbf{v} \cdot \mathbf{A}) \nonumber
$$

Collecting terms and using the well-known vector-product identity, plus the definition $\mathbf{B} = \boldsymbol{\nabla} \times \mathbf{A}$, gives

$$
\begin{align*} \frac{d}{dt}(\gamma m \mathbf{v}) &= − \left[ q\boldsymbol{\nabla}\Phi − q \frac{\partial \mathbf{A}}{\partial t} \right] + q [\boldsymbol{\nabla}(\mathbf{v} \cdot \mathbf{A}) − (\mathbf{v} \cdot \boldsymbol{\nabla})\mathbf{A}] \\[4pt] &= −q \left[ \boldsymbol{\nabla}\Phi − \frac{\partial \mathbf{A}}{\partial t} \right] + q [\mathbf{v} \times \boldsymbol{\nabla} \times \mathbf{A}] \\[4pt] \mathbf{F} &= q [\mathbf{E} + \mathbf{v} \times \mathbf{B}] \end{align*}
$$

If we adopt the definition that the relativistic canonical momentum is $p = \gamma mv$ then the left hand side is the relativistic force while the right-hand side is the well-known Lorentz force of electromagnetism. Thus the extended Lagrangian formulation correctly reproduces the well-known Lorentz force for a charged particle moving in an electromagnetic field.
::::

[^17-6-1]: Chapters $17.6$ and $17.7$ reproduce the Struckmeier presentation.[Str08]

[^17-6-2]: These formula involve total and partial derivatives with respect to both time, $t$ and parameter $s$. For clarity, the derivatives are written out in full because Lanczos[La49] and Johns[Jo05] use the opposite convention for the dot and prime superscripts as abbreviations for the differentials with respect to $t$ and $s$. The blackboard bold format is used to designate the extended versions of the action $\mathbb{S}$, Lagrangian $\mathbb{ L}$ and Hamiltonian $\mathbb{ H}$.

## 17.7: Lorentz-invariant formulations of Hamiltonian Mechanics

### Extended Canonical Formalism

A Lorentz-invariant formulation of Hamiltonian mechanics can be developed that is built upon the extended Lagrangian formalism assuming that the Hamiltonian and Lagrangian are related by a Legendre transformation. That is,

$$
H(\mathbf{q}, \mathbf{p}, t) = \sum^n_{\mu =1} p_{\mu} \frac{\partial q^{\mu}}{\partial t} − L(\mathbf{q}, \frac{\partial \mathbf{q}}{\partial t} , t) \tag{17.73} \label{eq-17-73}
$$

where the generalized momentum is defined by

$$
p_{\mu} = \frac{\partial L}{ \partial \left( \frac{\partial q^{\mu}}{\partial t} \right)} \tag{17.74} \label{eq-17-74}
$$

Struckmeier[Str08] assumes that the definitions of the extended Lagrangian $\mathbb{L}$, and the extended Hamiltonian $\mathbb{H}$, are related by a Legendre transformation, and are based on variational principles, analogous to the relation that exists between the conventional Lagrangian $L$ and Hamiltonian $H$. The Legendre transformation requires defining the extended generalized (canonical) momentum-energy four vector $\mathbb{P}(s)= ( \frac{\mathbb{E} (s)}{c} , \mathbf{p}(s))$. The momentum components of the momentum-energy four vector $\mathbb{P}(s)= (\frac{\mathbb{E} (s)}{c} , \mathbf{p}(s))$ are given by the $1 \leq \mu \leq n$ components using either the conventional or the extended Lagrangians as given in Equation [17.68](#eq-17-68)

$$
p_{\mu} (s) = \frac{\partial \mathbb{L}}{ \partial \left(\frac{dq^{\mu}}{ds} \right)} = \frac{\partial L}{ \partial \left(\frac{dq^{\mu}}{dt} \right)} \tag{17.68}
$$

The $\mu = 0$ component of the momentum-energy four vector is given by equation $(17.6.15)$

$$
p_0 = \frac{1}{c} \left( \frac{\partial \mathbb{L}}{ \partial \left( \frac{dt}{ds} \right)} \right) = −\frac{H(p_{\mu} , q^{\mu} , t)}{ c} = −\frac{\mathcal{E} (s)}{ c} \tag{17.75} \label{eq-17-75}
$$

where $\mathcal{E} (s)$ represents the instantaneous generalized energy of the conventional Hamiltonian at the point $s$, but not the functional form of $H(\mathbf{q}(s), \mathbf{p}(s), t(s))$. That is

$$
\mathcal{E} (s) \underset{=}{\not\equiv} H(\mathbf{q}(s), \mathbf{p}(s), t(s)) \tag{17.76} \label{eq-17-76}
$$

Note that $\mathcal{E} (s)$ does not give the function $H(\mathbf{q}, \mathbf{p}, t)$. Equations [17.68](#eq-17-68) and $(17.6.15)$ give that

$$
p_0(s) = −\frac{\mathcal{E} (s)}{ c} \tag{17.77} \label{eq-17-77}
$$

The extended Hamiltonian $\mathbb{H}(\mathbf{q}, \mathbf{p}, t, \mathcal{E} (s))$, in an extended phase space, can be defined by the Legendre transformation and the four-vector $\mathbb{P}$ to be

$$
\begin{align} \mathbb{H}(\mathbf{q}, \mathbf{p}, t, \mathcal{E} (s)) &= (\mathbb{P} \cdot \mathbf{q}) − \mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds} ,t, \frac{dt}{ds} ) \tag{17.78} \label{eq-17-78} \\[4pt] &= \sum^n_{\mu =0} p_{\mu} \left(\frac{dq^{\mu}}{ds} \right) − \mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds} ,t, \frac{dt}{ds} ) \nonumber \\[4pt] &= \sum^n_{\mu =1} p_{\mu} \left(\frac{dq^{\mu}}{ds} \right) − \mathcal{E} \frac{dt}{ds} − \mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds} ,t, \frac{dt}{ds}) \tag{17.79} \end{align}
$$

where the $p_0$ term has been written explicitly as $−\mathcal{E} \frac{dt}{ds}$ in Equation [17.79](#eq-17-78). The extended Hamiltonian $\mathbb{H}((\mathbf{q}, \mathbf{p}, t, \mathcal{E} (s))$ can carry all the information on the dynamical system that is carried by the extended Lagrangian $\mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds} ,t, \frac{dt}{ds} )$, if the Hesse matrix is non-singular. That is, if

$$
\text{det } \left( \frac{\partial^2 \mathbb{L}}{ \partial \left(\frac{dq^{\mu}}{ds} \right)\partial \left(\frac{dq_{\nu}}{ ds} \right)} \right) \neq 0 \tag{17.80} \label{eq-17-80}
$$

If the extended Lagrangian $\mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds} ,t, \frac{dt}{ds} )$ is not homogeneous in the $n+1$ velocities $\frac{dq^{\mu}}{ds}$, then the extended set of Euler-Lagrange equations $(17.6.18)$ is not redundant. Thus equation $(17.6.12)$ is not an identity but it can be regarded as an implicit equation that is always satisfied by the extended set of Euler-Lagrange equations. As a result, the Legendre transformation to an extended Hamiltonian exists. That is, equation $(17.6.12)$ is identical to the Legendre transform for $\mathbb{H}((\mathbf{q},\mathbf{p}, t, \mathcal{E} (s))$ which was shown to equal zero. Therefore

$$
\mathbf{H}(\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s)) = 0 \tag{17.81} \label{eq-17-81}
$$

which means that the extended Hamiltonian $\mathbb{H}((\mathbf{q}, \mathbf{p}, t, \mathcal{E} (s))$ directly defines the restricted hypersurface on which the particle motion is confined.

The extended canonical equations of motion, derived using the extended Hamiltonian $\mathbb{H}(\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s))$ with the usual Hamiltonian mechanics relations, are:

$$
\begin{align} \frac{\partial \mathbb{H}}{ \partial p_{\mu}} &= \frac{dq^{\mu}}{ds} \tag{17.82} \label{eq-17-82} \\[4pt] \frac{\partial \mathbb{H}}{ \partial q^{\mu}} &= −\frac{dp_{\mu}}{ ds} \tag{17.83} \\ \frac{\partial \mathbb{H}}{ \partial t} &= \frac{d\mathcal{E}}{ds} \tag{17.84} \\ \frac{\partial \mathbb{H}}{ \partial \mathcal{E}} &= − \frac{dt}{ds} \tag{17.85} \end{align}
$$

These canonical equations give that the total derivative of $\mathbb{H}((\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s))$ with respect to $s$, is

$$
\begin{align} \frac{d\mathbb{H}}{ ds} &= \frac{\partial \mathbb{H}}{ \partial p_{\mu}} \frac{dp_{\mu}}{ ds} + \frac{\partial \mathbb{H}}{ \partial q^{\mu}} \frac{dq^{\mu}}{ds} + \frac{\partial \mathbb{H}}{ \partial t} \frac{dt}{ds} + \frac{\partial \mathbb{H}}{ \partial \mathcal{E}} \frac{d\mathcal{E}}{ds} \nonumber \\[4pt] &= \frac{dq^{\mu}}{ds} \frac{dp_{\mu} }{ds} − \frac{dp_{\mu}}{ ds} \frac{dq^{\mu}}{ds } + \frac{d\mathcal{E}}{ds} \frac{dt}{ds} − \frac{dt}{ds} \frac{d\mathcal{E}}{ds} = 0 \tag{17.86} \label{eq-17-86} \end{align}
$$

That is, in contrast to the total time derivative of $H(\mathbf{q}, \mathbf{p}, t)$, the total $s$ derivative of the extended Hamiltonian $\mathbb{H}((\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s))$ always vanishes, that is, $\mathbb{H}((\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s))$ is autonomous which is ideal for use with Hamilton’s equations of motion. The constraints give that $\mathbb{H}((\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s)) = 0$, (Equation [17.81](#eq-17-81)) and $\frac{d\mathbb{H}}{ ds} = 0$, (Equation [17.86](#eq-17-86)) implying that the correlation between the extended and conventional Hamiltonians is given by

$$
\begin{align}\mathbb{H}((\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s)) &= \sum^n_{\mu =1} p_{\mu} \left(\frac{dq^{\mu}}{ds} \right) − \mathcal{E} \frac{dt}{ds} − \mathbb{L}(\mathbf{q}, \frac{d\mathbf{q}}{ds} ,t, \frac{dt}{ds} ) \tag{17.87} \label{eq-17-87} \\[4pt] &= \sum^n_{\mu =1} p_{\mu} \left(\frac{dq^{\mu}}{ds} \right) − \mathcal{E} \frac{dt}{ds} − L(\mathbf{q}, \frac{d\mathbf{q}}{ds} ,t,) \frac{dt}{ds} \tag{17.88} \\[4pt] &= \sum^n_{\mu =1} p_{\mu} \left(\frac{dq^{\mu}}{ds} \right) − \mathcal{E} \frac{dt}{ds} + \left[ H(\mathbf{q},\mathbf{p}, t) −\sum^n_{\mu =1} p_{\mu} \left(\frac{dq^{\mu}}{dt} \right) \right] \frac{dt}{ds} \tag{17.89} \\[4pt] &= (H(\mathbf{q}, \mathbf{p}, t) − \mathcal{E} ) \frac{dt}{ds} = 0 \tag{17.90} \end{align}
$$

since only the term with $\mu = 0$ does not cancel in Equation [17.79](#eq-17-78). Equations [17.81](#eq-17-81) and [17.90](#eq-17-87) give that both the left and right-hand sides of Equation [17.90](#eq-17-87) are zero while Equation [17.86](#eq-17-86) implies that $\mathbb{H}((\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s))$ is a constant of motion, that is, $s$ is a cyclic variable for $\mathbb{H}((\mathbf{q}(s), \mathbf{p}(s), t(s), \mathcal{E} (s))$. Formally one can consider the extended Hamiltonian is a constant which equals zero

$$
\mathbb{H}(\mathbf{q}, \mathbf{p}, t, \mathcal{E} (s)) = \mathbb{E} (s)=0 \tag{17.91} \label{eq-17-91}
$$

Equations [17.84](#eq-17-82), [17.85](#eq-17-82) imply that $(\mathcal{E}, t)$ form a pair of canonically conjugate variables in addition to the newly-introduced canonically-conjugate variables $(\mathbb{E} (s), s)$. Equation [17.90](#eq-17-87) shows that the motion in the $2n + 2$ extended phase space is constrained to the surface reflecting the fact that the observed system has one less degree of freedom than used by the extended Hamiltonian.

In summary, the Lorentz-invariant extended canonical formalism leads to Hamilton’s first-order equations of motion in terms of derivatives with respect to $s$, where $s$ is related to the proper time $\tau$ for a relativistic system.

### Extended Poisson Bracket representation

Struckmeier[Str08] investigated the usefulness of the extended formalism when applied to the Poisson bracket representation of Hamiltonian mechanics. The extended Poisson bracket for two differentiable functions $F$ and $G$ is defined as

$$
\left\{\left\{ F,G \right\}\right\} = \sum^n_{j=1} \left( \frac{\partial F}{ \partial q^j} \frac{\partial G}{ \partial p_j} − \frac{\partial F}{ \partial p_j} \frac{\partial G}{ \partial q^j} \right) − \frac{\partial F}{ \partial t} \frac{\partial G}{ \partial H} + \frac{\partial F}{ \partial H} \frac{\partial G}{ \partial t} \tag{17.92} \label{eq-17-92}
$$

As for the conventional Poisson bracket discussed in chapter $15$, the extended Poisson also leads to the fundamental Poisson bracket relations

$$
\left\{\left\{ q^i,q^j \right\}\right\} = 0 \quad \left\{\left\{ p_i,p_j \right\}\right\} = 0 \quad \left\{\left\{ q^i,p_j \right\}\right\} = \delta^i_j \tag{17.93} \label{eq-17-93}
$$

where $i, j = 0, 1, \dots , n$. These are identical to the non-extended fundamental Poisson brackets.

The discussion of observables in Hamiltonian mechanics in chapter $15.2.5$ can be trivially expanded to the extended Poisson bracket representation. In particular, the total $s$ derivative of the function $G$ is given by

$$
\frac{dG}{ ds} = \frac{\partial G}{ \partial s} + \left\{\left\{ G, \mathbb{H} \right\}\right\} \tag{17.94} \label{eq-17-94}
$$

If $G$ commutes with the extended Hamiltonian, that is, the Poisson bracket equals zero, and if $\frac{\partial G}{ \partial s} = 0$, then $\frac{dG}{ ds} = 0$. That is, the observable $G$ is a constant of motion.

Substitute the fundamental variables for $G$ gives

$$
\frac{dp_{\mu} }{ds} = \left\{\left\{ p_{\mu}, \mathbb{H} \right\}\right\} = − \frac{\partial \mathbb{H}}{ \partial q^{\mu}} \quad \frac{dq^{\mu}}{ds} = \left\{\left\{ q^{\mu}, \mathbb{H} \right\}\right\} = \frac{\partial \mathbb{H}}{ \partial p_{\mu}} \tag{17.95} \label{eq-17-95}
$$

where $i, j = 0, 1, \dots , n$. These are Hamilton’s extended canonical equations of motion expressed in terms of the system evolution parameter $s$. The extended Poisson bracket representation is a trivial extension of the conventional canonical equations presented in chapter $15.3$.

### Extended canonical transformation and Hamilton-Jacobi theory

Struckmeier[Str08] presented plausible extended versions of canonical transformation and Hamilton-Jacobi theories that can be used to provide a Lorentz-invariant formulation of Hamiltonian mechanics for relativistic one-body systems. A detailed description can be found in Struckmeier[Str08].[^17-7-1]

### Validity of the extended Hamilton-Lagrange formalism

It has been shown that the extended Lagrangian and Hamiltonian formalism, based on the parametric model of Lanczos[La49], leads to a plausible manifestly-covariant approach for the one-body system. The general features developed for handling Lagrangian and Hamiltonian mechanics carry over to the Special Theory of Relativity assuming the use of a non-standard, extended Lagrangian or Hamiltonian. This expansion of the range of validity of the well-known Hamiltonian and Lagrangian mechanics into the relativistic domain is important, and reduces any Lorentz transformation to a canonical transformation. The validity of this extended Hamilton-Lagrange formalism has been criticized, and problems exist extending this approach to the $N$-body system for $N > 1$. For example, as discussed by Goldstein[Go50] and Johns[Jo05], each of the $N$ moving bodies have their own world lines and momenta. Defining the total momentum $\mathbf{P}$ requires knowing simultaneously the momenta of the individual bodies, but simultaneity is body dependent and thus even the total momentum is not a simple four vector. A general method is required that will allow using a manifestly-covariant Lagrangian or Hamiltonian for the $N$-body system. For the one-body system, the extended Hamilton-Lagrange formalism provides a powerful and logical approach to exploit analytical mechanics in the relativistic domain that retains the form of the conventional Lagrangian/Hamiltonian formalisms. Note that Noether’s theorem relating energy and time is readily apparent using the extended formalism.

::::{admonition} Example 17.7.1: The Bohr-Sommerfeld hydrogen atom
:class: example

The classical relativistic hydrogen atom was first solved by Sommerfeld in 1916. Sommerfeld used Bohr’s “old quantum theory” plus Hamiltonian mechanics to make an important step in the development of quantum mechanics by obtaining the first-order expressions for the fine structure of the hydrogen atom. As in the non-relativistic case, the motion is confined to a plane allowing use of planar polar coordinates. Thus the relativistic Lagrangian is given by

$$
\begin{align*} L &= −\frac{mc^2}{ \gamma } − U \\[4pt] &= −mc^2 \sqrt{ 1 − \frac{\dot{r}^2 + r^2 \dot{\theta}^2}{ c^2}} + \frac{ke^2}{ r} \end{align*}
$$

The canonical momenta are given by

$$
\begin{align*} p_{\theta} &= \frac{\partial L}{ \partial \dot{\theta}} = m\gamma r^2 \dot{\theta} \\[4pt] p_r &= \frac{\partial L}{ \partial \dot{r}} = m\gamma \dot{r} \\[4pt] \dot{p}_{\theta} &= \frac{\partial L}{ \partial \theta} = 0 \\[4pt] \dot{p}_r &= \frac{\partial L}{ \partial r} = m\gamma r \dot{\theta}^2 + k \frac{e^2}{ r^2} \end{align*}
$$

As for the non-relativistic case, $\theta$ is a cyclic variable and thus the angular momentum $p_{\theta} = m\gamma r^2 \dot{\theta}$ is conserved.

:::{figure} ../images/lt-21261-16.7.1.png
:label: fig-17-7-1
:enumerator: 17.7.1
:alt: The advance of the perihelion of bound orbits due to the dependence of the relativistic mass on velocity.

The advance of the perihelion of bound orbits due to the dependence of the relativistic mass on velocity.
:::

The relativistic Hamiltonian for the Coulomb potential between an electron and the proton, assuming that the motion is confined to a plane, which allows use of planar polar coordinates, leads to

$$
H = \sqrt{ p^2_rc^2 + \frac{p^2_{\theta} c^2}{ r^2} + m^2c^4} − \frac{ke^2}{r} \nonumber
$$

The same equations of motion are obtained using Hamiltonian mechanics, that is:

$$
\begin{align*} \dot{\theta} &= \frac{\partial H}{ \partial p_{\theta}} = \frac{p_{\theta}}{ m\gamma r^2} \\[4pt] \dot{r} &= \frac{\partial H}{ \partial p_r} = \frac{p_r}{ m\gamma} \\[4pt] \dot{p}_{\theta} &= −\frac{\partial H}{ \partial \theta} = 0 \\[4pt] \dot{p}_r &= −\frac{\partial H}{ \partial r} = m \gamma r \dot{\theta}^2 + k \frac{e^2 }{r^2} \end{align*}
$$

The radial dependence can be solved using either Lagrangian or Hamiltonian mechanics, but the solution is non-trivial. Using the same techniques applied to solve Kepler’s problem, leads to the radial solution

$$
r = \frac{q}{ 1 + \epsilon \cos [\Gamma (\theta − \theta_0]} \quad \Gamma = \sqrt{ 1 − \frac{e^4}{ c^2 p^2_{\theta}}} \quad q = \frac{c^2\Gamma^2 p^2_{\theta}}{e^2 E} \quad \epsilon = \sqrt{1 + \frac{\Gamma^2 (1 − \frac{m^2c^4}{E^2} )}{ 1 − \Gamma^2}} \nonumber
$$

The apses are $r_{\text{min}} = \frac{q}{ (1+\epsilon)}$ for $\Gamma (\theta − \theta_0) = 0$, $2\pi , 4\pi$, and $r_{\text{max}} = \frac{q}{ (1−\epsilon)}$ for $\Gamma (\theta − \theta_0) = \pi , 3\pi ,$. The perihelion advances between cycles due to the change in relativistic mass during the trajectory as shown in ([Figure 17.7.1](#fig-17-7-1). This precession leads to the fine structure observed in the optical spectra of the hydrogen atom. The same precession of the perihelion occurs for planetary motion, however, there is a comparable size effect due to gravity that requires use of general relativity to compute the trajectories.
::::

[^17-7-1]: Note that Greiner[Gr10] includes a reproduction of the Struckmeier paper[Str08].

## 17.8: The General Theory of Relativity

The Special Theory of Relativity is restricted to inertial frames that are in uniform non-accelerated motion, and are assumed to exist over all of space-time. In 1916 Einstein published the General Theory of Relativity which expands the scope of relativistic mechanics to include non-inertial accelerating frames plus a unified theory of gravitation. The General Theory of Relativity incorporates both the Special Theory of Relativity as well as Newton’s Law of Universal Gravitation. It provides a unified theory of gravitation that is a geometric property of space and time. In particular, the curvature of space-time is directly related to the four-momentum of matter and radiation. Unfortunately, Einstein’s equations of general relativity are nonlinear partial differential equations that are difficult to solve exactly, and the theory requires knowledge of Riemannian geometry that goes beyond the scope of this book. However, it is useful to summarize the fundamental concepts upon which the theory is based, and some of the observable implications since the General Theory of Relativity is an important branch of classical mechanics.

### The Fundamental Concepts

The development of general relativity by Einstein was strongly influenced by the following five principles.

#### Mach’s Principle

The 1883 work "The Science of Mechanics" by the philosopher/physicist, Ernst Mach, criticized Newton’s concept of an absolute frame of reference, and suggested that local physical laws are determined by the large-scale structure of the universe. The concept is that local motion of a rotating frame is determined by the large-scale distribution of matter, that is, relative to the fixed stars. Einstein’s interpretation of Mach’s statement was that the inertial properties of a body is determined by the presence of other bodies in the universe, and he named this concept Mach’s Principle. Mach’s Principle has never been developed into a quantitative physical theory that would explain a mechanism by which the large-scale distribution of matter can produce such an effect.

#### Equivalence Principle

The equivalence principle comprises closely-related concepts dealing with the equivalence of gravitational and inertial mass. The **weak equivalence principle** states that the inertial mass and gravitational mass of a body are identical, leading to acceleration that is independent of the nature of the body. This experimental fact usually is attributed to Galileo. Recent measurements have shown that this weak equivalence principle is obeyed to a sensitivity of $5 \times 10^{−13}$. **Einstein’s equivalence principle** states that the outcome of any local non-gravitational experiment, in a freely falling laboratory, is independent of the velocity of the laboratory and its location in space-time. This principle implies that the result of local experiments must be independent of the velocity of the apparatus. Einstein’s equivalence principle has been tested by searching for variations of dimensionless fundamental constants such as the fine structure constant. The **strong equivalence principle** combines the weak equivalence and Einstein equivalence principles, and implies that the gravitational constant is constant everywhere in the universe. The strong equivalence principle suggests that gravity is geometrical in nature and does not involve any fifth force in nature. Einstein’s General Theory of Relativity satisfies the strong equivalence principle. Tests of the strong equivalence principle have involved searches for variations in the gravitational constant $G$ and masses of fundamental particles throughout the life of the universe.

#### Principle of Covariance

A physical law expressed in a covariant formulation has the same mathematical form in all coordinate systems, and is usually expressed in terms of tensor fields. Maxwell’s equations of electromagnetism are an example of such a covariant formulation. In the Special Theory of Relativity, the Lorentz, rotational, translational and reflection transformations between inertial coordinate frames all are covariant. The covariant quantities are the 4-scalars, and 4-vectors in Minkowski space-time. Einstein recognized that the principle of covariance, that is built into the Special Theory of Relativity, should apply equally to accelerated relative motion in the General Theory of Relativity. He exploited tensor calculus to extend the Lorentz covariance to the more general local covariance in the General Theory of Relativity. The reduction locally of the general metric tensor to the Minkowski metric corresponds to free-falling motion, that is geodesic motion, and thus encompasses gravitation. Unified field theory involves attempts to extend the General Theory of Relativity to incorporate other physical phenomena within a covariant framework in a purely geometric representation in space-time.

#### Correspondence principle

The Correspondence Principle states that the predictions of any new scientific theory must reduce to the predictions of well established earlier theories under circumstances for which the preceding theory was known to be valid. This also is referred to as the "correspondence limit". The Correspondence Principle is an important concept used both in quantum mechanics and relativistic mechanics. Einstein’s Special Theory of Relativity satisfies the Correspondence Principle because it reduces to classical mechanics in the limit of velocities small compared to the speed of light. The Correspondence Principle requires that the General Theory of Relativity must reduce to the Special Theory of Relativity for inertial frames, and should approximate Newton’s Theory of Gravitation in weak fields and at low velocities.

#### Principle of Minimal Gravitational Coupling

The principle of minimal gravitational coupling requires that the total Lagrangian for the field equations of general relativity consist of two additive parts, one part corresponding to the free gravitational Lagrangian, and the other part to external source fields in curved space-time. That is, no terms explicitly containing the curvature of space-time should be added in the extension from the special to general theories of relativity.

### Einstein’s postulates for the General Theory of Relativity

Einstein realized that the Equivalence Principle relating the gravitational and inertial masses implies that the constancy of the velocity of light in vacuum cannot hold in the presence of a gravitational field. That is, the Minkowskian line element must be replaced by a more general line element that takes gravity into account. Einstein proposed that the Minkowskian line element in four-dimensional space-time, be replaced by introducing a four-dimensional Riemannian geometrical structure where space, time, and matter are combined. As described by Lanczos[La49], [Har03], [Mu08] this astonishingly bold proposal implies that planetary motion is described as purely a geodesic phenomenon in a certain four-space of Riemannian structure, where the geodesic is the equation of a curve on a manifold for any possible set of coordinates. This implies that the concept of "gravitational force" is discarded, and planetary motion is a manifestation of a pure geodesic phenomenon for forceless motion in a four-dimensional Riemannian structure.

Chapter $5.10$ showed that the Lagrangian and Hamiltonian representations of variational mechanics are powerful approaches for determining the equation governing geodesic constrained motion. In addition, these representations are independent of the chosen frame of reference as required by the General Theory of Relativity. Thus variational mechanics is the preeminent theoretical representation of the General Theory of Relativity and the predictions are consistent with the fundamental concepts described in chapter $16.8$.

To summarize, the Special Theory of Relativity implies that the Newtonian concepts of absolute frame of reference and separation of space and time are invalid. The General Theory of Relativity goes beyond the Special Theory by implying that the gravitational force, and the resultant planetary motion, can be described as pure geodesic phenomena for forceless motion in a four-dimensional Riemannian structure.

### Experimental evidence

The evidence in support of Einstein’s Theory of General Relativity is compelling. The following are typical experimental manifestations of the General Theory of Relativity.

#### Kepler problem

In 1915 Einstein showed that relativistic mechanics explained the anomalous advance of the perihelion of the planet Mercury, that is, the axes of the elliptical Kepler orbit precess. Example $16.7.1$ discusses the analogue of this effect for the Bohr-Sommerfeld hydrogen atom.

#### Deflection of light

Eddington travelled to the island of Príncipe, near Africa, to watch the solar eclipse of 29 May 1919. During the eclipse, he took pictures of the stars in the region around the Sun. According to the theory of general relativity, stars with light rays that passed near the Sun would appear to have been slightly shifted because their light had been curved by the sun’s gravitational field. This effect is noticeable only during eclipses, since otherwise the Sun’s brightness obscures the affected stars. The results confirmed Einstein’s prediction of the deflection of light in a gravitational field which made Einstein famous.

#### Gravitational lensing

The deflection of light by the gravitational attraction of a massive object situated between a distant star and the observer results in the observation of multiple images of the distant quasar.

#### Gravitational time dilation and frequency shift

Processes occurring in a high gravitational field are slower than in a weak gravitational field; this is called gravitational time dilation. In addition, light climbing out of a gravitational well is red shifted. The gravitational time dilation has been measured many times and the continued operation of the Global Positioning System provides an ongoing validation. The gravitational red shift has been confirmed in the laboratory using the precise Mössbauer effect in nuclear physics. Tests in stronger gravitational fields are provided by studies of binary pulsars. All of these measurements confirm the general theory of relativity.

#### Gravitational waves detection

In 1916 Einstein predicted the existence of gravitational waves on the basis of the theory of general relativity. The first implied detection of gravitational waves were made in 1976 by Hulse and Taylor who detected a decrease in the orbital period due to significant energy loss which presumably was associated with emission of gravity waves by the compact neutron star in the binary pulsar $PSR 1913 + 16$. The most compelling direct evidence for observation of a gravitational wave was made on 15 September 2015 by the LIGO Laser Interferometer Gravitational-Wave Observatories. The waveform detected by the two LIGO observatories matched the predictions of General Relativity for gravitational waves emanating from the inward spiral plus merger of a pair of black holes of around 36 and 29 solar masses, followed by the resultant binary black hole. The gravitational wave emitted by this cataclysmic merger reached Earth as a ripple in space-time that changed the length of the $4$ $km$ LIGO arm by a thousandth of the width of the proton. The gravitational energy emitted was $3.0^{+0.5}_{−0.5} c^2$ solar masses. A second observation of gravitational waves was made on 26 December 2015, and four similar observations were made during 2017. The detection of such minuscule changes in space-time is a truly remarkable achievement. This direct detection of gravitational waves resulted in the award of the 2017 Nobel Prize to Rainer Weiss, Barry Barish, and Kip Thorne.

#### Black holes

If the mass to radius ratio of a massive object becomes sufficiently large, general relativity predicts formation of a black hole, which is a region of space from which neither light nor matter can escape. A supermassive black hole, with a mass that is $10^6 − 10^9$ solar masses, is thought to have played an important role in formation of the M87 galaxy. This black hole at the core of the massive elliptical M87 galaxy was observed April 2017 by the Event Horizon Telescope (EHT). [Figure 17.8.1](#fig-17-8-1) shows a polarized light image of this black hole, revealing a ring-like structure consistent with synchrotron emission from relativistic electrons that are gyrating around the inner edge of a vortex of magnetic field lines in the vicinity of the event horizon. (The Astrophysical Journal Letters, 910:L12, 20 March 2021).

:::{figure} ../images/lt-32981-17.6.3.png
:label: fig-17-8-1
:enumerator: 17.8.1
:alt: Polarized-light image of the M87 black hole

Polarized-light image of the M87 black hole
:::

## 17.9: Implications of Relativistic Theory to Classical Mechanics

Einstein’s theories of relativity have had an enormous impact on twentieth century physics and the philosophy of science. Relativistic mechanics is crucial to an understanding of the physics of the atom, nucleus and the substructure of the nucleons, but the impacts are minimal in everyday experience. As a consequence the enormous philosophical implications of Einstein’s theories of relativity may not be as readily apparent as other major developments during the 20$^{th}$ century. In spite of this, it is important to be cognizant of the consequences of these theories of nature. The Special Theory of Relativity replaces Newton’s Laws of motion; i.e. Newton’s law is only an approximation applicable for low velocities. The General Theory of Relativity replaces Newton’s Law of Gravitation and provides a natural explanation of the equivalence principle. Einstein’s theories of relativity imply a profound and fundamental change in the view of the separation of space, time, and mass, that contradicts the basic tenets that are the foundation of Newtonian mechanics. The Newtonian concepts of absolute frame of reference, plus the separation of space, time, and mass, are invalid at high velocities. Lagrangian and Hamiltonian variational approaches to classical mechanics provide the formalism necessary for handling relativistic mechanics. The present chapter has shown that logical extensions of Lagrangian and Hamiltonian mechanics lead to the relativistically-invariant extended Lagrangian and Hamiltonian formulations of mechanics which is adequate for handling one-body systems within the Special Theory of Relativity. However, major unsolved problems remain applying these formulations to systems having more than one body.

## 17.E: Relativistic Mechanics (Exercises)

1. A relativistic snake of proper length $100$ $cm$ is travelling to the right across a butcher’s table at $v = 0.6c$. You hold two meat cleavers, one in each hand which are $100$ $cm$ apart. You strike the table simultaneously with both cleavers at the moment when the left cleaver lands just behind the tail of the snake. You rationalize that since the snake is moving with $\beta = 0.6$, then the length of the snake is Lorentz contracted by the factor $\gamma = \frac{5}{ 4}$ and thus the Lorentz-contracted length of the snake is $80$ $cm$ and thus will not be harmed. However, the snake reasons that relative to it the cleavers are moving at $\beta = 0.6$ and thus are only $80$ $cm$ apart when they strike the $100$ $cm$ long snake and thus it will be severed. Use the Lorentz transformation to resolve this paradox.

2. Explain what is meant by the following statement: “Lorentz transformations are orthogonal transformations in Minkowski space.”

3. Which of the following are invariant quantities in space-time?

1. Energy

2. Momentum

3. Mass

4. Force

5. Charge

6. The length of a vector

7. The length of a four-vector

4. What does it mean for two events to have a spacelike interval? What does it mean for them to have a timelike interval? Draw a picture to support your answer. In which case can events be causally connected?

5. A supply rocket flies past two markers on the Space Station that are $50$ $m$ apart in a time of $0.2$ $\mu s$ as measured by an observer on the Space station.

1. What is the separation of the two markers as seen by the pilot riding in the supply rocket?

2. What is the elapsed time as measured by the pilot in the supply rocket?

3. What are the speeds calculated by the observer in the Space Station and the pilot of the supply rocket?

6. The Compton effect involves a photon of incident energy $E_i$ being scattered by an electron of mass $m_e$ which initially is stationary. The photon scattered at an angle $\theta$ with respect to the incident photon has a final energy $E_f$. Using the special theory of relativity derive a formula that related $E_f$ and $E_i$ to $\theta$.

7. Pair creation involves production of an electron-positron pair by a photon. Show that such a process is impossible unless some other body, such as a nucleus, is involved. Suppose that the nucleus has a mass $M$ and the electron mass $m_e$. What is the minimum energy that the photon must have in order to produce an electron-positron pair?

8. A $K$ meson of rest energy $494$ $MeV$ decays into a $\mu$ meson of rest energy $106$ $MeV$ and a neutrino of zero rest energy. Find the kinetic energies of the $\mu$ meson and the neutrino into which the $K$ meson decays while at rest.

## 17.S: Relativistic Mechanics (Summary)

### Special Theory of Relativity

The Special Theory of Relativity is based on Einstein’s postulates;

1. *The laws of nature are the same in all inertial frames of reference.*

2. *The velocity of light in vacuum is the same in all inertial frames of reference.*

For a primed frame moving along the $x_1$ axis with velocity $v$ Einstein’s postulates imply the following Lorentz transformations between the moving (primed) and stationary (unprimed) frames

::::{list-table}
* - $x^{\prime} = \gamma (x − vt)$
  - $x = \gamma (x^{\prime} + vt^{\prime} )$
* - $y^{\prime} = y$
  - $y = y^{\prime}$
* - $z^{\prime} = z$
  - $z = z^{\prime}$
* - $t^{\prime} = \gamma \left( t + \frac{vx }{c^2}\right)$
  - $t = \gamma \left( t ^{\prime} + \frac{vx^{\prime}}{c^2}\right)$
::::

where the Lorentz $\gamma$ factor $\gamma \equiv \frac{1}{\sqrt{1-\left(\frac{v}{c}\right)^2}}$

Lorentz transformations were used to illustrate Lorentz contraction, time dilation, and simultaneity. An elementary review was given of relativistic kinematics including discussion of velocity transformation, linear momentum, center-of-momentum frame, forces and energy.

### Geometry of space-time

The concepts of four-dimensional space-time were introduced. A discussion of four-vector scalar products introduced the use of contravariant and covariant tensors plus the Minkowski metric $g$ where the scalar product was defined. The Minkowski representation of space time and the momentum-energy four vector also were introduced.

### Lorentz-invariant formulation of Lagrangian mechanics

The Lorentz-invariant extended Lagrangian formalism, developed by Struckmeier[Str08], based on the parametric approach pioneered by Lanczos[La49], provides a viable Lorentz-invariant extension of conventional Lagrangian mechanics that is applicable for one-body motion in the realm of the Special Theory of Relativity.

### Lorentz-invariant formulation of Hamiltonian mechanics

The Lorentz-invariant extended Hamiltonian formalism, developed by Struckmeier based on the parametric approach pioneered by Lanczos, was introduced. It provides a viable Lorentz-invariant extension of conventional Hamiltonian mechanics that is applicable for one-body motion in the realm of the Special Theory of Relativity. In particular, it was shown that the Lorentz-invariant extended Hamiltonian is conserved making it ideally suited for solving complicated systems using Hamiltonian mechanics via use of the Poisson-bracket representation of Hamiltonian mechanics, canonical transformations, and the Hamilton-Jacobi techniques.

### The General Theory of Relativity

An elementary summary was given of the fundamental concepts of the General Theory of Relativity and the resultant unified description of the gravitational force plus planetary motion as geodesic motion in a four-dimensional Riemannian structure. Variational mechanics were shown to be ideally suited to applications of the General Theory of Relativity.

### Philosophical implications

Newton’s equations of motion, and his Law of Gravitation, that reigned supreme from 1687 to 1905, have been toppled from the throne by Einstein’s theories of relativistic mechanics. By contrast, the complete independence to coordinate frames in Lagrangian, and Hamiltonian formulations of classical mechanics, plus the underlying Principle of Least Action, are equally valid in both the relativistic and non-relativistic regimes. As a consequence, relativistic Lagrangian and Hamiltonian formulations underlie much of modern physics, especially quantum physics, which explains why relativistic mechanics plays such an important role in classical dynamics.
