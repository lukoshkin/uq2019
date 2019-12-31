import numpy as np


def pwCDF(fn, m, interval=(0, 1), samples=False):
    """
    Constructs piecewise CDF using PDF function or its points
    Args:
    ----
    fn          pdf or counts normalized to form a prob. density
    m           number of intervals at which `fn` is approximated
    interval    `fn`'s domain (if `samples=True`, then it is expected
                `(fn.min(), fn.max())` as `interval`)
    """
    A, B = interval
    dx = (B-A) / m
    if samples:
        p = np.histogram(fn, bins=m, density=True)[0]
    else:
        pts = np.linspace(A, B, m+1)
        pts = pts[:-1] + dx/2
        p = fn(pts)
    p = np.r_[p, 0]
    F = np.r_[0, p.cumsum()]
    F /= F[-1]
    def CDF(x):
        x = (x-A) / (B-A)
        ids = np.floor(m*x).astype('int')
        Fv = np.take(F, ids)
        pv = np.take(p, ids)
        return Fv + pv*(m*x-ids)*dx
    return CDF


def inverse_pwCDF(fn, m, interval=(0,1), CDF=False):
    """
    Constructs inverse CDF using CDF or PDF. There is no point
    to build the 'tails', since no points can be sampled from there.
    Still the right one is padded.
    Args:
    ----
    fn          PDF if `CDF` is `False`, CDF otherwise
    m           number of intervals at which `fn` is approximated
    interval    support of the CDF
    """
    eps = 1e-12

    A, B = interval
    y = np.linspace(A, B, m+1)
    dy = (B-A) / m
    if not CDF: 
        fn = pwCDF(fn, m, interval)
    nodes = fn(y)
    dx = np.diff(nodes)
    k = np.zeros_like(dx)
    # if the right arg. is passed as `fn`, every el. in dx is pos.
    # then `abs` or `np.abs` is redundant in kw. `where` below
    np.divide(dy, dx, out=k, where=dx>eps)
    b = y[:-1] - k * nodes[:-1]
    def inverse_CDF(x):
        mask = x < nodes[-1]
        appendix = np.full((~mask).sum(), B)
        ids = np.searchsorted(nodes, x[mask], side='right') - 1
        kv = np.take(k, ids)
        bv = np.take(b, ids)
        return np.r_[kv * x[mask] + bv, appendix]
    return inverse_CDF
