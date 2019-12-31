# Summary

## Sampling Techniques
### Lecture 2

* ***Monte-Carlo sampling***  
    Acts as a punching bag for the other methods presented in this lecture

* ***Halton sequences***  
    Quasi-random _low-discrepancy_ sequences (_that is, appear to be random for many purposes_). ***From Wiki***: They are constructed according to a deterministic method
    that uses coprime numbers as its bases. Even though standard Halton sequences perform very well in low dimensions, correlation problems have been noted between sequences
    generated from higher primes. One of the most prominent solutions is the scrambled Halton sequence, which uses permutations of the coefficients used in the construction of
    the standard sequence. Another solution is the leaped Halton, which skips points in the standard sequence.

* ***Rejection sampling***  
    _Procedure_  
    The rejection sampling method generates sampling values from a target distribution $X$ with arbitrary probability density function $f(x)$ by using a proposal distribution $Y$
    with probability density $g(x)$. The idea is that one can generate a sample value from $X$ by instead sampling from $Y$ and accepting the sample from $Y$ with probability
    $\frac{f(x)}{Mg(x)}$, repeating the draws from $Y$ until a value is accepted. $M$ here is a constant, finite bound on the likelihood ratio $f(x)/g(x)$, satisfying $1 < M < \infty$
    over the support of $X$; in other words, $M$ must satisfy $f(x) \le Mg(x)$ for all values of $x$. Note that this requires that the support of $Y$ must include the support of $X$ —
    in other words, $g(x) > 0$ whenever $f(x) > 0$.

    - [proofs and aplications of the method](http://www.columbia.edu/~ks20/4703-Sigman/4703-07-Notes-ARM.pdf)  

* ***Importance sampling***  
    In many applications we want to compute $\mu = \mathbb{E}(f(X))$  where $f(x)$ is nearly zero outside a region $A$ for which $P(X \in A)$ is small. The set $A$ may have small volume,
    or it may be in the tail of the $X$ distribution. A plain Monte Carlo sample from the distribution of $X$ could fail to have even one point inside the region $A$. It is clear intuitively
    that we must get some samples from the interesting or important region. We do this by sampling from a distribution that overweights the important region, hence the name **importance sampling**.  

    Mean's estimator is $\tilde{\mu}_q = \frac{1}{n}\sum_1^n \frac{f(\mathbf{X}_i)p(\mathbf{X}_i)}{q(\mathbf{X}_i)}, \quad \mathbf{X}_i \sim q$  

    _Procedure_  
    1. Choose the distribution $q$ close to the original one (to reduce the estimator's variance)
    2. Sample from it and calculate the estimate

    - [more about importance sampling](https://statweb.stanford.edu/~owen/mc/Ch-var-is.pdf)  

* ***Inverse transform sampling***  
    Works even when PDF does not exist  

    _Procedure_  
    1. Construct the inverse transform of the given CDF. (I implemented it in my [repo](link))
    2. Sample uniform noise
    3. Aplly the inverse CDF built to the generated noise

    - [look here how it works](http://www.columbia.edu/~ks20/4404-Sigman/4404-Notes-ITM.pdf)  

    Good method, but works only in 1D case

### Lecture 3

* ***Particular applications of importance sampling methods***  
    See in the lecture3.ipynb

* ***Latin hypercube sampling***  
    [From SMT documentation](https://smt.readthedocs.io/en/latest/_src_docs/sampling_methods/lhs.html): The LHS design is a statistical method for generating a quasi-random sampling distribution.
    It is among the most popular sampling techniques in computer experiments thanks to its simplicity and projection properties with high-dimensional problems. LHS is built as follows:
    we cut each dimension space, which represents a variable, into $n$ sections where $n$ is the number of sampling points, and we put only one point in each section.

## Polynomial Chaos Methods  
### Lecture 4  

A function from r.v. may be approximated with ***Generalized polynomial chaos (gPC)*** basis.

- _Strong gPC approximation_  
    Let $f(\xi)$ be a function of a random variable $\xi$ whose probability distribution is $F_\xi$. A generalized polynomial chaos approximation in a strong sense
    is $f_N \in \mathcal P_N$, where $\mathcal P_N$ is the space of polynomials of degree up to $N$, such that $\|f(\xi)-f_N(\xi)\| \to 0$ as $N \to \infty$, in a proper norm.

    So, you are given $f(\xi), \xi \sim F_\xi$ and a proper set of polynomials (likely), you can build $f_N(\xi)$ using $N$ polynomials, such that $\|f(\xi)-f_N(\xi)\| \to 0$ as $N \to \infty$.
    See how in lecture4.ipynb.

- _Weak gPC approximation_  
    Let $\eta$ be a random variable with distribution function $F_\eta(x) = \mathbb P(\eta \le x)$ and let $\theta$ be a (standard) random variable in a set of gPC basis functions.
    A weak gPC approximation is $\eta_N \in \mathcal P_N(\theta)$, where $\mathcal P_N(\theta)$ is the linear space of polynomials of $\theta$ of degree up to $N \ge 0$, such that
    $\eta_N$ converges to $\theta$ in a weak sense, e.g., in probability.

    This time, you don't know $\eta$ in a function form, you just have its distribution $F_\eta(x)$, a proper set of polynomials (likely) and can sample from $\theta \sim$ _distributed somehow_,
    still you are capable to build an approximation (in a weak sense). See how in lecture4.ipynb.
